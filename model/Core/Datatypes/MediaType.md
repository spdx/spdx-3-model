SPDX-License-Identifier: Community-Spec-1.0

# MediaType

## Summary

Standardized way of indicating the type of content of an Element. A String constrained to the RFC 6838 specification.

## Description

A MediaType is a string constrained to the RFC 6838 specification, and includes
`type-name`, `subtype-name` and optional `parameters`.
It provides a standardized way of indicating the type of content of an Element.
A list of all possible media types is available at https://www.iana.org/assignments/media-types/media-types.xhtml.

## Metadata

- name: MediaType
- SubclassOf: xsd:string

## Format

- pattern: ^([a-zA-Z0-9][-a-zA-Z0-9!#$&^_.+]{0,126})\/([a-zA-Z0-9][-a-zA-Z0-9!#$&^_.+]{0,126})(;.+)?$
