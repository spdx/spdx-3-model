# Change Log

## 3.0.1 (under development - last update 2024-08-10)

### Changes since 3.0

- **Removed:** `Software/contentType` property.
  - The `Software/File` class is meant to use the `Core/contentType` property.
- **Fixed:** Typo in `hasPrerequisite` entry.
  - Corrected the misspelling of `hasPrerequsite` to `hasPrerequisite` in
    `Core/RelationshipType`.
- **Fixed:** Licensing relationship type names.
  - Corrected `concludedLicense` to `hasConcludedLicense` and
    `declaredLicense` to `hasDeclaredLicense` in the "Profile conformance"
    section of AI, Dataset, Licensing, and Lite Profiles.
- **Fixed:** Change `parameter` property - [#836](https://github.com/spdx/spdx-3-model/pull/836)
  - Corrected `parameters` to `parameter` in Build Profile. 
- **Added:** `adler32` entry to `Core/HashAlgorithm` - [#826](https://github.com/spdx/spdx-3-model/pull/826)
  - The Adler-32 checksum, previously available in SPDX 2.3, has been
    reintroduced.
- **Improved:** JSON-LD examples.
  - All JSON-LD examples in the "Syntax" section of class descriptions are now
    validated.
  - Added JSON-LD examples for `AI/EnergyConsumption` and
    `AI/EnergyConsumptionDescription`.
- **Clarified:** `AI/autonomyType` property.
  - Specified the meaning of `yes`, `no`, and `noAssertion` values in the
    `AI/autonomyType` property description.
