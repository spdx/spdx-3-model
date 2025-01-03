SPDX-License-Identifier: Community-Spec-1.0

# DictionaryEntry

## Summary

A key with an associated value.

## Description

The class used for implementing a generic string mapping (also known as
associative array, dictionary, or hash map) in SPDX.

Each DictionaryEntry contains a key-value pair which maps the key to its
associated value.

To implement a dictionary, this class is to be used in a collection with
unique keys.

## Metadata

- name: DictionaryEntry
- Instantiability: Concrete

## Properties

- key
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- value
  - type: xsd:string
  - maxCount: 1

## Summary @zh-Hans

一个具有关联值的键。

## Description @zh-Hans

用于在SPDX中实现通用字符串映射（也称为关联数组、字典或哈希映射）的类。

每个`DictionaryEntry`包含一个键值对，映射键到其关联值。

要实现字典，这个类应该在一个具有唯一键的集合中使用。
