# Logical Element Examples
## Individual Elements
### Agents
- [Agent1](examples/agent1.json)
- [Person1](examples/person1.json) - minimal CreationInfo
- [Person2](examples/person2.json)) - full CreationInfo
- [Person3](examples/person3.json) -  no CreationInfo?? does this even mean anything?
- [Organization1](examples/org1.json)
- [Tool1](examples/tool1.json) - not an Agent

### Annotations
- [Annotation1](examples/annotation1.json)

### Artifacts
- [Package1](examples/package1.json)
- [Package2](examples/package2.json) - with ExternalIdentifier
- [Package3](examples/package3.json) - with ExternalReference
- [File1](examples/file1.json)
- [File2](examples/file2.json)
- [Snippet1](examples/snippet1.json)

### Relationships
- [Relationship1](examples/relationship1.json) - Package1, File1, File2
- [Relationship2](examples/relationship2.json) - with time properties
- [LifecycleScopeRelationship1](examples/relationship3.json)
- [AssessmentRelationship1](examples/relationship4.json)
- [SoftwareDependencyRelationship1](examples/relationship5.json)

### Collections
- [Bom1]
- [Sbom1](examples/sbom1.json) - Package1, File1, File2, Relationship1
- [Sbom2] - Package1, Package2

### SpdxDocuments
- [SpdxDocument1](examples/spdx_document1.json) - Metadata about Payload1
- [SpdxDocument2](examples/spdx_document1.json) - Metadata about Payload2
- [SpdxDocument3](examples/spdx_document1.json) - Metadata about Payload3

## Multiple Elements
### Payloads
- [Payload1] - File1, File2
- [Payload2] - Sbom1, Sbom2
- [Payload3] - Sbom1, Package1, File1, File2, Relationship1, plus Person1, Tool1, SpdxDocument3



- [Payload1 uncompressed](examples/spdx_payload1_uncompressed.json) - Two elements: File1 and File2
- [Payload1](examples/spdx_payload1.json) - File1 and File2 with namespaceMap and creationInfo in header
- [Payload2](examples) - File1 and File2 and SpdxDocument1


### Payload, SpdxDocument, and Bundle
One or more of the individual elements above can be serialized as either a list of values shown above,
or as a payload.

A Payload is a list of values compressed by:
- factoring out shared namespace prefixes using NamespaceMap, and
- factoring out shared creationInfo

```json
{
  "namespaceMap": {"...": "..."},
  "creationInfo": {"...": "..."},
  "element": ["....", "...", "...", "..."]
}
```
An SpdxDocument Element is metadata about a Payload.  
Bundle is a synonym for SpdxDocument.
