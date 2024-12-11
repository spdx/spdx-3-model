# Change Log

## 3.0.1 (2024-12-10)

### Changes since 3.0

- **Removed:** `Software/contentType` property - [#789](https://github.com/spdx/spdx-3-model/pull/789)
  - The `Software/File` class is meant to use the `Core/contentType` property.
- **Fixed:** Cardinalities in `Security/VexAffectedVulnAssessmentRelationship` class -
  [#908](https://github.com/spdx/spdx-3-model/pull/908)
  - Corrected `actionStatement` cardinality from `0..1` to `1..1` to match its textual description.
  - Corrected `actionStatementTime` cardinality from `0..*` to `0..1` to match its textual description.
- **Fixed:** Typo in `Core/import` property - [#847](https://github.com/spdx/spdx-3-model/pull/847)
  - Corrected `imports` to `import` in Core Profile.
- **Fixed:** Typo in `Build/parameter` property - [#836](https://github.com/spdx/spdx-3-model/pull/836)
  - Corrected `parameters` to `parameter` in Build Profile.
- **Fixed:** Typo in `hasInput` and `hasOutput` entries - [#854](https://github.com/spdx/spdx-3-model/pull/854)
  - Corrected `hasInputs` to `hasInput` and `hasOutputs` to `hasOutput` in
    `Core/RelationshipType`.
- **Fixed:** Typo in `hasPrerequisite` entry- [#817](https://github.com/spdx/spdx-3-model/pull/817)
  - Corrected the misspelling of `hasPrerequsite` to `hasPrerequisite` in
    `Core/RelationshipType`.
- **Fixed:** Licensing relationship type names in Profile conformance - [#779](https://github.com/spdx/spdx-3-model/pull/779)
  - Corrected `concludedLicense` to `hasConcludedLicense` and
    `declaredLicense` to `hasDeclaredLicense` in the "Profile conformance"
    section of AI, Dataset, Licensing, and Lite Profiles.
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

## 3.0 (2024-04-15)

For changes since the 3.0 release candidates, please visit:
<https://github.com/spdx/spdx-3-model/releases>.
