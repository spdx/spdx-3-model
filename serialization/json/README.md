# JSON Serialized Examples

[XML/RDF](https://cambridgesemantics.com/blog/semantic-university/learn-rdf/rdf-vs-xml/#:~:text=This%20brings%20us%20to%20the,is%20primarily%20a%20data%20model.),
Turtle, and JSON-LD are special-purpose data formats used to serialize
[RDF graphs](https://www.w3.org/TR/owl2-overview/#Overview).
In contrast, XML and JSON are general purpose data formats used to serialize arbitrary data,
including non-RDF applications such as
[GPX](https://en.wikipedia.org/wiki/GPS_Exchange_Format) or
[XLSX](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/f780b2d6-8252-4074-9fe3-5d7bc4830968).
Other general data formats include YAML, tag-value, and spreadsheet, as well as machine-oriented
formats such as [CBOR](https://cbor.io/), [Protobuf](https://protobuf.dev/),
and [Avro](https://avro.apache.org/).

JSON and other general data formats do not:
* assume that all data instances are nodes in a graph,
* reserve property names (such as @context, @id, @type, @graph) for special purposes, or
* require applications to perform any special processing based on reserved property names.

### Definitions:
* **Logical Value** - the value of an application variable prior to serializing or
after deserializing an Element instance.
* **ElementSet** - an arbitrary set of Logical Values.
* **Payload** - the result of serializing an ElementSet.
* **SpdxDocument** - an SPDX Element containing metadata about a Payload.

### Logical Values

A serialization testing application de-serializes an example Element in one
format (e.g., JSON) into logical value A, then compares it to the logical
value B resulting from de-serializing the same Element in another format.
In order to evaluate the expression A == B, A and B must be the same type
regardless of format and must include only properties defined in the logical
model.

### Element Sets

An ElementSet is a set of one or more Logical Values, and a serializer constructs
a Payload that represents those values and optionally an SpdxDocument Element
that describes the Payload.
A deserializer test reads the Payload and reconstructs the identical set of
Logical Values - if the Payload was constructed from two File elements,
deserializing it results in two File elements.

### SpdxDocument vs. Bundle

The serialization subgroup proposed developing a set of examples, including
Bundle, two Persons, and Bundle of two Persons.
This highlights the distinction between Elements and Payloads:
- two Person Elements is two logical values
- two Person Elements can be serialized into one Payload
- SpdxDocument is an Element that describes a Payload

The rationale for a Bundle type in the logical model has not been defined.
Every serialized value is a Payload.
* If Bundle is a physical byte sequence (Payload) then it is not a logical Element
* If Bundle is a logical Element then Bundle is a synonym (not an ancestor
or descendant) of SpdxDocument

The development of serialized Element examples will explore if a separate
Bundle type is needed, and decide whether to call the Element that refers
to serialized data "Bundle" or "SpdxDocument".