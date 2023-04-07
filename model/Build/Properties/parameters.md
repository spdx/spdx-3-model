SPDX-License-Identifier: Community-Spec-1.0

# parameters

## Summary

Property describing the parameters used in an instance of a build.

## Description

parameters is a key-value map of all build parameters and their values that were provided to the builder for a build instance. This is different from the [environment](environment.md) property in that the keys and values are provided as command line arguments or a configuration file to the builder.

## Metadata

- name: parameters
- Nature: DataProperty
- Range: map<string>string

