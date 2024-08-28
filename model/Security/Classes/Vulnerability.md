SPDX-License-Identifier: Community-Spec-1.0

# Vulnerability

## Summary

Specifies a vulnerability and its associated information.

## Description

Specifies a vulnerability and its associated information.

*Example*

```json
{
  "type": "Vulnerability",
  "spdxId": "urn:spdx.dev:vuln-1",
  "summary": "Use of a Broken or Risky Cryptographic Algorithm",
  "description": "The package `elliptic` before version 6.5.4 are vulnerable to ..."
  "modifiedTime": "2021-03-08T16:06:43Z",
  "publishedTime": "2021-03-08T16:02:50Z",
  "externalIdentifier": [
    {
      "type": "ExternalIdentifier",
      "externalIdentifierType": "cve",
      "identifier": "CVE-2020-2849",
      "identifierLocator": [
        "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28498",
        "https://www.cve.org/CVERecord?id=CVE-2020-28498"
      ],
      "issuingAuthority": "urn:spdx.dev:agent-cve.org"
    },
    {
      "type": "ExternalIdentifier",
      "externalIdentifierType": "securityOther",
      "identifier": "GHSA-r9p9-mrjm-926w",
      "identifierLocator": "https://github.com/advisories/GHSA-r9p9-mrjm-926w"
    },
    {
      "type": "ExternalIdentifier",
      "externalIdentifierType": "securityOther",
      "identifier": "SNYK-JS-ELLIPTIC-1064899",
      "identifierLocator": "https://security.snyk.io/vuln/SNYK-JS-ELLIPTIC-1064899"
    }
  ],
  "externalRef": [
    {
      "type": "ExternalRef",
      "externalRefType": "securityAdvisory",
      "locator": "https://nvd.nist.gov/vuln/detail/CVE-2020-28498"
    },
    {
      "type": "ExternalRef",
      "externalRefType": "securityAdvisory",
      "locator": "https://ubuntu.com/security/CVE-2020-28498"
    },
    {
      "type": "ExternalRef",
      "externalRefType": "securityOther",
      "locator": "https://github.com/indutny/elliptic/pull/244/commits"
    },
    {
      "type": "ExternalRef",
      "externalRefType": "securityOther",
      "locator": "https://github.com/christianlundkvist/blog/2020_05_26_secp256k1_twist_attacks.md"
    }
  ]
},
{
  "type": "Relationship",
  "spdxId": "urn:spdx.dev:vulnRelationship-1",
  "relationshipType": "hasAssociatedVulnerability",
  "from": "urn:npm-elliptic-6.5.2",
  "to": ["urn:spdx.dev:vuln-1"],
  "startTime": "2021-03-08T16:06:50Z"
},
{
  "type": "Relationship",
  "spdxId": "urn:spdx.dev:vulnAgentRel-1",  
  "relationshipType": "publishedBy",  
  "from": "urn:spdx.dev:vuln-1",
  "to": ["urn:spdx.dev:agent-snyk"],
  "startTime": "2021-03-08T16:06:50Z"
}
```

## Metadata

- name: Vulnerability
- SubclassOf: /Core/Artifact
- Instantiability: Concrete

## Properties

- publishedTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- modifiedTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
- withdrawnTime
  - type: /Core/DateTime
  - minCount: 0
  - maxCount: 1
