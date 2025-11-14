SPDX-License-Identifier: Community-Spec-1.0

# ContactPointRelationshipType

## Summary

Information about the type of contact point for `ContactPointRelationship`s.

## Description

Provides information about the type of contact point. For example, the `securityVulnerability` contact type can represent a type of contact to be used for reporting security vulnerabilities.

## Metadata

- name: ContactPointRelationshipType

## Entries

- compliance: A contact point for compliance (i.e. export control, licensing).
- other: A generic contact point to be used when the contact type does not match any of the other options.
- securityVulnerability: A contact for reporting security vulnerabilities.
- support: A contact point for support.
