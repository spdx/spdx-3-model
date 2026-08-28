# Safety Relevance Assertion Profile examples

The following non-normative examples show how a Safety Relevance Assertion
Profile (SRAP) can be represented using SPDX Core, Security, and
FunctionalSafety elements, including ChangeTrigger and ChangeImpactAnalysis.

SRAP is a usage pattern. It does not require a dedicated SRAPAssessment class.
ChangeTrigger records the source, reason, event, report, or external record
that starts a safety-relevant review. A Core Relationship with relationshipType
investigatedBy links the ChangeTrigger to the ChangeImpactAnalysis that
investigates it.

ChangeImpactAnalysis records the documented change impact analysis. It can
identify the impact-analysis process, analysis status, impact level, approver,
and SPDX elements that are impacted, added, changed, or invalidated.
RequirementVerification, EvaluationResult, EvidenceRelationship, and Core
Bundle are then reused for downstream verification, outcome, evidence, and
exchange.

Some referenced elements in these examples are assumed to exist in the prior
model or in authoritative engineering systems and are not retransmitted in the
delta Bundle.

## Example 1: Requirement value change

This example shows a product-line requirement that is revised for one deployed
product context. The prior requirement is preserved, the revised requirement is
created as a new element, and amendedBy links the old requirement to the new
requirement. A ChangeTrigger records why the analysis started, and
ChangeImpactAnalysis records the impact of that trigger on the requirement,
validation, and evidence chain.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:bundle-srap-delta-1",
    "name": "SRAP change record for lab finding LAB-2026-014",
    "context": "Infusion pump X deployed configuration 3.2",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:change-impact-analysis-lab-2026-014"],
    "element": [
      "urn:spdx.dev:change-trigger-lab-2026-014",
      "urn:spdx.dev:rel-trigger-investigatedBy-analysis-lab",
      "urn:spdx.dev:change-impact-analysis-lab-2026-014",
      "urn:spdx.dev:procedure-change-impact-analysis",
      "urn:spdx.dev:agent-safety-board",
      "urn:spdx.dev:req-alarm-latency-40ms",
      "urn:spdx.dev:req-alarm-latency-30ms",
      "urn:spdx.dev:rel-req-alarm-amendedBy",
      "urn:spdx.dev:verification-lab-2026-014",
      "urn:spdx.dev:rel-req-alarm-verifiedBy",
      "urn:spdx.dev:evaluation-lab-2026-014",
      "urn:spdx.dev:evidence-rel-lab-2026-014"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:change-trigger-lab-2026-014",
    "name": "Lab finding LAB-2026-014",
    "externalIdentifier": [
      {
        "type": "ExternalIdentifier",
        "externalIdentifierType": "other",
        "identifier": "LAB-2026-014",
        "identifierLocator": ["https://qms.example.invalid/lab/LAB-2026-014"],
        "issuingAuthority": "Meridian Medical Systems QMS"
      }
    ],
    "rationale": "Bench testing found alarm latency needs to be tightened for this deployed configuration."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:rel-trigger-investigatedBy-analysis-lab",
    "relationshipType": "investigatedBy",
    "from": "urn:spdx.dev:change-trigger-lab-2026-014",
    "to": ["urn:spdx.dev:change-impact-analysis-lab-2026-014"]
  },
  {
    "type": "Specification",
    "spdxId": "urn:spdx.dev:procedure-change-impact-analysis",
    "name": "Safety change impact analysis procedure",
    "specType": "specification",
    "externalIdentifier": [
      {
        "type": "ExternalIdentifier",
        "externalIdentifierType": "other",
        "identifier": "SOP-SAFETY-CIA-001",
        "identifierLocator": ["https://qms.example.invalid/procedure/SOP-SAFETY-CIA-001"],
        "issuingAuthority": "Meridian Medical Systems QMS"
      }
    ]
  },
  {
    "type": "Agent",
    "spdxId": "urn:spdx.dev:agent-safety-board",
    "name": "Meridian Medical Systems Safety Review Board"
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:change-impact-analysis-lab-2026-014",
    "name": "Change impact analysis for LAB-2026-014",
    "impactAnalysisProcess": ["urn:spdx.dev:procedure-change-impact-analysis"],
    "impactAnalysisStatus": "complete",
    "impactLevel": "medium",
    "approvedBy": ["urn:spdx.dev:agent-safety-board"],
    "invalidatedElement": ["urn:spdx.dev:req-alarm-latency-40ms"],
    "addedElement": ["urn:spdx.dev:req-alarm-latency-30ms"],
    "impactedElement": [
      "urn:spdx.dev:verification-lab-2026-014",
      "urn:spdx.dev:fmea-occlusion-latency-2026"
    ],
    "rationale": "The prior 40 ms requirement is replaced by a 30 ms requirement and associated verification evidence must be refreshed."
  },
  {
    "type": "Requirement",
    "spdxId": "urn:spdx.dev:req-alarm-latency-40ms",
    "requirementUID": {
      "type": "ExternalIdentifier",
      "externalIdentifierType": "requirementUID",
      "identifier": "SR-40"
    },
    "requirementStatement": "The pump shall raise an occlusion alarm within 40 ms.",
    "requirementStatus": "active"
  },
  {
    "type": "Requirement",
    "spdxId": "urn:spdx.dev:req-alarm-latency-30ms",
    "requirementUID": {
      "type": "ExternalIdentifier",
      "externalIdentifierType": "requirementUID",
      "identifier": "SR-40-REV-A"
    },
    "requirementStatement": "The pump shall raise an occlusion alarm within 30 ms.",
    "requirementStatus": "reviewable",
    "rationale": ["LAB-2026-014 indicates the prior latency threshold is insufficient for this deployed context."]
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:rel-req-alarm-amendedBy",
    "relationshipType": "amendedBy",
    "from": "urn:spdx.dev:req-alarm-latency-40ms",
    "to": ["urn:spdx.dev:req-alarm-latency-30ms"]
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:verification-lab-2026-014",
    "verificationMethod": "assessment",
    "rationale": "Assess the revised alarm latency requirement and rerun the impacted validation."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:rel-req-alarm-verifiedBy",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-alarm-latency-30ms",
    "to": ["urn:spdx.dev:verification-lab-2026-014"]
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:evaluation-lab-2026-014",
    "evaluation": "inconclusive",
    "evaluationBasedOn": "urn:spdx.dev:verification-lab-2026-014",
    "rationale": "The 30 ms requirement has been identified, but the validation rerun has not completed.",
    "comment": "Further testing is required before the revised requirement can be evaluated as pass or fail."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:evidence-rel-lab-2026-014",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:evaluation-lab-2026-014",
    "to": ["urn:spdx.dev:fmea-occlusion-latency-2026"],
    "evidenceCategory": "report"
  }
]
```

## Example 2: CVE-triggered safety impact analysis

This example shows the two-layer pattern for a CVE. The Security profile
continues to carry the vulnerability and VEX status. FunctionalSafety adds the
safety context, ChangeTrigger, ChangeImpactAnalysis, and downstream safety
assessment outcome. The FuSa layer references the Security layer; it does not
duplicate the VEX assessment.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:bundle-srap-cve-delta",
    "name": "SRAP change record for CVE-2024-XXXX safety impact analysis",
    "context": "Infusion pump X deployed configuration 3.2",
    "profileConformance": ["core", "security", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:change-impact-analysis-cve-2024-xxxx"],
    "element": [
      "urn:spdx.dev:vuln-cve-2024-xxxx",
      "urn:spdx.dev:vex-under-investigation-openssl",
      "urn:spdx.dev:safety-context-openssl-sr12",
      "urn:spdx.dev:change-trigger-cve-2024-xxxx",
      "urn:spdx.dev:rel-trigger-investigatedBy-analysis-cve",
      "urn:spdx.dev:change-impact-analysis-cve-2024-xxxx",
      "urn:spdx.dev:procedure-change-impact-analysis",
      "urn:spdx.dev:verification-cve-2024-xxxx-safety",
      "urn:spdx.dev:rel-sr12-verifiedBy-cve",
      "urn:spdx.dev:evaluation-cve-2024-xxxx-safety",
      "urn:spdx.dev:evidence-rel-cve-2024-xxxx-safety"
    ]
  },
  {
    "type": "security_Vulnerability",
    "spdxId": "urn:spdx.dev:vuln-cve-2024-xxxx",
    "summary": "Hypothetical OpenSSL TLS handshake memory corruption",
    "externalIdentifier": [
      {
        "type": "ExternalIdentifier",
        "externalIdentifierType": "cve",
        "identifier": "CVE-2024-XXXX",
        "identifierLocator": ["https://www.cve.org/CVERecord?id=CVE-2024-XXXX"]
      }
    ]
  },
  {
    "type": "security_VexUnderInvestigationVulnAssessmentRelationship",
    "spdxId": "urn:spdx.dev:vex-under-investigation-openssl",
    "relationshipType": "underInvestigationFor",
    "from": "urn:spdx.dev:vuln-cve-2024-xxxx",
    "to": ["urn:spdx.dev:infusion-pump-x-v3.2"],
    "security_assessedElement": "pkg:generic/openssl@3.0.8",
    "suppliedBy": "urn:spdx.dev:agent-meridian-medical",
    "security_publishedTime": "2026-08-28T16:00:00Z"
  },
  {
    "type": "functionalSafety_SafetyContextRelationship",
    "spdxId": "urn:spdx.dev:safety-context-openssl-sr12",
    "relationshipType": "hasRequirement",
    "from": "pkg:generic/openssl@3.0.8",
    "to": ["urn:spdx.dev:req-sr12-therapy-command-transport"],
    "scope": "runtime",
    "safetyIntegrityLevel": "sil2"
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:change-trigger-cve-2024-xxxx",
    "name": "CVE-2024-XXXX safety review trigger",
    "externalIdentifier": [
      {
        "type": "ExternalIdentifier",
        "externalIdentifierType": "cve",
        "identifier": "CVE-2024-XXXX",
        "identifierLocator": ["https://www.cve.org/CVERecord?id=CVE-2024-XXXX"]
      }
    ],
    "externalRef": [
      {
        "type": "ExternalRef",
        "externalRefType": "securityAdvisory",
        "locator": ["https://www.cve.org/CVERecord?id=CVE-2024-XXXX"]
      }
    ],
    "rationale": "The vulnerable OpenSSL version appears in the deployed pump SBOM."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:rel-trigger-investigatedBy-analysis-cve",
    "relationshipType": "investigatedBy",
    "from": "urn:spdx.dev:change-trigger-cve-2024-xxxx",
    "to": ["urn:spdx.dev:change-impact-analysis-cve-2024-xxxx"]
  },
  {
    "type": "Specification",
    "spdxId": "urn:spdx.dev:procedure-change-impact-analysis",
    "name": "Safety change impact analysis procedure",
    "specType": "specification",
    "externalIdentifier": [
      {
        "type": "ExternalIdentifier",
        "externalIdentifierType": "other",
        "identifier": "SOP-SAFETY-CIA-001",
        "identifierLocator": ["https://qms.example.invalid/procedure/SOP-SAFETY-CIA-001"],
        "issuingAuthority": "Meridian Medical Systems QMS"
      }
    ]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:change-impact-analysis-cve-2024-xxxx",
    "name": "Change impact analysis for CVE-2024-XXXX",
    "impactAnalysisProcess": ["urn:spdx.dev:procedure-change-impact-analysis"],
    "impactAnalysisStatus": "draft",
    "impactLevel": "high",
    "impactedElement": [
      "pkg:generic/openssl@3.0.8",
      "urn:spdx.dev:req-sr12-therapy-command-transport"
    ],
    "changedElement": ["urn:spdx.dev:verification-cve-2024-xxxx-safety"],
    "rationale": "SafetyContextRelationship shows OpenSSL participates in the SIL-2 therapy command transport requirement at runtime."
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:verification-cve-2024-xxxx-safety",
    "verificationMethod": "assessment",
    "rationale": "Assess whether the OpenSSL CVE affects the SIL-2 therapy command transport requirement."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:rel-sr12-verifiedBy-cve",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-sr12-therapy-command-transport",
    "to": ["urn:spdx.dev:verification-cve-2024-xxxx-safety"]
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:evaluation-cve-2024-xxxx-safety",
    "evaluation": "inconclusive",
    "evaluationBasedOn": "urn:spdx.dev:verification-cve-2024-xxxx-safety",
    "rationale": "Runtime reachability of the vulnerable TLS handshake path is still being investigated.",
    "comment": "Further testing is required before determining whether the safety requirement is affected."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:evidence-rel-cve-2024-xxxx-safety",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:evaluation-cve-2024-xxxx-safety",
    "to": ["urn:spdx.dev:tls-reachability-analysis-2026-08-28"],
    "evidenceCategory": "report"
  }
]
```

If testing later confirms that the vulnerable path affects the safety function,
the EvaluationResult can be replaced or amended by a new EvaluationResult with
evaluation set to fail and linked evidence describing the analysis, test report,
or incident record that supports the conclusion. The original safety case does
not need to be rewritten; the change impact delta can travel as the SPDX graph
or as a linked Core Bundle.
