SPDX-License-Identifier: Community-Spec-1.0

# cryptographicExpressionListVersion

## Summary

The version of the SPDX Cryptographic Algorithm List used in the cryptographic algorithm expression.

## Description

Recognizing that cryptographic algorithms are added to the [SPDX Cryptographic Algorithm List](https://github.com/spdx/cryptographic-algorithm-list/) with each subsequent version, the intent is to provide consumers with the version of the
SPDX Cryptographic Algorithm List and expression used.

This anticipates that, in the future, a cryptographic algorithm expression can use a version of the SPDX Cryptographic Algorithm List that is older than the current one.

The specified version of the SPDX Cryptographic Algorithm List shall include all listed cryptographic algorithms in the expression.

## Metadata

- name: cryptographicExpressionListVersion
- Nature: DataProperty
- Range: xsd:string
