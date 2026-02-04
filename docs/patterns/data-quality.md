# Data Quality & Best Practices: "Good Data Leads Data"

In the UKG ecosystem, data integrity is not just about avoiding errors—it's about building trust. If the operations team doesn't trust the dashboard, the project has failed.

## 🏆 The "Leading Data" Methodology

### 1. The Variance Control Loop
You must automate trust. Every morning, your pipeline should run a **Control Query**:

```sql
WITH bq_total AS (
  SELECT SUM(daily_hours) as hours FROM \`ukg.punches\` WHERE date = CURRENT_DATE() - 1
),
api_total AS (
  -- Result from the 'Payroll Summary' API endpoint
  SELECT 8430.5 as hours 
)
SELECT 
  bq_total.hours, 
  api_total.hours, 
  (bq_total.hours - api_total.hours) as drift
FROM bq_total, api_total
```
> **Rule**: If `drift != 0`, do not refresh the Tableau/PowerBI dashboard. Send a Slack alert instead.

### 2. Handling "Ghost" Employees
A common issue in WFM is employees who exist in the Timekeeping system but not in HR (or vice versa) due to sync lag.

*   **Best Practice**: Create a `qa_ghost_employee` table.
*   **Logic**: `SELECT person_id FROM punches WHERE person_id NOT IN (SELECT person_id FROM person_import)`
*   **Action**: These represent compliance risks (people working without a contract). Highlight them immediately.

### 3. Timezone Hygiene
UKG stores everything in UTC. Humans think in "Shift Time".
*   **Wrong**: `extract(hour from punch_time)` on the raw field.
*   **Right**: `extract(hour from DATETIME(punch_time, location_timezone))`

## 🛠️ Interactive Diagnostics

Use the included `etl_simulator.py` to test your assumptions about how data flows from the API to the Warehouse. It simulates:
1.  **Extraction**: Handling nested JSON arrays.
2.  **Transformation**: The "Coalesce Null" logic.
3.  **Loading**: Detecting duplicates before they hit BigQuery.

---
*"Build it right, or build it twice."*
