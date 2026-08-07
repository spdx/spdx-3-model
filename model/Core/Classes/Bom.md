SPDX-License-Identifier: Community-Spec-1.0

# Bom

## Summary

A container for a grouping of SPDX 3 content characterizing details
(provenance, composition, licensing, etc.) about a product.

## Description

A Bill of Materials (BOM) is a container for a grouping of SPDX 3 content
characterizing details about a product.

This could include details of the content and composition of the product,
provenance details of the product and/or
its composition, licensing information, known quality or security issues, etc.

The `version` property is an optional human readable hint for different versions of a BOM
representing the same basic `Bundle` of elements provided by the same BOM
`creationInfo` `createdBy` `Agent` with a BOM of the same `name`.
To accurately represent changes or updates to a BOM, a `Relationship`
should be created from the updated BOM to the original BOM with the `amendedBy`
relationship type.
Since the `spdxId` must be unique for each version of a given SBOM, it can be considered
a unique version string if the version field is not used.

## Metadata

- name: Bom
- SubclassOf: Bundle
- Instantiability: Concrete

## Properties

- /Core/version
  - type: xsd:string
  - minCount: 0
  - maxCount: 1

## SPARQL

- name_when_version
  - message: A value for Core/name is required when a value for Core/version is present
  - query: <<<
        SELECT $this WHERE {
            $this <Software/version> ?version .
            FILTER NOT EXISTS {
                $this <Software/name> ?name .
            }
        }
