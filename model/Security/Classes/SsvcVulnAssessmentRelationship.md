SPDX-License-Identifier: Community-Spec-1.0

# SsvcVulnAssessmentRelationship

## Summary

Provides an SSVC assessment for a vulnerability.

## Description

An SsvcVulnAssessmentRelationship describes the decision made using the
Stakeholder-Specific Vulnerability Categorization (SSVC) decision tree as
defined by
[CISA Stakeholder-Specific Vulnerability Categorization Guide](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc).

It is intended to communicate the results of using the CISA SSVC Calculator.

*Constraints*

- The relationship type must be set to hasAssessmentFor.

*Example*

```json
{
  "type": "security_SsvcVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:ssvc-1",
  "relationshipType": "hasAssessmentFor",
  "security_decisionType": "act",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "suppliedBy": "urn:spdx.dev:agent-jane-doe",
  "publishedTime": "2021-03-09T11:04:53Z"
}
```

## Metadata

- name: SsvcVulnAssessmentRelationship
- SubclassOf: VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- decisionType
  - type: SsvcDecisionType
  - minCount: 1
  - maxCount: 1

## Summary @zh-Hans

提供漏洞的SSVC评估。

## Description @zh-Hans

`SsvcVulnAssessmentRelationship`描述根据[CISA利益相关者特定漏洞分类（SSVC）指南](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc)使用SSVC决策树做出的决策。

其目的是传达CISA SSVC计算器的结果。

*约束条件*

- 关系类型必须设置为`hasAssessmentFor`。

*示例*

```json
{
  "@type": "SsvcVulnAssessmentRelationship",
  "@id": "urn:spdx.dev:ssvc-1",
  "relationshipType": "hasAssessmentFor",
  "security_decisionType": "act",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2021-03-09T11:04:53Z"
}
```
