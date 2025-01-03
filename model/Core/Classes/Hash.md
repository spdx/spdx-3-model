SPDX-License-Identifier: Community-Spec-1.0

# Hash

## Summary

A mathematically calculated representation of a grouping of data.

## Description

A hash is a grouping of characteristics unique to the result
of applying a mathematical algorithm
that maps data of arbitrary size to a bit string (the hash)
and is a one-way function, that is,
a function which is practically infeasible to invert.

This is commonly used for integrity checking of data.

Please note that different profiles may also provide additional methods for verifying the integrity of specific subclasses of Elements.

## Metadata

- name: Hash
- SubclassOf: IntegrityMethod

## Properties

- algorithm
  - type: HashAlgorithm
  - minCount: 1
  - maxCount: 1
- hashValue
  - type: xsd:string
  - minCount: 1
  - maxCount: 1

## Summary @zh-Hans

一组数据的数学计算表示。

## Description @zh-Hans

`Hash`是应用数学算法将任意大小的数据映射到位字符串（哈希值）的过程，是一种不可逆函数。

常用于数据完整性检查。

请注意，其他配置文件可能还会提供额外的方法用于验证特定`Element`子类的完整性。
