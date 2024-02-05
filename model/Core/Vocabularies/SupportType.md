SPDX-License-Identifier: Community-Spec-1.0

# SupportType

## Summary

Indicates the type of support that is associated with an artifact.

## Description
SupportType is an enumeration of the various types of support commonly found for artifacts in the software supply chain. Specific details of what that support entails are provided by agreements between the producer and consumer of the artifact. 

## Metadata

- name: SupportType

## Entries
- development - the artifact is in active development and is not considered ready for formal support from the supplier.
- support - the artifact has been released, and is supported from the supplier.   There is a validUntilDate that can provide additional information about the duration of support.
- limitedSupport - the artifact has been released, and there is limited support available from the supplier. There is a validUntilDate that can provide additional information about the duration of support.
- endOfSupport - there is a defined end of support for the artifact from the supplier.  This may also be referred to as end of life. There is a validUntilDate that can be used to signal when support ends for the artifact. 
- noSupport - there is no support for the artifact from the supplier, consumer assumes any support obligations.
- noAssertion - no assertion about the type of support is made.   This is considered the default if no other support type is used.
