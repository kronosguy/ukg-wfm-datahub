#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd


DICT_COL = "Dataset/Table (View)/Column Name"
UID_COL = "Unique Identifier"
DTYPE_COL = "DataType"
DESC_COL = "Description"
PIPELINE_COL = "Source Pipeline"
PII_COL = "PII/Confidential"
SCRUB_COL = "Scrubbing"


DATE_ROW_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def is_blank(x: Any) -> bool:
    return x is None or (isinstance(x, float) and pd.isna(x)) or (isinstance(x, str) and x.strip() == "")


def s(x: Any) -> str:
    if is_blank(x):
        return ""
    return str(x).strip()


def slugify(text: str) -> str:
    text = text.strip()
    text = text.replace("/", "-")
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-").lower()


def md_escape(text: str) -> str:
    return text.replace("\n", " ").replace("\r", " ").replace("|", "\\|").strip()


def md_table(rows: List[Dict[str, str]], headers: List[str]) -> str:
    if not rows:
        return "_No rows._"
    header_line = "| " + " | ".join(headers) + " |"
    sep_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    body_lines = []
    for r in rows:
        body_lines.append("| " + " | ".join(md_escape(r.get(h, "")) for h in headers) + " |")
    return "\n".join([header_line, sep_line] + body_lines)


@dataclass
class DatasetDoc:
    name: str
    unique_identifier: str = ""
    description: str = ""
    source_pipeline: str = ""
    pii_confidential: str = ""
    scrubbing: str = ""
    group_path: Tuple[str, ...] = field(default_factory=tuple)
    columns: List[Dict[str, str]] = field(default_factory=list)

    @property
    def slug(self) -> str:
        return slugify(self.name)

    @property
    def filename(self) -> str:
        return f"{self.slug}.md"


def classify_row(row: pd.Series) -> str:
    """
    Returns one of: 'ignore', 'group', 'dataset', 'column'
    """
    name = s(row.get(DICT_COL))
    dtype = s(row.get(DTYPE_COL))
    uid = s(row.get(UID_COL))
    pipeline = s(row.get(PIPELINE_COL))
    desc = s(row.get(DESC_COL))

    if is_blank(name):
        return "ignore"

    if DATE_ROW_RE.match(name):
        return "ignore"

    if not is_blank(dtype):
        return "column"

    has_dataset_metadata = (not is_blank(uid)) or (not is_blank(pipeline)) or (len(desc) > 0)
    looks_like_dataset_name = (" " not in name)  # vAccrualBalance, vTimecardPunch, m_* etc.
    if has_dataset_metadata and looks_like_dataset_name:
        return "dataset"

    return "group"


def update_group_path(current: Tuple[str, ...], new_group: str) -> Tuple[str, ...]:
    """
    Heuristic: keep a 2-level grouping that matches the dictionary structure:
      Level 1: "<Something> Dataset" (ex: "Detail Dataset", "Summary Dataset")
      Level 2: "<Domain> Detail Views" (ex: "Accrual Detail Views")
    """
    g = new_group.strip()

    if "dataset" in g.lower():
        return (g,)

    if len(current) >= 1:
        return (current[0], g)

    return (g,)


def parse_dictionary(df: pd.DataFrame) -> List[DatasetDoc]:
    datasets: List[DatasetDoc] = []
    current_group: Tuple[str, ...] = tuple()
    current_ds: Optional[DatasetDoc] = None

    for _, row in df.iterrows():
        kind = classify_row(row)

        if kind == "ignore":
            continue

        if kind == "group":
            grp = s(row.get(DICT_COL))
            current_group = update_group_path(current_group, grp)
            current_ds = None
            continue

        if kind == "dataset":
            current_ds = DatasetDoc(
                name=s(row.get(DICT_COL)),
                unique_identifier=s(row.get(UID_COL)),
                description=s(row.get(DESC_COL)),
                source_pipeline=s(row.get(PIPELINE_COL)),
                pii_confidential=s(row.get(PII_COL)),
                scrubbing=s(row.get(SCRUB_COL)),
                group_path=current_group,
            )
            datasets.append(current_ds)
            continue

        if kind == "column":
            if current_ds is None:
                continue

            current_ds.columns.append(
                {
                    "Column": s(row.get(DICT_COL)),
                    "Data Type": s(row.get(DTYPE_COL)),
                    "Description": s(row.get(DESC_COL)),
                    "PII/Confidential": s(row.get(PII_COL)),
                    "Scrubbing": s(row.get(SCRUB_COL)),
                }
            )
            continue

    return datasets


def write_dataset_page(out_dir: str, ds: DatasetDoc) -> None:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ds.filename)

    meta_rows = [
        {"Field": "Dataset / View / Table", "Value": ds.name},
        {"Field": "Unique Identifier", "Value": ds.unique_identifier},
        {"Field": "Source Pipeline", "Value": ds.source_pipeline},
    ]

    if ds.pii_confidential:
        meta_rows.append({"Field": "PII/Confidential", "Value": ds.pii_confidential})
    if ds.scrubbing:
        meta_rows.append({"Field": "Scrubbing", "Value": ds.scrubbing})

    content = []
    content.append(f"# {ds.name}")
    content.append("")
    if ds.group_path:
        content.append(f"**Group:** {' → '.join(ds.group_path)}")
        content.append("")
    if ds.description:
        content.append(ds.description)
        content.append("")

    content.append("## Metadata")
    content.append("")
    content.append(md_table(meta_rows, headers=["Field", "Value"]))
    content.append("")

    content.append("## Columns")
    content.append("")
    content.append(f"**Column count:** {len(ds.columns)}")
    content.append("")
    content.append(md_table(ds.columns, headers=["Column", "Data Type", "Description", "PII/Confidential", "Scrubbing"]))
    content.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))


def write_index_page(out_dir: str, datasets: List[DatasetDoc]) -> None:
    os.makedirs(out_dir, exist_ok=True)
    index_path = os.path.join(out_dir, "index.md")

    grouped: Dict[Tuple[str, ...], List[DatasetDoc]] = {}
    for ds in datasets:
        grouped.setdefault(ds.group_path, []).append(ds)

    group_keys = sorted(grouped.keys(), key=lambda k: " → ".join(k).lower())
    for k in group_keys:
        grouped[k] = sorted(grouped[k], key=lambda d: d.name.lower())

    lines: List[str] = []
    lines.append("# Datasets")
    lines.append("")
    lines.append("This index is generated from the Data Hub Data Dictionary Excel.")
    lines.append("")
    lines.append("## Browse by section")
    lines.append("")

    for k in group_keys:
        title = " → ".join(k) if k else "Uncategorized"
        lines.append(f"### {title}")
        lines.append("")
        for ds in grouped[k]:
            lines.append(f"- [{ds.name}]({ds.filename})")
        lines.append("")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dictionary", required=True, help="Path to dictionary.xlsx")
    ap.add_argument("--out", required=True, help="Output directory (ex: docs/datasets)")
    args = ap.parse_args()

    df = pd.read_excel(args.dictionary, sheet_name=0)

    df = df[df[DICT_COL].notna()].copy()

    datasets = parse_dictionary(df)

    for ds in datasets:
        write_dataset_page(args.out, ds)

    write_index_page(args.out, datasets)

    print(f"Generated {len(datasets)} dataset pages into: {args.out}")


if __name__ == "__main__":
    main()
