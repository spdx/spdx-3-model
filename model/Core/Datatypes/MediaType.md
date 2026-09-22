SPDX-License-Identifier: Community-Spec-1.0

# MediaType

## Summary

Standardized way of indicating the type of content of an Element or a property.
A string constrained to the RFC 2046 specification.

## Description

A MediaType is a string constrained to the
[RFC 2046 MIME Part Two: Media Types](https://datatracker.ietf.org/doc/rfc2046/).
It provides a standardized way of indicating the type of content of an Element
or a property.

When media type parameters are present, whitespace shall not occur adjacent to
semicolons (`;`) or equals signs (`=`).
Where possible without altering semantics, whitespace within quoted parameter
values should also be omitted.

*Example*

- `application/java-archive`
- `application/spdx+json`
- `application/spdx3+json`
- `application/vnd.oasis.opendocument.text`
- `image/avif`
- `text/csv;charset=UTF-8`
- `text/javascript`
- `text/spdx`
- `video/mp4;codecs="avc1.4d401e,mp4a.40.2";profiles="isom,iso2"`

A list of all possible media types is available at
[IANA Protocol Registries](https://www.iana.org/assignments/media-types/media-types.xhtml).

## Metadata

- name: MediaType
- SubclassOf: xsd:string

## Format

- pattern: ^[^/;\s]+/[^/;\s]+(;[^=;\s]+=("[^"]*"|[^;\s]+))*$
