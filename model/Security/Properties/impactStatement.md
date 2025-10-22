SPDX-License-Identifier: Community-Spec-1.0

# impactStatement

## Summary

Explains why a VEX product is not affected by a vulnerability. It is an
alternative in VexNotAffectedVulnAssessmentRelationship to the machine-readable
justification label.

## Description

When a VEX product element is related with a VexNotAffectedVulnAssessmentRelationship
and a machine readable justification label is not provided, then an impactStatement
that further explains how or why the product(s) are not affected by the vulnerability
shall be provided.

## Metadata

- name: impactStatement
- Nature: DataProperty
- Range: xsd:string

## Summary @zh-Hans

解释VEX产品不受漏洞影响的原因。它是`VexNotAffectedVulnAssessmentRelationship`中机器可读证明标签的替代方案。

## Description @zh-Hans

当VEX产品元素与`VexNotAffectedVulnAssessmentRelationship`关联且未提供机器可读证明标签时，必须提供一个`impactStatement`，进一步解释产品如何或为何不受漏洞影响。

