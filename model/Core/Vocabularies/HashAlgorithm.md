SPDX-License-Identifier: Community-Spec-1.0

# HashAlgorithm

## Summary

A mathematical algorithm that maps data of arbitrary size to a bit string.

## Description

A HashAlgorithm is a mathematical algorithm that maps data of arbitrary size to
a bit string (the hash) and is a one-way function, that is, a function which is
practically infeasible to invert.

**Note**
Inclusion in this vocabulary does not imply suitability for cryptographic integrity verification.

For cryptographic integrity, producers should provide at least one SHA-256 or stronger hash. Consumers may reject verification when only weaker algorithms are provided.

MD2, MD4, MD5, and SHA-1 are not collision resistant and should not be used for cryptographic integrity. Adler-32 is a non-cryptographic checksum intended only to detect accidental corruption. MD6 is experimental and non-standardized and should not be used for new integrity information.

Dilithium and FALCON are signature algorithms, and Kyber is a key-encapsulation mechanism; they are not hash algorithms.

## Metadata

- name: HashAlgorithm

## Entries

- adler32: Adler-32 checksum is part of the widely used zlib compression library as defined in [RFC 1950](https://datatracker.ietf.org/doc/rfc1950/) Section 2.3.
- blake2b256: BLAKE2b algorithm with a digest size of 256, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.
- blake2b384: BLAKE2b algorithm with a digest size of 384, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.
- blake2b512: BLAKE2b algorithm with a digest size of 512, as defined in [RFC 7693](https://datatracker.ietf.org/doc/rfc7693/) Section 4.
- blake3: [BLAKE3](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf)
- crystalsDilithium: [Dilithium](https://pq-crystals.org/dilithium/)
- crystalsKyber: [Kyber](https://pq-crystals.org/kyber/)
- falcon: [FALCON](https://falcon-sign.info/falcon.pdf)
- md2: MD2 message-digest algorithm, as defined in [RFC 1319](https://datatracker.ietf.org/doc/rfc1319/).
- md4: MD4 message-digest algorithm, as defined in [RFC 1186](https://datatracker.ietf.org/doc/rfc1186/).
- md5: MD5 message-digest algorithm, as defined in [RFC 1321](https://datatracker.ietf.org/doc/rfc1321/).
- md6: [MD6 hash function](https://people.csail.mit.edu/rivest/pubs/RABCx08.pdf)
- other: any hashing algorithm that does not exist in this list of entries
- sha1: SHA-1, a hashing algorithm, as defined in [RFC 3174](https://datatracker.ietf.org/doc/rfc3174/).
- sha224: SHA-2 with a digest length of 224, as defined in [RFC 3874](https://datatracker.ietf.org/doc/rfc3874/).
- sha256: SHA-2 with a digest length of 256, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).
- sha384: SHA-2 with a digest length of 384, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).
- sha512: SHA-2 with a digest length of 512, as defined in [RFC 6234](https://datatracker.ietf.org/doc/rfc6234/).
- sha3_224: SHA-3 with a digest length of 224, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
- sha3_256: SHA-3 with a digest length of 256, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
- sha3_384: SHA-3 with a digest length of 384, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
- sha3_512: SHA-3 with a digest length of 512, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
