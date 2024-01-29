SPDX-License-Identifier: Community-Spec-1.0

# LifecycleScopeType

## Summary

Provide an enumerated set of software lifecycle phases that can provide context to relationships.

## Description

This enumeration summarizes common phases when dependency and other relationships, have different implications, based on their context.  For example,  a build dependency, may have different implications than a runtime dependency.

## Metadata

- name: LifecycleScopeType

## Entries

- design: A relationship has specific context implications during an element's design.
- development: A relationship has specific context implications during development of an element. 
- build: A relationship has specific context implications during an element's build, during development.
- test: A relationship has specific context implications during an element's testing, during development.
- runtime: A relationship has specific context implications when an element is executing. 
- other: A relationship has other specific context information necessary to capture that the above set of enumerations does not handle.
