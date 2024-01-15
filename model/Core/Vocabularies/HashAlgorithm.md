SPDX-License-Identifier: Community-Spec-1.0

# HashAlgorithm

## Summary

A mathematical algorithm that maps data of arbitrary size to a bit string.

## Description

A HashAlgorithm is a mathematical algorithm that maps data of arbitrary size to a bit string (the hash)
and is a one-way function, that is, a function which is practically infeasible to invert.

## Metadata

- name: HashAlgorithm

## Entries

- blake2b256: blake2b algorithm with a digest size of 256 https://datatracker.ietf.org/doc/html/rfc7693#section-4
- blake2b384: blake2b algorithm with a digest size of 384 https://datatracker.ietf.org/doc/html/rfc7693#section-4
- blake2b512: blake2b algorithm with a digest size of 512 https://datatracker.ietf.org/doc/html/rfc7693#section-4
- blake3: https://github.com/BLAKE3-team/BLAKE3-specs/blob/master/blake3.pdf
- crystalsKyber: https://pq-crystals.org/kyber/index.shtml
- crystalsDilithium: https://pq-crystals.org/dilithium/index.shtml
- falcon: https://falcon-sign.info/falcon.pdf
- md2: https://datatracker.ietf.org/doc/rfc1319/
- md4: https://datatracker.ietf.org/doc/html/rfc1186
- md5: https://datatracker.ietf.org/doc/html/rfc1321
- md6: https://people.csail.mit.edu/rivest/pubs/RABCx08.pdf
- other: any hashing algorithm that does not exist in this list of entries
- sha1: https://datatracker.ietf.org/doc/html/rfc3174
- sha224: secure hashing algorithm with a digest length of 224 https://datatracker.ietf.org/doc/html/draft-ietf-pkix-sha224-01
- sha256: secure hashing algorithm with a digest length of 256 https://www.rfc-editor.org/rfc/rfc4634
- sha3_224: sha3 with a digest length of 224 https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf
- sha3_256: sha3 with a digest length of 256 https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf
- sha3_384: sha3 with a digest length of 384 https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf
- sha3_512: sha3 with a digest length of 512 https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf
- sha384: secure hashing algorithm with a digest length of 384 https://www.rfc-editor.org/rfc/rfc4634
- sha512: secure hashing algorithm with a digest length of 512 https://www.rfc-editor.org/rfc/rfc4634
