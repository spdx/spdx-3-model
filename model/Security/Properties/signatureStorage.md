SPDX-License-Identifier: Community-Spec-1.0

# signatureStorage

## Summary

A reference to a object that contains the cryptographic signature data.

## Description

The signatureStorage property provides a reference to an object that contains the signature data. In many signing formats (such as detached signatures), the signature is intentionally stored separately from the signed content to maintain clean separation between the data and its verification information.

## Metadata

- name: signatureStorage
- Nature: ObjectProperty
- Range: /Core/Artifact
