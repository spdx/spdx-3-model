# JSON Serialization

As noted by the [serialization team](https://github.com/spdx/meetings/blob/main/serialisation/Serialization%20Team%20Meeting%202023-07-20.md),
JSON serialization is targeted for easy adoption by the developer community:
* implied that they prefer JSON (based on prior discussions)
* also should be validated from a JSON schema all by itself (w/o a context file)
* easy to use as part of a library you incorporate into your code base
* how much extra code is needed to write beyond what's provided in standard tools,
e.g., how much logic is required for parsing, desire not much logic and custom parsing
required on top (may be unavoidable); don't want to introduce additional JSON complexities
in order to support JSON-LD.

Ignoring optimizations, every serialized SPDX document is a collection of Element instances.
In JSON this collection is equivalent to an array of element values
```
[
  Element1,
  Element2,
  ...,
  ElementN
]
```
where each Element has an individual **spdxId** and a **type** as defined by the logical model.
There are various methods for serializing individual Element values and optimizing document size,
which will be compared and selected based on the developer criteria, but every proposed method
must be equivalent to a collection of individual element values. This logical collection form
supports both translation to other serialization formats and validation using JSON Schema.

JSON objects are name:value pairs, and the choice of whether to serialize Element type as a
property name (e.g., "person", "package") or value type (e.g., "Person", "Package") will be
based on the developer criteria.
