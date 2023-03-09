SPDX-License-Identifier: Community-Spec-1.0

# Package

## Summary

Refers to any unit of content that can be associated with a distribution of software.

## Description

A package refers to any unit of content that can be associated with a distribution of software.
Typically, a package is composed of one or more files.  
Any of the following non-limiting examples may be (but are not required to be) represented in SPDX as a package:

 - a tarball, zip file or other archive
 - a directory or sub-directory
 - a separately distributed piece of software which another Package or File uses or depends upon (e.g., a Python package, a Go module, ...)
 - a container image, and/or each image layer within a container image
 - a collection of one or more sub-packages
 - a Git repository snapshot from a particular point in time

Note that some of these could be represented in SPDX as a file as well.

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

