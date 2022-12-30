# SPDX v3 Serialization

The SPDX logical model defines meaning, relationships and shape of the SPDX element graph, but the same
information can be serialized into many different byte sequences.  A physical data model (concrete schema)
specifies logical element serialization using a specific data format, while an information model
(abstract schema) specifies logical element serialization using any data format.  Reading information
into applications from multiple formats allows instances to be compared; writing it to multiple formats
allows it to be converted between formats without loss.

### Serialization Concepts

Information exists in the minds of users (producers and consumers), in the state of applications running
on systems, and in the data exchanged among applications.
Serialization converts application information into byte sequences (a.k.a. protocol data units, messages,
payloads, information exchage packages) that can be validated, communicated and stored.
De-serialization parses payloads back into application state.
Serialization is not a goal in and of itself, it is the mechanism by which applications exchange information
in order to make it available to users.

Serialization should be:
1) **lossless**, so that information is not modified in transit and all applications have the identical information
2) **transparent**, so that information is unaffected by how or if it has been serialized; users should not know or care.

Shannon's information theory defines the relationship between information and serialization (coding).
Mathematicians characterize conditions applied to a mechanism as *necessary* and/or *sufficient*:
a serialization that omits necessary data loses information, one that uses more data than sufficient
conveys no extra information.
TV bartender/philosopher Ted Danson put it most succinctly: a necessary and sufficient serialization
mechanism has "everything you need and nothing you don't."

![Information](images/interoperability.jpg)

### SPDX v3 Information

The classes of a logical model are either referenceable or datatypes.
* A **datatype** class is known only by its value.
Two instances of the class are equivalent if and only if every property in the class is equal.
* A **referenceable** class has a unique identifier (primary key) and each instance is known by its id.
Two instances of the class are considered equivalent if and only if their ids are equal.
If only a single value can correspond to an id, the class is a *mapping* and colliding values
are treated as an error.

All classes in an information model are datatypes. Referenceable classes in a logical model are translated
to equivalent data structures where ids have no particular significance other than as values to be serialized.
They can be serialized as lists where each list item has an id, or as maps from ids to values.
Both serializations convey the same information but their byte sequences are different.

SPDX v3 organizes all of its information into a single referenceable "Element" class - every bit of logical
state in SPDX exists as instances of element subclasses (element itself is abstract), and each element exists
independently of all other elements. Figure 2 illustrates a set of elements from the information perspective:

![Element Timeline](images/elements-timeline.jpg)

1) Each element (black dot) has a unique id, type, and creation information. Serialization examples should show 
realistic unique ids; current examples do not.
2) Individual elements are ordered by creation date from oldest at the bottom to newest at the top.  One or more
elements can be created at the same time, shown in a horizontal row.  Position within a row does not signify anything.
3) Although elements are logically related by graph edges, at the information layer references are just property
values within each element.
4) Elements can exist in an application without ever being serialized. But to communicate between applications,
one or more elements are serialized into *payloads*, illustrated as the red horizontal bar at t=5. The payload is
not an element, it is just a sequence of bytes carrying an arbitrary set of elements, equivalent to the
identical elements carried in a zip file.
5) Serialization is causal; the payload created at t=5 cannot contain any elements created after it (t>5).
6) A payload may contain elements with the same creation time as the payload, and may also contain
previously-created elements such as the red element created at t=3 and two red elements created at t=1.
In the figure, the payload created at t=5 contains seven elements with three different timestamps.
7) Elements in a payload may have properties that are unique IDs of elements not carried in the payload,
such as the IDs of the green elements created at t=2 and t=4.

Although it is possible to define nested serialization structures, there are practical disadvantages to doing so:
1) nesting can be arbitrarily deep
2) if a nesting limit (e.g., max 1 level deep) is declared, the identical element has a different value
when serialized at level 1 than at level 2
3) if one element is nested within multiple other elements, multiple copies of the data are carried in the payload 
4) if elements are nested, they have different serialized values than when serialized individually
5) if elements are nested, rules for property inheritance must be defined, resulting in even more serialized
variants of the same element

For these reasons, it is both simpler and more efficient to serialize all elements in a payload independently,
without nesting or alternate representations.

### SPDX Serialization Examples

The SPDX v3 model diagram includes some JSON examples, but they are used to illustrate and
develop the logical model, not specify how to construct and validate a byte sequence
to represent a set of logical values. When serialization specifications are defined, examples will be
needed to illustrate and develop those specifications.

Figure 3 shows a JSON example from the diagram as of 12/19/2022:

![Figure 3](images/diagram-sbom.jpg)

