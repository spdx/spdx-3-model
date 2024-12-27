SPDX-License-Identifier: Community-Spec-1.0

# buildType

## Summary

A buildType is a hint that is used to indicate the toolchain, platform, or
infrastructure that the build was invoked on.

## Description

A buildType is an IRI expressing the toolchain, platform, or infrastructure that
the build was invoked on.

The buildType is used to interpret the meaning of other build parameters by
defining the "type" of build; if the same buildType is seen in different Build
elements, it means they are the same kind of build, but difference instances
and possible with different configurations.

If you are not using a well-known buildType, it should be namespaced to a
domain you own to prevent conflicts with other buildType IRIs.

Examples of a buildType might be:

- A GitHub action workflow
- A step in a GitHub actions pipeline
- An invocation of a compiler or other tool
- A script that orchestrates builds at a higher level

Keep in mind that builds can be "nested" using the `ancestorOf` relationship.

If the buildType IRI is not recognized, it is still possible to inspect other
properties of the build, but it may not be possible to derive deeper meaning
from them.

For more information, see the SLSA definition of buildType.

## Metadata

- name: buildType
- Nature: DataProperty
- Range: xsd:anyURI

## Summary @zh-Hans

`buildType` 是一种提示，用于指明调用构建的工具链、平台或基础设施。

## Description @zh-Hans

`buildType` 是一个 IRI（Internationalized Resource Identifier，国际化资源标识符），表示调用构建的工具链、平台或基础设施。

`buildType` 通过定义构建的 “类型” 来解释其他构建参数的含义；不同 `Build` 元素中的相同 `buildType` 意味着它们是相同类型的构建，但实例不同，可能配置也不同。

如果你没有使用常用的 `buildType`，应将其命名空间设置为您拥有的域，以防止与其他 `buildType` IRI 发生冲突。

`buildType` 的示例可能包括：

- GitHub Actions 工作流
- GitHub Actions 流水线步骤
- 编译器或其他工具的调用
- 编排更高级别构建的脚本

请记住，使用 `ancestorOf` 关系可以“嵌套”构建。

如果 `buildType` IRI 无法识别，仍然可以检查构建的其他属性，但可能无法从中推导出更深层的含义。

有关更多信息，请参阅 SLSA（Software Logistics and Supply Chain Automation，软件物流和供应链自动化） 对 `buildType` 的定义。
