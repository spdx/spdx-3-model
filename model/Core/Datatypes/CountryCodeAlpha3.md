SPDX-License-Identifier: Community-Spec-1.0

# CountryCodeAlpha3

## Summary

A string constrained to the ISO 3166-1 alpha-3 three-letter format.

## Description

The string shall be in the [ISO 3166-1 alpha-3](https://www.iso.org/obp/ui/#iso:std:iso:3166:-1) three-letter format.

See the [ISO 3166-1 alpha-3 Wikipedia page](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) for more information.

## Metadata

- name: CountryCodeAlpha3
- SubclassOf: xsd:string

## Format

- pattern: ^[A-Z]{3}$
