SPDX-License-Identifier: Community-Spec-1.0

# contentIdentifier

## Summary

Used by SPDX producers to record the artifact’s gitoid: a canonical, unique, immutable identifier that can be used for software integrity verification.

Used by SPDX consumers to verify the integrity of a software artifact they received.

## Description

### SPDX Producers
The contentIdentifier is a canonical, unique, immutable artifact identifier for each software artifact. The ContentIdentifier for any software artifact can be calculated and recorded in SPDX 3.0 Snippet, File, or Package Elements. For additional information, see [OmniBOR](https://omnibor.io): an attempt to standardize how software artifacts are identified independent of which programming language, version control system, build tool, package manager, or software distribution mechanism is in use.  

The contentIdentifier is defined as the [Git Object Identifier](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) (gitoid) of type `blob` of the software artifact. The use of a git-based version control system is not necessary to calculate a contentIdentifier for any software artifact.

The gitoid is expressed in the ContentIdentifier property by using the IANA [gitoid URI scheme](https://www.iana.org/assignments/uri-schemes/prov/gitoid).

```
Scheme syntax: gitoid":"<git object type>":"<hash algorithm>":"<hash value>
```

The OmniBOR ID for the OmniBOR Document associated with a software artifact must NOT be recorded in this field. Rather, OmniBOR IDs should be recorded in the SPDX Element's ExternalIdentifier property. See [https://omnibor.io](https://omnibor.io) for more details.

### SPDX Consumers
The integrity of software objects can be verified by calculating the gitoid(s) (`git hash-object foo`) of the object(s) and comparing the results to the value stored in the SPDX contentIdentifier field. ContentIdentifiers are canonical: Omnibor specifies a reproducible algorithm for anyone with the software object to perform this calculation. ContentIdentifiers are unique: the gitoid value is the result of a specific implementation of a one-way hash function. If the calculated gitoid value is the same as the gitoid value stored in SPDX, you can be sure it’s the same software. ContentIdentifiers are immutable: if a software object changes the resulting contentIdentifier will differ. These properties enable the verification of software integrity between producer and consumer using SPDX.



## Metadata

- name: contentIdentifier
- Nature: DataProperty
- Range: xsd:anyURI

