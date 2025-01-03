SPDX-License-Identifier: Community-Spec-1.0

# LifecycleScopedRelationship

## Summary

Provide context for a relationship that occurs in the lifecycle.

## Description

Certain relationships are sensitive to where they occur in the lifecycle.  This parameter lets us avoid a proliferation of relationships, by parameterizing this context information for a relationship.

## Metadata

- name: LifecycleScopedRelationship
- SubclassOf: Relationship
- Instantiability: Concrete

## Properties

- scope
  - type: LifecycleScopeType
  - minCount: 0
  - maxCount: 1

## Summary @zh-Hans

为生命周期中发生的关系提供上下文。

## Description @zh-Hans

某些关系对其在生命周期中的发生位置敏感。该参数通过对关系的上下文信息进行参数化来避免关系泛滥。
