SPDX-License-Identifier: Community-Spec-1.0

# RelationshipType

## Summary

Information about the relationship between two Elements.

## Description

Provides information about the relationship between two Elements.
For example, you can represent a relationship between two different Files,
between a Package and a File, between two Packages, or between one SpdxDocument
and another SpdxDocument.

Relationship names should be descriptive enough to easily deduce the correct direction
from their name. The best way to do this is to make sure that the relationship
name completes the sentence:

`from` (is) (a) `RELATIONSHIP` `to`

## Metadata

- name: RelationshipType

## Entries

- affects: The `from` Vulnerability affects each `to` Element. The use of the `affects` type is constrained to `VexAffectedVulnAssessmentRelationship` classed relationships.
- amendedBy: The `from` Element is amended by each `to` Element.
- ancestorOf: The `from` Element is an ancestor of each `to` Element.
- availableFrom: The `from` Element is available from the additional supplier described by each `to` Element.
- configures: The `from` Element is a configuration applied to each `to` Element, during a LifecycleScopeType period.
- contains: The `from` Element contains each `to` Element.
- coordinatedBy: The `from` Vulnerability is coordinatedBy the `to` Agent(s) (vendor, researcher, or consumer agent).
- copiedTo: The `from` Element has been copied to each `to` Element.
- delegatedTo: The `from` Agent is delegating an action to the Agent of the `to` Relationship (which shall be of type invokedBy), during a LifecycleScopeType (e.g. the `to` invokedBy Relationship is being done on behalf of `from`).
- dependsOn: The `from` Element depends on each `to` Element, during a LifecycleScopeType period.
- descendantOf: The `from` Element is a descendant of each `to` Element.
- describes: The `from` Element describes each `to` Element. To denote the root(s) of a tree of elements in a collection, the rootElement property shall be used.
- doesNotAffect: The `from` Vulnerability has no impact on each `to` Element. The use of the `doesNotAffect` is constrained to `VexNotAffectedVulnAssessmentRelationship` classed relationships.
- expandsTo: The `from` archive expands out as an artifact described by each `to` Element.
- exploitCreatedBy: The `from` Vulnerability has had an exploit created against it by each `to` Agent.
- fixedBy: Designates a `from` Vulnerability has been fixed by the `to` Agent(s).
- fixedIn: A `from` Vulnerability has been fixed in each `to` Element. The use of the `fixedIn` type is constrained to `VexFixedVulnAssessmentRelationship` classed relationships.
- foundBy: Designates a `from` Vulnerability was originally discovered by the `to` Agent(s).
- generates: The `from` Element generates each `to` Element.
- hasAddedFile: Every `to` Element is a file added to the `from` Element (`from` hasAddedFile `to`).
- hasAssessmentFor: Relates a `from` Vulnerability and each `to` Element with a security assessment. To be used with `VulnAssessmentRelationship` types.
- hasAssociatedVulnerability: Used to associate a `from` Artifact with each `to` Vulnerability.
- hasConcludedLicense: The `from` SoftwareArtifact is concluded by the SPDX data creator to be governed by each `to` license.
- hasDataFile: The `from` Element treats each `to` Element as a data file. A data file is an artifact that stores data required or optional for the `from` Element's functionality. A data file can be a database file, an index file, a log file, an AI model file, a calibration data file, a temporary file, a backup file, and more. For AI training dataset, test dataset, test artifact, configuration data, build input data, and build output data, please consider using the more specific relationship types: `trainedOn`, `testedOn`, `hasTest`, `configures`, `hasInput`, and `hasOutput`, respectively. This relationship does not imply dependency.
- hasDeclaredLicense: The `from` SoftwareArtifact was discovered to actually contain each `to` license, for example as detected by use of automated tooling.
- hasDeletedFile: Every `to` Element is a file deleted from the `from` Element (`from` hasDeletedFile `to`).
- hasDependencyManifest: The `from` Element has manifest files that contain dependency information in each `to` Element.
- hasDistributionArtifact: The `from` Element is distributed as an artifact in each `to` Element (e.g. an RPM or archive file).
- hasDocumentation: The `from` Element is documented by each `to` Element.
- hasDynamicLink: The `from` Element dynamically links in each `to` Element, during a LifecycleScopeType period.
- hasEvidence: Every `to` Element is considered as evidence for the `from` Element (`from` hasEvidence `to`).
- hasExample: Every `to` Element is an example for the `from` Element (`from` hasExample `to`).
- hasHost: The `from` Build was run on the `to` Element during a LifecycleScopeType period (e.g. the host that the build runs on).
- hasInput: The `from` Build has each `to` Element as an input, during a LifecycleScopeType period.
- hasMetadata: Every `to` Element is metadata about the `from` Element (`from` hasMetadata `to`).
- hasOptionalComponent: Every `to` Element is an optional component of the `from` Element (`from` hasOptionalComponent `to`).
- hasOptionalDependency: The `from` Element optionally depends on each `to` Element, during a LifecycleScopeType period.
- hasOutput: The `from` Build element generates each `to` Element as an output, during a LifecycleScopeType period.
- hasPrerequisite: The `from` Element has a prerequisite on each `to` Element, during a LifecycleScopeType period.
- hasProvidedDependency: The `from` Element has a dependency on each `to` Element, dependency is not in the distributed artifact, but assumed to be provided, during a LifecycleScopeType period.
- hasRequirement: The `from` Element has a requirement on each `to` Element, during a LifecycleScopeType period.
- hasSpecification: Every `to` Element is a specification for the `from` Element (`from` hasSpecification `to`), during a LifecycleScopeType period.
- hasStaticLink: The `from` Element statically links in each `to` Element, during a LifecycleScopeType period.
- hasTest: Every `to` Element is a test artifact for the `from` Element (`from` hasTest `to`), during a LifecycleScopeType period.
- hasTestCase: Every `to` Element is a test case for the `from` Element (`from` hasTestCase `to`).
- hasVariant: Every `to` Element is a variant the `from` Element (`from` hasVariant `to`).
- invokedBy: The `from` Element was invoked by the `to` Agent, during a LifecycleScopeType period (for example, a Build element that describes a build step).
- modifiedBy: The `from` Element is modified by each `to` Element.
- other: Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationship types (this relationship is directionless).
- packagedBy: Every `to` Element is a packaged instance of the `from` Element (`from` packagedBy `to`).
- patchedBy: Every `to` Element is a patch for the `from` Element (`from` patchedBy `to`).
- publishedBy: Designates a `from` Vulnerability was made available for public use or reference by each `to` Agent.
- reportedBy: Designates a `from` Vulnerability was first reported to a project, vendor, or tracking database for formal identification by each `to` Agent.
- republishedBy: Designates a `from` Vulnerability's details were tracked, aggregated, and/or enriched to improve context (i.e. NVD) by each `to` Agent.
- serializedInArtifact: The `from` SpdxDocument can be found in a serialized form in each `to` Artifact.
- testedOn: The `from` Element has been tested on the `to` Element(s).
- trainedOn: The `from` Element has been trained on the `to` Element(s).
- underInvestigationFor: The `from` Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `VexUnderInvestigationVulnAssessmentRelationship` classed relationships.
- usesTool: The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period.

