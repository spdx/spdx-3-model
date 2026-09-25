SPDX-License-Identifier: Community-Spec-1.0

# MediaType

## Summary

Standardized way of indicating the type of content of an Element or a property.
A string constrained to the RFC 2046 specification.

## Description

A MediaType provides a standardized way of indicating the type of content of
an Element or a property.

The string shall be constrained to
[RFC 2046 MIME Part Two: Media Types](https://datatracker.ietf.org/doc/rfc2046/)
and shall be normalized in accordance with the
[WHATWG MIME Sniffing standard](https://mimesniff.spec.whatwg.org/#parsing-a-mime-type).
The following formatting constraints apply:

- The top-level type and subtype shall be represented in ASCII lowercase.
- When one or more media type parameters are present, whitespace characters
  shall not occur adjacent to the semicolon (`;`) delimiter or the equals
  sign (`=`).
- Parameter values shall not be enclosed in quotation marks (`"`)
  unless the value is an empty string or the value contains characters outside
  the standard HTTP token code point set.

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

- pattern: ^[^/;\s]+/[^/;\s]+(;[^=;\s]+=("([^"\\]|\\.)*"|[^";\s=]+))*$
