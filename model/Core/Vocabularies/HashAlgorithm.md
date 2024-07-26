SPDX-License-Identifier: Community-Spec-1.0

# HashAlgorithm

## Summary

A mathematical algorithm that maps data of arbitrary size to a bit string.

## Description

A HashAlgorithm is a mathematical algorithm that maps data of arbitrary size to
a bit string (the hash) and is a one-way function, that is, a function which is
practically infeasible to invert.

## Metadata

- name: HashAlgorithm

## Entries

- blake2b256: BLAKE2b algorithm with a digest size of 256, as defined in [RFC 7693](https://www.rfc-editor.org/info/rfc7693) Section 4.
- blake2b384: BLAKE2b algorithm with a digest size of 384, as defined in [RFC 7693](https://www.rfc-editor.org/info/rfc7693) Section 4.
- blake2b512: BLAKE2b algorithm with a digest size of 512, as defined in [RFC 7693](https://www.rfc-editor.org/info/rfc7693) Section 4.
- blake3: [BLAKE3](https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf)
- crystalsDilithium: [Dilithium](https://pq-crystals.org/dilithium/)
- crystalsKyber: [Kyber](https://pq-crystals.org/kyber/)
- falcon: [FALCON](https://falcon-sign.info/falcon.pdf)
- md2: MD2 message-digest algorithm, as defined in [RFC 1319](https://www.rfc-editor.org/info/rfc1319/).
- md4: MD4 message-digest algorithm, as defined in [RFC 1186](https://www.rfc-editor.org/info/rfc1186).
- md5: MD5 message-digest algorithm, as defined in [RFC 1321](https://www.rfc-editor.org/info/rfc1321).
- md6: [MD6 hash function](https://people.csail.mit.edu/rivest/pubs/RABCx08.pdf)
- other: any hashing algorithm that does not exist in this list of entries
- sha1: SHA-1, a secure hashing algorithm, as defined in [RFC 3174](https://www.rfc-editor.org/info/rfc3174).
- sha224: SHA-2 with a digest length of 224, as defined in [RFC 3874](https://www.rfc-editor.org/info/rfc3874).
- sha256: SHA-2 with a digest length of 256, as defined in [RFC 6234](https://www.rfc-editor.org/rfc/rfc6234).
- sha384: SHA-2 with a digest length of 384, as defined in [RFC 6234](https://www.rfc-editor.org/rfc/rfc6234).
- sha512: SHA-2 with a digest length of 512, as defined in [RFC 6234](https://www.rfc-editor.org/rfc/rfc6234).
- sha3_224: SHA-3 with a digest length of 224, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
- sha3_256: SHA-3 with a digest length of 256, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
- sha3_384: SHA-3 with a digest length of 384, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
- sha3_512: SHA-3 with a digest length of 512, as defined in [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final).
