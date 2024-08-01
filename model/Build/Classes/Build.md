SPDX-License-Identifier: Community-Spec-1.0

# Build

## Summary

Class that describes a build instance of software/artifacts.

## Description

A build is a representation of the process in which a piece of software or
artifact is built. It encapsulates information related to a build process and
provides an element from which relationships can be created to describe the
build's inputs, outputs, and related entities (e.g. builders, identities,
etc.).

Definitions of "buildType", "configSourceEntrypoint", "configSourceUri",
"parameters" and "environment" follow those defined in
[SLSA Provenance v0.2](https://slsa.dev/provenance/v0.2).

ExternalIdentifier of type "urlScheme" may be used to identify build logs.
In this case, the comment of the ExternalIdentifier should be "LogReference".

Note that buildStartTime and buildEndTime are optional, and may be omitted to
simplify creating reproducible builds.

## Metadata

- name: Build
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- buildType
  - type: xsd:anyURI
  - minCount: 1
  - maxCount: 1
- buildId
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- configSourceEntrypoint
  - type: xsd:string
  - minCount: 0
- configSourceUri
  - type: xsd:anyURI
  - minCount: 0
- configSourceDigest
  - type: /Core/Hash
  - minCount: 0
- parameters
  - type: /Core/DictionaryEntry
  - minCount: 0
- buildStartTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- buildEndTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- environment
  - type: /Core/DictionaryEntry
  - minCount: 0
