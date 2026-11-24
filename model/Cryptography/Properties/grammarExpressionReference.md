SPDX-License-Identifier: Community-Spec-1.0

# grammarExpressionReference

## Summary

Maps parameter positions in a Cryptographic Algorithm Expression to parameter names for the algorithm.

## Description

Maps parameter positions in a Cryptographic Algorithm Expression to parameter names for the algorithm.
A parameter value at position N after the algorithm identifier is interpreted as the value of the parameter assigned to position N. Each dictionary entry maps a parameter position to a parameter name.

Entry rules:
- Dictionary keys MUST be positive integers.
- Dictionary keys MUST start at 1.
- Dictionary keys MUST be consecutive, with no gaps.
- Dictionary keys MUST NOT be duplicated.
- Dictionary values MUST be parameter names defined for the algorithm.

## Metadata

- name: grammarExpressionReference
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry

