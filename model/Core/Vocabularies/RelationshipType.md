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
- serializedInArtifact: The `from` SpdxDocument can be found in a serialized form in each `to` Artifact.
- testedOn: The `from` Element has been tested on the `to` Element(s).
- tracedToDetail: The `from` Requirement is refined and further elaborated by each `to` Requirement, which contains more detailed implementation information.
- trainedOn: The `from` Element has been trained on the `to` Element(s).
- underInvestigationFor: The `from` /Security/Vulnerability impact is being investigated for each `to` Element. The use of the `underInvestigationFor` type is constrained to `/Security/VexUnderInvestigationVulnAssessmentRelationship` classed relationships.
- usesTool: The `from` Element uses each `to` Element as a tool, during a LifecycleScopeType period.
- validatedOn: The `from` Element has been validated on the `to` Element(s).
- verifiedBy: The `from` Requirement that has verification (test, review, analysis etc.) details defined in the `to` /FunctionalSafety/RequirementVerification.

## SPARQL

- affects_from
  - message: When relationship is affects, from must be a Vulnerability, Action, or DefinedProcess
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/affects> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Action> }
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/DefinedProcess> }
        }

- assumes_to
  - message: When relationship is assumes, to must be an Assumption
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/assumes> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <FunctionalSafety/Assumption> }
        }

- configures_type
  - message: When relationship is configures, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/configures> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- conformsTo_to
  - message: When relationship is conformsTo, to must be an Assumption or Specification
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/conformsTo> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <FunctionalSafety/Assumption> }
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Specification> }
        }

- coordinatedBy_from
  - message: When relationship is coordinatedBy, from must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/coordinatedBy> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- createdBy_from
  - message: When relationship is createdBy, from must be an Action or DefinedProcess
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/createdBy> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Action> }
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/DefinedProcess> }
        }

- createdBy_to
  - message: When relationship is createdBy, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/createdBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- delegatedTo_from
  - message: When relationship is delegatedTo, from must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/delegatedTo> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- delegatedTo_to
  - message: When relationship is delegatedTo, to must be a Relationship whose relationshipType is invokedBy
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/delegatedTo> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS {
                ?to rdf:type/rdfs:subClassOf* <Core/Relationship> .
                ?to <Core/relationshipType> <Core/RelationshipType/invokedBy> .
            }
        }

- delegatedTo_type
  - message: When relationship is delegatedTo, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/delegatedTo> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- dependsOn_type
  - message: When relationship id dependsOn, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/dependsOn> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- doesNotAffect_from
  - message: When relationship is doesNotAffect, from must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/doesNotAffect> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- doesNotAffect_type
  - message: When relationship is doesNotAffect, class must be VexNotAffectedVulnAssessmentRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/doesNotAffect> .
            FILTER NOT EXISTS { $this rdf:type <Security/VexNotAffectedVulnAssessmentRelationship> }
        }

- exploitCreatedBy_to
  - message: When relationship is exploitCreatedBy, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/exploitCreatedBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- fixedBy_from
  - message: When relationship is fixedBy, from must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/fixedBy> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- fixedBy_to
  - message: When relationship is fixedBy, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/fixedBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- fixedIn_from
  - message: When relationship is fixedIn, from must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/fixedIn> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- fixedIn_type
  - message: When relationship is fixedIn, class must be VexFixedVulnAssessmentRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/fixedIn> .
            FILTER NOT EXISTS { $this rdf:type <Security/VexFixedVulnAssessmentRelationship> }
        }

- foundBy_to
  - message: When relationship is foundBy, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/foundBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- hasAssessmentFor_from
  - message: When relationship is hasAssessmentFor, from must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasAssessmentFor> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- hasAssessmentFor_type
  - message: When relationship is hasAssessmentFor, class must be VulnAssessmentRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasAssessmentFor> .
            FILTER NOT EXISTS { $this rdf:type <Security/VulnAssessmentRelationship> }
        }

- hasAssociatedVulnerability_to
  - message: When relationship is hasAssociatedVulnerability, to must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasAssociatedVulnerability> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- hasConcludedLicense_to
  - message: When relationship is hasConcludedLicense, to must be an AnyLicenseInfo
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasConcludedLicense> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <SimpleLicensing/AnyLicenseInfo> }
        }

- hasContactPoint_to
  - message: When relationship is hasContactPoint, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasContactPoint> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- hasContactPoint_type
  - message: When relationship is hasContactPoint, class must be ContactPointRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasContactPoint> .
            FILTER NOT EXISTS { $this rdf:type <Core/ContactPointRelationship> }
        }

- hasDeclaredLicense_to
  - message: When relationship is hasDeclaredLicense, to must be an AnyLicenseInfo
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasDeclaredLicense> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <SimpleLicensing/AnyLicenseInfo> }
        }

- hasDynamicLink_type
  - message: When relationship is hasDynamicLink, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasDynamicLink> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- hasHost_from
  - message: When relationship is hasHost, from must be a Build
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasHost> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Build/Build> }
        }

- hasHost_type
  - message: When relationship is hasHost, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasHost> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- hasInput_from
  - message: When relationship is hasInput, from must be a Build, DefinedProcess, or Action
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasInput> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Build/Build> }
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/DefinedProcess> }
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Action> }
        }

