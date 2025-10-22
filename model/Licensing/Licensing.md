SPDX-License-Identifier: Community-Spec-1.0

# Licensing

## Summary

The Licensing profile defines a minimum set of license information to
facilitate compliance with typical license use cases.

## Description

The Licensing profile only contains the additional requirement that any
Software Artifact shall have a `Relationship` of type `hasConcludedLicense`.

Classes and property restrictions are defined in the SimpleLicensing profile
(classes and properties associated with
[license expression strings](../../annexes/spdx-license-expressions.md))
and in the ExpandedLicensing profile (classes and properties used for a
fully parsed syntax tree of license expressions).

There are 2 relationship types related to licensing - `hasDeclaredLicense` and
`hasConcludedLicense`.

If the `hasConcludedLicense` for a Software Artifact is not the same as its
`hasDeclaredLicense`, a written explanation should be provided in the
`hasConcludedLicense` relationship `comment` field.

A written explanation of a relationship to a `NoAssertionLicense` may be
provided in the `comment` field for the relationship.

*hasDeclaredLicense*

A hasDeclaredLicense identifies the license information actually found in the
Software Artifact, for example as detected by use of automated tooling.

This field is not intended to capture license information obtained from an
external source, such as a package's website. Such information can be
included, as needed, in the hasConcludedLicense field.

A hasDeclaredLicense may be expressed differently in practice for different
types of Software Artifacts. For example:

- for Packages,
  it would include license info for the Package as a
  whole, found in the Package itself (e.g., LICENSE file,
  README file, metadata in the Package, etc.),
  but it would not include any license information that is not in the Package
  itself (e.g., license information from the project's website or from a
  third party repository or website).
- for Files,
  it would include license info found in the File itself (e.g., license
  header or notice, comments indicating the license, SPDX-License-Identifier
  expression),
  but it would not include license info found in a different file
  (e.g., LICENSE file in the top directory of a repository).
- for Snippets,
  it would include license info found in the Snippet itself (e.g., license
  notice, comments, SPDX-License-Identifier expression),
  but it would not include license info found elsewhere in the File or in a
  different File (e.g., comment at top of File if it is not within the
  Snippet, LICENSE file in the top directory of a repository).

A hasDeclaredLicense relationship to NoneLicense indicates that the
corresponding Package, File or Snippet contains no license information
whatsoever.

A hasDeclaredLicense relationship to NoAssertionLicense
indicates that one of the following applies:

- the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
- the SPDX data creator has made no attempt to determine this field; or
- the SPDX data creator has intentionally provided no information (no meaning
  should be implied by doing so).

If a hasDeclaredLicense relationship is not present, no assumptions can be made
about whether or not a hasDeclaredLicense exists.

Note that a missing hasDeclaredLicense is not the same as a relationship to
NoAssertionLicense since the latter is a "known unknown" whereas no assumptions
can be made from a missing hasDeclaredLicense relationship.

*hasConcludedLicense*

A hasConcludedLicense is the license identified by the SPDX data creator,
based on analyzing the license information in the Software Artifact
and other information to arrive at a reasonably objective
conclusion as to what license governs the Software Artifact.

A hasConcludedLicense relationship to NoneLicense indicates that the
SPDX data creator has looked and did not find any license information for this
Software Artifact.

A hasConcludedLicense relationship to NoAssertionLicense
indicates that one of the following applies:

- the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
- the SPDX data creator has made no attempt to determine this field; or
- the SPDX data creator has intentionally provided no information (no
  meaning should be implied by doing so).

If a hasConcludedLicense is not present, no assumptions can be made
about whether or not a hasConcludedLicense exists.

Note that a missing hasConcludedLicense is not the same as a relationship to a
NoAssertionLicense since the latter is a "known unknown" whereas no assumptions
can be made from a missing hasConcludedLicense relationship.

## Metadata

- id: https://spdx.org/rdf/3.0/terms/Licensing
- name: Licensing

## Profile conformance

For an element collection to be conformant with this profile,
the following has to hold:

1. for every `/Software/SoftwareArtifact` there shall exist exactly one
   `/Core/Relationship` of type `hasConcludedLicense` having that element as
   its `from` property and a `/SimpleLicensing/AnyLicenseInfo` as its `to`
   property.

