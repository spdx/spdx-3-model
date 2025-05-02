SPDX-License-Identifier: Community-Spec-1.0

# VexUnderInvestigationVulnAssessmentRelationship

## Summary

Designates elements as products where the impact of a vulnerability is being
investigated.

## Description

VexUnderInvestigationVulnAssessmentRelationship links a vulnerability to a
number of products stating the vulnerability's impact on them is being
investigated. It represents the VEX under_investigation status.

*Constraints*

When linking elements using a VexUnderInvestigationVulnAssessmentRelationship
the following requirements must be observed:

- Elements linked with a VexUnderInvestigationVulnAssessmentRelationship are
  constrained to using the underInvestigationFor relationship type.

*Example*

```json
{
  "type": "security_VexUnderInvestigationVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:vex-underInvestigation-1",
  "relationshipType": "underInvestigationFor",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "suppliedBy": "urn:spdx.dev:agent-jane-doe",
  "publishedTime": "2021-03-09T11:04:53Z"
}
```

## Metadata

- name: VexUnderInvestigationVulnAssessmentRelationship
- SubclassOf:  VexVulnAssessmentRelationship
- Instantiability: Concrete

## Summary @zh-Hans

将元素指定为正在调查漏洞影响的产品。

## Description @zh-Hans

`VexUnderInvestigationVulnAssessmentRelationship`将一个漏洞与多个产品关联，表示漏洞对这些产品的影响正在调查中。此关系对应VEX的调查中（under_investigation）状态。

*约束条件*

使用`VexUnderInvestigationVulnAssessmentRelationship`关联元素时，必须遵循以下要求：

- 与`VexUnderInvestigationVulnAssessmentRelationship`关联的元素必须使用`underInvestigationFor`关系类型。
- 关系的`from:`端必须为一个`/Security/Vulnerability`类型的元素。

*示例*

```json
{
  "type": "VexUnderInvestigationVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:vex-underInvestigation-1",
  "relationshipType": "underInvestigationFor",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2021-03-09T11:04:53Z"
}
```
