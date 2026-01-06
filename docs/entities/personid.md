# personId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Person Identifier

## Fields

| Field    | Type   | Description                                                                                                                                           |
|:---------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| personId | INT64  | Person Identifier                                                                                                                                     |
| personId | INT64  | Used to join to people dimension                                                                                                                      |
| personId | INT64  | id of the employee to which that particular position is assigned                                                                                      |
| personId | INT64  | Used to join to people dimension personId for the employee who's schedule changed                                                                     |
| personId | INT64  | Person ID for whom the audit was made                                                                                                                 |
| personId | INT64  | personId for which the change occured                                                                                                                 |
| personId |        |                                                                                                                                                       |
| personId | INT64  | The employee ID of the initiator of an availability request, which is an ID that uniquely identifies an employee. This is not a person number.        |
| personId | INT64  | The employee ID of the initiator of an availability request, which is an ID that uniquely identifies an employee. This is not a person number.        |
| personId | INT64  | The employee ID of the initiator of an open shift coverage request, which is an ID that uniquely identifies an employee. This is not a person number. |
| personId | INT64  | The employee ID of the initiator of an shift coverage request, which is an ID that uniquely identifies an employee.This is not a person number.       |
| personId | INT64  | The employee ID of the initiator of an self schedule request, which is an ID that uniquely identifies an employee.This is not a person number.        |
| personId | INT64  | The employee ID of the initiator of an ESS request, which is an ID that uniquely identifies an employee. This is not a person number.                 |
| personId | INT64  | The employee ID of the initiator of an shift swap request, which is an ID that uniquely identifies an employee.This is not a person number.           |
| personId | INT64  | The employee ID of the initiator of  time off request, which is an ID that uniquely identifies an employee.This is not a person number.               |
| personId | INT64  | The ID of the person referencing the People view                                                                                                      |
| personId | INT64  | Person ID linked to the pay period                                                                                                                    |
| personId | INT64  | Primary Key  - Should be used for all joins to detail fact Views. Not the Person Id in Dimensions                                                     |
| personId | INT64  | unique identifiyer for person                                                                                                                         |
| personId | INT64  | **  Note this value will always be null because openShift is not tied to person **                                                                    |
| personId | INT64  | The personId for the person who entered comment                                                                                                       |
| personId | INT64  |                                                                                                                                                       |
| personId | INT64  | The employee ID of the initiator of the request, which is an ID that uniquely identifies an employee. This is not a person number.                    |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.
