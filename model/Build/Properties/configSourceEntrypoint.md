SPDX-License-Identifier: Community-Spec-1.0

# configSourceEntrypoint

## Summary

Property describes the invocation entrypoint of a build.

## Description

A build entrypoint is the invoked executable of a build which always runs when the build is triggered. For example, when a build is triggered by running a shell script, the entrypoint is `script.sh`. In terms of a declared build, the entrypoint is the position in a configuration file or a build declaration which is always run when the build is triggered. For example, in the following configuration file, the entrypoint of the build is `publish`.

```
name: Publish packages to PyPI

on:
create:
tags: "*"

jobs:
publish:
runs-on: ubuntu-latest
if: startsWith(github.ref, 'refs/tags/')
steps:

...
```

## Metadata

- name: configSourceEntrypoint
- Nature: DataProperty
- Range: xsd:string
