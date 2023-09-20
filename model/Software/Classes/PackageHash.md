SPDX-License-Identifier: Community-Spec-1.0

# PackageHash

## Summary

A verification method for software packages represented as a single blob of bytes, such as a tar archive or single executable.

## Description

The PackageHash is a hash of the single blob of bytes representing a software package.
The packageDownloadLocation should be a download locator that retrieves the package blob.  
A supplier can define a PackageHash in a Package without providing a PackageDownloadLocation. 
This lets consumers perform an offline verification of private blobs.

## Metadata

- name: PackageHash
- SubclassOf: /Software/PackageVerification

## Properties

- algorithm
  - type: /Core/HashAlgorithm
  - minCount: 1
  - maxCount: 1
- /core/hashValue
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
