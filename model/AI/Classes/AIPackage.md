-------
SPDX-License-Identifier: Community-Spec-1.0

# AIPackage

## Description

Metadata information that can be added to a package to describe an AI application or trained AI model. 

## Metadata

- SubclassOf: Software/Package
						Defaults are: 0..*
## Properties
-energyConsumption
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
  
-standardsCompliance
  - type: xsd:string
  - minCount: 0
  
-limitations
  - type: xsd:string
  - minCount: 0
  - maxCount:1

-typeOfModel
  - type: xsd:string
  - minCount: 0

-informationAboutTraining
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

-informationAboutApplication
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

-hyperparameters
  - type: xsd:string
  - minCount: 0


-dataPreprocessingSteps
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

-modelExplainabilityMechanisms
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

-sensitivePersonalInformation
  - type: PresenceType
  - minCount: 0
  - maxCount: 1

-metricsDecisionThresholds
  - type: xsd:string
  - minCount: 0

-metrics
  - type: xsd:string
  - minCount: 0

-domain
  - type: xsd:string
  - minCount: 0


-autonomyType
  - type: PresenceType
  - minCount: 0
  - maxCount: 1


-safetyRiskAssessment
  - type: SafetyRiskAssessmentType
  - minCount: 0
  - maxCount: 1

- contentIdentifier
  - type: anyURI
  - minCount: 0
  - maxCount: 1

- packagePurpose
  - type: SoftwarePurpose
  - minCount: 0
- downloadLocation
  - type: anyURI
  - minCount: 0
  - maxCount: 1
- packageUrl
  - type: anyURI
  - minCount: 0
  - maxCount: 1
- homePage
  - type: anyURI
  - minCount: 0
  - maxCount: 1

