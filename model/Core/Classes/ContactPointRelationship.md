SPDX-License-Identifier: Community-Spec-1.0

# ContactPointRelationship

## Summary

Provide context for a contact point relationship from an Artifact to an Agent.

## Description

Defines a specific contact point relationship linking an Artifact to an Agent.

For example, a software package (Artifact) may designate a security
vulnerability contact point (Agent) as the official channel for researchers
to report security vulnerabilities.

This relationship is restricted to the `hasContactPoint` relationship type.

## Metadata

- name: ContactPointRelationship
- SubclassOf: Relationship
- Instantiability: Concrete

## Properties

- contactType
  - type: ContactType
  - minCount: 1
  - maxCount: 1
