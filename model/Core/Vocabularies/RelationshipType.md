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

- amends: TODOdescription
- ancestor: TODOdescription
- buildDependency: TODOdescription
- buildTool: Build tool used to build an element. This may be used to describe the build tool of a Build instance.
- contains: TODOdescription
- copy: TODOdescription
- dataFile: TODOdescription
- dependencyManifest: TODOdescription
- dependsOn: TODOdescription
- descendant: This relationship may be used to describe child builds of a Build instance.
- describes: TODOdescription
- devDependency: TODOdescription
- devTool: TODOdescription
- distributionArtifact: TODOdescription
- documentation: TODOdescription
- dynamicLink: TODOdescription
- example: TODOdescription
- expandedFromArchive: TODOdescription
- fileAdded: TODOdescription
- fileDeleted: TODOdescription
- fileModified: TODOdescription
- generates: TODOdescription
- metafile: TODOdescription
- optionalComponent: TODOdescription
- optionalDependency: TODOdescription
- other: TODOdescription
- packages: TODOdescription
- patch: TODOdescription
- prerequisite: TODOdescription
- providedDependency: TODOdescription
- requirementFor: TODOdescription
- runtimeDependency: TODOdescription
- specificationFor: TODOdescription
- staticLink: TODOdescription
- suppliedBy: TODOdescription
- test: TODOdescription
- testCase: TODOdescription
- testDependency: TODOdescription
- testTool: TODOdescription
- variant: TODOdescription
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
