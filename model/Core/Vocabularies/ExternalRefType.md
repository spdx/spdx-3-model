SPDX-License-Identifier: Community-Spec-1.0

# ExternalRefType

## Summary

Specifies the type of an external reference.

## Description

ExternalRefType specifies the type of an external reference.

## Metadata

- name: ExternalRefType

## Entries

- altDownloadLocation: A reference to an alternative download location.
- altWebPage: A reference to an alternative web page.
- binaryArtifact: A reference to binary artifacts related to a package.
- bower: A reference to a Bower package. The package reference format, looks like `package#version`, is defined in the "install" section of [Bower API documentation](https://bower.io/docs/api/#install).
- buildMeta: A reference build metadata related to a published package.
- buildSystem: A reference build system used to create or publish the package.
- chat: A reference to the instant messaging system used by the maintainer for a package.
- certificationReport: A reference to a certification report for a package from an accredited/independent body.
- componentAnalysisReport: A reference to a Software Composition Analysis (SCA) report.
- cwe: [Common Weakness Enumeration](https://csrc.nist.gov/glossary/term/common_weakness_enumeration). A reference to a source of software flaw defined within the official [CWE List](https://cwe.mitre.org/data/) that conforms to the [CWE specification](https://cwe.mitre.org/).
- documentation: A reference to the documentation for a package.
- dynamicAnalysisReport: A reference to a dynamic analysis report for a package.
- eolNotice: A reference to the End Of Sale (EOS) and/or End Of Life (EOL) information related to a package.
- exportControlAssessment: A reference to a export control assessment for a package.
- funding: A reference to funding information related to a package.
- issueTracker: A reference to the issue tracker for a package.
- mailingList: A reference to the mailing list used by the maintainer for a package.
- mavenCentral: A reference to a Maven repository artifact. The package reference format, looks like `groupId:artifactId[:version]`, is defined in [Maven documentation](https://maven.apache.org/guides/mini/guide-naming-conventions.html).
- metrics: A reference to metrics related to package such as OpenSSF scorecards.
- npm: A reference to an npm package. The package reference format, looks like `package@version`, is defined in [npm Docs](https://docs.npmjs.com/cli/v10/configuring-npm/package-json).
- nuget: A reference to a NuGet package. The package reference format, looks like `package/version`, is defined in [NuGet documentation](https://docs.nuget.org).
- license: A reference to additional license information related to an artifact.
- other: Used when the type does not match any of the other options.
- privacyAssessment: A reference to a privacy assessment for a package.
- productMetadata: A reference to additional product metadata such as reference within organization's product catalog.
- purchaseOrder: A reference to a purchase order for a package.
- qualityAssessmentReport: A reference to a quality assessment for a package.
- releaseNotes: A reference to the release notes for a package.
- releaseHistory: A reference to a published list of releases for a package.
- riskAssessment: A reference to a risk assessment for a package.
- runtimeAnalysisReport: A reference to a runtime analysis report for a package.
- secureSoftwareAttestation: A reference to information assuring that the software is developed using security practices as defined by [NIST SP 800-218 Secure Software Development Framework (SSDF) Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) or [CISA Secure Software Development Attestation Form](https://www.cisa.gov/resources-tools/resources/secure-software-development-attestation-form).
- securityAdvisory: A reference to a published security advisory (where advisory as defined per [ISO 29147:2018](https://www.iso.org/standard/72311.html)) that may affect one or more elements, e.g., vendor advisories or specific NVD entries.
- securityAdversaryModel: A reference to the security adversary model for a package.
- securityFix: A reference to the patch or source code that fixes a vulnerability.
- securityOther: A reference to related security information of unspecified type.
- securityPenTestReport: A reference to a [penetration test](https://en.wikipedia.org/wiki/Penetration_test) report for a package.
- securityPolicy: A reference to instructions for reporting newly discovered security vulnerabilities for a package.
- securityThreatModel: A reference the [security threat model](https://en.wikipedia.org/wiki/Threat_model) for a package.
- socialMedia: A reference to a social media channel for a package.
- sourceArtifact: A reference to an artifact containing the sources for a package.
- staticAnalysisReport: A reference to a static analysis report for a package.
- support: A reference to the software support channel or other support information for a package.
- vcs: A reference to a version control system related to a software artifact.
- vulnerabilityDisclosureReport: A reference to a Vulnerability Disclosure Report (VDR) which provides the software supplier's analysis and findings describing the impact (or lack of impact) that reported vulnerabilities have on packages or products in the supplier's SBOM as defined in [NIST SP 800-161 Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/161/r1/final).
- vulnerabilityExploitabilityAssessment: A reference to a Vulnerability Exploitability eXchange (VEX) statement which provides information on whether a product is impacted by a specific vulnerability in an included package and, if affected, whether there are actions recommended to remediate. See also [NTIA VEX one-page summary](https://ntia.gov/files/ntia/publications/vex_one-page_summary.pdf).
