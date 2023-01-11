SPDX-License-Identifier: Community-Spec-1.0

# Package

## Description

If SPDX information is being used to describe packages, then one instance of the package information per package being described shall exist. It provides important meta information about the package as a whole. Packages are an abstract concept that can be used to refer to any distribution of software, typically consisting of one or more files and capable of containing sub-packages. Starting with SPDX 2.0, it is not necessary to have a package wrapping a set of files.

A package refers to any unit of content that can be associated with a distribution of software. Typically, a package is composed of one or more files. An SPDX document may, but is not required to, provide details about the individual files comprising a package (see File.md).

Any of the following non-limiting examples may be (but are not required to be) represented in SPDX as a package:

- a tarball, zip file or other archive
- a directory or sub-directory
- a separately distributed piece of software which another Package or File uses or depends upon (e.g., a Python package, a Go module, ...)
- a container image, and/or each image layer within a container image
- a collection of one or more sub-packages
- a Git repository snapshot from a particular point in time

Note that some of these could be represented in SPDX as a file as well.

In an SPDX document, relationship elements can be used to indicate relationships between packages, such as dependency relationships.

Cardinality: Optional, zero or many.

## Metadata

- SubclassOf: Core:Artifact

## Properties

- contentIdentifier
  - type: anyURI
  - minCount: 0
  - maxCount: 1
- packagePurpose
  - type: SoftwarePurpose
  - minCount: 0
- downloadLocation
  - type: anyURI
  - minCount: 0
  - maxCount: 1
- packageUrl
  - type: anyURI
  - minCount: 0
  - maxCount: 1
- homePage
  - type: anyURI
  - minCount: 0
  - maxCount: 1

