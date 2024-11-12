SPDX-License-Identifier: Community-Spec-1.0

# buildType

## Summary

A buildType is a hint that is used to indicate the toolchain, platform, or
infrastructure that the build was invoked on.

## Description

A buildType is an IRI expressing the toolchain, platform, or infrastructure that
the build was invoked on.

The buildType is used to interpret the meaning of other build parameters by
defining the "type" of build; if the same buildType is seen in different Build
elements, it means they are the same kind of build, but difference instances
and possible with different configurations.

If you are not using a well-known buildType, it should be namespaced to a
domain you own to prevent conflicts with other buildType IRIs.

Examples of a buildType might be:

- A GitHub action workflow
- A step in a GitHub actions pipeline
- An invocation of a compiler or other tool
- A script that orchestrates builds at a higher level

Keep in mind that builds can be "nested" using the `ancestorOf` relationship.

If the buildType IRI is not recognized, it is still possible to inspect other
properties of the build, but it may not be possible to derive deeper meaning
from them.

For more information, see the SLSA definition of buildType.

## Metadata

- name: buildType
- Nature: DataProperty
- Range: xsd:anyURI
