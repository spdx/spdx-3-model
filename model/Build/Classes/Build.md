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

ExternalIdentifier of type "urlScheme" may be used to identify build logs.
In this case, the comment of the ExternalIdentifier shall be "LogReference".

Note that `startTime` and `endTime` are optional, and may be omitted to
simplify creating reproducible builds.

`buildStartTime` and `buildEndTime` are deprecated.
Migrate to `startTime` and `endTime`
`buildStartTime` and `buildEndTime` will be removed in a future release.

## Metadata

- name: Build
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- /Core/endTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- /Core/startTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
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
- parameter
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
