# Serialized Logical Element Examples
## Individual Elements

| Example                              | RDF |                 JSON-LD                 |                    JSON                    | YAML | CBOR | Text |
|--------------------------------------|:---:|:---------------------------------------:|:------------------------------------------:|------|:----:|:----:|
| --- **Agents** ---                   |     |                                         |                                            |      |      |      |
| Agent1                               |     |    [o](jsonld/examples/agent1.json)     |       [o](json/examples/agent1.json)       |      |      |      |
| Person1 - minimal CreationInfo       |     |    [o](jsonld/examples/person1.json)    |      [o](json/examples/person1.json)       |      |      |      |
| Person2 - full CreationInfo          |     |    [o](jsonld/examples/person2.json)    |      [o](json/examples/person2.json)       |      |      |      |
| Person3 -  no CreationInfo???        |     |    [o](jsonld/examples/person3.json)    |      [o](json/examples/person3.json)       |      |      |      |
| Organization1                        |     |     [o](jsonld/examples/org1.json)      |        [o](json/examples/org1.json)        |      |      |      |
| Tool1 - not an Agent                 |     |      [o](json/examples/tool1.json)      |       [o](json/examples/tool1.json)        |      |      |      |
| --- **Annotations** ---              |     |                                         |                                            |      |      |      |
| Annotation1                          |     |  [o](jsonld/examples/annotation1.json)  |    [o](json/examples/annotation1.json)     |      |      |      |
| --- **Artifacts** ---                |     |                                         |                                            |      |      |      |
| Package1                             |     |   [o](jsonld/examples/package1.json)    |      [o](json/examples/package1.json)      |      |      |      |
| Package2 - with ExternalIdentifier   |     |   [o](jsonld/examples/package2.json)    |                                            |      |      |      |
| Package3 - with ExternalReference    |     |   [o](jsonld/examples/package3.json)    |                                            |      |      |      |
| File1                                |     |     [o](jsonld/examples/file1.json)     |       [o](json/examples/file1.json)        |      |      |      |
| File2                                |     |     [o](jsonld/examples/file2.json)     |       [o](json/examples/file2.json)        |      |      |      |
| Snippet1                             |     |   [o](jsonld/examples/snippet1.json)    |                                            |      |      |      |
| --- **Relationships** ---            |     |                                         |                                            |      |      |      |
| Relationship1 - Pkg1, File1, File2   |     | [o](jsonld/examples/relationship1.json) |                                            |      |      |      |
| Relationship2 - with time properties |     |                                         |                                            |      |      |      |
| LifecycleScopeRelationship1          |     |                                         |                                            |      |      |      |
| AssessmentRelationship1              |     |                                         |                                            |      |      |      |
| SoftwareDependencyRelationship1      |     |                                         |                                            |      |      |      |
| --- **Collections** ---              |     |                                         |                                            |      |      |      |
| Bom1                                 |     |                                         |                                            |      |      |      |
| Sbom1 - Pkg1, File1, File2, Rel1     |     |                                         |       [o](json/examples/sbom1.json)        |      |      |      |
| Sbom2 - Pkg1, Pkg2                   |     |                                         |       [o](json/examples/sbom1.json)        |      |      |      |
| --- **SpdxDocuments** ---            |     |                                         |                                            |      |      |      |
| SpdxDocument1 - describes Payload1   |     |                                         |   [o](json/examples/spdx_document1.json)   |      |      |      |
| SpdxDocument2 - describes Payload2   |     |                                         |   [o](json/examples/spdx_document2.json)   |      |      |      |
| SpdxDocument3 - describes Payload3   |     |                                         |   [o](json/examples/spdx_document3.json)   |      |      |      |

## Multiple Elements

| Example                 | RDF |                 JSON-LD                 |                 JSON                  | YAML  |               CBOR               | Text |
|-------------------------|:---:|:---------------------------------------:|:-------------------------------------:|-------|:--------------------------------:|:----:|
| Payload1 - File1, File2 |     |                                         | [o](json/examples/spdx_payload1.json) |       |                                  |      |
| Payload2 - Sbom1, Sbom2 |     |                                         | [o](json/examples/spdx_payload2.json) |       |                                  |      |
| Payload3 - v2.3         |     | [o](jsonld/examples/spdx_payload3.json) |                                       |       |                                  |      |

### Payload
In non-RDF serializations including JSON, an SpdxDocument Element is metadata about a Payload, and Bundle is a synonym for SpdxDocument.
A JSON Payload is a list of values compressed by:
- factoring out shared namespace prefixes
- factoring out shared creationInfo

```json
{
  "namespaceMap": {"...": "..."},
  "creationInfo": {"...": "..."},
  "element": ["....", "...", "...", "..."]
}
```
