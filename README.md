# SPDX 3 model

The System Package Data Exchange® (SPDX®) is a standard format for
communicating information about components associated with systems.

Components can include software, AI/ML models, and data today.
More component types that make up modern systems are planned to be included in
subsequent releases.

The prior version of this format was focused on Software, is an ISO/IEC
standard ([ISO/IEC 5962:2021](https://www.iso.org/standard/81870.html)) and has
wide industry adoption as a standardized Software Bill of Materials (SBOM).
All use cases supported by the prior version are supported here as well.

This repository holds the model for the information captured in SPDX version 3
standard.

## Branches and Formats

The editable files are written in a constrained subset of Markdown and are
stored in the `main` branch.

These files are automatically processed by
[spec-parser](https://github.com/spdx/spec-parser/)
and the following are generated:

- [MkDocs](https://www.mkdocs.org/) input, which then generates the
  [specification](https://spdx.github.io/spdx-spec/v3.0/)
- [JSON-LD context](http://niem.github.io/json/reference/json-ld/context/)
  file: [spdx-context.jsonld](https://spdx.org/rdf/3.0.0/spdx-context.jsonld)
- Model [SHACL](https://en.wikipedia.org/wiki/SHACL) and
  [OWL](https://www.w3.org/OWL/) files:
  - [Turtle format](https://en.wikipedia.org/wiki/Turtle_(syntax)):
    [spdx-model.ttl](https://spdx.org/rdf/3.0.0/spdx-model.ttl)
  - [JSON-LD format](https://json-ld.org/):
    [model.jsonld](https://spdx.github.io/spdx-3-model/model.jsonld)

People who wish to read the current version of the information
should be viewing the generated files, while anyone wanting to edit
should be working on the former.

## Model

The SPDX model is described using profiles related to the software application.
The profiles are organized as sub-directories under the ‘model’ directory.

Note:

1. The ‘Licensing’ profile has three categories (sub-directories): ‘Licensing’,
  ‘SimpleLicensing’, and ‘ExpandedLicensing’.
2. The ‘extension’ namespace (sub-directory) provides for adding information
  about the software application which is not otherwise covered under the SPDX
  model.

### Profiles of the model

#### AI

The AI profile describes an AI component's capabilities for a specific system
(domain, model type, industry standards). It details its usage within the
application, limitations, training methods, data handling, explainability, and
energy consumption.

#### Build

The Build profile contains information about the build done for the software application.
Fields include build type URI (of toolchain, platform, or infrastructure), locally unique
build identifier assigned by the developer, entry point of creation of build, URI of the
build configuration source if any, digest of build configuration source if any, build
parameters, start time of the build, end time of the build, and the system’s environment
variables at the time of the build.

#### Core

The Core profile describes the foundational classes and properties that are used by all
profiles of the SPDX model.

#### Dataset

The Dataset profile describes a dataset's core aspects (type, size, collection
method), access method, preparation (preprocessing, noise handling), intended
use (e.g. hardware calibration, machine learning), and related considerations
(data quality and privacy).

#### Licensing

The Licensing profile describes the aspects of licensing for the software application under
three categories (sub-directories) - Licensing, SimpleLicensing, and ExpandedLicensing.

The Licensing category describes information about declared licenses and concluded (detected) licenses.
The SimpleLicensing category describes information about text-formatted licenses.
The ExpandedLicensing category describes information about parseable and machine-readable licenses.

#### Lite

The SPDX Lite profile defines a subset of the SPDX specification for use cases and
workflows in some industries.

#### Security

The Security profile contains information about vulnerabilities and their assessments
based on CVSS (versions 2, 3, and 4), EPSS, Exploit Catalog, SSVC, and VEX (affected,
not affected, under investigation, and fixed categories).

#### Software

The Software profile contains information about files, packages, SBOMs, snippets, and
artifacts of the software application.

## Contribute!

For information about how to contribute to a specific profile,
please see [Contributing.md](Contributing.md).

Feel free to join us and contribute!

The discussions are happening on the spdx-tech mailing list
and during our weekly meetings.

All the details are in: <https://spdx.dev/participate/tech/>
