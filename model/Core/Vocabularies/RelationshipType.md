SPDX-License-Identifier: Community-Spec-1.0

# RelationshipType

## Summary

Information about the relationship between two Elements.

## Description

Provides information about the relationship between two Elements.
For example, you can represent a relationship between two different Files,
between a Package and a File, between two Packages, or between one SPDXDocument and another SPDXDocument.

## Metadata

- name: RelationshipType

## Entries

- affects: (Security/VEX) Designates one or more elements as affected by a vulnerability
- amends: Every `to` Element amends the `from` Element
- ancestor: Every `to` Element is an ancestor of the `from` Element
- availableFrom:  This relationship is used to identify additional suppliers where an artifact is available from.
- buildDependency: Every `to` Element is a build dependency of the `from` Element
- buildTool: Build tool used to build an Element. This may be used to describe the build tool of a Build instance
- coordinatedBy: (Security) Used to identify the vendor, researcher, or consumer agent performing coordination for a vulnerability
- contains: Every `to` Element is contained by the `from` Element
- configOf: (Build) Configuration information applied to an Element instance during a LifeycleScopeType period.  Example: Build configuration of the build instance
- copy: Every `to` Element is a copy of the `from` Element
- dataFile: Every `to` Element is a data file related to the the `from` Element
- dependencyManifest: Every `to` Element is manifest file containing dependency information related to the `from` Element
- dependsOn: Every `to` Element is a dependecy of the `from` Element
- descendant: This relationship may be used to describe child builds of a Build instance.
- describes: Every `to` Element is  described by the `from` Element.  This can be used to denote the root(s) of a tree of elements contained in an SBOM.
- devDependency: Every `to` Element is a development dependency for the `from` Element
- devTool: Every `to` Element is a development tool for the `from` Element
- distributionArtifact: Every `to` Element is an artifact intended for distribution of the `from` Element (e.g. an RPM or archive file)
- documentation: Every `to` Element is documentation for the `from` Element
- doesNotAffect: (Security/VEX) Specifies a vulnerability has no impact on one or more elements
- dynamicLink: Every `to` Element is dynamically linked to the `from` Element
- example: Every `to` Element is an example for the `from` Element
- evidenceFor: (Dataset) Every `to` Element is can be considered as evidence for the `from` Element
- expandedFromArchive: Every `to` Element is an artifact expanded from the `from` archive file
- exploitCreatedBy: (Security) Designates an agent has created an exploit against a vulnerability
- fileAdded: Every `to` Element is is a file added to the `from` Element
- fileDeleted: Every `to` Element is a file deleted from the `from` Element
- fileModified: Every `to` Element is a modification of the `from` Element
- fixedBy: (Security) Designates a vulnerability has been fixed by an agent
- fixedIn: (Security/VEX) A vulnerability has been fixed in one or more elements
- foundBy: (Security) Designates an agent was the original discoverer of a security vulnerability
- generates: Every `to` Element is generated from the `from` Element
- hasAssessmentFor: (Security) Relates a Vulnerability and an Element with a security assessment.
- hasAssociatedVulnerability: (Security) Used to associate a security vulnerability with a software artifact
- hostOf: (Build) The`from` Element in which every instance of the `to` Element during a LifecycleScopeType period runs on.   Example: host that the build runs on for an element.
- inputOf: (Build) Input to the Element instance during a LifecycleScopeType period.   Example: input to the build instance for an element. 
- invokedBy: (Build) Every`to` Agent that invoked a `from` Element instance during a LifecycleScopeType period.  Example: Agent that invoked the build for an element
- metafile: Every `to` Element is is a file containing metadata about the `from` Element
- onBehalfOf: (Build) Every `to` Agent acting on behalf of another `from` Agent during a LifecycleScopeType period
- optionalComponent: Every `to` Element is an optional component of the `from` Element
- optionalDependency: Every `to` Element is an optional dependency of the `from` Element
- other: Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationhip types
- outputOf: (Build) `from` Element that is output `to` the Element instance during a LifecycleScopeType period.  Example: output of the build instance
- packages: Every `to` Element is a packaged form of the `from` Element
- patch: Every `to` Element is a patch for the `from` Element
- prerequisite: Every `to` Element is a prerequisite of the `from` Element
- providedDependency: Every `to` Element is a dependency not included in the distributed artifact but is assumed to be provided the `from` Element
- publishedBy: (Security) Designates the agent that made a vulnerability record available for public use or reference
- reportedBy: (Security) Designates the agent that first reported a vulnerability to the project, vendor, or tracking database for formal identification 
- republishedBy: (Security) Designates the agent that tracked, aggregated, and/or enriched vulnerability details to improve context (i.e. NVD)
- requirementFor: Every `to` Element is required for the `from` Element
- runtimeDependency: Every `to` Element is a runtime dependency for the `from` Element
- specificationFor: Every `to` Element is a specification for the `from` Element
- staticLink: Every `to` Element is statically linked to the `from` Element
- test: Every `to` Element is a test artifact for the `from` Element
- testCase: Every `to` Element is a test case for the `from` Element
- testDependency: Every `to` Element is a test dependency for the `from` Element
- testTool: Every `to` Element is a test tool for the `from` Element
- testedOn: (AI, Dataset) The `from` Element has been tested on the `to` Element
- trainedOn: (AI, Dataset) The `from` Element has been trained by the `to` Element(s)
- underInvestigationFor: (Security/VEX) The impact of a vulnerability is being investigated
- variant: Every `to` Element is a variant the `from` Element
