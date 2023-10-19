SPDX-License-Identifier: Community-Spec-1.0

# contentIdentifier

## Summary

Provides a place to record the canonical, unique, immutable identifier for each software artifact using the artifact's gitoid.

## Description

The contentIdentifier provides a canonical, unique, immutable artifact identifier for each software artifact. SPDX 3.0 describes software artifacts as Snippet, File, or Package Elements. The ContentIdentifier can be calculated for any software artifact and can be recorded for any of these SPDX 3.0 Elements using Omnibor, an attempt to standardize how software artifacts are identified independent of which programming language, version control system, build tool, package manager, or software distribution mechanism is in use.  

The contentIdentifier is defined as the [Git Object Identifier](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) (gitoid) of type `blob` of the software artifact. The use of a git-based version control system is not necessary to calculate a contentIdentifier for any software artifact.

The gitoid is expressed in the ContentIdentifier property by using the IANA [gitoid URI scheme](https://www.iana.org/assignments/uri-schemes/prov/gitoid).

```
Scheme syntax: gitoid":"<git object type>":"<hash algorithm>":"<hash value>
```

The OmniBOR ID for the OmniBOR Document associated with a software artifact should not be recorded in this field. Rather, OmniBOR IDs should be recorded in the SPDX Element's ExternalIdentifier property. See [https://omnibor.io](https://omnibor.io) for more details.

## Metadata

- name: contentIdentifier
- Nature: DataProperty
- Range: xsd:anyURI

