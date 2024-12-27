SPDX-License-Identifier: Community-Spec-1.0

# configSourceEntrypoint

## Summary

Property describes the invocation entrypoint of a build.

## Description

A build entrypoint is the invoked executable of a build which always runs when
the build is triggered, according to the buildType.

For example, when a build is triggered by running a shell script, the
entrypoint is `script.sh`.

In terms of a declared build, the entrypoint is the position in a configuration
file or a build declaration which is always run when the build is triggered.

For example, in the following configuration file, the entrypoint of the build
is `publish`.

```yaml
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

## Summary @zh-Hans

此属性描述构建调用入口点。

## Description @zh-Hans

构建入口点是根据 `buildType` 触发构建时始终运行的构建可执行文件。

例如，当通过运行 shell 脚本触发构建时，入口点是 `script.sh`。

对于声明的构建，入口点是在配置文件或构建声明中的位置，该位置在触发构建时始终运行。

例如，在下面的配置文件中，构建的入口点是 `publish`。

```yaml
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
