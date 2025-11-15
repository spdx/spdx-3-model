SPDX-License-Identifier: Community-Spec-1.0

# TestProcess

## Summary

Test Process defines the testing process for an element.

## Description

Tests are processes based on requirements. The process's requirements are met by the test process.

Relationship:

For each `TestProcess` there is at least one `/Core/Relationship` class or subclass with the relationshipType of 'contains’ on the from and a `Requirements` class or subclass on the to.

## Metadata

- name: TestProcess
- SubclassOf: UseProcess
- Instantiability: Concrete
