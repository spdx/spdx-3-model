SPDX-License-Identifier: Community-Spec-1.0

# useSensitivePersonalInformation

## Summary

Records if sensitive personal information is used during model training or could be used during the inference.

## Description

useSensitivePersonalInformation notes if sensitive personal information
is used in the training or inference of the AI models.
This might include biometric data, addresses or other data that can be used to infer a person's identity.

Related: `hasSensitivePersonalInformation` in `/Dataset/Dataset`

## Metadata

- name: useSensitivePersonalInformation
- Nature: ObjectProperty
- Range: /Core/PresenceType
