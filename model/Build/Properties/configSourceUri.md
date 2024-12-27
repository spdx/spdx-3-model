SPDX-License-Identifier: Community-Spec-1.0

# configSourceUri

## Summary

Property that describes the URI of the build configuration source file.

## Description

If a build configuration exists for the toolchain or platform performing the
build, the configSourceUri of a build is the URI of that build configuration,
according to the buildType.

For example, a build triggered by a GitHub Action is defined by a build
configuration YAML file. In this case, the configSourceUri is the URL of that
YAML file.

## Metadata

- name: configSourceUri
- Nature: DataProperty
- Range: xsd:anyURI

## Summary @zh-Hans

此属性描述构建配置源文件的 URI（Uniform Resource Identifier，统一资源标识符）。

## Description @zh-Hans

如果存在用于执行构建的工具链或平台的构建配置，则构建的 `configSourceUri` （配置源统一标识符）就是根据 `buildType` 确定的该构建配置的 URI。

例如，由 GitHub Actions 触发的构建由构建配置 YAML 文件定义。在这种情况下，`configSourceUri` 就是该 YAML 文件的 URL（Uniform Resource Locator，统一资源定位符）。
