SPDX-License-Identifier: Community-Spec-1.0

# packageUrl

## Summary

Provides a place for the SPDX data creator to record the package URL string (in accordance with the [package URL spec](https://github.com/package-url/purl-spec/blob/master/PURL-SPECIFICATION.rst)) for a software Package.

## Description

A packageUrl (commonly pronounced and referred to as "purl") is an attempt to standardize package representations in order to reliably identify and locate software packages. A purl is a URL string which represents a package in a mostly universal and uniform way across programming languages, package managers, packaging conventions, tools, APIs and databases.

the purl URL string is defined by seven components:
```
scheme:type/namespace/name@version?qualifiers#subpath
```

The definition for each component can be found in the [purl specification](https://github.com/package-url/purl-spec/blob/master/PURL-SPECIFICATION.rst). Components are designed such that they form a hierarchy from the most significant on the left to the least significant components on the right. 

Parsing a purl string into its components works from left to right. Some extra type-specific normalizations are required. For more information, see [How to parse a purl string in its components](https://github.com/package-url/purl-spec/blob/master/PURL-SPECIFICATION.rst#how-to-parse-a-purl-string-in-its-components).


## Metadata

- name: packageUrl
- Nature: DataProperty
- Range: xsd:anyURI

