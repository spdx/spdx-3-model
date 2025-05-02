SPDX-License-Identifier: Community-Spec-1.0

# VexFixedVulnAssessmentRelationship

## Summary

Links a vulnerability and elements representing products (in the VEX sense) where
a fix has been applied and are no longer affected.

## Description

VexFixedVulnAssessmentRelationship links a vulnerability to a number of elements
representing VEX products where a vulnerability has been fixed and are no longer
affected. It represents the VEX fixed status.

*Constraints*

When linking elements using a VexFixedVulnAssessmentRelationship, the following
requirements must be observed:

- Elements linked with a VulnVexFixedAssessmentRelationship are constrained to
  using the fixedIn relationship type.

*Example*

```json
{
  "type": "security_VexFixedVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:vex-fixed-in-1",
  "relationshipType": "fixedIn",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.4",
  "suppliedBy": "urn:spdx.dev:agent-jane-doe",
  "publishedTime": "2021-03-09T11:04:53Z"
}
```

## Metadata

- name: VexFixedVulnAssessmentRelationship
- SubclassOf: VexVulnAssessmentRelationship
- Instantiability: Concrete

## Summary @zh-Hans

将漏洞与代表产品（根据VEX定义）的元素关联，这些产品已修复漏洞且不再受影响。

## Description @zh-Hans

`VexFixedVulnAssessmentRelationship`将一个漏洞与多个代表VEX产品的元素关联，这些产品已修复漏洞且不再受影响。此关系对应VEX的已修复（fixed）状态。

*约束条件*

使用`VexFixedVulnAssessmentRelationship`关联元素时，必须遵循以下要求：

- 与`VulnVexFixedAssessmentRelationship`关联的元素必须使用`fixedIn`关系类型。
- 关系的`from:`端必须为一个`/Security/Vulnerability`类型的元素。

*示例*

```json
{
  "type": "VexFixedVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:vex-fixed-in-1",
  "relationshipType": "fixedIn",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.4",
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2021-03-09T11:04:53Z"
}
```
