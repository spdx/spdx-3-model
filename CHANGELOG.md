# Change Log

## 3.0.1 (2024-09-26)

### Changes since 3.0

- **Removed:** `Software/contentType` property - [#789](https://github.com/spdx/spdx-3-model/pull/789)
  - The `Software/File` class is meant to use the `Core/contentType` property.
- **Fixed:** Typo in `hasPrerequisite` entry - [#817](https://github.com/spdx/spdx-3-model/pull/817)
  - Corrected the misspelling of `hasPrerequsite` to `hasPrerequisite` in
    `Core/RelationshipType`.
- **Fixed:** Licensing relationship type names - [#779](https://github.com/spdx/spdx-3-model/pull/779)
  - Corrected `concludedLicense` to `hasConcludedLicense` and
    `declaredLicense` to `hasDeclaredLicense` in the "Profile conformance"
    section of AI, Dataset, Licensing, and Lite Profiles.
- **Fixed:** Typo in `import` property - [#847](https://github.com/spdx/spdx-3-model/pull/847)
  - Corrected `imports` to `import` in Core Profile.
- **Fixed:** Typo in `Build/parameter` property - [#836](https://github.com/spdx/spdx-3-model/pull/836)
  - Corrected `parameters` to `parameter` in Build Profile.
- **Fixed:** Typo in `hasInput` and `hasOutput` relationship type names - [#854](https://github.com/spdx/spdx-3-model/pull/854)
  - Corrected `hasInputs` to `hasInput` and `hasOutputs` to `hasOutput` in
    `Core/RelationshipType`.
- **Added:** `adler32` entry to `Core/HashAlgorithm` - [#826](https://github.com/spdx/spdx-3-model/pull/826)
  - The Adler-32 checksum, previously available in SPDX 2.3, has been
    reintroduced.
- **Added:** `Core/SpdxOrganization` - [#880](https://github.com/spdx/spdx-3-model/pull/880)
  - An `SpdxOrganization` individual, an Organization representing the SPDX
    Project, is added. It is by definition the creator of all Element type individuals
    defined by the SPDX Project.
- **Clarified:** `AI/autonomyType` - [#741](https://github.com/spdx/spdx-3-model/pull/741)
  - Specified the meaning of `yes`, `no`, and `noAssertion` values in the
    `AI/autonomyType` property description.
- **Clarified:** `Build/buildType` - [#875](https://github.com/spdx/spdx-3-model/pull/875)
  - Its intent is added: "The buildType is used to interpret the meaning of
    other build parameters by defining the "type" of build...".
- **Clarified:** `hasDataFile` entry in `Core/RelationshipType` - [#815](https://github.com/spdx/spdx-3-model/pull/815)
- **Improved:** JSON-LD examples.
  - All JSON-LD examples in the "Syntax" section of class descriptions are now
    validated - [#794](https://github.com/spdx/spdx-3-model/pull/794)
  - Added JSON-LD examples for `AI/EnergyConsumption` and
    `AI/EnergyConsumptionDescription` - [#780](https://github.com/spdx/spdx-3-model/pull/780)
- **Updated:** Model diagrams.
  - Use updated names
  - Specify XSD data types
  - All named individuals are removed - [#884](https://github.com/spdx/spdx-3-model/pull/884)
- General typos and formatting fixes
