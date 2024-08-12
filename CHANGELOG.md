# Change Log

## 3.0.1 (under development - last update 2024-08-10)

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
- **Added:** `adler32` entry to `Core/HashAlgorithm` - [#826](https://github.com/spdx/spdx-3-model/pull/826)
  - The Adler-32 checksum, previously available in SPDX 2.3, has been
    reintroduced.
- **Clarified:** `AI/autonomyType` property - [#741](https://github.com/spdx/spdx-3-model/pull/741)
  - Specified the meaning of `yes`, `no`, and `noAssertion` values in the
    `AI/autonomyType` property description.
- **Improved:** JSON-LD examples.
  - All JSON-LD examples in the "Syntax" section of class descriptions are now
    validated.
  - Added JSON-LD examples for `AI/EnergyConsumption` and
    `AI/EnergyConsumptionDescription`.
