SPDX-License-Identifier: Community-Spec-1.0

# LitePackage  

## Summary

LitePackage contains the minimum part for package.

## Description

LitePackage contains the minimum part for package.

## Metadata

- name: LitePackage
- SubclassOf: /Software/Package
- Instantiability: Concrete

## Properties

- packageComment
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

## External properties restrictions

- /Core/Element/name
  - minCount: 1
- /Software/Package/packageVersion  
  - minCount: 1  
- /Software/Package/packageUrl  
  - minCount: 1  
- /Software/SoftwareArtifact/concludedLicense  
  - minCount: 1  
- /Software/SoftwareArtifact/declaredLicense  
  - minCount: 1  
- /Software/SoftwareArtifact/copyrightText  
  - minCount: 1  
