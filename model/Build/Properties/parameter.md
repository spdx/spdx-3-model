SPDX-License-Identifier: Community-Spec-1.0

# parameter

## Summary

Property describing a parameter used in an instance of a build.

## Description

parameter is a key-value of a build parameter and its value that
was provided to the builder for a build instance. This is different from the
[environment](environment.md) property in that the key and value are provided
as command line arguments or a configuration file to the builder.

## Metadata

- name: parameter
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
