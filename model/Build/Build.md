SPDX-License-Identifier: Community-Spec-1.0

# Build

## Summary

The Build Profile defines the set of information required to describe an
instance of a Software Build.

## Description

A Software Build is defined here as the act of converting software inputs into
software artifacts using software build tools. Inputs can include source code,
config files, artifacts that are build environments, and build tools. Outputs
can include intermediate artifacts to other build inputs or the final
artifacts.

The Build profile provides a subclass of Element called Build.

It also provides a minimum set of required Relationship Types from the Core
profile:

- hasInput: Describes the relationship from the Build element to its inputs.
- hasOutput: Describes the relationship from the Build element to its outputs.
- invokedBy: Describes the relationship from the Build element to the Agent
  that invoked it.

In addition, the following Relationship Types may be used to describe a Build.

- hasHost: Describes the relationship from the Build element to the build stage
  or host.
- configures: Describes the relationship from a configuration to the Build
  element.
- ancestorOf: Describes a relationship from a Build element to Build elements
  that describe its child builds.
- descendantOf: Describes a relationship from a child Build element to its
  parent.
- usesTool: Describes a relationship from a Build element to a build tool.

All relationships in the Build Profile are scoped to the "build"
LifecycleScopeType period.

The `hasInput` relationship can be applied to a config file or a build tool if
the nature of these inputs are not known at the creation of an SPDX document.

## Metadata

- id: https://spdx.org/rdf/3.0.1/terms/Build
- name: Build

## Profile Conformance

Conformance to the Build profile requires one or more instances of the Build
class. In addition, there must be at least three instances `Relationship`s with
type `LifecycleScopedRelationship`, where the "scope" property must be "build"
and the "from" property must be the Build instance.

At the minimum, the Build profile must contain a `hasInput`, `hasOutput`, and
`invokedBy` relationshipType. If an input is known to be a build configuration
or a build tool, the `hasInput` relationshipType can be replaced by a
`configures` or `usesTool` relationshipType.
