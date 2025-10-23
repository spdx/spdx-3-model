SPDX-License-Identifier: Community-Spec-1.0

# actionStatement

## Summary

Provides advise on how to mitigate or remediate a vulnerability when a VEX product
is affected by it.

## Description

When an element is referenced with a VexAffectedVulnAssessmentRelationship,
the relationship shall include one actionStatement that should describe actions
to remediate or mitigate the vulnerability.

## Metadata

- name: actionStatement
- Nature: DataProperty
- Range: xsd:string

## Summary @zh-Hans

提供关于在VEX产品受漏洞影响时如何缓解或修复漏洞的建议。

## Description @zh-Hans

使用`VexAffectedVulnAssessmentRelationship`引用元素时，**必须**包含一个`actionStatement`，**应当**描述缓解或修复漏洞的措施。
