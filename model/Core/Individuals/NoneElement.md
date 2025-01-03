SPDX-License-Identifier: Community-Spec-1.0

# NoneElement

## Summary

An Individual Value for Element representing a set of Elements with
cardinality (number/count) of zero.

## Description

NoneElement should be used if the SPDX creator desires to assert that
there are NO elements for the given context of use.

For example, a Relationship with
`relationshipType`="ancestorOf",
`from`=Element1,
and `to`=NoneElement
is explicitly expressing an assertion that
Element1 has no descendants.

## Metadata

- name: NoneElement
- type: IndividualElement

## Property Values

- name: "NONE"

## Summary @zh-Hans

表示基数（数量/计数）为零的一组`Element`的单独值。

## Description @zh-Hans

如果SPDX创建者希望断言给定使用的上下文中没有元素，则应使用`NoneLicenseElement`。

例如，关系`relationshipType=ancestorOf`，`from=Element1`，`to=NoneElement`明确表达了`Element1`没有后代的断言。
