SPDX-License-Identifier: Community-Spec-1.0

# CountryCodeAlpha3

## Summary

A string containing an assigned ISO 3166-1 alpha-3 country code.

## Description

The value shall be an uppercase three-letter country code assigned by [ISO 3166-1 alpha-3](https://www.iso.org/obp/ui/#iso:std:iso:3166:-1) at the time the SPDX element is created.

The pattern constraint validates only the lexical form; it does not establish that the value is an assigned ISO 3166-1 alpha-3 code. Implementations should validate values against the applicable ISO code list.

## Metadata

- name: CountryCodeAlpha3
- SubclassOf: xsd:string

## Format

- pattern: ^[A-Z]{3}$
