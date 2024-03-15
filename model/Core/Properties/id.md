SPDX-License-Identifier: Community-Spec-1.0

# id

## Summary

Identifies a serialized SPDX object to be referenced by other objects

## Description

The id uniquely identifies a serialized SPDX object with a given serialized
document. It may either be a fully qualifier URI (e.g.
`http://example.org/my-object`), or a blank node (e.g.  `_:myobject`), although
specific objects may place additional constraints on the what is allowed in the
identifier

## Metadata

- name: id
- Nature: IdProperty
- Range: xsd:string
