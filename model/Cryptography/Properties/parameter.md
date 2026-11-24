SPDX-License-Identifier: Community-Spec-1.0

# parameter

## Summary

Parameter of a cryptographic algorithm.

## Description

Parameter of a cryptographic algorithm. 

The parameter `Key` is the parameter name from the SPDX Cryptographic Algorithm List.
The parameter `Value` is the parameter value. If more than one value is needed, use a Cryptographic Algorithm Parameter Expression string for the Value; e.g., Key: `operationMode`, Value: `[GCM|CCM]`.

## Metadata

- name: parameter
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
