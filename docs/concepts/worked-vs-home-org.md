# Worked Org vs Home Org

This is the #1 source of “the numbers don’t match.”

## Home org
Where the employee is assigned (HR/position-based).

Use when:
- reporting headcount by home department
- org-level workforce planning tied to assignments

## Worked org
Where the labor actually occurred (timecard/schedule location).

Use when:
- reporting overtime/utilization by operational unit
- analyzing staffing coverage, workload, or productivity
- investigating “where hours happened”

## Best practice
Every dashboard must state:
- “This report uses **Worked Org**” OR “This report uses **Home Org**”
- how rollups are applied (facility → dept → unit)
- the fallback rule when worked org is missing

## Common failure mode
A report uses worked hours but slices by home org → leadership thinks a unit is over budget when the hours were actually worked elsewhere.
