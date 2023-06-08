SPDX-License-Identifier: Community-Spec-1.0

# actionStatementTime

## Summary

Records the time when a recommended action was communicated in a VEX statement 
to mitigate a vulnerability.

## Description

When a VEX statement communicates an affected status, the author MUST
include an action statement with a recommended action to help mitigate the
vulnerability's impact. The actionStatementTime property records the time
when the action statement was first communicated.

## Metadata

- name: actionStatementTime
- Nature: DataProperty
- Range: /Core/DateTime

