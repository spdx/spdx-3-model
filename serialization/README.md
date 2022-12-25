# SPDX v3 Serialization

The SPDX logical model defines meaning, relationships and shape of the SPDX element graph, but the same
information can be serialized into many different byte sequences.  A physical data model (concrete schema)
specifies logical element serialization using a specific data format, while an information model
(abstract schema) specifies logical element serialization using any data format,
allowing data in one format to be compared with and converted to other formats.

## Serialization Concepts

Information exists in the minds of users (producers and consumers), in applications running on the systems they use,
and in the data exchanged among systems. Serialization converts application information into byte sequences
(messages, payloads, information exchage packages) that can be communicated and stored. De-serialization
parses payloads back into application state. Serialization is not a goal in and of itself, it is the mechanism by
which applications exchange information in order to make it available to users.

Serialization should be:
1) **lossless**, so that information is not modified in transit and all applications have the identical information
2) **transparent**, so that information is unaffected by how or if it has been serialized; users should not know or care.

Shannon's information theory defines the relationship between information and serialization (coding).
Mathematicians characterize conditions applied to a mechanism as *necessary* and/or *sufficient*:
a serialization that omits necessary data loses information, one that uses more data than sufficient
conveys no extra information.
Thespian bartender and philosopher Ted Danson put it most succinctly: a necessary and sufficient serialization
mechanism includes "everything you need and nothing you don't."

![Information](images/interoperability.jpg)




The SPDX v3 model diagram includes some JSON examples, but they are used to illustrate and
develop the logical model, not specify how to construct and validate a byte sequence
to represent a set of logical values.
Figure 1 shows a JSON example from the logical model diagram as of 12/19/2022:

![Figure 1](images/diagram-sbom.jpg)

This example contains three elements in a nested structure: an SBOM (null-sbom), a Package
(spdx-tools-3.0.1), and a Person (iamwillbar). The first task is to determine the logical values of these
three elements. Note that "logical value" is an "interface" - an answer to the question
"what is the value of each property defined in the logical model", not a data structure. But the
answers to those questions are displayed as data, so the distinction between logical values and
physical data must be kept in mind.

Figure 2 shows the logical value of each of the elements from the example:

![Figure 2](images/elements.jpg)

The `person` element illustrates a problem with the logical model that can be resolved by adding
an `identifiedBy` property to the Identity type. For serialization purposes, assume that the
problem has been resolved in some manner.



![Figure 3](images/payload.jpg)

Figure 3 shows the same three elements serialized individually without nesting, along with an
SpdxDocument containing information about the serialized payload.
On the left is the expanded version of the payload with no space optimization, and on the right
is the same payload optimized using namespace-relative element IDs and creation property defaults.
The payload structure is simple, containing just a set of optimization-related properties and the
set of independent (non-nested) element values.

![Figure 4](images/sbom.jpg)

Figure 4 shows the example SBOM element (null-sbom), greatly simplified from the nested version.
It includes just the element IDs of the SBOM and a profile list that overrides the default.
Two IDs (Person "iamwillbar" and Package "spdx-tools-3.0.1") are actual elements included
in the payload, and the other two ("project" and "doc") are IDs assigned to external data
objects for which no elements exist.

![Figure 4](images/person.jpg)

Figure 4 shows the example Person element.

## References

[iepd](https://niem.github.io/reference/iepd/)

[danson](https://www.youtube.com/watch?v=BjeLEoc8Kjg)