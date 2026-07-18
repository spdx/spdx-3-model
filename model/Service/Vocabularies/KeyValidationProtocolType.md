SPDX-License-Identifier: Community-Spec-1.0

# KeyValidationProtocolType

## Summary

Protocols which support PKI key validation.

## Description

This enumeration provides common protocols used in key validation used during the authentication of servers or services over a network.

## Metadata

- name: KeyValidationProtocolType

## Entries

- ocsp: Online Certificate Status Protocol, or OCSP, is a common scheme used to maintain the security of a server and other network resources as defined in [RFC 2560](https://datatracker.ietf.org/doc/rfc2560/)
- crl: Certificate Revocation List, or CRL, is a list of revoked certificates as defined in [RFC 5280]](https://datatracker.ietf.org/doc/rfc5280/) that is downloaded from the Certificate Authority (CA).
- other: A key validation protocol not covered by one of the other KeyValidationProtocolType.