- hasOptionalDependency_type
  - message: When relationship is hasOptionalDependency, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasOptionalDependency> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- hasOutput_from
  - message: When relationship is hasOutput, from must be a Build, DefinedProcess, or Action
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasOutput> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Build/Build> }
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/DefinedProcess> }
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Action> }
        }

- hasPrerequisite_type
  - message: When relationship is hasPrerequisite, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasPrerequisite> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- hasProvidedDependency_type
  - message: When relationship is hasProvidedDependency, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasProvidedDependency> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- hasRequirement_type
  - message: When relationship is hasRequirement, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasRequirement> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- hasResolution_from
  - message: When relationship is hasResolution, from must be a ResolutionAction
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasResolution> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <SupplyChain/ResolutionAction> }
        }

- hasResolution_to
  - message: When relationship is hasResolution, to must be an OutOfSpecAction
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasResolution> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <SupplyChain/OutOfSpecAction> }
        }

- hasRoleIn_type
  - message: When relationship is hasRoleIn, class must be RoleRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasRoleIn> .
            FILTER NOT EXISTS { $this rdf:type <Core/RoleRelationship> }
        }

- hasSpecification_type
  - message: When relationship is hasSpecification, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasSpecification> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- hasStaticLink_type
  - message: When relationship is hasStaticLink, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasStaticLink> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- hasTest_type
  - message: When relationship is hasTest, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/hasTest> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- implementedBy_from
  - message: When relationship is implementedBy, from must be a Requirement
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/implementedBy> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Requirement> }
        }

- invokedBy_to
  - message: When relationship is invokedBy, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/invokedBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- invokedBy_type
  - message: When relationship is invokedBy, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/invokedBy> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- performedBy_from
  - message: When relationship is performedBy, from must be an Action
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/performedBy> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Action> }
        }

- performedBy_to
  - message: When relationship is performedBy, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/performedBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- providesSupportFor_from
  - message: When relationship is providesSupportFor, from must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/providesSupportFor> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- providesSupportFor_to
  - message: When relationship is providesSupportFor, to must be an Artifact
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/providesSupportFor> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Artifact> }
        }

- providesSupportFor_type
  - message: When relationship is providesSupportFor, class must be SupportRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/providesSupportFor> .
            FILTER NOT EXISTS { $this rdf:type <Core/SupportRelationship> }
        }

- publishedBy_from
  - message: When relationship is publishedBy, from must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/publishedBy> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- publishedBy_to
  - message: When relationship is publishedBy, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/publishedBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- reportedBy_from
  - message: When relationship is reportedBy, from must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/reportedBy> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- reportedBy_to
  - message: When relationship is reportedBy, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/reportedBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- republishedBy_from
  - message: When relationship is republishedBy, from must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/republishedBy> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- republishedBy_to
  - message: When relationship is republishedBy, to must be an Agent
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/republishedBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Agent> }
        }

- resolved_from
  - message: When relationship is resolved, from must be a ResolutionAction
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/resolved> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <SupplyChain/ResolutionAction> }
        }

- resolved_to
  - message: When relationship is resolved, to must be an OutOfSpecAction
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/resolved> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <SupplyChain/OutOfSpecAction> }
        }

- runsOn_to
  - message: When relationship is runsOn, to must be a Hardware
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/runsOn> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Hardware/Hardware> }
        }

- runsOn_type
  - message: When relationship is runsOn, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/runsOn> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- serializedInArtifact_from
  - message: When relationship is serializedInArtifact, from must be a SpdxDocument
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/serializedInArtifact> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/SpdxDocument> }
        }

- serializedInArtifact_to
  - message: When relationship is serializedInArtifact, to must be an Artifact
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/serializedInArtifact> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Artifact> }
        }

- tracedToDetail_from
  - message: When relationship is tracedToDetail, from must be a Requirement
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/tracedToDetail> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Requirement> }
        }

- tracedToDetail_to
  - message: When relationship is tracedToDetail, to must be a Requirement
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/tracedToDetail> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <Core/Requirement> }
        }

- underInvestigationFor_from
  - message: When relationship is underInvestigationFor, from must be a Vulnerability
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/underInvestigationFor> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Security/Vulnerability> }
        }

- underInvestigationFor_type
  - message: When relationship is underInvestigationFor, class must be VexUnderInvestigationVulnAssessmentRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/underInvestigationFor> .
            FILTER NOT EXISTS { $this rdf:type <Security/VexUnderInvestigationVulnAssessmentRelationship> }
        }

- usesTool_type
  - message: When relationship is usesTool, class must be LifecycleScopedRelationship
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/usesTool> .
            FILTER NOT EXISTS { $this rdf:type <Core/LifecycleScopedRelationship> }
        }

- verifiedBy_from
  - message: When relationship is verifiedBy, from must be a Requirement
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/verifiedBy> .
            $this <Core/from> ?from .
            FILTER NOT EXISTS { ?from rdf:type/rdfs:subClassOf* <Core/Requirement> }
        }

- verifiedBy_to
  - message: When relationship is verifiedBy, to must be a RequirementVerification
  - query: <<<

        SELECT $this WHERE {
            $this <Core/relationshipType> <Core/RelationshipType/verifiedBy> .
            $this <Core/to> ?to .
            FILTER NOT EXISTS { ?to rdf:type/rdfs:subClassOf* <FunctionalSafety/RequirementVerification> }
        }
