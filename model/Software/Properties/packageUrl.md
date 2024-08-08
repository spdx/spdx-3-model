SPDX-License-Identifier: Community-Spec-1.0

# packageUrl

## Summary

Provides a place for the SPDX data creator to record the package URL string
(in accordance with the Package URL specification) for a software Package.

## Description

A package URL (commonly pronounced and referred to as "purl") is an attempt to
standardize package representations in order to reliably identify and locate
software packages. A purl is a URL string which represents a package in a
mostly universal and uniform way across programming languages, package
managers, packaging conventions, tools, APIs and databases.

A purl is a URL composed of seven components:

```text
scheme:type/namespace/name@version?qualifiers#subpath
```

The definition for each component and known purl types can be found in the
[Package URL specification](../../../annexes/pkg-url-specification.md).
Known purl type definitions can be found in the
[Package URL type definitions](https://github.com/package-url/purl-spec/blob/b33dda1cf4515efa8eabbbe8e9b140950805f845/PURL-TYPES.rst).

Components are designed such that they form a hierarchy from the most
significant on the left to the least significant components on the right.

Parsing a purl string into its components works from left to right. Some extra
type-specific normalizations are required. For more information, see
[How to parse a purl string in its components](https://github.com/package-url/purl-spec/blob/b33dda1cf4515efa8eabbbe8e9b140950805f845/PURL-SPECIFICATION.rst#how-to-parse-a-purl-string-in-its-components).

## Metadata

- name: packageUrl
- Nature: DataProperty
- Range: xsd:anyURI