## Summary @zh-Hans

关于两个`Element`之间关系的信息。

## Description @zh-Hans

提供关于两个`Element`之间关系的信息。
例如，可以表示两个不同`File`之间的关系，`Package`与`File`之间的关系，两个`Package`之间的关系，或者一个`SpdxDocument`与另一个`SpdxDocument`之间的关系。

关系名称应该具有足够的描述性，以便根据其名称轻松推断出正确的方向。最佳做法是确保关系名称能够完整地表达以下句子:

`from`（是）`RELATIONSHIP` `to`

## Entries @zh-Hans

- affects: `from` `Vulnerability`影响每一个`to` `Element`。`affects`类型仅限于`VexAffectedVulnAssessmentRelationship`类关系中使用。
- amendedBy: `from` `Element`被每一个`to` `Element`修正。
- ancestorOf: `from` `Element`是每个`to` `Element`的祖先。
- availableFrom: `from` `Element`由每个`to` `Element`描述的额外供应商提供。
- configures: `from` `Element`是在一个`LifecycleScopeType`期间应用于每一个`to` `Element`的配置。
- contains: `from` `Element`包含每一个`to` `Element`。
- coordinatedBy: `from`的`Vulnerability`由`to` `Agent`（供应商、研究人员或消费者代理）协调。
- copiedTo: `from` `Element`被复制到每一个`to` `Element`。
- delegatedTo: 在`LifecycleScopeType`期间（例如`to` `invokedBy` `Relationship`正在作为`from`的代理），`from` `Agent`将操作委托给`to` `Relationship`的`Agent`（必须是`invokedBy`类型）。
- dependsOn: `from` `Element`在`LifecycleScopeType`期间依赖于每一个`to` `Element`。
- descendantOf: `from` `Element`是每一个`to` `Element`的后代。
- describes: `from` `Element`描述每一个`to` `Element`。要标识集合中元素树的根，应该使用`rootElement`属性。
- doesNotAffect: `from` `Vulnerability`对每一个`to` `Element`没有影响。`doesNotAffect`仅限于`VexNotAffectedVulnAssessmentRelationship`类关系中使用 。
- expandsTo: `from`存档展开成每一个`to` `Element`所描述的工件。
- exploitCreatedBy: 针对`from` `Vulnerability`的利用是由每一个`to` `Agent`创建的。
- fixedBy: `from` `Vulnerability`被`to` `Agent`修复。
- fixedIn: `from` `Vulnerability`在每一个`to` `Element`中被修复。`fixedIn`类型仅限于`VexFixedVulnAssessmentRelationship`类关系中使用。
- foundBy: 指定`from` `Vulnerability`最初是由`to` `Agent`发现的。
- generates: `from` `Element`生成每一个`to` `Element`。
- hasAddedFile: 每一个`to` `Element`是添加到`from` `Element`的文件（`from` `hasAddedFile` `to`）。
- hasAssessmentFor: 将`from` `Vulnerability`和每一个`to` `Element`与安全评估关联。用于`VulnAssessmentRelationship`类型。
- hasAssociatedVulnerability: 将`from` `Artifact`与每一个`to` `Vulnerability`关联。
- hasConcludedLicense: 由SPDX数据创建者决定，`from` `SoftwareArtifact`受每一个`to`许可的管辖。
- hasDataFile: `from` `Element`将每一个`to` `Element`视为数据文件。数据文件是一种工件，存储了`from` `Element`功能所需或可选的数据。数据文件可以是数据库文件、索引文件、日志文件、AI模型文件、校准数据文件、临时文件、备份文件等。对于AI训练数据集、测试数据集、测试工件、配置数据、构建输入数据和构建输出数据，请考虑使用更具体的关系类型：`trainedOn`、`testedOn`、`hasTest`、`configures`、`hasInput`和`hasOutput`。这种关系不暗示依赖性。
- hasDeclaredLicense: 通过自动化工具检测等手段，发现`from` `SoftwareArtifact`实际上包含每一个`to`许可。
- hasDeletedFile: 每一个`to` `Element`是从`from` `Element`删除的文件（`from` `hasDeletedFile` `to`）。
- hasDependencyManifest: `from` `Element`具有包含每一个`to` `Element`依赖信息的清单文件。
- hasDistributionArtifact: `from` `Element`以工件形式在每一个`to` `Element`中分发（例如RPM或存档文件）。
- hasDocumentation: `from` `Element`由每一个`to` `Element`记录。
- hasDynamicLink: `from` `Element`在`LifecycleScopeType`期间在每一个`to` `Element`中动态链接。
- hasEvidence: 每一个`to` `Element`被认为是`from` `Element`的证据（`from` `hasEvidence` `to`）。
- hasExample: 每一个`to` `Element`是`from` `Element`的示例（`from` `hasExample` `to`）。
- hasHost: 在`LifecycleScopeType`期间，`from` `Build`（拿不准，但是你70行的构建用的inline）在`to` `Element`上运行（例如运行构建的主机）。
- hasInput: 在`LifecycleScopeType`期间，`from` `Build`有每一个`to` `Element`作为输入。
- hasMetadata: 每一个`to` `Element`是关于`from` `Element`的元数据（`from` `hasMetadata` `to`）。
- hasOptionalComponent: 每一个`to` `Element`是`from` `Element`的可选组件（`from` `hasOptionalComponent` `to`）。
- hasOptionalDependency: 在`LifecycleScopeType`期间，`from` `Element`可选地依赖于每一个`to` `Element`。
- hasOutput: 在`LifecycleScopeType`期间，`from` `Build` `Element`生成每一个`to` `Element`作为输出。
- hasPrerequisite: 在`LifecycleScopeType`期间，`from` `Element`有对每一个`to` `Element`的先决条件。
- hasProvidedDependency: 在`LifecycleScopeType`期间，`from` `Element`对每一个`to` `Element`有依赖性。该依赖关系不包含在分发的工件中，但被假定已提供。
- hasRequirement: 在`LifecycleScopeType`期间，`from` `Element`对每一个`to` `Element`有要求。
- hasSpecification: 在`LifecycleScopeType`期间，`from` `Element`的每一个`to` `Element`是一个规范（`from` `hasSpecification` `to`）。
- hasStaticLink: 在`LifecycleScopeType`期间，`from` `Element`在每一个`to` `Element`中静态链接。
- hasTest: 在`LifecycleScopeType`期间，每一个`to` `Element`是`from` `Element`的测试工件（`from` `hasTest` `to`）。
- hasTestCase: 每一个`to` `Element`是`from` `Element`的测试用例（`from` `hasTestCase` `to`）。
- hasVariant: 每一个`to` `Element`是`from` `Element`的变体（`from` `hasVariant` `to`）。
- invokedBy: 在`LifecycleScopeType`期间， `from` `Element`由`to` `Agent`调用（例如描述构建步骤的`Build` `Element`）。
- modifiedBy: `from` `Element`被每一个`to` `Element`修改。
- other: 每一个`to` `Element`与`from` `Element`相关，但这种关系类型不符合任何SPDX关系类型（此关系无方向性）。
- packagedBy: 每一个`to` `Element`是`from` `Element`的打包实例（`from` `packagedBy` `to`）。
- patchedBy: 每一个`to` `Element`是`from` `Element`的补丁（`from` `patchedBy` `to`）。
- publishedBy: 指定`from` `Vulnerability`由每一个`to` `Agent`公开使用或引用。
- reportedBy: 指定`from` `Vulnerability`首次被每一个`to` `Agent`报告给项目、供应商或跟踪数据库，以便进行正式识别。
- republishedBy: 指定每一个`to` `Agent`跟踪、聚合和/或丰富`from` `Vulnerability`的详细信息以改善上下文（即NVD）。
- serializedInArtifact: `from` `SpdxDocument`的序列化形式可以在每一个`to` `Artifact`中被找到。
- testedOn: `from` `Element`在`to` `Element`上进行了测试。
- trainedOn: `from` `Element`在`to` `Element`上进行了训练。
- underInvestigationFor: `from` `Vulnerability`对每一个`to` `Element`的影响正在调查中。`underInvestigationFor`类型仅限于`VexUnderInvestigationVulnAssessmentRelationship`类关系中使用 。
- usesTool: 在`LifecycleScopeType`期间，`from` `Element`使用每一个`to` `Element`作为工具。
