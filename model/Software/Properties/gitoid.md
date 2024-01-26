SPDX-License-Identifier: Community-Spec-1.0

# gitoid

## Summary

Used to record the artifact’s gitoid: a canonical, unique, immutable identifier that can be used for software integrity verification.

## Description

The gitoid is a canonical, unique, immutable artifact identifier for each software artifact.
The gitoid for any software artifact can be calculated and recorded in SPDX 3.0 Snippet, File, or Package Elements.

The gitoid is defined as the Git Object Identifier of type `blob` of the software artifact, expressed in the [gitoid URI scheme](https://www.iana.org/assignments/uri-schemes/prov/gitoid).

The OmniBOR ID for the OmniBOR Document associated with a software artifact should not be recorded in this field. Rather, OmniBOR IDs should be recorded in the SPDX Element's ExternalIdentifier property.

## Metadata

- name: contentIdentifier
- Nature: DataProperty
- Range: xsd:anyURI