## Summary @zh-Hans

许可配置文件定义了一组许可信息的最低要求，以促进遵从典型许可证用例。

## Description @zh-Hans

许可配置文件仅包含一个附加要求，即任何软件工件必须具有类型为`hasConcludedLicense`的`Relationship`。

类和属性的限制在 `SimpleLicensing profile`（与[许可表达字符串](../../annexes/spdx-license-expressions.md)相关的类和属性）和`ExpandedLicensing profile`（用于许可表达式的完全解析语法树的类和属性）中定义。

与许可相关的关系类型有两种 -`hasDeclaredLicense`and`hasConcludedLicense`。

如果软件工件的`hasConcludedLicense`与其`hasDeclaredLicense`不同，则**应当**在`hasConcludedLicense`关系的`comment`字段中提供书面解释。

**可以**在关系的`comment`字段中提供与`NoAssertionLicense`的关系的书面解释。

*hasDeclaredLicense*

`hasDeclaredLicense`识别了在软件工件中实际找到的许可信息，例如通过自动化工具检测到的许可信息。

此字段不打算捕获外部来源（例如软件包的官方网站）的许可信息。这类信息可以根据需要包含在`hasConcludedLicense`字段中。

`hasDeclaredLicense`在实际应用中可能会因不同类型的软件工件而有所不同。例如：

- 对于软件包
  - 包括在软件包本身中找到的软件包的所有许可信息（例如，LICENSE文件，README文件，软件包中的元数据等）
  - 不包括不在软件包本身中的任何许可信息（例如，项目网站或第三方代码仓库或网站的许可信息）

- 对于文件
  - 包括在文件本身中找到的许可信息（例如，许可标题或声明，指示许可的注释，SPDX-License-Identifier表达式）
  - 不包括在不同文件中找到的许可信息（例如，代码仓库顶层目录中的LICENSE文件）

- 对于代码片段
  - 包括在代码片段本身中找到的许可信息（例如，许可声明，注释，SPDX-License-Identifier表达式）
  - 不包括在文件的其他地方或不同文件中找到的许可信息（例如，对于不在代码片段内的内容，在文件顶部的注释；在代码仓库顶层目录中的LICENSE文件）

对于`NoAssertionLicense`的`hasDeclaredLicense`关系表明相应的软件包、文件或代码片段不包含任何许可信息。

对于`NoAssertionLicense`的`hasDeclaredLicense`关系表明以下之一适用：

- SPDX数据创建者已尝试但无法得出合理的客观结论；
- SPDX数据创建者没有尝试确定该字段；或者
- SPDX数据创建者故意未提供任何信息（不应因此推断出任何意义）。

如果不存在`hasDeclaredLicense`关系，则无法对是否存在`hasDeclaredLicense`做出任何假设。

请注意，缺少`hasDeclaredLicense`与缺少对`NoAssertionLicense`关系不同，因为后者是“已知的未知”，而缺少`hasDeclaredLicense`关系则无法做出任何假设。

*hasConcludedLicense*

`hasConcludedLicense`是SPDX数据创建者根据分析软件工件中的许可信息和其他信息得出的合理客观结论，确定的软件工件所适用的许可证。

对于`NoneLicense`的`hasConcludedLicense`关系表明SPDX数据创建者已查找但未找到此软件工件的任何许可信息。

对于`NoneLicense`的`hasConcludedLicense`关系表明以下之一适用：

- SPDX数据创建者已尝试但无法得出合理的客观结论；
- SPDX数据创建者没有尝试确定此字段；或者
- SPDX数据创建者故意未提供任何信息（不应因此推断出任何意义）。

如果不存在`hasConcludedLicense`，则无法对是否存在`hasConcludedLicense`做出任何假设。

请注意，缺少`hasConcludedLicense`与缺少对`NoAssertionLicense`的关系不同，因为后者是“已知的未知”，而缺少`hasConcludedLicense`关系则无法做出任何假设。

## Profile conformance @zh-Hans

要使元素集符合此配置文件，必须满足以下条件：

1. 对于每个`/Software/SoftwareArtifact`，**必须**存在一个类型为`hasConcludedLicense`的`/Core/Relationship`，其`from`属性为该元素，`to`属性为`/SimpleLicensing/AnyLicenseInfo`。
