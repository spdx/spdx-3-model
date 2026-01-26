SPDX-License-Identifier: Community-Spec-1.0

# SoftwarePurpose

## Summary

Provides information about the primary purpose of an Element.

## Description

This field provides information about the primary purpose of an Element.

Software Purpose is intrinsic to how the Element is being used rather than the
content of the Element.

This field is a reasonable estimate of the most likely usage of the Element
from the producer and consumer perspective from which both parties can draw
conclusions about the context in which the Element exists.

## Metadata

- name: SoftwarePurpose

## Entries

- application: The Element is a software application.
- archive: The Element is an archived collection of one or more files (.tar, .zip, etc.).
- bom: The Element is a bill of materials.
- configuration: The Element is configuration data.
- container: The Element is a container image which can be used by a container runtime application.
- data: The Element is data.
- device: The Element refers to a chipset, processor, or electronic board.
- diskImage: The Element refers to a disk image that can be written to a disk, booted in a VM, etc. A disk image typically contains most or all of the components necessary to boot, such as bootloaders, kernels, firmware, userspace, etc.
- deviceDriver: The Element represents software that controls hardware devices.
- documentation: The Element is documentation.
- evidence: The Element is the evidence that a specification or requirement has been fulfilled.
- executable: The Element is an Artifact that can be run on a computer.
- file: The Element is a single file which can be independently distributed (configuration file, statically linked binary, Kubernetes deployment, etc.).
- filesystemImage: The Element is a file system image that can be written to a disk (or virtual) partition.
- firmware: The Element provides low level control over a device's hardware.
- framework: The Element is a software framework.
- install: The Element is used to install software on disk.
- library: The Element is a software library.
- manifest: The Element is a software manifest.
- model: The Element is a machine learning or artificial intelligence model.
- module: The Element is a module of a piece of software.
- operatingSystem: The Element is an operating system.
- other: The Element doesn't fit into any of the other categories.
- patch: The Element contains a set of changes to update, fix, or improve another Element.
- platform: The Element represents a runtime environment.
- requirement: The Element provides a requirement needed as input for another Element.
- source: The Element is a single or a collection of source files.
- specification: The Element is a plan, guideline or strategy how to create, perform or analyze an application.
- test: The Element is a test used to verify functionality on an software element.
