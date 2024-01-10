SPDX-License-Identifier: Community-Spec-1.0

# PackageGitoid

## Summary

Verification method to be used for a Package which represents an artifact that logically binds a number of single files together using a Git Object ID (Gitoid).

## Description

https://www.iana.org/assignments/uri-schemes/prov/gitoid Gitoid stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) and a gitoid of type blob is a unique hash of a binary artifact. 

Note that in addition to being used as a verification method, gitoid is also a reccomended ExternalIdentifier to be used for the package with the ExternalIdentifierType gitoid.

## Metadata

- name: PackageGitoid
- SubclassOf: /Software/PackageVerification

## Properties

- gitoid
  - type: xsd:string
