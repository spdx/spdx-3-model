SPDX-License-Identifier: Community-Spec-1.0

# spdxId

## Summary

Identifies an Element to be referenced by other Elements.

## Description

An spdxId uniquely identifies an Element which may thereby be referenced by
other Elements.
These references may be internal or external.

While there may be several versions of the same Element,
each one needs to be able to be referred to uniquely
so that relationships between Elements can be clearly articulated.

Best practices for creating spdxIds for SPDX documents (and their Elements) on
the public internet are as follows:

SPDX document:

```text
https://[CreatorWebsite]/[pathToSpdx]/[DocumentName]-[UUID]
```

Element inside an SPDX document:

```text
https://[CreatorWebsite]/[pathToSpdx]/[DocumentName]-[UUID]#[ElementName]
```

where:

- `CreatorWebsite` is a website hosted by the creator of the document.
  (e.g. an SPDX document provided by the SPDX project would be `spdx.org`)
- `PathToSpdx` is a path to where SPDX documents are stored on the website.
- `DocumentName` is a name given to the SPDX document,
  typically the primary package name followed by its version.
- `UUID` is a universally unique identifier.
  The UUID could be a random UUID or a name-based version-5 UUID generated from
  an SHA-1 hash known to be unique for the specific SPDX document version.
- `ElementName` is a name given to the Element,
  typically the Element type followed by a sequence number.
- If the creator does not own their own website, a default `CreatorWebsite` and
  `PathToSpdx` can be used: `spdx.org/spdxdocs`. Note that the SPDX documents
  are not currently stored or accessible on this website.
  The URI is only used to create a unique ID following the above conventions.

The SPDX document spdxId shall not contain a URI "part"
(e.g. the `#` character), since it may be used in SPDX Element spdxIds
to separate the document namespace from the element’s SPDX identifier.

*Example*

```text
https://spdx.org/spdxdocs/spdx-tools-v2.0.4-a0b427e6-9427-414c-9acc-d6e7c3a0d205
```

The spdxId shall be unique for the SPDX document including the specific
version of the SPDX document. If the SPDX document is updated, thereby
creating a new version, a new spdxId for the updated document shall be used.
There can only be one spdxId for an SPDX document and only one SPDX document
for a given spdxId.

NOTE:
While an spdxId is a URI, it does not need to be accessible.
It is only intended to provide a unique ID.
Although an spdxId can point to an actual document on the web,
this is not always guaranteed.

## Metadata

- name: spdxId
- Nature: DataProperty
- Range: xsd:anyURI
