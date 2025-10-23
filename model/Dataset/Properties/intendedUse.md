SPDX-License-Identifier: Community-Spec-1.0

# intendedUse

## Summary

Describes what the given dataset should be used for.

## Description

A free-form text that describes what the given dataset should be used for.

Some datasets are collected to be used only for particular purposes.

For example, medical data collected from a specific demography should only be applicable
for training machine learning models to make predictions for that demography.
In such a case, the intendedUse field would capture this information.
Similarly, if a dataset is collected for building a facial recognition model,
the intendedUse field would specify that.

## Metadata

- name: intendedUse
- Nature: DataProperty
- Range: xsd:string

## Summary @zh-Hans

该属性描述给定数据集的预期用途。

## Description @zh-Hans

一段自由格式的文本，描述给定数据集应该被用于什么目的。

有些数据集是为了特定目的而收集的。

例如，从特定人群收集的医疗数据可能只适用于训练针对该人群做出预测的机器学习模型。在这种情况下，`intendedUse` 字段可以指定这一信息。同样，如果一个数据集是为了构建面部识别模型而收集的，`intendedUse` 字段可以对此进行说明。
