# Logical Element Examples

### Agents
- [Agent1](examples/agent1.logval)
- [Person1 with minimal CreationInfo](examples/person1.logval) - "person"
- [Person2 with full CreationInfo](examples/person2.logval)) - second of "two persons"
- [Person3 with no CreationInfo](examples/person3.logval) - ?? does this even mean anything?
- [Organization1](examples/org1.logval)
- [Tool1](examples/tool1.logval) - not an Agent

### Annotations
- [Annotation1](examples/annotation1.logval)

### Relationships
- [Relationship1 with Package contains two Files](examples/relationship1.logval)
- [Relationship2 with time properties](examples/relationship2.logval)
- [LifecycleScopeRelationship3](examples/relationship3.logval)
- [AssessmentRelationship4](examples/relationship4.logval)
- [SoftwareDependencyRelationship5](examples/relationship5.logval)

### Artifacts
- [Package1](examples/package1.logval)
- [Package2 with ExternalIdentifier](examples/package2.logval)
- [Package3 with ExternalReference](examples/package3.logval)
- [File1](examples/file1.logval)
- [File2](examples/file2.logval)
- [Snippet1](examples/snippet1.logval)

### Collections
- [Bom1](examples/bom1.logval)
- [Sbom1 with two Files](examples/sbom1.logval) - One Element: Sbom1

### Documents
- [SpdxDocument1 with two Files](examples/spdx_document1.logval) - File1 and File2 - this is a "bundle"
- [SpdxDocument2 with two Persons](examples/spdx_document2.logval) - Person1 and Person2 - also a "bundle"
- [SpdxDocument3 with Sbom1 with two files](examples/spdx_document3.logval) - Sbom1, File1, File2, Org1, Tool1, SpdxDocument3
- [SpdxDocument4 with NamespaceMap](examples/spdx_document4.logval)
- [SpdxDocument5 with ExternalMap](examples/spdx_document5.logval)
---
- Bundle - same as any SpdxDocument
- Bundle of two Persons - same as SpdxDocument2