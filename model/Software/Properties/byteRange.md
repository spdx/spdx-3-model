SPDX-License-Identifier: Community-Spec-1.0

# byteRange

## Summary

Defines the byte range in the original host file that the snippet information applies to.

## Description

This field defines the byte range in the original host file that the snippet information applies to.
A range of bytes is independent of various formatting concerns, and the most accurate way 
of referring to the differences. The choice was made to start the numbering of 
the byte range at 1 to be consistent with the W3C pointer method vocabulary.

## Metadata

- name: byteRange
- Nature: DataProperty
- Range: positiveIntegerRange

