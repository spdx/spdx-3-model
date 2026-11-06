SPDX-License-Identifier: Community-Spec-1.0

# issuerAgent

## Summary

issuerAgent is the agent that issued this Certificate.

## Description

issuerAgent specifies the Agent that signed and issued this Certificate. The issuerAgent vouches for the authenticity of the certificate's subject and is responsible for verifying the identity information provided by the certificate requester before issuing the certificate. This property establishes the trust relationship between the issuing authority and the certificate holder.

## Metadata

- name: issuerAgent
- Nature: ObjectProperty
- Range: /Core/Agent
