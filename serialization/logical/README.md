# Logical Value Examples

[XML/RDF](https://cambridgesemantics.com/blog/semantic-university/learn-rdf/rdf-vs-xml/#:~:text=This%20brings%20us%20to%20the,is%20primarily%20a%20data%20model.),
Turtle, and JSON-LD are special-purpose data formats used to serialize
[RDF graphs](https://www.w3.org/TR/owl2-overview/#Overview).
In contrast, XML and JSON are general purpose data formats used to serialize arbitrary data,
including non-RDF applications such as
[GPX](https://en.wikipedia.org/wiki/GPS_Exchange_Format) or
[XLSX](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/f780b2d6-8252-4074-9fe3-5d7bc4830968)).
Other general data formats include YAML, tag-value, and spreadsheet, as well as machine-oriented
formats such as [CBOR](https://cbor.io/), [Protobuf](https://protobuf.dev/),
and [Avro](https://avro.apache.org/).

General data formats do not:
* assume that all data instances are nodes in a graph,
* reserve property names (such as @context, @id, @type, @graph) for special purposes, or
* require applications to perform any special processing based on reserved property names.

In order to develop equivalent serialized SPDX Element examples for both RDF and general
data formats, it is necessary to define what applications know about an Element - the
"logical value" of each example. Before serialization and after de-serialization the
logical value must be unaffected by how, or even if, the element has been serialized.

For clarity, logical values should not be expressed in any serialization data format.
An example logical value of an Annotation element would be a flat set of key-value pairs:
```
                             spdxId = 'http://spdx.acme.org/3FA9CB25#annotation34'
     type.annotation.annotationType = 'review'
            type.annotation.subject = 'http://spdx.acme.org/3FA9CB25#person5'
        type.annotation.contentType = 'text/plain'
          type.annotation.statement = 'Keanu Reeves is back as cyberpunk icon Neo but fans of the original will find this cynical reboot a bitter pill to swallow.'
           creationInfo.specVersion = 'v3.0'
             creationInfo.profile.0 = 'core'
               creationInfo.created = '2023-06-02T13:49:24+00:00'
           creationInfo.dataLicense = 'CC0-1.0'
             creationInfo.createdBy = 'http://spdx.acme.org/3FA9CB25#person1'
```
Or logical values could be formatted (less readably) as markdown bullets:

* spdxId: 'http://spdx.acme.org/3FA9CB25#annotation34'
* type.annotation.annotationType: 'review'
* type.annotation.subject: 'http://spdx.acme.org/3FA9CB25#person5'
* type.annotation.contentType: 'text/plain'
* ...

A serialization testing application would de-serialize an example Element in each
serialized format into the logical value, then compare it to logical values
de-serialized from corresponding examples of that Element in other formats.

Definitions:
* **Payload** - the sequence of bytes in a serialization data format that carries
one or more logical Element values
* **SpdxDocument** - an SPDX Element containing metadata about a Payload
* **ElementSet** - an arbitrary set of Element logical values.

An ElementSet could be a directory containing one or more logical value files,
and a serializer test reads those files and constructs a Payload and optionally
an SpdxDocument element describing that Payload.
A deserializer test reads the Payload and reconstructs the identical directory
of logical value files.

### SpdxDocument vs. Bundle

The serialization subgroup proposed developing a set of examples, including
Bundle, two Persons, and Bundle of two Persons.
This highlights the distinction between Elements and Payloads:
- two Person Elements is two logical values
- two Person Elements can be serialized into one Payload
- an SpdxDocument Element describes a Payload containing two Person Elements

The rationale for a Bundle type in the logical model has not been defined.
Every serialized value is a Payload, and if Bundle is an Element then Bundle must
be a synonym for (not an ancestor or descendant of) the SpdxDocument Element that
contains metadata about the Payload.

The development of logical and serialized Element examples will explore if a
Bundle type is needed.