SPDX-License-Identifier: Community-Spec-1.0

# buildType

## Summary

A buildType is a hint that is used to indicate the toolchain, platform, or infrastructure that the build was invoked on.

## Description

A buildType is a URI expressing the toolchain, platform, or infrastructure that the build was invoked on. For example, if the build was invoked on GitHub's CI platform using github actions, the buildType can be expressed as `https://github.com/actions`. In contrast, if the build was invoked on a local machine, the buildType can be expressed as `file://username@host/path/to/build`.

## Metadata

- name: buildType
- Nature: DataProperty
- Range: xsd:anyURI
