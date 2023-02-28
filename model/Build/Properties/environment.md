SPDX-License-Identifier: Community-Spec-1.0

# environment

## Summary

Property describing the session in which a build is invoked.

## Description

environment is a map of environment variables and values that are set during a build session. This is different from the [parameters](parameters.md) property in that it describes the environment variables set before a build is invoked rather than the variables provided to the builder.

## Metadata

- name: environment
- Nature: DataProperty
- Range: map<string>string
