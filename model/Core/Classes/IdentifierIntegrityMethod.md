SPDX-License-Identifier: Community-Spec-1.0

# IdentifierIntegrityMethod

## Summary

An integrity method which uses an `ExternalIdentifier` for integrity verification.

## Description

Some (but not all) of the External Identifier values can be computed from the artefact itself for the purpose of verification.

The `Element` using this integrity method MUST have a matching `externalIdentifier` using the `externalIdentifierType` defined in this integrity method class.

The following `ExternalIdentifierType`s support such verification:
- gitoid: https://www.iana.org/assignments/uri-schemes/prov/gitoid Gitoid stands for Git Object ID and a gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent the software Artifact ID or the OmniBOR Identifier for the software artifact's associated OmniBOR Document; this ambiguity exists because the OmniBOR Document is itself an artifact, and the gitoid of that artifact is its valid identifier. Omnibor is a minimalistic schema to describe software Artifact Dependency Graphs. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's ContentIdentifier property. Gitoids calculated on the OmniBOR Document (OmniBOR Identifiers) should be recorded in the SPDX 3.0 Element's ExternalIdentifier property.
- swhid: https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html

## Metadata

- name: IdentifierIntegrityMethod
- SubclassOf: IntegrityMethod

## Properties

- externalIdentifierType
  - type: ExternalIdentifierType
  - minCount: 1
  - maxCount: 1
