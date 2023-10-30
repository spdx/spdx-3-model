SPDX-License-Identifier: Community-Spec-1.0

# X-Collection

## Summary

A collection of SPDX Elements that could potentially be serialized.

## Description

The X-Collection provides a convenient way to express information about collections of SPDX Elements that could potentially be serialized as complete
units (e.g., all in-scope SPDX data within a single JSON-LD file). X-Collection is indpendent of any particular serialization format or instance.
Information we wish to preserve about a specific instance of serialization of this SPDX content is NOT expressed using the X-Collection but rather using an associated Artifact representing a particular instance of SPDX data physical serialization.

Any instance of serialization of SPDX data MUST NOT contain more than one X-Collection element definition.

## Metadata

- name: X-collection
- SubclassOf: ElementCollection
- Instantiability: Concrete

## Properties

- imports
  - type: ExternalMap
- namespaceMap
  - type:NamespaceMap
- dataLicense
  - type: AnyLicenseInfo
