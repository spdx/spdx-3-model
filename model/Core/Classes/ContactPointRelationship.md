SPDX-License-Identifier: Community-Spec-1.0

# ContactPointRelationship

## Summary

A contact point from an Artifact to an Agent.

## Description

Specifies a point of contact specific to an Artifact. For example, a software package may have a security contact point that researchers should use for reporting security vulnerabilities. This relationship is restricted to using the `hasContactPoint` relationship type.

## Metadata

- name: ContactPointRelationship
- SubclassOf: Relationship
- Instantiability: Concrete

## Properties

- contactType
  - type: ContactPointRelationshipType
  - minCount: 1
  - maxCount: 1
