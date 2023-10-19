SPDX-License-Identifier: Community-Spec-1.0

# Lite

## Summary

The Lite Profile defines the minimum set of information required for verifying the list of software package and ensureing compliance.

## Description  

The Lite profile namespace defines the additional requirements needed to follow essential compliance rules in the software supply chain. It enables comparison and verification of information against what was recorded in earlier versions of SPDX item descriptions.  
This is intended to include the following items as minimum information:  

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
