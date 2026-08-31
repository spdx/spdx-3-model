SPDX-License-Identifier: Community-Spec-1.0

# signatureValue

## Summary

The actual cryptographic signature data generated during the signing process.

## Description

The signatureValue property contains the cryptographic signature bytes that were produced when the content was signed. This value is generated using a signing algorithm applied to the data being signed, typically creating a hash of the content that is then encrypted with the signer's private key.

The signature value enables verification that the content has not been altered since signing and confirms the identity of the signer. When a verifier has access to the signer's public key and the original unsigned content, they can recompute what the signature value should be and compare it against the stored value to confirm authenticity.

This property is typically encoded as a base64 string representation of the raw binary signature bytes, though other encodings may be used depending on the signature format. The specific encoding and format of this value are indicated by the signatureFormat property when present.

## Metadata

- name: signatureValue
- Nature: DataProperty
- Range: xsd:string
