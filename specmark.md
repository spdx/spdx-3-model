# Markdown for SPDX 3 model specification

The SPDX 3 model is written in a constrained subset of a Markdown flavour
([Python-Markdown](https://www.mkdocs.org/user-guide/writing-your-docs/#writing-with-markdown)
which is used by [MkDocs](https://www.mkdocs.org/) site generator).

Specific headings and formatting are used to provide information for the
generation of a machine-readable specification, by the
[spec-parser](https://github.com/spdx/spec-parser/).

Organisation:

- All the model files are inside the `model/` directory.
- Profiles are organized in subdirectories (`Core/`, `Dataset/`, etc.)
- Entities are organised by type in subdirectories (`Classes/`, `Datatypes/`,
  `Individuals/`, `Properties/`, and `Vocabularies/`).
- Each entity (class, datatype, individual, property, and vocabulary)
  is defined in a distinct file.

Content structure:

- Each file must start with SPDX license information:
  `SPDX-License-Identifier: Community-Spec-1.0`
  and follows by one blank line.
- The content immediately after the license information must begin with an
  H1 heading containing the entity's name.
- Each entity type has a predefined set of allowed H2 headings and
  labeled lists that must be used to structure its content.
- There must be a blank line before and after a heading.
- There must be a blank line before the beginning of a list.
- There must be a blank line after the end of a list.

## Classes

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

### Class example

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

## Datatypes

Allowed headings:

- Summary
- Description
- Metadata
  - name: \<datatype_name\>
  - SubclassOf: \<class_name\>
- Format
  - pattern: \<regular_expression\>

### Datatype example

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

## Individuals

Allowed headings:

- Summary
- Description
- Metadata
  - name: \<individual_name\>
  - type:  \<class_name\>
- Property Values
  - \<property_name\>: \<property_value\>
  - ...

### Individual example

```markdown
SPDX-License-Identifier: Community-Spec-1.0

# NoneElement

## Summary

An Individual Value example.

## Description

Blah.

## Metadata

- name: NoneElement
- type: Element

## Property Values

- name: "NONE"
```

## Properties

Allowed headings:

- Summary
- Description
- Metadata
  - name: \<property_name\>
  - Nature: "DataProperty" OR "ObjectProperty"
  - Range: \<datatype_name\> OR \<class_name\>

### Property example

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

## Vocabularies

Allowed headings:

- Summary
- Description
- Metadata
  - name
- Entries
  - \<entry_name\>: \<entry_description\>
  - ...

Each entry in Entries must be written in a single line.

### Vocabulary example

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
