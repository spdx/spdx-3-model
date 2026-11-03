SPDX-License-Identifier: Community-Spec-1.0

# LanguageTag

## Summary

A string constrained to the IETF BCP 47 language tag format,
which is used to identify human languages.

## Description

A language tag provides a standardized way to identify the language of content,
a performance, or an action.

The language tag shall be in the format as describes in the Section 2 of
[IETF RFC 5646](https://datatracker.ietf.org/doc/rfc5646/) (part of BCP 47).

Each tag consists of one or more subtags separated by hyphens
("-", Unicode U+002D).
Subtags contain only basic Latin letters and digits.

Language tags and their subtags are to be treated as case insensitive.

*Example*

- `es` (Spanish)
- `es-UY` (Spanish as used in Uruguay)
- `hau-NG` (Hausa as used in Nigeria)
- `hy-Latn-IT-arevela` (Eastern Armenian written in Latin script, as used in Italy)
- `sl-rozaj-biske` (San Giorgio dialect of Resian dialect of Slovenian)
- `yue-Hant-HK` (Cantonese using traditional Han characters, as spoken in Hong Kong)

See the
[IETF language tag Wikipedia page](https://en.wikipedia.org/wiki/IETF_language_tag)
for more information.

## Metadata

- name: LanguageTag
- SubclassOf: xsd:string

## Format

- pattern: ^([a-zA-Z]{2,8}|[iIxX])(-[a-zA-Z0-9]{1,8})*$
