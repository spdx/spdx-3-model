SPDX-License-Identifier: Community-Spec-1.0

# specifiedKeySize

## Summary

The default key size, in bits, or a range of key sizes, determined by the algorithm's authors, standardization bodies, or compliance agencies.

## Description

The default key size, in bits, or a range of key sizes that is specified for a cryptographic algorithm or security mechanism by the algorithm’s authors, standardization bodies, or compliance agencies.
If the key size is not a range, set the `beginIntegerRange` and `endIntegerRange` to the same value.

## Metadata

- name: specifiedKeySize
- Nature: ObjectProperty
- Range: /Core/PositiveIntegerRange
