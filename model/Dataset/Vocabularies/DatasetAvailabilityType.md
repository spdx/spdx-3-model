SPDX-License-Identifier: Community-Spec-1.0

# DatasetAvailabilityType

## Summary

Availability of dataset

## Description

Describes the possible types of availability of a dataset, indicating whether the dataset can be directly downloaded, can be assembled using a script for scraping the data, is only available after a clickthrough or a registration form.

## Metadata

- name: DatasetAvailabilityType

## Entries

- directDownload: the dataset is publicly available and can be downloaded directly.
- scrapingScript: the dataset provider is not making available the underlying data and the dataset must be reassembled, typically using the provided script for scraping the data.
- query: the dataset is publicly available, but not all at once, and can only be accessed through queries which return parts of the dataset.
- clickthrough: the dataset is not publicly available and can only be accessed after affirmatively accepting terms on a clickthrough webpage.
- registration: the dataset is not publicly available and an email registration is required before accessing the dataset, although without an affirmative acceptance of terms.

