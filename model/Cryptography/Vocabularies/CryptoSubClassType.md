SPDX-License-Identifier: Community-Spec-1.0

# CryptoSubClassType

## Summary

The cryptographic sub-algorithm enumeration.

## Description

Specifies the type of a cryptographic sub-algorithm.

## Metadata

- name: CryptoSubClassType

## Entries

- hashFunction: A function that transforms input data of any length into a fixed-size output, with collision and preimage resistance as core properties.
- passwordHashing: A hash function construction with deliberately high computational or memory cost, typically incorporating a salt.
- checksum: A fixed-size value computed from input data, without the collision resistance of a cryptographic hash function.
- blockCipher: A symmetric-key algorithm operating on fixed-size blocks, using the same key for encryption and decryption.
- streamCipher: A symmetric-key algorithm built around a pseudorandom keystream, combined with plaintext bit by bit or byte by byte.
- encoding: A symmetric-key transformation without a cipher's diffusion and collision properties.
- publicKeyEncryption: An asymmetric-key scheme combining a public-key primitive with a padding or randomization mechanism.
- publicKeyCipher: The raw asymmetric-key mathematical primitive, without an added padding or randomization scheme.
- ellipticCurveCryptography: An asymmetric-key algorithm structured around point arithmetic over an elliptic curve group.
- digitalSignature: An asymmetric-key algorithm pairing a private-key signing operation with a public-key verification operation.
- protocol: A defined sequence of asymmetric-key operations exchanged between parties, rather than a single-step algorithm.
- hybridCipher: An asymmetric-key construction combining a public-key operation with a symmetric-key algorithm.
- keyExchangeMechanism: An asymmetric-key construction based on an interactive exchange of public values between two parties.
- keyEncapsulationMechanism: An asymmetric-key construction pairing a public-key encapsulation operation with a private-key decapsulation operation.
- hashBasedMAC: MAC constructed using a cryptographic hash function as the underlying primitive.
- blockCipherMAC: MAC constructed using a block cipher as the underlying primitive.
- polynomialMAC: MAC constructed from polynomial evaluation over a finite field, keyed via a stream or block cipher.
- passwordBased: KDF that derives keys from a password or passphrase, using a salt and an intentionally slow or memory-hard computation.
- keyBased: KDF that derives keys from existing cryptographic keying material, such as a master secret, shared secret, or session key, rather than a password.
- trueRandomNumberGenerator: An algorithm that derives randomness from a physical entropy source, such as hardware noise, ring oscillators, thermal effects, or quantum sources, and is not seed-reproducible.
- deterministicRandomBitGenerator: A deterministic, seed-based algorithm that produces cryptographically secure pseudo-random output.
