---
SPDX-FileCopyrightText: 2024 SPDX Project
SPDX-License-Identifier: Community-Spec-1.0
---

# Markdown for SPDX 3 model specification

The SPDX 3 model is written in a constrained subset of a Markdown markup
language*, with predefined headings.

This document provides guidelines for writing model files in the specific
syntax used by SPDX 3.

Following these guidelines ensures consistency and avoids rendering issues when
using spec-parser and MkDocs to generate model ontologies and model textual
specifications.

## Table of contents

- [Overview](#overview)
- [Directory organisation](#directory-organisation)
- [File content structure and formatting](#file-content-structure-and-formatting)
  - [Model file example](#model-file-example)
- [Syntax](#syntax)
  - [Classes](#classes)
  - [Datatypes](#datatypes)
  - [Individuals](#individuals)
  - [Properties](#properties)
  - [Vocabularies](#vocabularies)
- [Writing style](#writing-style)
- [Translation](#translation)

## Overview

Each model element (class, datatype, individual, property, and vocabulary)
is defined in a distinct file.

Specific headings and formatting are used to provide information for the
generation of a machine-readable specification, in
[Resource Description Framework (RDF)](https://en.wikipedia.org/wiki/Resource_Description_Framework)
data model, by the [spec-parser](https://github.com/spdx/spec-parser/).

For instance, a summary listed under the "Summary" heading will be represented
as a `rdfs:comment` in the RDF file. Likewise, a value specified for the
"minCount" of a property name under the "Properties" heading will be
translated into a `sh:minCount` in the RDF file.
See [an example](#model-file-example).

Descriptions provided under the "Description" heading are intended for human
reference and will not be incorporated into the RDF file.

The same Markdown files are used to generate the HTML files for
[the website](https://spdx.github.io/spdx-spec/).

*The Markdown flavour used for the specification is
[Python-Markdown](https://www.mkdocs.org/user-guide/writing-your-docs/#writing-with-markdown)
as it is used by [MkDocs](https://www.mkdocs.org/) site generator.
It differs slightly from
[GitHub Flavored Markdown Spec](https://github.github.com/gfm/).

## Directory organisation

Apart from the content in each individual file, the file itself has to be
placed in a specific location, as the spec-parser implies some model semantic
from the location of the file:

- Each element (class, datatype, individual, property, and vocabulary)
  is defined in a distinct file.
- Model file names are case-sensitive and must be identical to the element they
  represent.
- All model files must be located within the `model/` directory.
- Profiles should be organised into subdirectories (e.g., `Core/`, `Dataset/`).
- Elements should be categorised by their type in subdirectories (e.g.,
  `Classes/`, `Datatypes/`, `Individuals/`, `Properties/`, `Vocabularies/`).

File and directory organisation:

```text
.
├── model
:   :
│   ├── Core
│   │   ├── Classes
:   :   :   :
│   │   │   └── Tool.md
│   │   ├── Datatypes
:   :   :   :
│   │   │   └── SemVer.md
│   │   ├── Individuals
:   :   :   :
│   │   │   └── NoneElement.md
│   │   ├── Properties
:   :   :   :
│   │   │   └── verifiedUsing.md
│   │   └── Vocabularies
:   :       :
│   │       └── SupportType.md
│   ├── Dataset
:   :
```

The living repository at
<https://github.com/spdx/spdx-3-model/tree/main/model>
is the best reference.

## File content structure and formatting

Each model file must adhere to a strict content structure:

- All files must be encoded in UTF-8.
- Each file must start with SPDX license information:
  `SPDX-License-Identifier: Community-Spec-1.0`
  and follows by one blank line.
- The content immediately after the license information must begin with an
  H1 heading containing the element's name.
- Each element type has a predefined set of [allowed H2 headings](#syntax) and
  labeled lists that must be used to structure its content.

Additionally, since MkDocs uses a strict
[Python-Markdown](https://python-markdown.github.io/#differences),
each model file must adhere to specific formatting guidelines:

- Blank lines:
  - There must be a blank line before and after a heading.
  - There must be a blank line before and after a list.
- Indentation:
  - Use spaces instead of tabs.
  - When a list item consists of multiple paragraphs, each subsequent paragraph
    in a list item must be indented by 4 spaces. This applies to any
    block-level elements nested in a list, including paragraphs, sub-lists,
    blockquotes, code blocks, etc.

### Model file example

This example is taken from the actual file for
[SimpleLicensingText](https://github.com/spdx/spdx-3-model/blob/main/model/SimpleLicensing/Classes/SimpleLicensingText.md?plain=1)
class.
Its name and location in the repository is
`model/SimpleLicensing/Classes/SimpleLicensingText.md`.

```markdown
SPDX-License-Identifier: Community-Spec-1.0

# SimpleLicensingText

## Summary

A license or addition that is not listed on the SPDX License List.

## Description

A SimpleLicensingText represents a License or Addition that is not listed on
the [SPDX License List](https://spdx.org/licenses),
and is therefore defined by an SPDX data creator.

## Metadata

- name: SimpleLicensingText
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- licenseText
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
```

will give this RDF graph
(in [Turtle syntax](https://en.wikipedia.org/wiki/Turtle_(syntax))):

```ttl
<https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/SimpleLicensingText> a owl:Class,
        sh:NodeShape ;
    rdfs:comment "A license or addition that is not listed on the SPDX License List."@en ;
    rdfs:subClassOf <https://spdx.org/rdf/3.0.1/terms/Core/Element> ;
    sh:nodeKind sh:IRI ;
    sh:property [ sh:datatype xsd:string ;
            sh:maxCount 1 ;
            sh:minCount 1 ;
            sh:nodeKind sh:Literal ;
            sh:path <https://spdx.org/rdf/3.0.1/terms/SimpleLicensing/licenseText> ] .
```

## Syntax

### Classes

Allowed headings:

- Summary
- Description
- Metadata
  - name: \<class_name\>
  - SubclassOf: \<class_name\> OR "none" *(Must have one if Instantiability is "Concrete")*
  - Instantiability: "Abstract" OR "Concrete" *(Default: Concrete)*
- Properties *(Optional)*
  - \<property_name\>
    - type: \<datatype_name\>
    - minCount: \<number\> *(Optional)*
    - maxCount: \<number\> *(Optional)*
  - ...
- External properties restrictions *(Optional)*
  - \<external_property_name\>
    - minCount: \<number\> *(Optional)*
    - maxCount: \<number\> *(Optional)*
  - ...

#### Class example

```markdown
SPDX-License-Identifier: Community-Spec-1.0

# Bot

## Summary

An automated agent.

## Description

A class example.

## Metadata

- name: Bot
- SubclassOf: Agent
- Instantiability: Concrete

## Properties

- prohibitedTask
  - type: xsd:string
  - minCount: 1

## External properties restrictions

- /Core/Element/name
  - minCount: 1
```

### Datatypes

Allowed headings:

- Summary
- Description
- Metadata
  - name: \<datatype_name\>
  - SubclassOf: \<class_name\>
- Format
  - pattern: \<regular_expression\>

#### Datatype example

```markdown
SPDX-License-Identifier: Community-Spec-1.0

# DateTime

## Summary

A string representing a specific date and time.

## Description

A DateTime is a string representation of a specific date and time.

## Metadata

- name: DateTime
- SubclassOf: xsd:dateTimeStamp

## Format

- pattern: ^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$
```

### Individuals

Allowed headings:

- Summary
- Description
- Metadata
  - name: \<individual_name\>
  - type: \<class_name\>
  - IRI: \<IRI\>
- Property Values
  - \<property_name\>: \<property_value\>
  - ...

#### Individual example

```markdown
SPDX-License-Identifier: Community-Spec-1.0

# NoneElement

## Summary

A named individual example.

## Description

A named individual of Element class that representing none.

## Metadata

- name: NoneElement
- type: Element

## Property Values

- name: "NONE"
```

### Properties

Allowed headings:

- Summary
- Description
- Metadata
  - name: \<property_name\>
  - Nature: "DataProperty" OR "ObjectProperty"
  - Range: \<datatype_name\> OR \<class_name\>

#### Property example

```markdown
SPDX-License-Identifier: Community-Spec-1.0

# sensor

## Summary

Describes a sensor used for collecting the data.

## Description

Describes a sensor that was used for collecting the data
and its calibration value as a key-value pair.

## Metadata

- name: sensor
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
```

### Vocabularies

Allowed headings:

- Summary
- Description
- Metadata
  - name
- Entries
  - \<entry_name\>: \<entry_description\>
  - ...

Each entry in Entries must be written in a single line.

#### Vocabulary example

```markdown
SPDX-License-Identifier: Community-Spec-1.0

# RpsType

## Summary

Specifies the hand shapes used in Rock-Paper-Scissors.

## Description

RpsType specifies the type of a hand shape.

## Metadata

- name: RpsType

## Entries

- paper: A flat, open hand.
- rock: A closed fist.
- scissors: Two fingers extended, forming a V shape.
```

## Writing style

To ensure clear and consistent documentation generation, follow these
recommendations when writing paragraph text and incorporating links.

- **Avoid overly long paragraphs.**

    Breaking up text into smaller paragraphs, using bullet points, or creating numbered lists can significantly improve readability and comprehension by separating distinct concepts, processes, criteria, or categories.
    This makes the specification easier to scan and understand.

- **Avoid bare URLs.**

    Always provide a descriptive label for each link. Avoid using bare URLs.
    This improves accessibility for screen readers and provides context for
    users.

    Here's an example of a **recommended** link using descriptive text:

    ```Markdown
    [SPDX Project](https://spdx.dev/)
    ```

    Here's an example of a **not recommended** bare URL:

    ```Markdown
    https://spdx.dev/
    ```

- **Bare URLs: Use with caution.**

    While descriptive link text is generally preferred for better readability
    and accessibility,
    there may be specific instances where bare URLs might be necessary.
    This could include cases where URLs need to be clearly visible in both
    digital and print formats or when the URL serves as a metadata value.

    The IRI field in the Metadata section MUST use a bare URL:

    ```markdown
    ## Metadata

    - name: SpdxOrganization
    - type: Organization
    - IRI: https://spdx.org/
    ```

    Be aware that MkDocs *will not* automatically convert bare URLs into
    clickable links.

    To ensure that URLs remain clickable on the specification website,
    you should enclose them within angle brackets (`<` and `>`).

    Here's an example of a **clickable** URL:

    ```Markdown
    SPDX Project GitHub: <https://github.com/spdx/>
    ```

    Here's an example of an **unclickable** URL:

    ```Markdown
    SPDX Project GitHub: https://github.com/spdx
    ```

- **Standard format for RFC URLs.**

    When referencing RFCs (Request for Comments) or other relevant IETF
    documents, utilize the following format for the URL:

    ```text
    https://datatracker.ietf.org/doc/<number>/
    ```

    Here's an example of a **correct** link to an RFC:

    ```Markdown
    [RFC 3986](https://datatracker.ietf.org/doc/rfc3986/)
    ```

    Here are examples of **incorrect** links to RFCs:

    Incorrect. Missing trailing slash:

    ```Markdown
    [RFC 3986](https://datatracker.ietf.org/doc/rfc3986)
    ```

    Incorrect. Linking to HTML version:

    ```Markdown
    [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)
    ```

    Incorrect. Using a different website:

    ```Markdown
    [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986)
    ```

- **Code Highlighting.**

    When using code blocks, specify the appropriate computer language code.
    For instance, use `json` for JSON, `yaml` for YAML, and `text` for plain
    text. This ensures correct syntax highlighting and improves readability.

    For example, start a JSON code block with this markup:

    ```markdown
    ```json
    ```

    A code block with a specified language will be rendered with syntax
    highlighting, appearing as follows:

    ```json
    {
      "type": "Relationship",
      "from": "urn:spdx.dev:28984",
      "to": ["urn:acme-4.2"]
    }
    ```

    A code block without a specified language will be rendered without syntax
    highlighting, appearing as follows:

    ```text
    {
      "type": "Relationship",
      "from": "urn:spdx.dev:28984",
      "to": ["urn:acme-4.2"]
    }
    ```

## Translation

Model summaries, descriptions, and vocabulary entry descriptions can be
translated. Please see [translation.md](./translation.md) for details.
