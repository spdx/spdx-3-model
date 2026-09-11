SPDX-License-Identifier: Community-Spec-1.0

# contentModality

## Summary

Provides information about the content modality of an Element or a property.

## Description

A content modality describes the nature of the information channel or sensory
type through which content is communicated, perceived, or processed by agents
and software. This is used to specify how the content is intended to be
exchanged or presented (e.g., text, image, audio, video).

Use the value "other" if the modality is not listed in the defined `Modality`
vocabulary, and you should optionally provide the specific modality in the
`comment` property.

## Metadata

- name: contentModality
- Nature: ObjectProperty
- Range: Modality
