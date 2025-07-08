SPDX-License-Identifier: Community-Spec-1.0

# Component

## Summary

Refers to an abstract, conceptual software entity.

## Description

A Component represents an abstract, conceptual software entity,
independent of any specific version, supplier, or packaging format.
It serves as a high-level identifier for a piece of software,
such as "Linux kernel", "OpenSSL," or "Log4j".

The primary purpose of a Component is to group multiple related
software [Packages](./Package.md) and to be able to act as a central point
for storing metadata that is common across all those packages.
This might include information like the project's primary license,
its official homepage, or its originating author or organization.

## Metadata

- name: Component
- SubclassOf: /Core/Element

## Properties

- attributionText
  - type: xsd:string
  - minCount: 0
- copyrightText
  - type: xsd:string
  - minCount: 0
- homePage
  - type: xsd:anyURI
  - minCount: 0
- packageVersion
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- sourceInfo
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Core/Element/name
  - minCount: 1

