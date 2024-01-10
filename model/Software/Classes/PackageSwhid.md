SPDX-License-Identifier: Community-Spec-1.0

# PackageSwhid

## Summary

Verification method to be used for a Package which represents an artifact that logically binds a number of single files together using the SoftWare Heritage persistent Identifiers.

## Description

[SoftWare Heritage persistent Identifiers](https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html) (SWHID) are guaranteed to remain stable (persistent) over time and can be computed from the artefact itself for the purpose of verification.

Note that in addition to being used as a verification method, SWHID is also a reccomended ExternalIdentifier to be used for the package with the ExternalIdentifierType swhid.

## Metadata

- name: PackageSwhid
- SubclassOf: /Software/PackageVerification

## Properties

- swhid
  - type: xsd:string
