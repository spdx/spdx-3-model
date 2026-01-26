SPDX-License-Identifier: Community-Spec-1.0

# environment

## Summary

Property describing the session in which a build is invoked.

## Description

environment is a map of environment variables and values that are set during a
build session, according to the buildType.

This is different from the [parameter](parameter.md) property in that it
describes the environment variables set before a build is invoked rather than
the variables provided to the builder.

## Metadata

- name: environment
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
