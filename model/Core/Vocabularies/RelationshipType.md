SPDX-License-Identifier: Community-Spec-1.0

# RelationshipType

## Summary

Information about the relationship between two Elements.

## Description

Provides information about the relationship between two Elements.
For example, you can represent a relationship between two different Files,
between a Package and a File, between two Packages, or between one SpdxDocument
and another SpdxDocument.

Relationship names should be descriptive enough to easily deduce the correct direction
from their name. The best way to do this is to make sure that the relationship
name completes the sentence:

`from` (is) (a) `RELATIONSHIP` `to`

## Metadata

- name: RelationshipType

## Entries

- affects: The `from` /Security/Vulnerability, Action or DefinedProcess affects each `to` Element.
- amendedBy: The `from` Element is amended by each `to` Element.
- ancestorOf: The `from` Element is an ancestor of each `to` Element.
- assumes: The `from` Element assumes each `to` /FunctionalSafety/Assumption.
- availableFrom: The `from` Element is available from the additional supplier described by each `to` Element.
- configures: The `from` Element is a configuration applied to each `to` Element, during a LifecycleScopeType period.
- conformsTo: The `from` Element conforms to each `to` /FunctionalSafety/Assumption or Specification.
- contains: The `from` Element contains each `to` Element.
- coordinatedBy: The `from` /Security/Vulnerability is coordinatedBy the `to` Agent(s) (vendor, researcher, or consumer agent).
- copiedTo: The `from` Element has been copied to each `to` Element.
- createdBy: The `from` Action or DefinedProcess is createdBy `to` Agent(s).
- delegatedTo: The `from` Agent is delegating an action to the Agent of the `to` Relationship (which shall be of type invokedBy), during a LifecycleScopeType period (e.g. the `to` invokedBy Relationship is being done on behalf of `from`).
- dependsOn: The `from` Element depends on each `to` Element, during a LifecycleScopeType period.
- descendantOf: The `from` Element is a descendant of each `to` Element.
- describes: The `from` Element describes each `to` Element. To denote the root(s) of a tree of elements in a collection, the rootElement property shall be used.
- doesNotAffect: The `from` /Security/Vulnerability has no impact on each `to` Element. The use of the `doesNotAffect` is constrained to `/Security/VexNotAffectedVulnAssessmentRelationship` classed relationships.
- evaluatedOn: The `from` Element has been evaluated on the `to` Element(s).
- expandsTo: The `from` Element expands out as an artifact described by each `to` Element.
- exploitCreatedBy: The `from` /Security/Vulnerability has had an exploit created against it by each `to` Agent.
- finetunedOn: The `from` Element has been finetuned on the `to` Element(s).
- fixedBy: Designates a `from` /Security/Vulnerability has been fixed by the `to` Agent(s).
- fixedIn: A `from` /Security/Vulnerability has been fixed in each `to` Element. The use of the `fixedIn` type is constrained to `/Security/VexFixedVulnAssessmentRelationship` classed relationships.
- follows: The `to` Element succeeds the `from` Element, establishing a unidirectional sequence. This succession is defined as chronological, procedural, or logical. It is used to represent either a temporal order (e.g., in a workflow) or a logical order for processing and traversal (e.g., in an ordered list).
- foundBy: Designates a `from` /Security/Vulnerability was originally discovered by the `to` Agent(s).
- generates: The `from` Element generates each `to` Element.
- hasAddedFile: Every `to` Element is a file added to the `from` Element (`from` hasAddedFile `to`).
- hasAssessmentFor: Relates a `from` /Security/Vulnerability and each `to` Element with a security assessment. The use of the `hasAssessmentFor` type is constrained to `/Security/VulnAssessmentRelationship` classed relationships.
- hasAssociatedVulnerability: Used to associate a `from` Artifact with each `to` /Security/Vulnerability.
- hasConcludedLicense: The `from` Artifact is concluded by the SPDX data creator to be governed by each `to` /SimpleLicensing/AnyLicenseInfo. If the `to` of an Artifact's `hasConcludedLicense` is not the same as the `to` of its `hasDeclaredLicense`, a written explanation should be provided in the comment field of the `hasConcludedLicense` relationship.
- hasContactPoint: The `from` Artifact has each `to` Agent as a contact point. The use of the `hasContactPoint` type is constrained to `ContactPointRelationship` classed relationships. The type of contact (i.e. security) may be specified using a `ContactPointRelationship` element.
- hasDataFile: The `from` Element treats each `to` Element as a data file. A data file is an artifact that stores data required or optional for the `from` Element's functionality. The `hasDataFile` relationship does not imply a dependency. Examples of data files include database files, index files, log files, AI model files, calibration data files, temporary files, and backup files. For configuration data, build input data, build output data, test artifacts, test datasets, and training datasets, the more specific relationship types `configures`, `hasInput`, `hasOutput`, `hasTest`, `testedOn`, and `trainedOn` shall be used, respectively.
- hasDeclaredLicense: The `from` Artifact was discovered to actually contain each `to` /SimpleLicensing/AnyLicenseInfo (for example, as detected by automated tooling).
- hasDeletedFile: Every `to` Element is a file deleted from the `from` Element (`from` hasDeletedFile `to`).
- hasDependencyManifest: The `from` Element has manifest files that contain dependency information in each `to` Element.
- hasDistributionArtifact: The `from` Element is distributed as an artifact in each `to` Element (e.g. an RPM or archive file).
- hasDocumentation: The `from` Element is documented by each `to` Element.
- hasDynamicLink: The `from` Element dynamically links in each `to` Element, during a LifecycleScopeType period.
- hasEvidence: Every `to` Element is considered as evidence for the `from` Element (`from` hasEvidence `to`).
- hasExample: Every `to` Element is an example for the `from` Element (`from` hasExample `to`).
- hasHost: The `from` /Build/Build was run on the `to` Element during a LifecycleScopeType period (e.g. the host that the build runs on).
- hasInput: The `from` /Build/Build, DefinedProcess or Action element has each `to` Element as an input.
- hasMetadata: Every `to` Element is metadata about the `from` Element (`from` hasMetadata `to`).
- hasNeed: The `from` Role has the `to` /FunctionalSafety/Need.
- hasOptionalComponent: Every `to` Element is an optional component of the `from` Element (`from` hasOptionalComponent `to`).
- hasOptionalDependency: The `from` Element optionally depends on each `to` Element, during a LifecycleScopeType period.
- hasOutput: The `from` /Build/Build, DefinedProcess or Action element generates each `to` Element as an output.
- hasPrerequisite: The `from` Element has a prerequisite on each `to` Element, during a LifecycleScopeType period.
- hasProvidedDependency: The `from` Element has a dependency on each `to` Element, dependency is not in the distributed artifact, but assumed to be provided, during a LifecycleScopeType period.
- hasRequirement: The `from` Element has a requirement on each `to` Element, during a LifecycleScopeType period.
- hasResolution: The `from` /SupplyChain/ResolutionAction points to the `to` /SupplyChain/OutOfSpecAction that is addressed.
- hasRoleIn: The `from` Element has a role in the `to` Element. The use of the hasRoleIn is constrained to `RoleRelationship` classed relationships.
- hasSpecification: Every `to` Element is a specification for the `from` Element (`from` hasSpecification `to`), during a LifecycleScopeType period.
- hasStaticLink: The `from` Element statically links in each `to` Element, during a LifecycleScopeType period.
- hasTest: Every `to` Element is a test artifact for the `from` Element (`from` hasTest `to`), during a LifecycleScopeType period.
- hasTestCase: Every `to` Element is a test case for the `from` Element (`from` hasTestCase `to`).
- hasVariant: Every `to` Element is a variant the `from` Element (`from` hasVariant `to`).
- implementedBy: The `from` Requirement is implemented in the `to` Element(s).
- isQualifiedFor: The `from` Agent is qualified for or can provided the `to` Role.
- invokedBy: The `from` Element was invoked by the `to` Agent, during a LifecycleScopeType period (for example, a /Build/Build element that describes a build step).
- locatedAt: `from` Element located at a specific `to` Location. A time period is optional.
- modifiedBy: The `from` Element is modified by each `to` Element.
- other: Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationship types (this relationship is directionless).
- packagedBy: Every `to` Element is a packaged instance of the `from` Element (`from` packagedBy `to`).
- patchedBy: Every `to` Element is a patch for the `from` Element (`from` patchedBy `to`).
- performedBy: Every `from` Action is performedBy `to` Agent.
- pretrainedOn: The `from` Element has been pretrained on the `to` Element(s).
- providesSupportFor: The `from` Agent provides support for each `to` Artifact. The use of the `providesSupportFor` type is constrained to `SupportRelationship` classed relationships.
- publishedBy: Designates a `from` /Security/Vulnerability was made available for public use or reference by each `to` Agent.
- reportedBy: Designates a `from` /Security/Vulnerability was first reported to a project, vendor, or tracking database for formal identification by each `to` Agent.
- republishedBy: Designates a `from` /Security/Vulnerability's details were tracked, aggregated, and/or enriched to improve context (i.e. NVD) by each `to` Agent.
- resolved: The `to` /SupplyChain/OutOfSpecAction is resolved in the `from` /SupplyChain/ResolutionAction.
- runsOn: The `from` Element (the instructions) runs on each `to` /Hardware/Hardware (processing element), during a LifecycleScopeType period.
- satisfies: The `from` Requirement satisfies `to` /FunctionalSafety/Need. Note: The Requirement is not generally intended to singularly satisfy a particular Need. It is more likely that a set of higher level Requirements is required to achieve a reasonable satisfaction of an expressed /FunctionalSafety/Need.
- serializedInArtifact: The `from` SpdxDocument can be found in a serialized form in each `to` Artifact.
- testedOn: The `from` Element has been tested on the `to` Element(s).
- tracedToDetail: The `from` Requirement is refined and further elaborated by each `to` Requirement, which contains more detailed implementation information.
- trainedOn: The `from` Element has been trained on the `to` Element(s).
- underInvestigationFor: The `from` /Security/Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `/Security/VexUnderInvestigationVulnAssessmentRelationship` classed relationships.
- usesTool: The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period.
- validatedOn: The `from` Element has been validated on the `to` Element(s).
- verifiedBy: The `from` Requirement that has verification (test, review, analysis etc.) details defined in the `to` /FunctionalSafety/RequirementVerification.
