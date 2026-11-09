SPDX-License-Identifier: Community-Spec-1.0

# tokenCount

## Summary

Number of text tokens in a software artifact.

## Description

tokenCount records the number of tokens in a software artifact containing
text data.

Token counts depend on the tokenization method used;
the same text can yield different counts across different tokenizers.

The tokenization method should be documented separately --
for example, in the `description` of the element, or in the
`dataCollectionProcess` or `dataPreprocessing` properties if the element is
a `/Dataset/DatasetPackage`.

## Metadata

- name: tokenCount
- Nature: DataProperty
- Range: xsd:nonNegativeInteger
