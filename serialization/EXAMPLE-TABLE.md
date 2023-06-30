# SPDXv3 Serialization Playground

The purpose of this repo is to facilitate experimentation with and comparison between various suggested method for serializing the SPDXv3 logical model.

## Tenets
1. The [logical model](https://github.com/spdx/spdx-3-model/tree/main/model) is the single authoritative source for SPDXv3 content.
All examples submitted to the playground should be converted to instances that match the logical model.
If changes to the logical model invalidate examples, the examples should be updated accordingly.
2. Each serialization method has a sponsor (individual or group) that is responsible for creating the examples and test code for that method.
3. The barrier to entry is minimal. A sponsor may create as few or as many examples as they deem appropriate for defining the method.
The sponsor:
    * names the method
    * creates a subfolder with the method name, a README describing the method, examples of serialized data, and code to translate between model and serialized values
    * adds a column for the method to the comparison table with links to the examples that exist
    * adds a row to the comparison table if new examples are useful for illustrating the method.
    * submits a PR for the method, which the maintainers will merge with minimal bureaucracy
4. Although examples may be initially submitted to illustrate ideas before code has been developed to process them, it will
eventually be necessary to demonstrate that the examples correctly reflect the model.
The code for a method includes four programs:
    * element_to_model
    * model_to_element
    * element_set_to_payload
    * payload_to_element_set

## Individual Element Examples
* The code for a method translates between individual element examples and the corresponding model types in both directions

| Model Examples                                       | [RDF](rdf/README.md) | [XML](xml/README.md) | [JSON-LD](jsonld/README.md) |        [JSON1](json1/README.md)        |        [JSON2](json2/README.md)         | [JSON3](json3/README.md) | Protobuf | CBOR | YAML | [Text1](text1/README.md) |
|------------------------------------------------------|:--------------------:|----------------------|-----------------------------|:--------------------------------------:|:---------------------------------------:|--------------------------|----------|:----:|------|:------------------------:|
| --- **Agents** ---                                   |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Agent](logical/agent.json)-1                        |                      |                      |                             |    [o](json1/examples/agent1.json)     |     [o](json2/examples/agent1.json)     |                          |          |      |      |                          |
| [Person](logical/person.json)-1 minimal CreationInfo |                      |                      |                             |    [o](json1/examples/person1.json)    |    [o](json2/examples/person1.json)     |                          |          |      |      |                          |
| [Person](logical/person.json)-2 full CreationInfo    |                      |                      |                             |    [o](json1/examples/person2.json)    |    [o](json2/examples/person2.json)     |                          |          |      |      |                          |
| [Person](logical/person.json)-3 no CreationInfo???   |                      |                      |                             |    [o](json1/examples/person3.json)    |    [o](json2/examples/person3.json)     |                          |          |      |      |                          |
| [Organization](logical/organization.json)-1          |                      |                      |                             |     [o](json1/examples/org1.json)      |      [o](json2/examples/org1.json)      |                          |          |      |      |                          |
| [Tool](logical/tool.json)-1 not an Agent             |                      |                      |                             |     [o](json2/examples/tool1.json)     |     [o](json2/examples/tool1.json)      |                          |          |      |      |                          |
| --- **Annotations** ---                              |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Annotation](logical/annotation.json)-1              |                      |                      |                             |  [o](json1/examples/annotation1.json)  |  [o](json2/examples/annotation1.json)   |                          |          |      |      |                          |
| --- **Artifacts** ---                                |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Package]()-1                                        |                      |                      |                             |   [o](json1/examples/package1.json)    |    [o](json2/examples/package1.json)    |                          |          |      |      |                          |
| [Package]()-2 with ExternalIdentifier                |                      |                      |                             |   [o](json1/examples/package2.json)    |                                         |                          |          |      |      |                          |
| [Package]()-3 with ExternalReference                 |                      |                      |                             |   [o](json1/examples/package3.json)    |                                         |                          |          |      |      |                          |
| [File]()-1                                           |                      |                      |                             |     [o](json1/examples/file1.json)     |     [o](json2/examples/file1.json)      |                          |          |      |      |                          |
| [File]()-2                                           |                      |                      |                             |     [o](json1/examples/file2.json)     |     [o](json2/examples/file2.json)      |                          |          |      |      |                          |
| [Snippet]()-1                                        |                      |                      |                             |   [o](json1/examples/snippet1.json)    |                                         |                          |          |      |      |                          |
| --- **Relationships** ---                            |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Relationship]()-1 - Pkg1, File1, File2              |                      |                      |                             | [o](json1/examples/relationship1.json) |                                         |                          |          |      |      |                          |
| [Relationship]()-2 - with time properties            |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [LifecycleScopeRelationship]()-1                     |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [AssessmentRelationship]()-1                         |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [SoftwareDependencyRelationship]()-1                 |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| --- **Collections** ---                              |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Bom]()-1                                            |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [Sbom]()-1 Pkg1, File1, File2, Rel1                  |                      |                      |                             |                                        |     [o](json2/examples/sbom1.json)      |                          |          |      |      |                          |
| [Sbom]()-2 Pkg1, Pkg2                                |                      |                      |                             |                                        |     [o](json2/examples/sbom1.json)      |                          |          |      |      |                          |
| --- **SpdxDocuments** ---                            |                      |                      |                             |                                        |                                         |                          |          |      |      |                          |
| [SpdxDocument]()-1 describes Payload1                |                      |                      |                             |                                        | [o](json2/examples/spdx_document1.json) |                          |          |      |      |                          |
| [SpdxDocument]()-2 describes Payload2                |                      |                      |                             |                                        | [o](json2/examples/spdx_document2.json) |                          |          |      |      |                          |
| [SpdxDocument]()-3 describes Payload3                |                      |                      |                             |                                        | [o](json2/examples/spdx_document3.json) |                          |          |      |      |                          |

## Multiple Element Examples
* An element set is the list of individual element example values that are included in a Payload.  
* A Payload is the result of combining the element set into serialized data in a method-specific manner.
* The code for a method translates between the Payload and its element set in both directions. 

| Example                 | [RDF](rdf/README.md) | [XML](xml/README.md) | [JSON-LD](jsonld/README.md) |       [JSON1](json_ld/README.md)       |        [JSON2](json1/README.md)        | [JSON3](json2/README.md) | Protobuf | CBOR | YAML | [Text1](text1/README.md) |
|-------------------------|:--------------------:|----------------------|-----------------------------|:--------------------------------------:|:--------------------------------------:|--------------------------|----------|:----:|------|:------------------------:|
| Payload1 - File1, File2 |                      |                      |                             |                                        | [o](json2/examples/spdx_payload1.json) |                          |          |      |      |                          |
| Payload2 - Sbom1, Sbom2 |                      |                      |                             |                                        | [o](json2/examples/spdx_payload2.json) |                          |          |      |      |                          |
| Payload3 - v2.3         |                      |                      |                             | [o](json1/examples/spdx_payload3.json) |                                        |                          |          |      |      |                          |

