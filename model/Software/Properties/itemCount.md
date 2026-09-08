SPDX-License-Identifier: Community-Spec-1.0

# itemCount

## Summary

Number of discrete constituent items within a software artifact.

## Description

itemCount property records the total number of discrete constituent items
contained within a software artifact. These items may include, but are not
limited to, images, records, data samples, or files.

The count shall represent logical items regardless of physical representation.
Constituent items can be stored within a database, embedded in a container
format, or represented as encoded binaries within a single file.

The unit of count is not encoded within this property.
If the unit of count is not apparent from the context,
the unit shall be specified in the `description` property of the element.

## Metadata

- name: itemCount
- Nature: DataProperty
- Range: xsd:nonNegativeInteger
