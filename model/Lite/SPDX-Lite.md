SPDX-License-Identifier: Community-Spec-1.0

# Lite

## Summary

The Lite Profile defines the minimum set of information required for verifying the list of software package and ensureing compliance during the design phase, while maintaining interoperability with information documented using earlier SPDX syntax conventions.

## Description  

The Lite profile namespace contains only the additional requirements to comply with the various compliance processes required when considering the software supply chain.  
This is intended to include the following information as minimum information:  

- Creation information of the SBOM  
- Package information  
- License information for the package  
- Relationship  

## Metadata

- id: https://rdf.spdx.org/v3/Lite
- name: Lite

## External properties restrictions  

- /Software/Sbom  
  - /Core/Element/creationInfo  
    * minCount: 1 (default)  
- /Software/Package  
  - /Core/Element/spdxId  
    * minCount: 1 (default)  
- /Software/Package  
  - /Core/Element/name  
    * minCount: 1 (default)  
- /Software/Package
  - /Core/Element/creationInfo  
    * minCount: 1 (default)  
- /Software/Package  
  - /Core/Artifact/suppliedBy  
    * minCount: 1  
- /Software/Package/packageVersion  
  * minCount: 1  
- /Software/Package  
  - /Software/SoftwareArtifact/copyrightText  
    * minCount: 1  

- /Core/Relationship/relatoinshipType  
  * minCount: 1 (default)  
- /Core/Relationship/from  
  * minCount: 1 (default)  

- /SimpleLicensing/LicenseExpression/licenseExpression  
  * minCount: 1 (default)  
- /SimpleLicensing/SimpleLicensingText/liecnseText  
  * minCount: 1 (default)  

## EOF  
