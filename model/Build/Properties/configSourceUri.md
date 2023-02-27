SPDX-License-Identifier: Community-Spec-1.0

# configSourceUri

## Summary

Property that describes the URI of the build configuration source file.

## Description

The configSourceUri of a build is the URI of the build configuration, if existing, used by a toolchain or platform. For example, a build triggered by a github action has a configSourceUri as the URL of the YAML file for the GitHub repository.

## Metadata

- name: configSourceUri
- Nature: DataProperty
- Range: anyURI
