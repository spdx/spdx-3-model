SPDX-License-Identifier: Community-Spec-1.0

# ExternalIdentifierType

## Summary

Specifies the type of an external identifier.

## Description

ExternalIdentifierType specifies the type of an external identifier.

## Metadata

- name: ExternalIdentifierType

## Entries

- cpe22: [Common Platform Enumeration Specification 2.2](https://cpe.mitre.org/files/cpe-specification_2.2.pdf)
- cpe23: [Common Platform Enumeration: Naming Specification Version 2.3](https://csrc.nist.gov/publications/detail/nistir/7695/final)
- cve: Common Vulnerabilities and Exposures identifiers, an identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the [CVE specification](https://csrc.nist.gov/glossary/term/cve_id).
- duns: [Data Universal Numbering System (D-U-N-S) Number](https://www.dnb.com/en-us/smb/duns.html) is a unique nine-digit identifier, issued by Dun & Bradstreet, that identifies a business entity, often on a location-specific basis.
- email: Email address, as defined in [RFC 3696](https://datatracker.ietf.org/doc/rfc3696/) Section 3.
- gitoid: [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg).
- gln: [Global Location Number (GLN)](https://www.gs1.org/standards/id-keys/gln) is a 13-digit number, assigned by GS1, that uniquely identifies a legal entity (e.g., a company or customer), a function within a legal entity, a physical location (e.g., a warehouse or a specific shelf in a store), or a digital location (e.g., an Electronic Data Interchange (EDI) gateway).
- glue: [GLobal Unique Enterprise (GLUE) Identifiers](https://datatracker.ietf.org/doc/draft-ietf-spice-glue-id/), as defined by the IETF Internet-Draft, is expressed as a GLUE URI, a Uniform Resource Identifier that standardizes the representation of existing organizational entity identifiers.
- gtin: [Global Trade Item Number (GTIN)](https://www.gs1.org/standards/id-keys/gtin) is a number, assigned by GS1, that uniquely identifies a trade item (product or service).
- hsCodes: The [Harmonized System (HS)](https://www.wcoomd.org/en/topics/nomenclature/overview/what-is-the-harmonized-system.aspx) of tariff nomenclature is an internationally standardized system of names and numbers, defined by the World Customs Organization, used to classify traded products.
- lei: The [Legal Entity Identifier (LEI)](https://www.gleif.org/en/organizational-identity/introducing-the-legal-entity-identifier-lei) is a 20-character, alpha-numeric code based on the [ISO 17442](https://www.iso.org/standard/78829.html) standard developed by the International Organization for Standardization.
- other: Used when the type does not match any of the other options.
- packageUrl: Package URL, as defined in the corresponding [Annex](../../../annexes/pkg-url-specification.md) of this specification.
- securityOther: Used when there is a security related identifier of unspecified type.
- swhid: SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.
- swid: Concise Software Identification (CoSWID) tag, as defined in [RFC 9393](https://datatracker.ietf.org/doc/rfc9393/) Section 2.3.
- urlScheme: [Uniform Resource Identifier (URI) Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). The scheme used in order to locate a resource.
