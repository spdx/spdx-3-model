SPDX-License-Identifier: Community-Spec-1.0

# MediaType

## Summary

Standardized way of indicating the type of content of an Element or a Property.
A String constrained to the RFC 2046 specification.

## Description

A MediaType is a string constrained to the
[RFC 2046 MIME Part Two: Media Types](https://datatracker.ietf.org/doc/rfc2046/).
It provides a standardized way of indicating the type of content of an Element
or a Property.

*Example*

- `application/java-archive`
- `application/vcard+json`
- `application/vnd.oasis.opendocument.text`
- `image/avif`
- `text/csv;charset=UTF-8`
- `text/javascript`
- `text/spdx`

A list of all possible media types is available at
[IANA Protocol Registries](https://www.iana.org/assignments/media-types/media-types.xhtml).

## Metadata

- name: MediaType
- SubclassOf: xsd:string

## Format

- pattern: ^[^\/]+\/[^\/]+$

## Summary @zh-Hans

用于标准化指示`Element`或`Property`内容类型的方法。
是一个符合RFC 2046规范的字符串。

## Description @zh-Hans

`MediaType`是一个符合[RFC 2046 MIME第二部分：媒体类型](https://datatracker.ietf.org/doc/rfc2046/)规范的字符串。
它提供了一种标准化的方法来指示`Element`或`Property`的内容类型。

*示例*

- `application/java-archive`
- `application/vcard+json`
- `application/vnd.oasis.opendocument.text`
- `image/avif`
- `text/csv;charset=UTF-8`
- `text/javascript`
- `text/spdx`

可能的媒体类型列表可在[IANA Protocol Registries](https://www.iana.org/assignments/media-types/media-types.xhtml)获取。
