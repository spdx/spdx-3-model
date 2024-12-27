SPDX-License-Identifier: Community-Spec-1.0

# energyConsumption

## Summary

Indicates the amount of energy consumption incurred by an AI model.

## Description

Captures the energy consumption of an AI model, either known or estimated.

In the absence of direct measurements, an SPDX data creator may choose to
estimate the energy consumption based on information about computational
resources (e.g., number of floating-point operations), training time, and other
relevant training details.

## Metadata

- name: energyConsumption
- Nature: ObjectProperty
- Range: EnergyConsumption

## Summary @zh-Hans

表示AI模型产生的能耗量。

## Description @zh-Hans

表示AI模型的能耗，可以是已知的或估算的。

在没有直接测量的情况下，SPDX数据创建者可以根据计算资源（例如浮点运算次数）、训练时间以及其他相关训练细节的信息来估算能耗。
