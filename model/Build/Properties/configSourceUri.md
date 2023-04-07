SPDX-License-Identifier: Community-Spec-1.0

# configSourceUri

## Summary

Property that describes the URI of the build configuration source file.

## Description

If a build configuration exists for the toolchain or platform performing the build, the configSourceUri of a build is the URI of that build configuration. For example, a build triggered by a GitHub action is defined by a build configuration YAML file. In this case, the configSourceUri is the URL of that YAML file. 
m
## Metadata

- name: configSourceUri
- Nature: DataProperty
- Range: xsd:anyURI
