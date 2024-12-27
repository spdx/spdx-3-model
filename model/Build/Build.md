SPDX-License-Identifier: Community-Spec-1.0

# Build

## Summary

The Build Profile defines the set of information required to describe an
instance of a Software Build.

## Description

A Software Build is defined here as the act of converting software inputs into
software artifacts using software build tools. Inputs can include source code,
config files, artifacts that are build environments, and build tools. Outputs
can include intermediate artifacts to other build inputs or the final
artifacts.

The Build profile provides a subclass of Element called Build.

It also provides a minimum set of required Relationship Types from the Core
profile:

- hasInput: Describes the relationship from the Build element to its inputs.
- hasOutput: Describes the relationship from the Build element to its outputs.
- invokedBy: Describes the relationship from the Build element to the Agent
  that invoked it.

In addition, the following Relationship Types may be used to describe a Build.

- hasHost: Describes the relationship from the Build element to the build stage
  or host.
- configures: Describes the relationship from a configuration to the Build
  element.
- ancestorOf: Describes a relationship from a Build element to Build elements
  that describe its child builds.
- descendantOf: Describes a relationship from a child Build element to its
  parent.
- usesTool: Describes a relationship from a Build element to a build tool.

All relationships in the Build Profile are scoped to the "build"
LifecycleScopeType period.

The `hasInput` relationship can be applied to a config file or a build tool if
the nature of these inputs are not known at the creation of an SPDX document.

## Metadata

- id: https://spdx.org/rdf/3.0.1/terms/Build
- name: Build

## Profile Conformance

Conformance to the Build profile requires one or more instances of the Build
class. In addition, there must be at least three instances `Relationship`s with
type `LifecycleScopedRelationship`, where the "scope" property must be "build"
and the "from" property must be the Build instance.

At the minimum, the Build profile must contain a `hasInput`, `hasOutput`, and
`invokedBy` relationshipType. If an input is known to be a build configuration
or a build tool, the `hasInput` relationshipType can be replaced by a
`configures` or `usesTool` relationshipType.

## Summary @zh-Hans

`Build` 配置文件定义了描述 `Software Build` 实例所需的一组信息。

## Description @zh-Hans

`Software Build` 定义为使用软件构建工具将软件输入转换为软件工件的行为。输入可以包括源代码、配置文件、构建环境以及构建工具。输出可以包括作为其他构建输入的中间工件或最终工件。

`Build` 配置文件提供了 `Build` 元素，它是 `Element` 的子类。

它还提供了来自 `Core` 配置文件所需关系类型的最小集合。


- hasInput: 描述了从 `Build` 元素到其输入的关系。
- hasOutput: 描述了从 `Build` 元素到其输出的关系。
- invokedBy: 描述了从 `Build` 元素到调用其代理的关系。

此外，以下 `RelationshipType` 可以用于描述一个构建。

- hasHost: 描述了从 `Build` 元素到构建阶段或主机的关系。
- configures: 描述了从配置到 `Build` 元素的关系。
- ancestorOf: 描述了从 `Build` 元素到描述其子构建的 `Build` 元素的关系。
- descendantOf: 描述了从子 `Build` 元素到其父 `Build` 元素的关系。
- usesTool: 描述了从 `Build` 元素到构建工具的关系。

构建配置文件中的所有关系都限定在 “build” `LifecycleScopeType` 期间。

如果在创建 SPDX 文档时这些输入性质未知，`hasInput` 关系可以应用于配置文件或构建工具。

## Profile Conformance @zh-Hans

符合 `Build` 配置文件要求至少有一个或多个 `Build` 类的实例。此外，还必须至少有三个类型为 `LifecycleScopedRelationship` 的 `Relationship` 实例，其 “scope” 属性必须是 “build”，而 “from” 属性必须是构建实例。

至少，构建配置文件必须包含 `hasInput`，`hasOutput` 和 `invokedBy` `RelationshipType`。如果已知输入是构建配置或构建工具， 可以用 `configures` 或 `usesTool` 替换 `hasInput` `RelationshipType`。
