SPDX-License-Identifier: Community-Spec-1.0

# notValidAfter

## Summary

notValidAfter is the date and time on which this Certificate expires and is no longer valid.

## Description

notValidAfter specifies the exact date and time when the Certificate ends its validity period. After this timestamp, the Certificate should not be considered valid for its intended purpose, even if it bears the signature of its issuer. This property is part of the Certificate's validity window, which spans from notValidBefore to notValidAfter. The notValidAfter timestamp establishes the end point of the certificate's operational lifetime.

## Metadata

- name: notValidAfter
- Nature: DataProperty
- Range: /Core/DateTime
