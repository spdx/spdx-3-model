# Classes draft
## main draft
```mermaid
---
title: SPDX Operations Profile
---
classDiagram
    Element <|-- Relationship
    Element <|-- Agent
    Element <|-- Artifact
    Artifact <|-- CompliancePackage
    Agent <|-- Organization
    Agent <|-- Person
    Agent <|-- Country
    Relationship <|-- OperationsAssessmentRelationship
    OperationsAssessmentRelationship <|-- ExportControlAssessmentRelationship
    OperationsAssessmentRelationship <|-- ObligationsAssessmentRelationship
    OperationsAssessmentRelationship <|-- ApplicationFactsAssessmentRelationship
    OperationsAssessmentRelationship <|-- DeliverableFactsAssessmentRelationship
    OperationsAssessmentRelationship <|-- SupplierDeliverableFactsAssessmentRelationship

    note for Organization "ID \naddress \nwebsite"
    note for OperationsAssessmentRelationship "Inspired by VulnAssessmentRelationship"
namespace Core {
    class Element{
        <<Core>>
    }
    class Relationship{
        <<Core>>
    }
    class Artifact{
        <<Core>>
    }
    class Agent{
        <<Core>>
    }
    class Organization{
        <<Core>>
    }
    class Person{
        <<Core>>
    }
}
namespace OperationsClasses {

    class Country{
        + countryCode: CountryCode[1]
    }
    class CompliancePackage{
        + sourceCodeLink
    }
    class OperationsAssessmentRelationship{
        + Core/Relationship/to: Element[1]
        + assessedElement: Element[0..1]
        + suppliedBy: Agent[0..n]
        + publishedTime: DateTime[0..1]
        + modifiedTime: DateTime[0..1]
        + withdrawnTime: DateTime[0..1]
    }
    class ExportControlAssessmentRelationship{
        + notRequired: Boolean[1]
        + purpose: String[0..1]
        + countryOfOrigin: Country[0..n]
        + manufacturer: ?Agent/Organization?[0..n]
        + Classification: ExportControlClassification[1..n]
        + SpecialTechnology: SpecialTechnology[0..1]
        + ExportControlQandA: QandA[0..n]
    }
    class ObligationsAssessmentRelationship{
        + Obligation: String [0..n]
    }
    
    class ApplicationFactsAssessmentRelationship{
		+ productOwner: Person[0..1]
		+ documentationLink: security/locator[0..n]
		+ productAccessURL: security/locator[0..n]
		+ applicationFactsComment: comment[0..n]
		+ distributionTarget
		+ distributedDeliverables
		+ technicalDeployment
		+ contact: Agent [1]
		+ scope
		+ relationType
		+ supplyChainContext: String[1]
		+ releaseCycles
		+ fossComplianceBundleProvision
		+ contractSetup
		+ fossTermsTowardsCustomer
		+ distributionTermsTowardsCustomer
		+ customerFossContact: Person[0..n]
    }
    class DeliverableFactsAssessmentRelationship{
		+ swLanguage
		+ dependencyManager: Agent[1]
		+ packageManager
		+ environmentFramework
		+ applicationCategory
		+ applicationType
		+ distributionMethod
		+ operatingSystem
		+ consistsOf
		+ developedBy
		+ contact
		+ linkToArchitecture
		+ osmConcept
        + deliverableReview: QandA[0..n]
		+ deliverabelComment: comment[0..n]
    }
    class SupplierDeliverableFactsAssessmentRelationship{
        + supplierName
        + deliverableFromSupplier
        + fossTermsTowardsSupplier
        + distributionTermsFromSupplier
        + fossComplianceBundleConsumption
        + ?supplierFossContact: Person[1]
        + supplierDeliverableFactsComment: comment[0..n]
    }
}
```
## nonElementClasses
```mermaid
classDiagram
namespace OperationsNonElementClasses {
    class QandA{
        + question: String[0..1]
        + clarification: String[0..1]
    }
    class ExportControlClassification{
        + classificationSystem
        + classificationValue
        + classificationComment
    }
    class SpecialTechnology{
        + includesCrypto: Boolean[1]
        + cryptoDetail: Crypto[0..n]
        + externalServerCommunication: Boolean
        + includesArtificialIntelligence: Boolean
    }
}

```
## Enumerations
- CountryCode
    - Enumeration, external provider (official country code)
- classificationSystem
    - Enumeration, possibly external provider

# Notes
- remove 'supplierFossContact' from 'SupplierDeliverableFactsAssessmentRelationship'?
    - this is probably better tracked in CRM and linked to 'Agent' class supplier information 
- 'Delivery' as its own relationship rather than part of an assessment?