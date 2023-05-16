SPDX-License-Identifier: Community-Spec-1.0

# RelationshipType

## Summary

Information about the relationship between two Elements.

## Description

Provides information about the relationship between two Elements.
For example, you can represent a relationship between two different Files,
between a Package and a File, between two Packages, or between one SPDXDocument and another SPDXDocument.

Build Profile specific RelationshipType descriptions can be found [here](https://github.com/spdx/spdx-3-build-profile/blob/main/model/relationships.md)

## Metadata

- name: RelationshipType

## Entries

- amends: Every `to` Element amends the `from` Element
- ancestor: Every `to` Element is an ancestor of the `from` Element
- availableFrom:  This relationship is used to identify additional suppliers where an artifact is available from.
- buildDependency: Every `to` Element is a build dependency of the `from` Element
- buildTool: Build tool used to build an Element. This may be used to describe the build tool of a Build instance
- contains: Every `to` Element is contained by the `from` Element
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
- dynamicLink: Every `to` Element is dynamically linked to the `from` Element
- example: Every `to` Element is an example for the `from` Element
- expandedFromArchive: Every `to` Element is an artifact expanded from the `from` archive file
- fileAdded: Every `to` Element is is a file added to the `from` Element
- fileDeleted: Every `to` Element is a file deleted from the `from` Element
- fileModified: Every `to` Element is a modification of the `from` Element
- generates: Every `to` Element is generated from the `from` Element
- metafile: Every `to` Element is is a file containing metadata about the `from` Element
- optionalComponent: Every `to` Element is an optional component of the `from` Element
- optionalDependency: Every `to` Element is an optional dependency of the `from` Element
- other: Every `to` Element is related to the `from` Element where the relationship type is not described by any of the SPDX relationhip types
- packages: Every `to` Element is a packaged form of the `from` Element
- patch: Every `to` Element is a patch for the `from` Element
- prerequisite: Every `to` Element is a prerequisite of the `from` Element
- providedDependency: Every `to` Element is a dependency not included in the distributed artifact but is assumed to be provided the `from` Element
- requirementFor: Every `to` Element is required for the `from` Element
- runtimeDependency: Every `to` Element is a runtime dependency for the `from` Element
- specificationFor: Every `to` Element is a specification for the `from` Element
- staticLink: Every `to` Element is statically linked to the `from` Element
- test: Every `to` Element is a test artifact for the `from` Element
- testCase: Every `to` Element is a test case for the `from` Element
- testDependency: Every `to` Element is a test dependency for the `from` Element
- testTool: Every `to` Element is a test tool for the `from` Element
- variant: Every `to` Element is a variant the `from` Element
- buildInputOf: Input to the build instance
- buildOutputOf: Output of the build instance
- buildConfigOf: Build configuration of the build instance
- buildInvokedBy: Agent that invoked the build
- buildOnBehalfOf: Actor for which buildInvokedBy is acting on behalf of
- buildHostOf: Element in which the build instance runs on
- hasAssociatedVulnerability: (Security) Used to associate a security vulnerability with a software artifact
- coordinatedBy: (Security) Used to identify the vendor, researcher, or consumer agent performing coordination for a vulnerability
- hasAssessmentFor: (Security) Relates a Vulnerability and an Element with a security assessment.
- exploitCreatedBy: (Security) Designates an agent has created an exploit against a vulnerability
- fixedBy: (Security) Designates a vulnerability has been fixed by an agent
- foundBy: (Security) Designates an agent was the original discoverer of a security vulnerability
- publishedBy: (Security) Designates the agent that made a vulnerability record available for public use or reference
- reportedBy: (Security) Designates the agent that first reported a vulnerability to the project, vendor, or tracking database for formal identification 
- republishedBy: (Security) Designates the agent that tracked, aggregated, and/or enriched vulnerability details to improve context (i.e. NVD)
- affects: (Security/VEX) Designates one or more elements as affected by a vulnerability
- doesNotAffect: (Security/VEX) Specifies a vulnerability has no impact on one or more elements
- fixedIn: (Security/VEX) A vulnerability has been fixed in one or more elements
- underInvestigationFor: (Security/VEX) The impact of a vulnerability is being investigated