This example contains three elements in a nested structure: an SBOM (null-sbom), a Package
(spdx-tools-3.0.1), and a Person (iamwillbar). The first task is to determine the logical values of these
three elements. Note that "logical value" is an "interface" - an answer to the question
"what is the value of each property defined in the logical model", not a data structure. But the
answers to those questions are displayed as data, so the distinction between logical values and
physical data must be kept in mind.

The logical values of these elements are:

**Package:**
```json
{
  "id": "urn:spdx.dev:spdx-tools-3.0.1",
  "type": {
    "package": {
      "packagePurpose": ["application"],
      "downloadLocation": "https://spdx.dev/downloads/spdx-tools-3.0.1.tgz",
      "homePage": "https://spdx.dev/tools.3.0",
      "originator": ["urn:spdx.dev:project"]
    }
  },
  "externalIdentifier": [
    {"type": "purl", "identifier": ""},
    {"type": "cpe_2.2", "identifier": ""}
  ],
  "verifiedUsing": [{"hash": {"sha256": "14a657a7118a333cc1fdc6af05071a59cda067fd11130d4ee5d6d47c26e7863f"}}],
  "creator": ["urn:spdx.dev:iamwillbar"],
  "created": "2022-05-02T20:28:00.000Z",
  "specVersion": "3.0",
  "profile": ["core", "software"],
  "dataLicense": "CC0-1.0"
}
```
**Person:**
```json
{
  "id": "urn:spdx.dev:iamwillbar",
  "type": {
    "person": {
      "identifiedBy": [
        {"email": "willbar@microsoft.com"},
        {"account": {"authority": "github.com", "localId": "iamwillbar"}}
      ]
    }
  },
  "name": "William Bartholomew",
  "creator": ["urn:spdx.dev:iamwillbar"],
  "created": "2022-05-02T20:28:00.000Z",
  "specVersion": "3.0",
  "profile": ["core"],
  "dataLicense": "CC0-1.0"
}
```
**Sbom:**
```json
{
  "id": "urn:spdx.dev:null-sbom",
  "type": {
    "sbom": {
      "element": [
        "urn:spdx.dev:iamwillbar",
        "urn:spdx.dev:spdx-tools-3.0.1",
        "urn:spdx.dev:project",
        "urn:spdx.dev:doc"
      ]
    }
  },
  "creator": ["urn:spdx.dev:iamwillbar"],
  "created": "2022-05-02T20:28:00.000Z",
  "specVersion": "3.0",
  "profile": ["core", "software"],
  "dataLicense": "CC0-1.0"
}
```
Note that every JSON structure has both leaf-path (RFC 6901) and hierarchical representions. The two represent
identical values and can be converted back and forth without any semantic knowledge.
For example, the path representation of the Sbom element is:

**Sbom (path):**
```json
{
  "id": "urn:spdx.dev:null-sbom",
  "type/sbom/element/0": "urn:spdx.dev:iamwillbar",
  "type/sbom/element/1": "urn:spdx.dev:spdx-tools-3.0.1",
  "type/sbom/element/2": "urn:spdx.dev:project",
  "type/sbom/element/3": "urn:spdx.dev:doc",
  "creator/0": "urn:spdx.dev:iamwillbar",
  "created": "2022-05-02T20:28:00.000Z",
  "specVersion": "3.0",
  "profile/0": "core",
  "profile/1": "software",
  "dataLicense": "CC0-1.0"
}
```
Because they represent identical logical values, choosing a represenation is a matter of taste and personal preference;
one or the other should be chosen for documentation purposes. The logical representation does not affect
the serialization format, although the same choices can be used the serialization spec.


The `person` element illustrates a problem with the logical model that can be resolved by adding
an `identifiedBy` property to the Identity type. For the purpose of illustrating serialization, assume that the
problem has been resolved in this manner.

**Payload:**

Figure 5 shows the same three elements serialized individually without nesting, along with an
SpdxDocument containing information about the serialized payload.
On the left is the expanded version of the payload with no space optimization, and on the right
is the same payload optimized using namespace-relative element IDs and creation property defaults.
The payload structure is simple, containing just a set of optimization-related properties and the
set of independent (non-nested) element values.

![Figure 5](images/payload.jpg)



![Figure 6](images/sbom.jpg)

Figure 4 shows the example SBOM element (null-sbom), greatly simplified from the nested version.
It includes just the element IDs of the SBOM and a profile list that overrides the default.
Two IDs (Person "iamwillbar" and Package "spdx-tools-3.0.1") are actual elements included
in the payload, and the other two ("project" and "doc") are IDs assigned to external data
objects for which no elements exist.

![Figure 6](images/person.jpg)

Figure 6 shows the example Person element.

## References

[iepd](https://niem.github.io/reference/iepd/)

[danson](https://www.youtube.com/watch?v=BjeLEoc8Kjg)