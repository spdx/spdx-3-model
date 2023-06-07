# Logical Element Examples

### Agents
- [Agent1](examples/agent1.json)
- [Person1 with minimal CreationInfo](examples/person1.json) - "person"
- [Person2 with full CreationInfo](examples/person2.json)) - second of "two persons"
- [Person3 with no CreationInfo](examples/person3.json) - ?? does this even mean anything?
- [Organization1](examples/org1.json)
- [Tool1](examples/tool1.json) - not an Agent

### Annotations
- [Annotation1](examples/annotation1.json)

### Relationships
- [Relationship1 with Package contains two Files](examples/relationship1.json)
- [Relationship2 with time properties](examples/relationship2.json)
- [LifecycleScopeRelationship3](examples/relationship3.json)
- [AssessmentRelationship4](examples/relationship4.json)
- [SoftwareDependencyRelationship5](examples/relationship5.json)

### Artifacts
- [Package1](examples/package1.json)
- [Package2 with ExternalIdentifier](examples/package2.json)
- [Package3 with ExternalReference](examples/package3.json)
- [File1](examples/file1.json)
- [File2](examples/file2.json)
- [Snippet1](examples/snippet1.json)

### Collections
- [Bom1](examples/bom1.json)
- [Sbom1 with two Files](examples/sbom1.json) - Sbom1 with File1 and File2

### Documents
- [SpdxDocument1 with two Files](examples/spdx_document1.json) - File1 and File2 - this is a "bundle"
- [SpdxDocument2 with two Persons](examples/spdx_document2.json) - Person1 and Person2 - also a "bundle"
- [SpdxDocument3 with Sbom1 with two files and dependencies](examples/spdx_document3.json) - Sbom1, File1, File2, Org1, SpdxDocument3
- [SpdxDocument4 with NamespaceMap](examples/spdx_document4.json)
- [SpdxDocument5 with ExternalMap](examples/spdx_document5.json)
---
- Bundle - same as any SpdxDocument
- Bundle of two Persons - same as SpdxDocument2