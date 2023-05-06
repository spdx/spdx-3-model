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

- amends: The `to` element(s) amends the `from` element
- ancestor: The `to` element(s) is an ancestor of the `from` element
- availableFrom:  This relationship is used to identify additional suppliers where an artifact is available from.
- buildDependency: The `to` element(s) is a build dependency of the `from` element
- buildTool: Build tool used to build an element. This may be used to describe the build tool of a Build instance.
- contains: The `to` element(s) is contained by the `from` element
- copy: The `to` element(s) is a copy of the `from` element
- dataFile: The `to` element(s) is a data file related to the the `from` element
- dependencyManifest: The `to` element(s) is manifest file containing dependency information related to the `from` element
- dependsOn: The `to` element(s) is a dependecy of the `from` element
- descendant: This relationship may be used to describe child builds of a Build instance.
- describes: The `to` element(s) is  described by the `from` element.  This can be used to denote the root(s) of a tree of elements contained in an SBOM.
- devDependency: The `to` element(s) is a development depenency for the `from` element
- devTool: The `to` element(s) is a development tool for the `from` element
- distributionArtifact: The `to` element(s) is an artifact intended for distribution of the `from` element (e.g. an RPM or archive file)
- documentation: The `to` element(s) is documentation for the `from` element
- dynamicLink: The `to` element(s) is dynamically linked to the `from` element
- example: The `to` element(s) is an example for the `from` element
- expandedFromArchive: The `to` element(s) is an artifact expanded from the `from` archive file
- fileAdded: The `to` element(s) is is a file added to the `from` element
- fileDeleted: The `to` element(s) is a file deleted from the `from` element
- fileModified: The `to` element(s) is a modification of the `from` element
- generates: The `to` element(s) is generated from the `from` element
- metafile: The `to` element(s) is is a file containing metadata about the `from` element
- optionalComponent: The `to` element(s) is an optional component of the `from` element
- optionalDependency: The `to` element(s) is an optional dependency of the `from` element
- other: The `to` element(s) is related to the `from` element where the relationship type is not described by any of the SPDX relationhip types
- packages: The `to` element(s) is a packged form of the `from` element
- patch: The `to` element(s) is a patch for the `from` element
- prerequisite: The `to` element(s) is a prerequisite of the `from` element
- providedDependency: The `to` element(s) is a dependency not included in the distributed artifact but is assumed to be provided the `from` element
- requirementFor: The `to` element(s) is required for the `from` element
- runtimeDependency: The `to` element(s) is a runtime dependency for the `from` element
- specificationFor: The `to` element(s) is a specification for the `from` element
- staticLink: The `to` element(s) is statically linked to the `from` element
- test: The `to` element(s) is a test artifact for the `from` element
- testCase: The `to` element(s) is a test case for the `from` element
- testDependency: The `to` element(s) is a test dependency for the `from` element
- testTool: The `to` element(s) is a test tool for the `from` element
- variant: The `to` element(s) is a variant the `from` element
- buildInputOf: Input to the build instance
- buildOutputOf: Output of the build instance
- buildConfigOf: Build configuration of the build instance
- buildInvokedBy: Agent that invoked the build
- buildOnBehalfOf: Actor for which buildInvokedBy is acting on behalf of
- buildHostOf: Element in which the build instance runs on
- hasAssociatedVulnerability: (Security) Used to associate a security vulnerability with a software artifact
- coordinatedBy: (Security) Used to identify the vendor, researcher, or consumer agent performing coordination for a vulnerability
- hasCvssV2AssessmentFor: (Security) Specifies a CVSS V2 assessment of a vulnerability
- hasCvssV3AssessmentFor: (Security) Specifies a CVSS V3 assessment of a vulnerability
- hasEpssAssessmentFor: (Security) Specifies a EPSS assessment of a vulnerability
- hasExploitCatalogAssessmentFor: (Security) Specifies a exploit catalog assessment of a vulnerability
- hasSsvcAssessmentFor: (Security) Specifies a SSVC assessment of a vulnerability
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
