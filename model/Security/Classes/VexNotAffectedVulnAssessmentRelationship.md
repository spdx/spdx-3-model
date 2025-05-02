SPDX-License-Identifier: Community-Spec-1.0

# VexNotAffectedVulnAssessmentRelationship

## Summary

Links a vulnerability and one or more elements designating the latter as products
not affected by the vulnerability.

## Description

VexNotAffectedVulnAssessmentRelationship connects a vulnerability and a number
of elements designating them as products not affected by the vulnerability.
This relationship corresponds to the VEX not_affected status.

*Constraints*

When linking elements using a VexNotVulnAffectedAssessmentRelationship, the
following requirements must be observed:

- Relating elements with a VexNotAffectedVulnAssessmentRelationship is
  restricted to the doesNotAffect relationship type.
- Both impactStatement and justificationType properties have a cardinality of
  0..1 making them optional. Nevertheless, to produce a valid VEX not_affected
  statement, one of them MUST be defined. This is specified in the Minimum
  Elements for VEX.

*Example*

```json
{
  "type": "security_VexNotAffectedVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:vex-not-affected-1",
  "relationshipType": "doesNotAffect",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "security_justificationType": "componentNotPresent",
  "security_impactStatement": "Not using this vulnerable part of this library.",
  "suppliedBy": "urn:spdx.dev:agent-jane-doe",
  "publishedTime": "2021-03-09T11:04:53Z"
}
```

## Metadata

- name: VexNotAffectedVulnAssessmentRelationship
- SubclassOf: VexVulnAssessmentRelationship
- Instantiability: Concrete

## Properties

- justificationType
  - type: VexJustificationType
  - minCount: 0
  - maxCount: 1
- impactStatement
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- impactStatementTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1

## Summary @zh-Hans

将漏洞与一个或多个元素关联，指定后者为不受漏洞影响的产品。

## Description @zh-Hans

`VexNotAffectedVulnAssessmentRelationship`将一个漏洞与多个元素关联，这些元素指定未受漏洞影响的产品。此关系对应VEX的未受影响（not_affected）状态。

*约束条件*

使用`VexNotVulnAffectedAssessmentRelationship`关联元素时，必须遵循以下要求：

- 与`VexNotAffectedVulnAssessmentRelationship`关联的元素必须使用`doesNotAffect`关系类型。
- 关系的`from:`端必须为一个`/Security/Vulnerability`类型的元素。
- `impactStatement`和`justificationType`属性的基数均为`0..1`，意味着它们是可选属性。但是，要生成有效的VEX not_affected语句，二者必须定义其一。这在VEX的最小元素规范中有所规定。

*示例*

```json
{
  "type": "VexNotAffectedVulnAssessmentRelationship",
  "spdxId": "urn:spdx.dev:vex-not-affected-1",
  "relationshipType": "doesNotAffect",
  "from": "urn:spdx.dev:vuln-cve-2020-28498",
  "to": ["urn:product-acme-application-1.3"],
  "security_assessedElement": "urn:npm-elliptic-6.5.2",
  "security_justificationType": "componentNotPresent",
  "security_impactStatement": "Not using this vulnerable part of this library.",
  "suppliedBy": ["urn:spdx.dev:agent-jane-doe"],
  "publishedTime": "2021-03-09T11:04:53Z"
}
```
