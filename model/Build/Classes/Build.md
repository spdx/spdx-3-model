SPDX-License-Identifier: Community-Spec-1.0

# Build

## Summary

Class that describes a build instance of software/artifacts.

## Description

A build is a representation of the process in which a piece of software or artifact is built. It encapsulates information related to a build process and
provides an element from which relationships can be created to describe the build's inputs, outputs, and related entities (e.g. builders, identities, etc.).

Definitions of "BuildType", "ConfigSource", "Parameters" and "Environment" follow
those defined in [SLSA provenance](https://slsa.dev/provenance/v0.2).

ExternalIdentifier of type "urlScheme" may be used to identify build logs. In this case, the comment of the ExternalIdentifier should be "LogReference".

## Metadata

- name: Build
- SubclassOf: Core:Element
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
  - type: Hash
  - minCount: 0
- parameters
  - type: xsd:map<string>string
  - minCount: 0
- buildStart
  - type: xsd:dateTime
  - minCount:0
  - maxCount:1
- buildEnd
  - type: xsd:dateTime
  - minCount:0
  - maxCount:1
- environment
  - type: xsd:map<string>string
  - minCount: 0
