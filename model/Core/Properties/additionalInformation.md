SPDX-License-Identifier: Community-Spec-1.0

# additionalInformation

## Summary

Additional information for an element when a standard property is unavailable.

## Description

Provides additional information about an element.
It is structured as a key-value pair and used to extend the element's
description with domain-specific or context-dependent information that is not
explicitly covered by other standard properties.

An `additionalInformationSpecificaiton` can be provided for the interpretation
of the key and/or its values.

*Usage guidance:*

This property is intended strictly for domain-specific, custom, or experimental
metadata that cannot be represented by any other standardized property within
the SPDX 3 specification.
Implementers should not use this property if an explicit, dedicated property
exists elsewhere in the specification to represent the target data.
Overuse of this property reduces semantic interoperability and should be
avoided.

For the rich additional information that the key of string and value of string
pair structure cannot fully captured, an extension based on the Extension
profile can be considered.

*Difference from `comment` property:*

While `comment` is a comment of a creator of an Element towards the
Element, the `additionalInformation` can be an intrinsic property of the
Element itself.

## Metadata

- name: additionalInformation
- Nature: ObjectProperty
- Range: DictionaryEntry
