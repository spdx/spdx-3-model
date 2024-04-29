SPDX-License-Identifier: Community-Spec-1.0

# MediaType

## Summary

Standardized way of indicating the type of content of an Element. A String constrained to the RFC 2046 specification.

## Description

A MediaType is a string constrained to the [RFC 2046](https://www.ietf.org/rfc/rfc2046.txt) specification. It provides a standardized
way of indicating the type of content of an Element.

A list of all possible media types is available at
[https://www.iana.org/assignments/media-types/media-types.xhtml](https://www.iana.org/assignments/media-types/media-types.xhtml).

## Metadata

- name: MediaType
- SubclassOf: xsd:string

## Format

- pattern: ^[^\/]+\/[^\/]+$
