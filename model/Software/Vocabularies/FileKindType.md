SPDX-License-Identifier: Community-Spec-1.0

# FileKindType

## Summary

Enumeration of the different kinds of SPDX file.

## Description

An SPDX File can represent a regular file, a directory of zero or more Files, or a symbolic link to a File.

In the future, this can be extended to other kinds (e.g. network based files).

## Metadata

- name: FileKindType

## Entries

- file: The file represents a single file (default).
- directory: The file represents a directory and all content stored in that directory.
- symlink: This file represents a symbolic link (soft link).
