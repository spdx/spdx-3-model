SPDX-License-Identifier: Community-Spec-1.0

# profileConformance

## Summary

Describes one a profile which the creator of this ElementCollection intends to
conform to.

## Description

Describes a profile to which the creator of this ElementCollection intends to
conform.

The profileConformance will apply to all Elements contained within the
collection as well as the collection itself.

Conformance to a profile is defined by the additional restrictions documented
in the profile specific documentation and schema files.

Use of this property allows the creator of an ElementCollection to communicate
to consumers their intent to adhere to the profile additional restrictions.

The profileConformance has a default value of "core" if no other
profileConformance is specified since all ElementCollections and Element must
adhere to the Core profile.

## Metadata

- name: profileConformance
- Nature: ObjectProperty
- Range: ProfileIdentifierType

## Summary @zh-Hans

描述此`ElementCollection`的创建者意图遵循的配置文件。

## Description @zh-Hans

描述此`ElementCollection`的创建者意图遵循的配置文件。

`profileConformance`将应用于集合中的所有`Element`以及集合本身。

对配置文件的符合性由配置文件特定的文档和架构文件中记录的附加限制来定义。

使用此属性允许`ElementCollection`的创建者向消费者传达其遵循配置文件附加限制的意图。

如果没有指定其他`profileConformance`，则`profileConformance`的默认值为`Core`，因为所有`ElementCollections`和`Element`都必须遵循`Core`配置文件。
