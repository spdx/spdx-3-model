# SPDX 3 model

The System Package Data Exchange® (SPDX®) is a standard format for communicating information about components associated with systems.

Components can include software, AI/ML models, and data today.  More component types that make up modern systems are planned to be included in subsequent releases.

The prior version of this format was focused on Software, is an ISO/IEC standard (ISO/IEC 5962:2021) and has wide industry adoption
as a standardized Software Bill of Materials (SBOM).   All use cases supported by the prior version, are supported here as well.

This repository holds the model for the information captured in SPDX version 3 standard.

## Branches and Formats

The editable files are written in a constrained subset of Markdown and are stored in the `main` branch.

These files are automatically processed by spec-parser and the following are generated::

- [MkDocs](https://www.mkdocs.org/) input, which then generates the [specification](https://spdx.github.io/spdx-spec/v3.0/)
- [JSON-LD context](http://niem.github.io/json/reference/json-ld/context/) file: [spdx-context.jsonld](https://spdx.org/rdf/3.0.0/spdx-context.jsonld)
- Model [SHACL](https://en.wikipedia.org/wiki/SHACL) and [OWL](https://www.w3.org/OWL/) files:
  - [Turtle format](https://en.wikipedia.org/wiki/Turtle_(syntax)): [spdx-model.ttl](https://spdx.org/rdf/3.0.0/spdx-model.ttl)
  - [JSON-LD format](https://json-ld.org/): [model.jsonld](https://spdx.github.io/spdx-3-model/model.jsonld)

People who wish to read the current version of the information
should be viewing the generated files, while anyone wanting to edit
should be working on the former.

## Model

The SPDX model is described using profiles related to the software application.
The profiles are organized as sub-directories under the ‘model’ directory.

Note:

1. The ‘Licensing’ profile has three categories (sub-directories): ‘Licensing’, ‘SimpleLicensing’, and ‘ExpandedLicensing’.
2. The ‘extension’ namespace (sub-directory) provides for adding information
   about the software application which is not otherwise covered under the SPDX model.

### Profiles of the model

#### AI

The AI profile describes the characteristics and capabilities of the AI component
of the software application. Fields include the domain of the application (banking,
telecom, …), type of AI model (neural networks, logistic regression, …), industry
standards compliance (ISO/IEC 42001, …), information about how the AI model is used
within the application, energy consumed by the AI model, limitations of the AI model
(dataset of a specific demography cannot be used by the model, …), how the model would
be trained, hyperparameters, how data would be preprocessed, whether the model can
explain its reasoning, whether sensitive personal information is used during the model
training, metrics used for measuring model performance, decision thresholds for those
metrics, autonomy type of the model (supervised, unsupervised, …), and safety risk
assessment information.

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

The Dataset profile describes the characteristics of the dataset(s) used by the AI system.
Fields include type of the dataset (image, text, relational DB, …), how the data is collected,
how the collected data would be used, size of the dataset, information about noise in the
fields of the dataset and/or noise that affects the entire dataset, information about
preprocessing before dataset is constructed, sensors used to collect data, known biases
in the data of the dataset, information about whether the dataset contains sensitive or
identifiable personal information, anonymization methods used to mask sensitive or identifiable
personal information, confidentiality levels of data points in the dataset as defined in the
Traffic Light Protocol, information about dataset update mechanism, and information about
availability aspects of the dataset (public, restricted, …).

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
All the details are in: https://spdx.dev/participate/tech/
