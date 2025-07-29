SPDX-License-Identifier: Community-Spec-1.0

# requirementNamespace

## Summary

Namespace of the requirement.

## Description

The requirement namespace is used to get a lasting connection between the project, the requirement has been created for, and the actual requirement. E.g. in Zephyr Project, providing an RTOS, all requirements IDs start with "ZEP", to make sure that if requirements are used in bigger systems, that e.g. re-use requirements from Zephyr, Xen and whatever, it is clear where the requirement came from. This is a good practice that is used in requirements engineering for a long time.

## Metadata

- name: requirementNamespace
- Nature: RequirementProperty
- Range: xsd:string
