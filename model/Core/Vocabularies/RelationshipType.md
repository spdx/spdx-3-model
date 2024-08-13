SPDX-License-Identifier: Community-Spec-1.0

# RelationshipType

## Summary

Information about the relationship between two Elements.

## Description

Provides information about the relationship between two Elements.
For example, you can represent a relationship between two different Files,
between a Package and a File, between two Packages, or between one SpdxDocument
and another SpdxDocument.

Relationship names be descriptive enough to easily deduce the correct direction
from their name. The best way to do this is to make sure that the relationship
name completes the sentence:

`from` (is) (a) `RELATIONSHIP` `to`

## Metadata

- name: RelationshipType

## Entries

- affects: The `from` Vulnerability affects each `to` Element. The use of the `affects` type is constrained to `VexAffectedVulnAssessmentRelationship` classed relationships.
- amendedBy: The `from` Element is amended by each `to` Element.
- ancestorOf: The `from` Element is an ancestor of each `to` Element.
- availableFrom: The `from` Element is available from the additional supplier described by each `to` Element.
- configures: The `from` Element is a configuration applied to each `to` Element, during a LifecycleScopeType period.
- contains: The `from` Element contains each `to` Element.
- coordinatedBy: The `from` Vulnerability is coordinatedBy the `to` Agent(s) (vendor, researcher, or consumer agent).
- copiedTo: The `from` Element has been copied to each `to` Element.
- delegatedTo: The `from` Agent is delegating an action to the Agent of the `to` Relationship (which must be of type invokedBy), during a LifecycleScopeType (e.g. the `to` invokedBy Relationship is being done on behalf of `from`).
- dependsOn: The `from` Element depends on each `to` Element, during a LifecycleScopeType period.
- descendantOf: The `from` Element is a descendant of each `to` Element.
- describes: The `from` Element describes each `to` Element. To denote the root(s) of a tree of elements in a collection, the rootElement property should be used.
- doesNotAffect: The `from` Vulnerability has no impact on each `to` Element. The use of the `doesNotAffect` is constrained to `VexNotAffectedVulnAssessmentRelationship` classed relationships.
- expandsTo: The `from` archive expands out as an artifact described by each `to` Element.
- exploitCreatedBy: The `from` Vulnerability has had an exploit created against it by each `to` Agent.
- fixedBy: Designates a `from` Vulnerability has been fixed by the `to` Agent(s).
- fixedIn: A `from` Vulnerability has been fixed in each of the `to` Element(s). The use of the `fixedIn` type is constrained to `VexFixedVulnAssessmentRelationship` classed relationships.
- foundBy: Designates a `from` Vulnerability was originally discovered by the `to` Agent(s).
- generates: The `from` Element generates each `to` Element.
- hasAddedFile: Every `to` Element is a file added to the `from` Element (`from` hasAddedFile `to`).
- hasAssessmentFor: Relates a `from` Vulnerability and each `to` Element(s) with a security assessment. To be used with `VulnAssessmentRelationship` types.
- hasAssociatedVulnerability: Used to associate a `from` Artifact with each `to` Vulnerability.
- hasConcludedLicense: The `from` Software Artifact is concluded by the SPDX data creator to be governed by each `to` license.
- hasDataFile: The `from` Element treats each `to` Element as a data file. A data file is an artifact that stores data required or optional for the `from` Element's functionality. A data file can be a database file, an index file, a log file, an AI model file, a calibration data file, a temporary file, a backup file, and more. For AI training dataset, test dataset, test artifact, configuration data, build input data, and build output data, please consider using the more specific relationship types: `trainedOn`, `testedOn`, `hasTest`, `configures`, `hasInputs`, and `hasOutputs`, respectively. This relationship does not imply dependency.
- hasDeclaredLicense: The `from` Software Artifact was discovered to actually contain each `to` license, for example as detected by use of automated tooling.
- hasDeletedFile: Every `to` Element is a file deleted from the `from` Element (`from` hasDeletedFile `to`).
- hasDependencyManifest: The `from` Element has manifest files that contain dependency information in each `to` Element.
- hasDistributionArtifact: The `from` Element is distributed as an artifact in each Element `to` (e.g. an RPM or archive file).
- hasDocumentation: The `from` Element is documented by each `to` Element.
- hasDynamicLink: The `from` Element dynamically links in each `to` Element, during a LifecycleScopeType period.
- hasEvidence: Every `to` Element is considered as evidence for the `from` Element (`from` hasEvidence `to`).
- hasExample: Every `to` Element is an example for the `from` Element (`from` hasExample `to`).
- hasHost: The `from` Build was run on the `to` Element during a LifecycleScopeType period (e.g. the host that the build runs on).
- hasInputs: The `from` Build has each `to` Elements as an input, during a LifecycleScopeType period.
- hasMetadata: Every `to` Element is metadata about the `from` Element (`from` hasMetadata `to`).
- hasOptionalComponent: Every `to` Element is an optional component of the `from` Element (`from` hasOptionalComponent `to`).
- hasOptionalDependency: The `from` Element optionally depends on each `to` Element, during a LifecycleScopeType period.
- hasOutputs: The `from` Build element generates each `to` Element as an output, during a LifecycleScopeType period.
- hasPrerequisite: The `from` Element has a prerequisite on each `to` Element, during a LifecycleScopeType period.
- hasProvidedDependency: The `from` Element has a dependency on each `to` Element, dependency is not in the distributed artifact, but assumed to be provided, during a LifecycleScopeType period.
- hasRequirement: The `from` Element has a requirement on each `to` Element, during a LifecycleScopeType period.
- hasSpecification: Every `to` Element is a specification for the `from` Element (`from` hasSpecification `to`), during a LifecycleScopeType period.
- hasStaticLink: The `from` Element statically links in each `to` Element, during a LifecycleScopeType period.
- hasTest: Every `to` Element is a test artifact for the `from` Element (`from` hasTest `to`), during a LifecycleScopeType period.
- hasTestCase: Every `to` Element is a test case for the `from` Element (`from` hasTestCase `to`).
- hasVariant: Every `to` Element is a variant the `from` Element (`from` hasVariant `to`).
- invokedBy: The `from` Element was invoked by the `to` Agent, during a LifecycleScopeType period (for example, a Build element that describes a build step).
- modifiedBy: The `from` Element is modified by each `to` Element.
- other: Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationhip types (this relationship is directionless).
- packagedBy: Every `to` Element is a packaged instance of the `from` Element (`from` packagedBy `to`).
- patchedBy: Every `to` Element is a patch for the `from` Element (`from` patchedBy `to`).
- publishedBy: Designates a `from` Vulnerability was made available for public use or reference by each `to` Agent.
- reportedBy: Designates a `from` Vulnerability was first reported to a project, vendor, or tracking database for formal identification by each `to` Agent.
- republishedBy: Designates a `from` Vulnerability's details were tracked, aggregated, and/or enriched to improve context (i.e. NVD) by each `to` Agent.
- serializedInArtifact: The `from` SpdxDocument can be found in a serialized form in each `to` Artifact.
- testedOn: The `from` Element has been tested on the `to` Element(s).
- trainedOn: The `from` Element has been trained on the `to` Element(s).
- underInvestigationFor: The `from` Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `VexUnderInvestigationVulnAssessmentRelationship` classed relationships.
- usesTool: The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period.
