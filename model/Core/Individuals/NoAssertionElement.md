SPDX-License-Identifier: Community-Spec-1.0

# NoAssertionElement

## Summary

An Individual Value for Element representing a set of Elements of unknown
identify or cardinality (number).

## Description

NoAssertionElement should be used if

- the SPDX creator has attempted to but cannot reach a reasonable objective
  determination;
- the SPDX creator has made no attempt to determine this field; or
- the SPDX creator has intentionally provided no information (no meaning should
  be implied by doing so).

For example, a Relationship with
`relationshipType`="ancestorOf",
`from`=Element1,
and
`to`=NoAssertionElement
is explicitly expressing that
no assertion is being made about any potential descendants of Element1.

## Metadata

- name: NoAssertionElement
- type: IndividualElement

## Property Values

- name: "NOASSERTION"

## Summary @zh-Hans

表示一组未知标识或基数（数量）的`Element`的单独值。

## Description @zh-Hans

对于以下情况，应使用`NoAssertionElement`：

- SPDX创建者尝试但无法达成合理的客观判断；
- SPDX创建者未尝试确定此字段；
- SPDX创建者故意不提供信息（这样做不应被暗示为有任何含义）。
例如，关系`relationshipType=ancestorOf`、`from=Element1`和`to=NoAssertionElement`明确表示不对`Element1`的任何潜在后代作出任何断言。
