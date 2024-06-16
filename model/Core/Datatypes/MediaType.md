SPDX-License-Identifier: Community-Spec-1.0

# MediaType

## Summary

Standardized way of indicating the type of content of an Element or a Property.
A String constrained to the RFC 2046 specificiation.

## Description

A MediaType is a string constrained to the
[RFC 2046 specification (MIME Part Two: Media Types)](https://www.rfc-editor.org/rfc/rfc2046).
It provides a standardized way of indicating the type of content of an Element
or a Property.

**Examples**

- `text/csv`
- `image/avif`
- `application/vcard+json`

A list of all possible media types is available at
<https://www.iana.org/assignments/media-types/media-types.xhtml>.

## Metadata

- name: MediaType
- SubclassOf: xsd:string

## Format

- pattern: ^[^\/]+\/[^\/]+$
