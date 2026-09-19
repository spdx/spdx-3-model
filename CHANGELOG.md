---
SPDX-FileCopyrightText: 2023-present SPDX contributors
SPDX-FileType: DOCUMENTATION
SPDX-License-Identifier: Community-Spec-1.0
---

<!-- markdownlint-disable MD024 -->

# Change log

All notable changes to the SPDX 3 model will be documented in this file.

## 3.1-dev [Unreleased]

The next in a series of releases that will lead to
the general availability of SPDX 3.1 model.

The SPDX 3.1 model expands beyond software to include safety, hardware,
operations, supply chain, and more.
This release candidate is for testing and validation;
it may contain changes that could be modified or reverted before the
final release.

One of the major changes in this release candidate is the removal of
minor version from namespace IRIs ([#1277]).

### Added

- `doi`, `eli`, `isni`, and other intellectual property/regulatory identifiers
  to `/Core/ExternalIdentifierType` vocabulary ([#1187])
- `bom` entry to `/Core/ExternalRefType` vocabulary ([#1201])
- Guidelines for creating an spdxId for an SPDX document (informative)
  ([#1215])
- `/Core/rationale` property ([#1218])
- Role ([#1221])
- "symlink" entry to FileKindType vocabulary ([#1254])

### Changed

- Refined `/Core/DateTime` datatype pattern ([#1213], [#1245])
  - Replaced `\d` with `[0-9]` to ensure intended behavior and improve
    regex portability.
- Updated `/Core/startTime` and `/Core/endTime` descriptions ([#1217])
  - Expanded definitions to include support for actions and projects.
- Renamed `/Operations/assessmentTimestamp` to
  `/Operations/assessmentTime` ([#1219])
  - *Non-breaking change*, as this property was introduced in the 3.1-RC1
    and was never part of an official release.
- Renamed `/Core/SemVer` to `/Core/VersionNumber`;
  relaxed the patch version requirement ([#1234], [#1265], [#1283])
  - *Non-breaking change*, as the type is used only for internal versioning
    (`/Core/specVersion`, `/SimpleLicensing/licenseListVersion`)
    and is not referenced elsewhere in the model.
- Updated `/Core/DefinedProcess`, `/Hardware/Hardware`,
  `/Hardware/ProductSpecification`, and `/Software/Package` to use
  a generic `version` property (not a specific `xxxVersion`) ([#1265])
  - *Non-breaking change*, as `/Core/DefinedProcess` and Hardware classes
    were introduced in the 3.1-RC1 and was never part of an official
    release. For `/Software/Package`, the `/Software/packageVersion` is
    still available, but deprecated.
- Removed the minor version in namespace IRIs ([#1277])

### Deprecated

- `/Build/buildStartTime` and `/Build/buildEndTime` properties ([#1217])
  - New documents should use `/Core/startTime` and `/Core/endTime` instead.

### Removed

- Redundant start and end time properties:
  `/Core/actionStartTime`, `/Core/actionEndTime`,
  `/Operations/projectStartTime`, and `/Operations/projectEndTime` ([#1217])
  - *Non-breaking change*, as these properties were introduced in the 3.1-RC1
    and were never part of an official release.
  - Replaced with `/Core/startTime` and `/Core/endTime` properties.
- Redundant rationale properties:
  `/Core/processRationale`, `/Core/requirementRationale`,
  `/FunctionalSafety/evaluationRationale`, and
  `/FunctionalSafety/verificationRationale` ([#1218])
  - *Non-breaking change*, as these properties were introduced in the 3.1-RC1
    and were never part of an official release.
  - Replaced with `/Core/rationale` property.

### Fixed

- Fixed typos, formatting issues, and broken examples; updated reference links.

[#1187]: https://github.com/spdx/spdx-3-model/pull/1187
[#1201]: https://github.com/spdx/spdx-3-model/pull/1201
[#1213]: https://github.com/spdx/spdx-3-model/pull/1213
[#1215]: https://github.com/spdx/spdx-3-model/pull/1215
[#1217]: https://github.com/spdx/spdx-3-model/pull/1217
[#1218]: https://github.com/spdx/spdx-3-model/pull/1218
[#1219]: https://github.com/spdx/spdx-3-model/pull/1219
[#1221]: https://github.com/spdx/spdx-3-model/pull/1221
[#1234]: https://github.com/spdx/spdx-3-model/pull/1234
[#1245]: https://github.com/spdx/spdx-3-model/pull/1245
[#1254]: https://github.com/spdx/spdx-3-model/pull/1254
[#1265]: https://github.com/spdx/spdx-3-model/pull/1265
[#1277]: https://github.com/spdx/spdx-3-model/pull/1277
[#1283]: https://github.com/spdx/spdx-3-model/pull/1283

## [3.1-RC1] - 2026-01-24

The first in a series of releases that will lead to
the general availability of SPDX 3.1 model.

The SPDX 3.1 model expands beyond software to include safety, hardware,
operations, supply chain, and more.
This release candidate is for testing and validation;
it may contain changes that could be modified or reverted before the
final release.

This release also significantly expands and modifies the vocabulary.
For instance, `/Core/RelationshipType` has grown from 59 to 76 entries,
and several element types were revised to allow for more flexible usage across
different profiles.

### Added

- FunctionalSafety profile
- Hardware profile
- Operations profile
- Service profile
- SupplyChain profile
- `/Core/ElementMap` class and `/Core/elementValue` property ([#969][])
  - A class and a property used for implementing mapping a string key to
    an Element.
- `/Core/inLanguage` property ([#1066][], [#1124][])
  - A human language used within the content of an Element or a property.
- `/Core/intendedUse` property ([#1109][])
  - How or for what item or artifact is meant to be used for.
- `/Core/isoAutomationLevel` property ([#1064][])
  - A spectrum of system automation capability.
- `/SimpleLicensing/customIdToLicense` property ([#969][])
  - Maps custom licensing string to the corresponding licensing Element.
- `/Software/artifactSize` property ([#966][])
  - Size of a software artifact, in bytes.

### Changed

- Use "SPDX 3 JSON" name (instead of "SPDX 3 JSON-LD")
  for serialization format ([#1019][])
- Standardized RDF IRIs to use two-level versioning (major.minor)
  instead of three-level (major.minor.patch) ([#1046][])
  - Previous: `https://spdx.org/rdf/x.y.z/terms/...`
  - New: `https://spdx.org/rdf/x.y/terms/...`
- Relax property and relationship requirements of `/AI/AIPackage`
  and `/Dataset/DatasetPackage` classes ([#1158][])

### Deprecated

- `/AI/autonomyType` property
  - New documents should use `/Core/isoAutomationLevel` instead.
- `/Dataset/datasetSize` property
  - New documents should use `/Software/artifactSize` instead.
- `/Dataset/intendedUse` property
  - New documents should use `/Core/intendedUse` instead.
- `/SimpleLicensing/customIdToUri` property
  - New documents should use `/SimpleLicensing/customIdToLicense` instead.

### Fixed

- Fixed typos, formatting issues, and broken examples; updated reference links.

[#966]: https://github.com/spdx/spdx-3-model/pull/966
[#969]: https://github.com/spdx/spdx-3-model/pull/969
[#1019]: https://github.com/spdx/spdx-3-model/pull/1019
[#1046]: https://github.com/spdx/spdx-3-model/issues/1046
[#1064]: https://github.com/spdx/spdx-3-model/pull/1064
[#1066]: https://github.com/spdx/spdx-3-model/pull/1066
[#1109]: https://github.com/spdx/spdx-3-model/pull/1109
[#1124]: https://github.com/spdx/spdx-3-model/pull/1124
[#1158]: https://github.com/spdx/spdx-3-model/pull/1158

## [3.0.1] - 2024-12-12

Patch release for the SPDX 3.0 model.

Key changes:

- Corrected naming conventions:
  Updated specific classes and properties to align with the original design
  intent. These are classified as non-breaking corrections to resolve
  inconsistencies in the 3.0.0 specification.
- Restored missing entities:
  Added classes and vocabulary entries that were intended for the initial
  model but omitted in error.

### Added

- `adler32` entry to `/Core/HashAlgorithm` vocabulary ([#826][])
  - Reintroduced the Adler-32 checksum, previously available in SPDX 2.3.
- `/Core/SpdxOrganization` individual ([#880][])
  - An `SpdxOrganization` individual, a `Organization` representing the SPDX
    Project, is added. It is by definition the creator of all Element type
    individuals defined by the SPDX Project.
- `/Core/IndividualElement` class ([#937][])
  - A concrete subclass of Element used by Individuals in the Core profile.

### Changed

- Clarified `/AI/autonomyType` property ([#741][])
  - Specified the meaning of `yes`, `no`, and `noAssertion` values in the
    `/AI/autonomyType` property description.
- Clarified `/Build/buildType` property ([#875][])
  - Its intent is added: "The buildType is used to interpret the meaning of
    other build parameters by defining the 'type' of build...".
- Clarified `hasDataFile` entry in `/Core/RelationshipType` ([#815][])
  - Its description is enhanced with examples and counter-examples.
- Clarified `/Core/packageVerificationCodeExcludedFile` property ([#913][])
  - Its description is now stating that every filename is preceded with a `./`.
- Improved JSON-LD examples.
  - All JSON-LD examples in the "Syntax" section of class descriptions are now
    validated ([#794][])
  - Added JSON-LD examples for `/AI/EnergyConsumption` and
    `/AI/EnergyConsumptionDescription` ([#780][])
- Updated model diagrams.
  - Used updated names and specified XSD datatypes ([#852][])
  - Removed all named individuals ([#884][])
  - Adjusted layout to also fit printed format and removed all vocabulary
    entries ([#935][])
  - Add `/Core/IndividualElement` class to the Core diagram ([#941][])

### Removed

- `/Software/contentType` property ([#789][])
  - The `/Core/contentType` property in intended for `/Software/File`.

### Fixed

- Cardinalities in `/Security/VexAffectedVulnAssessmentRelationship` class
  ([#908][])
  - Corrected `actionStatement` cardinality from `0..1` to `1..1`
    to match its textual description.
  - Corrected `actionStatementTime` cardinality from `0..*` to `0..1`
    to match its textual description.
- Typo in `Core/import` property ([#847][])
  - Corrected `imports` to `import` in Core profile.
- Typo in `/Build/parameter` property ([#836][])
  - Corrected `parameters` to `parameter` in Build profile.
- Typo in `hasInput` and `hasOutput` entries ([#854][])
  - Corrected `hasInputs` to `hasInput` and `hasOutputs` to `hasOutput` in
    `/Core/RelationshipType`.
- Typo in `hasPrerequisite` entry ([#817][])
  - Corrected the misspelling of `hasPrerequsite` to `hasPrerequisite` in
    `/Core/RelationshipType`.
- Licensing relationship type names in profile conformance ([#779][])
  - Corrected `concludedLicense` to `hasConcludedLicense` and
    `declaredLicense` to `hasDeclaredLicense` in profile conformance
    section of AI, Dataset, Licensing, and Lite profiles.
- `/Security/actionStatement` property ([#908][])
  - Corrected its cardinality from `0..1` to `1..1`.
- `/Security/actionStatementTime` property ([#908][])
  - Corrected its cardinality from `0..*` to `0..1`.
- Fixed general typos and formatting issues.

[#741]: https://github.com/spdx/spdx-3-model/pull/741
[#779]: https://github.com/spdx/spdx-3-model/pull/779
[#780]: https://github.com/spdx/spdx-3-model/pull/780
[#789]: https://github.com/spdx/spdx-3-model/pull/789
[#794]: https://github.com/spdx/spdx-3-model/pull/794
[#815]: https://github.com/spdx/spdx-3-model/pull/815
[#817]: https://github.com/spdx/spdx-3-model/pull/817
[#826]: https://github.com/spdx/spdx-3-model/pull/826
[#836]: https://github.com/spdx/spdx-3-model/pull/836
[#847]: https://github.com/spdx/spdx-3-model/pull/847
[#852]: https://github.com/spdx/spdx-3-model/pull/852
[#854]: https://github.com/spdx/spdx-3-model/pull/854
[#884]: https://github.com/spdx/spdx-3-model/pull/884
[#875]: https://github.com/spdx/spdx-3-model/pull/875
[#880]: https://github.com/spdx/spdx-3-model/pull/880
[#908]: https://github.com/spdx/spdx-3-model/pull/908
[#913]: https://github.com/spdx/spdx-3-model/pull/913
[#935]: https://github.com/spdx/spdx-3-model/pull/935
[#937]: https://github.com/spdx/spdx-3-model/pull/937
[#941]: https://github.com/spdx/spdx-3-model/pull/941

## [3.0] - 2024-04-15

First release of SPDX 3.0 model.

Also referred to as version 3.0.0.

## [3.0-rc2] - 2024-02-17

The second in a series of releases that will lead to
the general availability of SPDX 3.0 model.

## [3.0-rc1] - 2023-05-07

The first in a series of releases that will lead to
the general availability of SPDX 3.0 model.

[3.1-rc1]: https://github.com/spdx/spdx-3-model/releases/tag/3.1-rc1
[3.0.1]: https://github.com/spdx/spdx-3-model/releases/tag/3.0.1
[3.0]: https://github.com/spdx/spdx-3-model/releases/tag/3.0
[3.0-rc2]: https://github.com/spdx/spdx-3-model/releases/tag/3.0-rc2
[3.0-rc1]: https://github.com/spdx/spdx-3-model/releases/tag/3.0-rc1

---

The format of this changelog is based on [Keep a Changelog][keepachangelog].

[keepachangelog]: https://keepachangelog.com/
