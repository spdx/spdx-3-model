# Lite serialization

## Summary

The SPDX Lite serialization specification defines a subset of the SPDX
specification, from the point of view of use cases in some industries.

SPDX Lite aims at the balance between the SPDX standard and actual workflows in
some industries.

## Supported SPDX fields

The SPDX Lite serialization supports a subset of the entire SPDX specification.
Any unsupported properties may result in a parsing error.

The following classes and fields are supported within the Lite profile:

- /Software/Package
  - /Core/Element/name
  - /Software/Package/packageVersion
  - /Software/Package/packageUrl
  - /Software/SoftwareArtifact/copyrightText
  
TODO: Add remaining classes

## Format

TBD: We could use the tag/value format or we could support other serializations
