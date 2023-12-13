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
- archive: the Element is an archived collection of one or more files (.tar, .zip, etc)
- bom: Element is a bill of materials
- configuration: Element is configuration data
- container: the Element is a container image which can be used by a container runtime application
- data: Element is data
- device: the Element refers to a chipset, processor, or electronic board
- diskImage: the Element refers to a disk image that can be written to a disk, booted in a VM, etc. A disk image typically contains most or all of the components necessary to boot, such as bootloaders, kernels, firmware, userspace, etc.
- deviceDriver: Element represents software that controls hardware devices
- documentation: Element is documentation
- evidence: the Element is the evidence that a specification or requirement has been fulfilled
- executable: Element is an Artifact that can be run on a computer
- file: the Element is a single file which can be independently distributed (configuration file, statically linked binary, Kubernetes deployment, etc)
- filesystemImage: the Element is a file system image that can be written to a disk (or virtual) partition
- firmware: the Element provides low level control over a device's hardware
- framework: the Element is a software framework
- install: the Element is used to install software on disk
- library: the Element is a software library
- manifest: the Element is a software manifest
- model: the Element is a machine learning or artificial intelligence model
- module: the Element is a module of a piece of software
- operatingSystem: the Element is an operating system
- other: the Element doesn't fit into any of the other categories
- patch: Element contains a set of changes to update, fix, or improve another Element
- platform: Element represents a runtime environment
- requirement: the Element provides a requirement needed as input for another Element
- source: the Element is a single or a collection of source files
- specification: the Element is a plan, guideline or strategy how to create, perform or analyse an application
- test: The Element is a test used to verify functionality on an software element 
