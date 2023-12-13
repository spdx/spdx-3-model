# Notes on Serialization

## Serialization info

This directory contains the specifications and examples for all supported SPDX serialization formats.

There is a specification markdown file for each supported format describing the serialization.

A collection of elements can be serialized in multiple formats.

Within the model, we have an SpdxDocument which represents the common properties of the collection of elements across all serialization data formats.

We can represent/characterize the actual serialized bytes using an Artifact element in the model.

A Relationship of type spdxDocumentForArtfact can be used to relate an SpdxDocument to one more serialized for of the SpdxDocument.

When serializing the physical SpdxDocument, any properties of the logical element which can be represented using native mechanisms in the specific serialization format (e.g. @context prefixes in JSON-LD in place of the namespaceMap) should use these mechanisms and the remaining properties should be serialized within the “XCollection” element itself.

There is at most one SpdxDocument in the serialization.

There is at most one SpdxDocument element defined in any given instance of serialization.

## Serialization formats

The specification markdown files describing rules for each serialization format will contain an SpdxDocument section describing how each of the properties of SpdxDocument are serialized for the given serialization format.

The specification and examples are numbered for easier referencing -- the order is **not** significant.

Current supported formats are:
- [JSON-LD](json-ld.md)

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
