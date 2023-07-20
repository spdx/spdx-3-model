# Notes on Serialization

## Serialization info

_TBD_

## Serialization formats

The files in this directory provide some notes on the specific serialization formats.

The notes are numbered for easier referencing -- the order is **not** significant.

## Use cases

Examples of how to serialize the following cases:
- Person
- Agent
- Annotation
- File
- Package
- Package with ExternalIdentifier
- Package with ExternalReference
- Relationship with Package contains two Files
- Relationship with time properties
- Sbom with two Files
- SpdxDocument with two Files
- SpdxDocument with NamespaceMap
- SpdxDocument with ExternalMap
- Person with minimal CreationInfo (Person1)
- Person with full CreationInfo (Person2)
- Bundle
- two Persons
- Bundle of two Persons

Payloads containing multiple elements:
- 1: two Persons: [Person1, Person2]
- 2: two Files: [File1, File2]
- 3: Relationship with Package contains two Files: [Relationship1, Package1, File1, File2]
- 4: Sbom with two files: [Sbom1, File1, File2]
- 5: SpdxDocument(Payload2) with two Files, no NamespaceMap: [SpdxDocument1, File1, File2]
- 6: SpdxDocument(Payload6) with two Files, no NamespaceMap: [SpdxDocument2, File1, File2]
- 7: SpdxDocument(Payload6) with NamespaceMap: [SpdxDocument2, File1, File2]
- 8: SpdxDocument(Payload6) with NamespaceMap and CreationInfoMap: [SpdxDocument2, File1, File2]
- 9: SpdxDocument with ExternalMap: [SpdxDocument3, ?, ?]
- 10: Bundle of two Persons [Person1, Person2] (same as 1)

Licensing use cases:
- single artifact under one listed license
- single artifact under one custom license
- single artifact under license expression of listed licenses
- single artifact under license expression of listed and custom licenses
- two artifacts under same license expression of listed and custom licenses

- security use cases to be added here
- build use cases to be added here
