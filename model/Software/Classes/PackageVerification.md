SPDX-License-Identifier: Community-Spec-1.0

# PackageVerification

## Summary

An integrity method which supports verification of software packages.

## Description

This is an abstract class representing integrity methods applicable for verification of software packages.

Several use cases for SPDX depend on the consumer being able to verify the provenance and integrity of their software. 
SPDX can support several different scenarios depending on what information is available to the producer, what information is available to the consumer, and how the SPDX document is delivered. 
These scenarios are described below along with recommended PackageVerification subclass used to verifying the SPDX packages.

- A Package can be represented as a single blob of bytes, such as a tar archive or single executable: subclass PackageHash.  Note: PackageDownloadLocation should be a download locator that retrieves the package blob.  A supplier can define a PackageHash in a Package without providing a PackageDownloadLocation. This lets consumers perform an offline verification of private blobs.
- A Package represents an artifact that logically binds a number of single files together : subclass PackageGitoid. Gitoid stands for Git Object ID and a gitoid of type blob is a unique hash of a binary artifact. 
- Package meta data was imported from an SPDX 2.X document: subclass PackageVerificationCode.  The PackageVerificationCode is the algorithm used in SPDX versions prior to 3.0.  The PackageVerificationCode subclass is provided for compatibility.  Note that the PackageGitoid subclass is preferred if compatibility with SPDX version 2.X is not required.

## Metadata

- name: PackageVerification
- SubclassOf: /Core/IntegrityMethod
- Instantiability: Abstract
