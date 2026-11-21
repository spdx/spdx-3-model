SPDX-License-Identifier: Community-Spec-1.0

# VerificationType

## Summary

Enumeration of methods used to verify that a requirement is met.

## Description

VerificationType lists the methods commonly used to confirm that a requirement
is met. Each entry names one method; `other` covers methods that do not fit the
listed ones.

## Metadata

- name: VerificationType

## Entries

- analysis: A methodical evaluation of data, designs, or processes to check that they are correct against a standard or expectation, for example FMEA, FTA, STPA, or static analysis for MISRA compliance.
- assessment: A systematic examination of specific work products, such as requirements, verification specifications, or reports, to evaluate whether they comply with a specification, regulation, or standard. An assessment involves a judgement and records the rationale for it.
- audit: An examination of whether processes and activities comply with policies, standards, or regulations, usually carried out in audit meetings. Unlike an assessment, an audit does not necessarily review individual work products in detail.
- demonstration: Operating the item under verification and observing or recording its behavior to confirm that it meets the requirement.
- inspection: A thorough examination of documentation, records, processes, or systems against a defined set of acceptance criteria, such as a checklist. An inspection records the roles involved, for example to show the inspector's independence, and when and how it was performed.
- other: A verification method not covered by the other entries.
- review: An examination of documentation, records, processes, or systems to confirm that they comply with a higher-level requirement, for example as a peer review, an offline review, or a review meeting.
- test: Running controlled tests, experiments, or simulations to verify that specific requirements, such as performance, functionality, or robustness requirements, are met.
