# Change Log

## 3.1-dev (TBA)

The SPDX 3.1 model expands beyond software to include safety, hardware, supply chain,
operations, and more. This release candidate is for testing and validation;
it may contain changes that could be modified or reverted before the
final release.

### Changes since 3.0.1

The following list covers general updates and potential breaking changes.
Deprecations are listed in a separate section below.
For profile-specific additions,
please refer to the relevant profile documentation.

This release also significantly expands and modifies the vocabulary.
For instance, `/Core/RelationshipType` has grown from 59 to 76 entries,
and several element types were revised to allow for more flexible usage across
different profiles.

Items marked 'Changed', 'Removed' or 'Fixed' indicate potential
semantic changes to the model and may affect compatibility.

- **Changed:** Standardized RDF IRIs to use two-level versioning (major.minor)
  instead of three-level (major.minor.patch) -
  [#1046](https://github.com/spdx/spdx-3-model/issues/1046)
  - Previous: `https://spdx.org/rdf/x.y.z/terms/...`
  - New: `https://spdx.org/rdf/x.y/terms/...`
- **Changed:** Relax property and relationship requirements of `/AI/AIPackage`
  and `/Dataset/DatasetPackage` classes -
  [#1158](https://github.com/spdx/spdx-3-model/pull/1158)
- **Added:** `/Core/ElementMap` class and `/Core/elementValue`
  property - [#969](https://github.com/spdx/spdx-3-model/pull/969)
  - A class and a property used for implementing mapping a string key to
    an Element.
- **Added:** `/Core/inLanguage` property -
  [#1066](https://github.com/spdx/spdx-3-model/pull/1066),
  [#1124](https://github.com/spdx/spdx-3-model/pull/1124)
  - A human language used within the content of an Element or a property.
- **Added:** `/Core/intendedUse` property -
  [#1109](https://github.com/spdx/spdx-3-model/pull/1109/)
  - How or for what item or artifact is meant to be used for.
- **Added:** `/Core/isoAutomationLevel` property -
  [#1064](https://github.com/spdx/spdx-3-model/pull/1064)
  - A spectrum of system automation capability.
- **Added:** `/SimpleLicensing/customIdToLicense` property -
  [#969](https://github.com/spdx/spdx-3-model/pull/969)
  - Maps custom licensing string to the corresponding licensing Element.
- **Added:** `/Software/artifactSize` property -
  [#966](https://github.com/spdx/spdx-3-model/pull/966)
  - Size of a software artifact, in bytes.
- **Clarified:** Serialization and validation documents -
  [#1019](https://github.com/spdx/spdx-3-model/pull/1019)
  - Use "SPDX 3 JSON" name (instead of "SPDX 3 JSON-LD").
- Fixed typos, formatting issues, and broken examples; updated reference links.

### Deprecations since 3.0.1

- `/AI/autonomyType` property
  - New documents should use `/Core/isoAutomationLevel` instead.
- `/Build/buildStartTime` and `/Build/buildEndTime` properties
  - New documents should use `/Core/startTime` and `/Core/endTime` instead.
- `/Dataset/datasetSize` property
  - New documents should use `/Software/artifactSize` instead.
- `/Dataset/intendedUse` property
  - New documents should use `/Core/intendedUse` instead.
- `/SimpleLicensing/customIdToUri` property
  - New documents should use `/SimpleLicensing/customIdToLicense` instead.

### Release notes

Release notes for the 3.1-RC1 model, detailing all changes from 3.0.1
through 3.1-RC1, are available at:
<https://github.com/spdx/spdx-3-model/releases/tag/3.1-rc1>.

## 3.0.1 (2024-12-10)

### Changes since 3.0

Items marked 'Removed' or 'Fixed' indicate potential
semantic changes to the model and may affect compatibility.

- **Removed:** `Software/contentType` property - [#789](https://github.com/spdx/spdx-3-model/pull/789)
  - The `Software/File` class is meant to use the `Core/contentType` property.
- **Fixed:** Cardinalities in `Security/VexAffectedVulnAssessmentRelationship` class -
  [#908](https://github.com/spdx/spdx-3-model/pull/908)
  - Corrected `actionStatement` cardinality from `0..1` to `1..1` to match its textual description.
  - Corrected `actionStatementTime` cardinality from `0..*` to `0..1` to match its textual description.
- **Fixed:** Typo in `Core/import` property - [#847](https://github.com/spdx/spdx-3-model/pull/847)
  - Corrected `imports` to `import` in Core profile.
- **Fixed:** Typo in `Build/parameter` property - [#836](https://github.com/spdx/spdx-3-model/pull/836)
  - Corrected `parameters` to `parameter` in Build profile.
- **Fixed:** Typo in `hasInput` and `hasOutput` entries - [#854](https://github.com/spdx/spdx-3-model/pull/854)
  - Corrected `hasInputs` to `hasInput` and `hasOutputs` to `hasOutput` in
    `Core/RelationshipType`.
- **Fixed:** Typo in `hasPrerequisite` entry- [#817](https://github.com/spdx/spdx-3-model/pull/817)
  - Corrected the misspelling of `hasPrerequsite` to `hasPrerequisite` in
    `Core/RelationshipType`.
- **Fixed:** Licensing relationship type names in profile conformance - [#779](https://github.com/spdx/spdx-3-model/pull/779)
  - Corrected `concludedLicense` to `hasConcludedLicense` and
    `declaredLicense` to `hasDeclaredLicense` in profile conformance
    section of AI, Dataset, Licensing, and Lite profiles.
- **Fixed:** `Security/actionStatement` property - [#908](https://github.com/spdx/spdx-3-model/pull/908)
  - Corrected its cardinality from `0..1` to `1..1`.
- **Fixed:** `Security/actionStatementTime` property - [#908](https://github.com/spdx/spdx-3-model/pull/908)
  - Corrected its cardinality from `0..*` to `0..1`.
- **Added:** `adler32` entry to `Core/HashAlgorithm` - [#826](https://github.com/spdx/spdx-3-model/pull/826)
  - Reintroduced the Adler-32 checksum, previously available in SPDX 2.3.
- **Added:** `Core/SpdxOrganization` individual - [#880](https://github.com/spdx/spdx-3-model/pull/880)
  - An `SpdxOrganization` individual, a `Organization` representing the SPDX
    Project, is added. It is by definition the creator of all Element type individuals
    defined by the SPDX Project.
- **Added:** `Core/IndividualElement` class - [#937](https://github.com/spdx/spdx-3-model/pull/937)
  - A concrete subclass of Element used by Individuals in the Core profile.
- **Clarified:** `AI/autonomyType` property - [#741](https://github.com/spdx/spdx-3-model/pull/741)
  - Specified the meaning of `yes`, `no`, and `noAssertion` values in the
    `AI/autonomyType` property description.
- **Clarified:** `Build/buildType` property - [#875](https://github.com/spdx/spdx-3-model/pull/875)
  - Its intent is added: "The buildType is used to interpret the meaning of
    other build parameters by defining the 'type' of build...".
- **Clarified:** `hasDataFile` entry in `Core/RelationshipType` - [#815](https://github.com/spdx/spdx-3-model/pull/815)
  - Its description is enhanced with examples and counter-examples.
- **Clarified:** `Core/packageVerificationCodeExcludedFile` property - [#913](https://github.com/spdx/spdx-3-model/pull/913)
  - Its description is now stating that every filename is preceded with a `./`.
- **Improved:** JSON-LD examples.
  - All JSON-LD examples in the "Syntax" section of class descriptions are now
    validated - [#794](https://github.com/spdx/spdx-3-model/pull/794)
  - Added JSON-LD examples for `AI/EnergyConsumption` and
    `AI/EnergyConsumptionDescription` - [#780](https://github.com/spdx/spdx-3-model/pull/780)
- **Updated:** Model diagrams.
  - Used updated names and specified XSD datatypes - [#852](https://github.com/spdx/spdx-3-model/pull/852)
  - Removed all named individuals - [#884](https://github.com/spdx/spdx-3-model/pull/884)
  - Adjusted layout to also fit printed format and removed all vocabulary
    entries - [#935](https://github.com/spdx/spdx-3-model/pull/935)
  - Add `Core/IndividualElement` class
    to the Core diagram - [#941](https://github.com/spdx/spdx-3-model/pull/941)
- Fixed general typos and formatting issues.

### Release notes

The version 3.0.1 model release notes,
with full change records from 3.0 to 3.0.1, are available at:
<https://github.com/spdx/spdx-3-model/releases/tag/3.0.1>.

## 3.0 (2024-04-15)

For changes since the 3.0 release candidates, please visit:
<https://github.com/spdx/spdx-3-model/releases>.
