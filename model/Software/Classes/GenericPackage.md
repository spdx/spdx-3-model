SPDX-License-Identifier: Community-Spec-1.0

# GenericPackage

## Summary

Refers to a generic, conceptual software entity.

## Description

A GenericPackage represents a generic, conceptual software entity,
independent of any specific version, supplier, or packaging format.
It serves as a high-level identifier for a piece of software,
such as "Linux kernel", "OpenSSL," or "Log4j".

The primary purpose of a GenericPackage is to group multiple related
software [Packages](./Package.md) and to be able to act as a central point
for storing metadata that is common across all those packages.
This could include information like the project's primary license,
its official homepage, or its originating author or organization.

Since there could be relationships between GenericPackages
and between GenericPackages and Packages, values of different properties
could be different.
The precedence rule is that every attribute of a more specific entity
overwrites attribute values of a more general entity.
This way, property values of a Package are always valid;
When an GenericPackage is related to a Package via a `hasInstance` relationship, the GenericPackage’s properties serve only as annotations—they provide additional context or metadata but do not set or update the property values on the Package. If the Package does not define a particular property, the GenericPackage’s value can be used as an annotation, but it does not become the Package’s own property. This annotation behavior extends recursively through chains of GenericPackages, always respecting the precedence of more specific entities.
The chain can continue further to more GenericPackages,
as long as there are "parent" GenericPackage and no values have been specified.

A Package shall have no more than one `hasInstance` relationship from `GenericPackage` Elements.

It should be noted that this class will rarely appear in SBOMs,
where exact Packages should be listed.

## Metadata

- name: GenericPackage
- SubclassOf: /Core/Element
- Instantiability: Concrete

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
