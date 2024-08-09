# Notes on serialization

## Serialization information

For information on what can be included in an SPDX serialization and how they
are structured, please refer to the
[Serialization information](https://github.com/spdx/spdx-spec/blob/development/v3.0.1/docs/serializations.md)
section of the SPDX specification.

## Serialization formats

The specification Markdown files describing rules for each serialization format
will contain an SpdxDocument section describing how each of the properties of
SpdxDocument are serialized for the given serialization format.

The specification and examples are numbered for easier referencing
-- the order is **not** significant.

Current supported formats are:

- [JSON-LD](jsonld.md)

## Use cases

Examples of how to serialize the following cases:

### Core and Software Profiles use cases

- `Agent`
- `Annotation`
- `Bundle`
  - `Bundle` of two `Person`s
- `File`
- `Package`
  - `Package` with `ExternalIdentifier`
  - `Package` with `ExternalRef`
- `Person`
  - `Person` with full `CreationInfo`
  - `Person` with no `CreationInfo`
  - `Person` with minimal `CreationInfo`
  - Two `Person`s
- `Relationship`
  - `Relationship` with `Package` contains two `File`s
  - `Relationship` with time properties
- `Sbom` with two `File`s
- `SpdxDocument`
  - `SpdxDocument` with `ExternalMap`
  - `SpdxDocument` with `NamespaceMap
  - `SpdxDocument` with two `File`s

### Licensing Profile use cases

- Single `Artifact` under one `ListedLicense`
- Single `Artifact` under one `CustomLicense`
- Single `Artifact` under license expression of `ListedLicense`s
- Single `Artifact` under license expression of `ListedLicense` and `CustomLicense`
- Two `Artifact`s under same license expression of `ListedLicense` and `CustomLicense`

### Security Profile use cases

The following list begins with base examples and sequentially adds expositional
elements and relationships step-by-step:

- An initial set of vulnerability elements
- Adding vulnerability elements with security external reference types
  including `securityFix`, `vulnerabilityDisclosureReport`,
  and `vulnerabilityExploitabilityAssessment`
- Adding `hasAssociatedVulnerability` relationship between a vulnerability
  element and a software profile element
- Adding multiple `hasAssessmentFor` relationships for vulnerability assessment
  relationships between vulnerability element and package element for VEX,
  CVSS, etc. to communicate, e.g.,
  - Changes to a vulnerability element’s status affecting a specific package
    element using VEX (Vulnerability Exploitability eXchange) (see the
    serialized examples listed in *Syntax* under each vulnerability assessment
    relationship class definition)
  - How a vulnerability element may be fixed for a particular software package
    element
  - Results of a vulnerability scan or audit
- Adding `foundBy`, `publishedBy`, `reportedBy` relationships between an agent
  element and a vulnerability element
