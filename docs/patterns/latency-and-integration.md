# Latency, Windows, and Real-Time Myths

> **Lesson #1**: Data Hub unlocks powerful analytics, but it is **NOT** real-time.

If your stakeholders expect to see a punch on the dashboard 5 minutes after it happens, **you must reset expectations immediately**.

---

## ⏳ The Latency Reality

The pipeline from the UKG Timekeeping engine to your analytics warehouse involves multiple hops:
1.  **Transaction**: Employee punches in.
2.  **App Queue**: Transaction processed by WFM application.
3.  **Data Hub Extractor**: Runs on a schedule/trigger (~4h latency typical within UKG infrastructure).
4.  **Downstream Landing**: Movement to Snowflake/Databricks/BigQuery.

**Total Delay**: Expect **5–6 hours** from event to dashboard. 

### Why this matters
*   **Don't** build "Real-time Overtime Alerts" on Data Hub. Use the OData API or HyperFinds for that.
*   **Do** build "Yesterday's Performance" or "Weekly Trends" reports.

---

## 🔄 CDC vs. Full Load

Data Hub uses different strategies for different entitites. You cannot assume everything is an incremental Change Data Capture (CDC) stream.

| Category | Type | Examples | Strategy |
| :--- | :--- | :--- | :--- |
| **Transactional** | CDC (Incremental) | Punches, Schedule Segments, Audit, Calc Results | Ingest `last_modified > max(watermark)` |
| **Setup / Config** | Full Load | Pay Rules, Business Structure, Work Rules, Labor Categories | **Snapshot**. Compare hash of current vs previous to detect changes. |
| **Hybrid** | Mixed | Person, Person Job Assignment | Often behaves like CDC but requires careful SCD Type 2 handling. |

> **Gotcha**: If you treat "Business Structure" as CDC, you will miss updates because rows aren't always flagged as "changed" in the way you expect. **Always full-load small setup tables.**

---

## 🪟 Windowing Strategy

The default Data Hub configuration acts as a moving window:
*   **Lookback**: 30 Days
*   **Lookforward**: 7 Days

### The Risk of Changing Windows
Expanding this window (e.g., to "Year to Date") has massive implications:
1.  **Volume**: API payload size explodes.
2.  **Runtime**: Extraction times may exceed your SLA.
3.  **Cost**: Egress costs (if not on Google Cloud Interconnect) will spike.

**Recommendation**: Keep the tight window for hourly runs. Run a separate "Historical Catch-up" pipeline only when necessary.

---

## ☁️ GCP: Who owns the plumbing?

*   **Enterprise Model**: Google Cloud Platform (GCP) is owned by the **Customer**. You have full access to the raw buckets/BigQuery.
*   **Premium Model**: GCP is owned by **UKG**. You receive the data via a delivery mechanism (e.g., SFTP, OData, or specific view access).

*Know your contract.* If you are on Premium, you cannot write custom BQ User Defined Functions (UDFs) against the raw data like you can in Enterprise.
