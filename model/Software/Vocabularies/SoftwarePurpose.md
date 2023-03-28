SPDX-License-Identifier: Community-Spec-1.0

# SoftwarePurpose

## Summary

Provides information about the primary purpose of an Element.

## Description

This field provides information about the primary purpose of an Element.
Software Purpose is intrinsic to how the Element is being used rather than the content of the Element.
This field is a reasonable estimate of the most likely usage of the Element
from the producer and consumer perspective from which both parties can draw conclusions
about the context in which the Element exists.

## Metadata

- name: SoftwarePurpose

## Entries

- application: the Element is a software application
- archive: the Element refers to an archived collection of files (.tar, .zip, etc)
- bom: TODOdescription
- configuration: TODOdescription
- container: the Element refers to a container image which can be used by a container runtime application
- data: TODOdescription
- device: the Element refers to a chipset, processor, or electronic board
- documentation: TODOdescription
- executable: TODOdescription
- file: the Element is a single file which can be independently distributed (configuration file, statically linked binary, Kubernetes deployment, etc)
- firmware: the Element provides low level control over a device's hardware
- framework: the Element is a software framework
- install: the Element is used to install software on disk
- library: the Element is a software library
- module: TODOdescription
- operatingSystem: the Element refers to an operating system
- other: the Element doesn't fit into any of the other categories
- patch: TODOdescription
- source: the Element is a collection of source files

