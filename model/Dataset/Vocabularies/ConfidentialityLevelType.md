SPDX-License-Identifier: Community-Spec-1.0

# ConfidentialityLevelType

## Summary

Confidentiality level.

## Description

Describes the different confidentiality levels as defined by the
[Traffic Light Protocol](https://en.wikipedia.org/wiki/Traffic_Light_Protocol).

Within the context of this classification:

- a community is a group sharing common goals, practices, and informal trust
  relationships.
- an organization is a group sharing a common affiliation by formal membership
  and bound by common policies established by the organization.
- clients are persons or entities receiving services from an organization.

## Metadata

- name: ConfidentialityLevelType

## Entries

- red: Personal for named recipients only. The dataset is highly confidential and shall be shared only with named recipients.
- amberStrict: Limited distribution - organization only. The dataset shall be shared only with specific organizations on a need-to-know basis.
- amber: Limited distribution - organization and clients. The dataset shall be shared only with specific organizations and their clients on a need-to-know basis.
- green: Community wide. The dataset shall be shared only within a community of peers and partners.
- clear: Unlimited. Subject to standard copyright rules, the dataset may be shared freely, without restriction.
