# Quickstart

## What this is
A practical reference for reporting on **UKG Pro WFM Data Hub** data delivered into **BigQuery**.

## What you’ll find here
- Which data to use for common reporting needs (OT, accruals, schedule vs worked)
- Grain + key guidance to prevent duplicate inflation
- Cost-safe query patterns (partition filters)
- Troubleshooting and validation checks

## Ground rules
- Pick the grain first
- Join on IDs, not names
- Always bound your date/partition filters
- Validate before publishing dashboards

---

## Data Hub basics (public-safe)
Data Hub is a delivery system integrated with UKG Pro WFM and deployed on GCP. It extracts large volumes of WFM data, processes it, and delivers it into BigQuery tables/views for reporting and analytics.

### Wrappers and pipelines
- **Pipeline**: a specific extraction/load process into BigQuery
- **Wrapper**: runs one or more pipelines in a controlled sequence
- **Initial loads** are historical; later loads are incremental (but backfills can still update history)

### Why reporting teams should care
- Some datasets are **detail** (easy to double-count)
- Some datasets are **summary** (safe for dashboards)
- History can change due to late edits/backfills
- Mappings (like paycode categories) can reclassify metrics without your SQL changing

---

## Validation reality: “Does BigQuery match the UKG UI?”
Sometimes yes, sometimes not by default.

Common mismatch causes:
- worked org vs home org
- calendar vs pay period vs fiscal period
- mapping changes (paycode categories)
- join duplication / grain mismatch

Best practice:
- validate with a small employee sample across a known window
- document the KPI contract (what counts as OT/premium/etc.)
