SPDX-License-Identifier: Community-Spec-1.0

# useSensitivePersonalInformation

## Summary

Records if sensitive personal information is used during model training or
could be used during the inference.

## Description

Notes if sensitive personal information is used in the training or inference of
the AI models.

This might include biometric data, addresses or other data that can be used to
infer a person's identity.

Related: `hasSensitivePersonalInformation` in `/Dataset/DatasetPackage`

## Metadata

- name: useSensitivePersonalInformation
- Nature: ObjectProperty
- Range: /Core/PresenceType

## Summary @zh-Hans

记录在模型训练或推理中是否使用了敏感个人信息。

## Description @zh-Hans

记录AI模型的训练或推理中是否使用了敏感个人信息。

这可能包括生物特征数据、地址或其他可用于推断个人身份的数据。

相关：`/Dataset/DatasetPackage`中的`hasSensitivePersonalInformation`

