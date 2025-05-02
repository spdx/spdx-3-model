SPDX-License-Identifier: Community-Spec-1.0

# EpssVulnAssessmentRelationship

## Summary

Provides an EPSS assessment for a vulnerability.

## Description

An EpssVulnAssessmentRelationship relationship describes the likelihood or
probability that a vulnerability will be exploited in the wild, and the
percentile ranking of probability relative to all other vulnerabilities' EPSS
scores, using the Exploit Prediction Scoring System (EPSS) as defined at
[The EPSS Model](https://www.first.org/epss/model).

*Constraints*

- The relationship type must be set to hasAssessmentFor.
- The probability must be between 0 and 1.
- The percentile must be between 0 and 1.

*Example*

```json
{
  "type": "security_EpssVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:epss-CVE-2020-28498",
  "relationshipType": "hasAssessmentFor",
  "security_probability": "0.00105",
  "security_percentile": "0.42356",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "suppliedBy": "urn:spdx.dev:agent-jane-doe",
  "publishedTime": "2023-10-05T00:00:30Z"
}
```

## Metadata

- name: EpssVulnAssessmentRelationship
- SubclassOf: VulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- probability
  - type: xsd:decimal
  - minCount: 1
  - maxCount: 1
- percentile
  - type: xsd:decimal
  - minCount: 1
  - maxCount: 1

## External properties restrictions

- /Security/VulnAssessmentRelationship/publishedTime
  - minCount: 1

## Summary @zh-Hans

提供漏洞的EPSS评估。

## Description @zh-Hans

根据[EPSS模型](https://www.first.org/epss/model)中定义的漏洞利用预测评分系统（EPSS），`EpssVulnAssessmentRelationship`关系描述漏洞在实际环境中被利用的可能性或概率，以及相对于所有其他漏洞的EPSS评分的百分位排名。

*约束条件*

- 关系类型必须设置为`hasAssessmentFor`。
- 概率范围为0到1。
- 百分位数范围为0到1。

*示例*

```json
{
  "type": "EpssVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:epss-CVE-2020-28498",
  "relationshipType": "hasAssessmentFor",
  "security_probability": "0.00105",
  "security_percentile": "0.42356",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2023-10-05T00:00:30Z"
}
```
