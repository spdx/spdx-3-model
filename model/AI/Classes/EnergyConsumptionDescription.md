SPDX-License-Identifier: Community-Spec-1.0

# EnergyConsumptionDescription

## Summary

The class that helps note down the quantity of energy consumption and the unit
used for measurement.

## Description

This class is designed to store energy consumption data, including the quantity
and the unit of measurement.

The `energyQuantity` property stores the amount of energy consumed,
and the `energyUnit` property stores the unit used for measurement.

For example, 0.042 kilowatt-hour of energy will have `0.042` as a value for
property `energyQuantity`, and `"kilowattHour"` as a value for property
`energyUnit`.

*Example*

```json
{
  "type": "ai_EnergyConsumptionDescription",
  "ai_energyQuantity": "0.042",
  "ai_energyUnit": "kilowattHour"
}
```

## Metadata

- name: EnergyConsumptionDescription
- Instantiability: Concrete

## Properties

- energyQuantity
  - type: xsd:decimal
  - minCount: 1
  - maxCount: 1
- energyUnit
  - type: EnergyUnitType
  - minCount: 1
  - maxCount: 1

## Summary @zh-Hans

这个类帮助记录能耗的数量及其使用的测量单位。

## Description @zh-Hans

这个类旨在存储能耗数据，包括数量和测量单位。

`energyQuantity`属性存储能耗的数量，而`energyUnit`属性存储测量单位。

例如，0.042千瓦时的能量，其`energyQuantity`属性的值将为`0.042`，`energyUnit`属性的值为`"kilowattHour"`。
