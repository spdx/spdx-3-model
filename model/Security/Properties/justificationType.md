SPDX-License-Identifier: Community-Spec-1.0

# justificationType

## Summary

Impact justification label to be used when linking a vulnerability to an element
representing a VEX product with a VexNotAffectedVulnAssessmentRelationship
relationship.

## Description

When stating that an element is not affected by a vulnerability, the
VexNotAffectedVulnAssessmentRelationship shall include a justification from the
machine-readable labels catalog informing the reason the element is not impacted.

impactStatement which is a string with English prose can be used instead or as
complementary to the justification label, but one of both shall be defined.

## Metadata

- name: justificationType
- Nature: ObjectProperty
- Range: VexJustificationType

## Summary @zh-Hans

用于将漏洞与代表VEX产品的元素（具有`VexNotAffectedVulnAssessmentRelationship`关系）关联时使用的影响证明标签。

## Description @zh-Hans

当声明某个元素不受漏洞影响时，`VexNotAffectedVulnAssessmentRelationship`必须包含机器可读标签目录中的证明，说明此元素不受影响的原因。

`impactStatement`是一个英文文本字符串，可以替代或作为证明标签的补充，但二者必须定义其一。
