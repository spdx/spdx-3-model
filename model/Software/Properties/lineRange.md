SPDX-License-Identifier: Community-Spec-1.0

# lineRange

## Summary

Defines the line range in the original host file that the snippet information applies to.

## Description

This field defines the line range in the original host file that the snippet information applies to.
If there is a disagreement between the byte range and line range, the byte range values will take precedence.
A range of lines is a convenient reference for those files where there is a known line delimiter. 
The choice was made to start the numbering of the lines at 1 to be consistent with the W3C pointer method vocabulary.

## Metadata

- name: lineRange
- Nature: DataProperty
- Range: positiveIntegerRange

