SPDX-License-Identifier: Community-Spec-1.0

# suppliedBy

## Summary

Identifies who or what supplied the artifact or VulnAssessmentRelationship
referenced by the Element.

## Description

Identify the actual distribution source for the artifact (e.g., snippet, file,
package, vulnerability) or VulnAssessmentRelationship being referenced.

This might or might not be different from the originating distribution source
for the artifact (e.g., snippet, file, package, vulnerability) or
VulnAssessmentRelationship.

## Metadata

- name: suppliedBy
- Nature: ObjectProperty
- Range: Agent

## Summary @zh-Hans

标识被`Element`引用的`Artifact`或`VulnAssessmentRelationship`的提供方。

## Description @zh-Hans

标识被引用的`Artifact`（例如，代码片段、文件、包、漏洞）或`VulnAssessmentRelationship`的实际分发来源。

这可能与`Artifact`（例如，代码片段、文件、包、漏洞）或`VulnAssessmentRelationship`的原始分发来源不同。
