# Notes on Serialization

## Serialization info

_TBD_

## Serialization formats

The files in this directory provide some notes on the specific serialization formats.

The notes are numbered for easier referencing -- the order is **not** significant.

## Use cases

Examples of how to serialize the following cases:

### Core and software profile use cases:
- Person
- Agent
- Annotation
- File
- Package
- Package with ExternalIdentifier
- Package with ExternalReference
- Relationship with Package contains two Files
- Relationship with time properties
- SBOM with two Files
- SpdxDocument with two Files
- SpdxDocument with NamespaceMap
- SpdxDocument with ExternalMap
- Person with no CreationInfo
- Person with minimal CreationInfo
- Person with full CreationInfo
- Bundle
- two Persons
- Bundle of two Persons

### Licensing profile use cases:
- single artifact under one listed license
- single artifact under one custom license
- single artifact under license expression of listed licenses
- single artifact under license expression of listed and custom licenses
- two artifacts under same license expression of listed and custom licenses

### Security profile use cases:
The following list begins with base examples and sequentially adds expositional elements and relationships step-by-step:
- An initial set of vulnerability elements
- Adding vulnerability elements with security external reference types including FIXME
- Adding hasAssociatedVulnerability relationship between a vulnerability element and a software profile element
- Adding multiple hasAssessmentFor relationships for vulnerability assessment relationships between vulnerability element and package element for VEX, CVSS, etc. to communicate, e.g.,
  - changes to a vulnerability element’s status affecting a specific package element using VEX (Vulnerability Exploitability eXchange)  (see the serialized examples listed in Syntax under each SPDX-3-MODEL/model/Security Class definition)
  - how a vulnerability element may be fixed for a particular software package element
  - results of a vulnerability scan or audit
- Adding foundBy, publishedBy, reportedBy relationships between an agent element and a vulnerability element


### Build Profile use cases to be added here
