SPDX-License-Identifier: Community-Spec-1.0

# Email

## Summary

An individual identifier in RFC 822 email address format.

## Description

An Email identifier is a String constrained to be an addr-spec as defined in RFC 822 Section 6.1,
consisting of a local-part "@" domain.  Like a URI, an email id only provides identification;
access to a resource is neither guaranteed nor implied by the presence of an email id.
The email address syntax is defined in https://www.rfc-editor.org/rfc/rfc822#section-6.1.

## Metadata

- name: Email
- SubclassOf: xsd:string

## Properties

