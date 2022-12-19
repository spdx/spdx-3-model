# SPDX v3 Serialization

![Figure 1](images/diagram-sbom.jpg)

Figure 1 shows a JSON example from the logical model diagram as of 12/19/2022, containing three elements
in a nested layout:an SBOM, a Package, and a Person.

![Figure 2](images/payload.jpg)

Figure 2 shows the same three elements serialized individually without nesting, along with an
SpdxDocument containing information about the serialized payload.
On the left is the expanded version of the payload with no space optimization, and on the right
is the same payload optimized using namespace-relative element IDs and creation property defaults.
The payload structure is simple, containing just a set of optimization-related properties and the
set of independent (non-nested) element values.

![Figure 3](images/sbom.jpg)

Figure 3 shows the example SBOM element (null-sbom), greatly simplified from the nested version.
It includes just the element IDs of the SBOM and a profile list that overrides the default.
Two IDs (Person "iamwillbar" and Package "spdx-tools-3.0.1") are actual elements included
in the payload, and the other two ("project" and "doc") are IDs assigned to external data
objects for which no elements exist.

![Figure 4](images/person.jpg)

Figure 4 shows the example Person element.