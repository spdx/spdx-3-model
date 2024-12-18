# Translation

Translation of the SPDX specification.

## Table of contents

- [Model translation](#model-translation)
- [Model translation example](#model-translation-example)

## Model translation

Only model summaries, descriptions, and vocabulary entry descriptions can be
translated.

Other content, such as model metadata, cannot be translated.

To add translations, include them directly at the end of the model file
using the [same set of heading names][headings]
followed by a language tag (e.g.,
`## Summary @ga` for a summary in Irish,
`## Description @kok` for a description in Konkani, or
`## Entries @sr-Latn` for an entry list in Serbian written using
the Latin script).

These textual descriptions are encoded as a
["language-tagged string"][language-tagged-string] in RDF.
Therefore, the language tag used to identify the language must follow the
well-formedness rules defined in [IETF BCP 47 (RFC 5646)][rfc5646].
Appendix A of that document provides examples of valid language tags.

English remains the normative language in all cases.

[headings]: ./format.md#syntax
[language-tagged-string]: https://www.w3.org/TR/rdf11-concepts/#dfn-language-tagged-string
[rfc5646]: https://datatracker.ietf.org/doc/rfc5646

### Model translation example

Here's an example of an `AnnotationType` vocabulary with translations for
Japanese, Chinese (simplified script), and Chinese (traditional script),
sorted by language tag.

Note that the "Metadata" section and the names of entries within the "Entries"
section remain untranslated:

```markdown
SPDX-License-Identifier: Community-Spec-1.0

# AnnotationType

## Summary

Specifies the type of an annotation.

## Description

AnnotationType specifies the type of an annotation.

## Metadata

- name: AnnotationType

## Entries

- review: Used when someone reviews the Element.

## Summary @ja

注釈の種類を指定します。

## Description @ja

AnnotationType は、注釈の種類を指定します。

## Entries @ja

- review: 誰かが Element をレビューし、注釈をつけたときに使われます。

## Summary @zh-Hans

指定注释的类型。

## Description @zh-Hans

AnnotationType指定注释的类型。

## Entries @zh-Hans

- review: 当其人评审元素时使用的注释。

## Summary @zh-Hant

指定註解的類型。

## Description @zh-Hant

AnnotationType指定註解的類型。

## Entries @zh-Hant

- review: 當其人審核元素時使用的註解。

```

The above model Markdown file will generate the following RDF
(showing partial):

```ttl
<https://spdx.org/rdf/3.0.1/terms/Core/AnnotationType> a owl:Class;
    rdfs:comment "Specifies the type of an annotation."@en ;
    rdfs:comment "注釈の種類を指定します。"@ja ;
    rdfs:comment "指定注释的类型。"@zh-hans ;
    rdfs:comment "指定註解的類型。"@zh-hant ;
    .
```
