# Dataset Spec (Template)

## Dataset name
**<DATASET_NAME>**

## Purpose
What this dataset is for (dashboards, investigation, feature engineering, etc.)

## Grain
What one row represents.

## Primary keys
Fields that make a row unique at the grain.

## Source tables/views
List the upstream sources.

## Transform rules
- filters applied
- joins performed
- derived fields and definitions

## Partitioning / clustering (if used)
How data is organized for performance.

## Data quality checks
- uniqueness checks
- null checks
- range checks
- reconciliation checks

## Security classification
- PII present? (yes/no)
- masking/removal approach
- access model

## Ownership
Who maintains this dataset.
