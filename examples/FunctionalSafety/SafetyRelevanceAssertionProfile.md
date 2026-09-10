# Safety Relevance Assertion Profile examples

The following non-normative examples show how a Safety Relevance Assertion
Profile (SRAP) can be represented using SPDX Core, Security, and
FunctionalSafety elements.

SRAP is a usage pattern. It does not require a dedicated SRAPAssessment class.
Each example uses the same graph shape:

- a Core Bundle carries the delta or change record;
- ChangeTrigger records the source, reason, event, report, or external record
  that initiates the safety-relevant review;
- a Core Relationship links the ChangeImpactAnalysis to the ChangeTrigger. The
  examples use relationshipType other as a placeholder until the trigger-analysis
  relationship term is finalized;
- ChangeImpactAnalysis records the impact-analysis status, impact level,
  approval, and the SPDX elements that are impacted, added, or removed from the
  analyzed safety context;
- RequirementVerification, EvaluationResult, and EvidenceRelationship are reused
  when downstream verification, result, and evidence need to be communicated.

When the work is still waiting on evidence, a decision, or a test rerun, use
impactAnalysisStatus with a draft value on ChangeImpactAnalysis. Do not use
EvaluationResult with an inconclusive value to mean "not started". Use an
inconclusive EvaluationResult only when an evaluation was performed but cannot
be clearly classified as pass or fail, and include a comment or rationale.

SPDX elements are not edited in place. If a requirement, validation, test,
design artifact, or other work product changes, create a new SPDX element and
link the old element to the new element with a relationship such as amendedBy
when that relationship is appropriate. The prior model can remain referenced
instead of being retransmitted.

The examples below omit some organization-specific records, such as detailed
QMS workflow data, when those records remain authoritative outside SPDX.

## Example 1: Product-line requirement value change

A product-line safety requirement is tightened for a deployed product context.
The previous requirement remains historically valid, the revised requirement is
created as a new element, and the delta Bundle communicates the trigger, impact
analysis, requirement revision, verification result, and evidence.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex1-bundle",
    "name": "SRAP change record for vehicle dynamics data VD-2026-040",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex1-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:srap-ex1-change-trigger",
      "urn:spdx.dev:srap-ex1-trigger-analysis-link",
      "urn:spdx.dev:srap-ex1-change-impact-analysis",
      "urn:spdx.dev:req-brake-response-40ms",
      "urn:spdx.dev:req-brake-response-30ms",
      "urn:spdx.dev:srap-ex1-amended-by",
      "urn:spdx.dev:srap-ex1-verification",
      "urn:spdx.dev:srap-ex1-verified-by",
      "urn:spdx.dev:srap-ex1-evaluation",
      "urn:spdx.dev:srap-ex1-evidence"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:srap-ex1-change-trigger",
    "name": "Vehicle dynamics data VD-2026-040",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "VD-2026-040",
      "identifierLocator": ["https://qms.example.invalid/vehicle-dynamics/VD-2026-040"],
      "issuingAuthority": "Example Mobility Safety Engineering"
    }],
    "rationale": "New vehicle dynamics data shows the previous braking response threshold is no longer sufficient for this product context."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex1-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex1-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex1-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex1-change-impact-analysis",
    "name": "Change impact analysis for VD-2026-040",
    "impactAnalysisProcess": ["urn:spdx.dev:sop-change-impact-analysis"],
    "impactAnalysisStatus": "approved",
    "impactLevel": "medium",
    "approvedBy": ["urn:spdx.dev:agent-safety-review-board"],
    "impactedElement": ["urn:spdx.dev:test-brake-response-t001"],
    "removedElement": ["urn:spdx.dev:req-brake-response-40ms"],
    "addedElement": ["urn:spdx.dev:req-brake-response-30ms"],
    "rationale": "The active product context changes from a 40 ms requirement to a 30 ms requirement and requires revalidation."
  },
  {
    "type": "Requirement",
    "spdxId": "urn:spdx.dev:req-brake-response-40ms",
    "requirementUID": {"type": "ExternalIdentifier", "externalIdentifierType": "requirementUID", "identifier": "SR-BRAKE-040"},
    "requirementStatement": "The braking command response shall complete within 40 ms.",
    "requirementStatus": "active"
  },
  {
    "type": "Requirement",
    "spdxId": "urn:spdx.dev:req-brake-response-30ms",
    "requirementUID": {"type": "ExternalIdentifier", "externalIdentifierType": "requirementUID", "identifier": "SR-BRAKE-030"},
    "requirementStatement": "The braking command response shall complete within 30 ms.",
    "requirementStatus": "reviewable"
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex1-amended-by",
    "relationshipType": "amendedBy",
    "from": "urn:spdx.dev:req-brake-response-40ms",
    "to": ["urn:spdx.dev:req-brake-response-30ms"]
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex1-verification",
    "verificationMethod": "assessment",
    "rationale": "Assess the previous threshold against the new product-line dynamics data."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex1-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-brake-response-40ms",
    "to": ["urn:spdx.dev:srap-ex1-verification"]
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex1-evaluation",
    "evaluation": "fail",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex1-verification",
    "rationale": "The 40 ms requirement is not met for the analyzed product context."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex1-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex1-evaluation",
    "to": ["urn:spdx.dev:vehicle-dynamics-report-VD-2026-040"],
    "evidenceCategory": "report"
  }
]
```

## Example 2: CVE in a safety-relevant component

The Security profile carries the vulnerability and VEX status. FunctionalSafety
adds the safety context and the SRAP change impact analysis so the same CVE can
be evaluated for safety relevance without duplicating the Security/VEX layer.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex2-bundle",
    "name": "SRAP change record for CVE-2024-9999",
    "profileConformance": ["core", "security", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex2-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:vuln-cve-2024-9999",
      "urn:spdx.dev:vex-under-investigation-cve-2024-9999",
      "urn:spdx.dev:safety-context-openssl-sr12",
      "urn:spdx.dev:srap-ex2-change-trigger",
      "urn:spdx.dev:srap-ex2-trigger-analysis-link",
      "urn:spdx.dev:srap-ex2-change-impact-analysis",
      "urn:spdx.dev:srap-ex2-verification",
      "urn:spdx.dev:srap-ex2-verified-by",
      "urn:spdx.dev:srap-ex2-evaluation",
      "urn:spdx.dev:srap-ex2-evidence"
    ]
  },
  {
    "type": "security_Vulnerability",
    "spdxId": "urn:spdx.dev:vuln-cve-2024-9999",
    "summary": "Hypothetical TLS memory corruption in OpenSSL",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "cve",
      "identifier": "CVE-2024-9999",
      "identifierLocator": ["https://www.cve.org/CVERecord?id=CVE-2024-9999"]
    }]
  },
  {
    "type": "security_VexUnderInvestigationVulnAssessmentRelationship",
    "spdxId": "urn:spdx.dev:vex-under-investigation-cve-2024-9999",
    "relationshipType": "underInvestigationFor",
    "from": "urn:spdx.dev:vuln-cve-2024-9999",
    "to": ["urn:spdx.dev:infusion-pump-x-v3.2"],
    "security_assessedElement": "pkg:generic/openssl@3.0.8",
    "suppliedBy": "urn:spdx.dev:agent-device-manufacturer"
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
    "spdxId": "urn:spdx.dev:srap-ex2-change-trigger",
    "name": "CVE-2024-9999 safety relevance review",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "cve",
      "identifier": "CVE-2024-9999",
      "identifierLocator": ["https://www.cve.org/CVERecord?id=CVE-2024-9999"]
    }],
    "rationale": "The vulnerable component appears in a runtime path mapped to a SIL-2 therapy command requirement."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex2-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex2-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex2-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex2-change-impact-analysis",
    "name": "Change impact analysis for CVE-2024-9999",
    "impactAnalysisProcess": ["urn:spdx.dev:sop-change-impact-analysis"],
    "impactAnalysisStatus": "draft",
    "impactLevel": "high",
    "impactedElement": [
      "pkg:generic/openssl@3.0.8",
      "urn:spdx.dev:req-sr12-therapy-command-transport",
      "urn:spdx.dev:safety-context-openssl-sr12"
    ],
    "addedElement": ["urn:spdx.dev:srap-ex2-verification"],
    "rationale": "SafetyContextRelationship shows the vulnerable component is safety relevant at runtime."
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex2-verification",
    "verificationMethod": "assessment",
    "rationale": "Assess whether the CVE affects the SIL-2 therapy command transport requirement."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex2-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-sr12-therapy-command-transport",
    "to": ["urn:spdx.dev:srap-ex2-verification"]
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex2-evaluation",
    "evaluation": "inconclusive",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex2-verification",
    "rationale": "The reachability analysis was performed, but exploitability of the affected TLS path in the safety function cannot yet be classified as pass or fail.",
    "comment": "Additional runtime tracing is needed before the safety impact conclusion is final."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex2-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex2-evaluation",
    "to": ["urn:spdx.dev:tls-reachability-report-2026-09"],
    "evidenceCategory": "report"
  }
]
```

## Example 3: Field incident after deployment

A deployed device reports a safety-relevant incident. SRAP communicates the
incident reference, the analysis that decides which safety artifacts are
affected, and the resulting design or validation updates.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex3-bundle",
    "name": "SRAP change record for field incident INC-2026-0821",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex3-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:srap-ex3-change-trigger",
      "urn:spdx.dev:srap-ex3-trigger-analysis-link",
      "urn:spdx.dev:srap-ex3-change-impact-analysis",
      "urn:spdx.dev:req-dose-confirmation-v1",
      "urn:spdx.dev:req-dose-confirmation-v2",
      "urn:spdx.dev:srap-ex3-amended-by",
      "urn:spdx.dev:srap-ex3-verification",
      "urn:spdx.dev:srap-ex3-evaluation",
      "urn:spdx.dev:srap-ex3-evidence"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:srap-ex3-change-trigger",
    "name": "Field incident INC-2026-0821",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "INC-2026-0821",
      "identifierLocator": ["https://servicenow.example.invalid/incident/INC-2026-0821"],
      "issuingAuthority": "Example Service Operations"
    }],
    "rationale": "A deployed system reported delayed confirmation of a safety command."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex3-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex3-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex3-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex3-change-impact-analysis",
    "name": "Change impact analysis for INC-2026-0821",
    "impactAnalysisStatus": "approved",
    "impactLevel": "critical",
    "impactedElement": ["urn:spdx.dev:req-dose-confirmation-v1", "urn:spdx.dev:test-dose-confirmation"],
    "removedElement": ["urn:spdx.dev:req-dose-confirmation-v1"],
    "addedElement": ["urn:spdx.dev:req-dose-confirmation-v2", "urn:spdx.dev:test-dose-confirmation-regression"],
    "rationale": "The incident removes the active product-context requirement and creates a revised requirement plus a regression validation."
  },
  {
    "type": "Requirement",
    "spdxId": "urn:spdx.dev:req-dose-confirmation-v2",
    "requirementUID": {"type": "ExternalIdentifier", "externalIdentifierType": "requirementUID", "identifier": "SR-DOSE-CONFIRM-REV-B"},
    "requirementStatement": "The system shall confirm delivery-command acceptance before enabling therapy execution.",
    "requirementStatus": "reviewable"
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex3-amended-by",
    "relationshipType": "amendedBy",
    "from": "urn:spdx.dev:req-dose-confirmation-v1",
    "to": ["urn:spdx.dev:req-dose-confirmation-v2"]
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex3-verification",
    "verificationMethod": "assessment",
    "rationale": "Assess the field incident against the existing dose confirmation requirement and linked validation."
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex3-evaluation",
    "evaluation": "fail",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex3-verification",
    "rationale": "The active requirement did not address the observed delayed-confirmation failure mode."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex3-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex3-evaluation",
    "to": ["urn:spdx.dev:device-log-INC-2026-0821", "urn:spdx.dev:field-service-report-INC-2026-0821"],
    "evidenceCategory": "log"
  }
]
```

## Example 4: Customer or hospital report with no safety impact

A hospital report is reviewed and the analysis concludes no safety-relevant
change is needed. SRAP still communicates the trigger, analysis, verification
result, and evidence so downstream consumers can see why no action was taken.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex4-bundle",
    "name": "SRAP change record for hospital report CAPA-2026-0134",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex4-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:srap-ex4-change-trigger",
      "urn:spdx.dev:srap-ex4-trigger-analysis-link",
      "urn:spdx.dev:srap-ex4-change-impact-analysis",
      "urn:spdx.dev:srap-ex4-verification",
      "urn:spdx.dev:srap-ex4-verified-by",
      "urn:spdx.dev:srap-ex4-evaluation",
      "urn:spdx.dev:srap-ex4-evidence"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:srap-ex4-change-trigger",
    "name": "Hospital report CAPA-2026-0134",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "CAPA-2026-0134",
      "identifierLocator": ["https://qms.example.invalid/capa/CAPA-2026-0134"],
      "issuingAuthority": "Example Hospital Quality System"
    }],
    "rationale": "A customer reported confusing alarm wording during routine operation."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex4-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex4-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex4-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex4-change-impact-analysis",
    "name": "Change impact analysis for CAPA-2026-0134",
    "impactAnalysisStatus": "approved",
    "impactLevel": "none",
    "impactedElement": ["urn:spdx.dev:req-alarm-message-clarity", "urn:spdx.dev:user-manual-alarm-section"],
    "rationale": "The report was reviewed and does not change safety requirements, design, or validation."
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex4-verification",
    "verificationMethod": "assessment",
    "rationale": "Assess whether the reported alarm wording creates a safety requirement or validation change."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex4-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-alarm-message-clarity",
    "to": ["urn:spdx.dev:srap-ex4-verification"]
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex4-evaluation",
    "evaluation": "pass",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex4-verification",
    "rationale": "The assessment found the existing requirement and validation evidence remain sufficient."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex4-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex4-evaluation",
    "to": ["urn:spdx.dev:hospital-report-CAPA-2026-0134", "urn:spdx.dev:human-factors-review-CAPA-2026-0134"],
    "evidenceCategory": "report"
  }
]
```

## Example 5: Lab finding

A lab test finding identifies a new hazard-control gap. SRAP records the lab
finding as the trigger, the safety impact analysis, the new requirement and
test elements, and the failed assessment result that justifies the change.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex5-bundle",
    "name": "SRAP change record for lab finding LAB-2026-077",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex5-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:srap-ex5-change-trigger",
      "urn:spdx.dev:srap-ex5-trigger-analysis-link",
      "urn:spdx.dev:srap-ex5-change-impact-analysis",
      "urn:spdx.dev:req-occlusion-detect-v1",
      "urn:spdx.dev:req-occlusion-detect-v2",
      "urn:spdx.dev:srap-ex5-amended-by",
      "urn:spdx.dev:srap-ex5-verification",
      "urn:spdx.dev:srap-ex5-evaluation",
      "urn:spdx.dev:srap-ex5-evidence"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:srap-ex5-change-trigger",
    "name": "Lab finding LAB-2026-077",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "LAB-2026-077",
      "identifierLocator": ["https://qms.example.invalid/lab/LAB-2026-077"],
      "issuingAuthority": "Example Reliability Lab"
    }],
    "rationale": "Bench testing found an occlusion detection edge case under a new waveform."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex5-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex5-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex5-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex5-change-impact-analysis",
    "name": "Change impact analysis for LAB-2026-077",
    "impactAnalysisStatus": "complete",
    "impactLevel": "high",
    "impactedElement": ["urn:spdx.dev:hazard-occlusion", "urn:spdx.dev:test-occlusion-detection"],
    "removedElement": ["urn:spdx.dev:req-occlusion-detect-v1"],
    "addedElement": ["urn:spdx.dev:req-occlusion-detect-v2", "urn:spdx.dev:test-occlusion-edge-waveform"],
    "rationale": "The lab finding requires a revised occlusion detection requirement and a new targeted validation."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex5-amended-by",
    "relationshipType": "amendedBy",
    "from": "urn:spdx.dev:req-occlusion-detect-v1",
    "to": ["urn:spdx.dev:req-occlusion-detect-v2"]
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex5-verification",
    "verificationMethod": "assessment",
    "rationale": "Assess the current occlusion detection requirement against the lab waveform finding."
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex5-evaluation",
    "evaluation": "fail",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex5-verification",
    "rationale": "The existing requirement does not cover the edge waveform observed in the lab."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex5-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex5-evaluation",
    "to": ["urn:spdx.dev:lab-report-LAB-2026-077"],
    "evidenceCategory": "report"
  }
]
```

## Example 6: Validation test failure

A validation run fails after a regression signal. SRAP communicates that the
test failure triggers a change impact analysis, which then identifies the
affected validation and the new rerun or corrective verification.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex6-bundle",
    "name": "SRAP change record for validation failure VAL-FAIL-2026-019",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex6-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:srap-ex6-change-trigger",
      "urn:spdx.dev:srap-ex6-trigger-analysis-link",
      "urn:spdx.dev:srap-ex6-change-impact-analysis",
      "urn:spdx.dev:srap-ex6-verification",
      "urn:spdx.dev:srap-ex6-evaluation",
      "urn:spdx.dev:srap-ex6-evidence"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:srap-ex6-change-trigger",
    "name": "Validation failure VAL-FAIL-2026-019",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "verificationUID",
      "identifier": "VAL-FAIL-2026-019",
      "identifierLocator": ["https://validation.example.invalid/runs/VAL-FAIL-2026-019"]
    }],
    "rationale": "The latest validation run failed after a regression in the watchdog timeout path."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex6-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex6-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex6-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex6-change-impact-analysis",
    "name": "Change impact analysis for VAL-FAIL-2026-019",
    "impactAnalysisStatus": "complete",
    "impactLevel": "medium",
    "impactedElement": ["urn:spdx.dev:test-watchdog-timeout", "urn:spdx.dev:req-watchdog-timeout"],
    "removedElement": ["urn:spdx.dev:evaluation-watchdog-timeout-pass-2026-08"],
    "addedElement": ["urn:spdx.dev:verification-watchdog-timeout-rerun"],
    "rationale": "The previous passing validation evidence no longer applies to the analyzed build and a rerun is required."
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex6-verification",
    "verificationMethod": "test",
    "rationale": "Rerun watchdog timeout validation on the affected build."
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex6-evaluation",
    "evaluation": "fail",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex6-verification",
    "rationale": "The watchdog timeout validation failed on the affected build."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex6-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex6-evaluation",
    "to": ["urn:spdx.dev:validation-log-VAL-FAIL-2026-019"],
    "evidenceCategory": "log"
  }
]
```

## Example 7: Post-deployment configuration change

A site-specific runtime configuration change alters a threshold after deployment.
SRAP uses the external configuration record as the trigger and captures the
context-specific reassessment without treating the configuration change as a
product-line requirement revision.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex7-bundle",
    "name": "SRAP change record for deployed configuration CFG-2026-310",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex7-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:srap-ex7-change-trigger",
      "urn:spdx.dev:srap-ex7-trigger-analysis-link",
      "urn:spdx.dev:srap-ex7-change-impact-analysis",
      "urn:spdx.dev:srap-ex7-safety-context",
      "urn:spdx.dev:srap-ex7-verification",
      "urn:spdx.dev:srap-ex7-evaluation",
      "urn:spdx.dev:srap-ex7-evidence"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:srap-ex7-change-trigger",
    "name": "Site configuration change CFG-2026-310",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "CFG-2026-310",
      "identifierLocator": ["https://config.example.invalid/changes/CFG-2026-310"],
      "issuingAuthority": "Example Device Operations"
    }],
    "rationale": "A deployed site changed a runtime dosing threshold within an approved configuration range."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex7-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex7-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex7-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex7-change-impact-analysis",
    "name": "Change impact analysis for CFG-2026-310",
    "impactAnalysisStatus": "approved",
    "impactLevel": "low",
    "impactedElement": ["urn:spdx.dev:req-dose-threshold-runtime", "urn:spdx.dev:config-dose-threshold"],
    "addedElement": ["urn:spdx.dev:srap-ex7-safety-context"],
    "rationale": "The configuration remains within the validated range, but the site-specific safety context is recorded."
  },
  {
    "type": "functionalSafety_SafetyContextRelationship",
    "spdxId": "urn:spdx.dev:srap-ex7-safety-context",
    "relationshipType": "configures",
    "from": "urn:spdx.dev:config-dose-threshold",
    "to": ["urn:spdx.dev:req-dose-threshold-runtime"],
    "scope": "runtime",
    "safetyIntegrityLevel": "sil2"
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex7-verification",
    "verificationMethod": "assessment",
    "rationale": "Assess whether the deployed threshold remains within the validated safety envelope."
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex7-evaluation",
    "evaluation": "pass",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex7-verification",
    "rationale": "The configured threshold is within the validated range for the runtime context."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex7-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex7-evaluation",
    "to": ["urn:spdx.dev:configuration-record-CFG-2026-310"],
    "evidenceCategory": "report"
  }
]
```

## Example 8: Environmental change

A new operating environment introduces latency, temperature, power, or EMI
conditions that were not part of the previous safety case. SRAP communicates
the environmental trigger, the impacted assumptions and tests, and any
inconclusive evaluation that needs follow-up.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex8-bundle",
    "name": "SRAP change record for environmental report ENV-2026-044",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex8-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:srap-ex8-change-trigger",
      "urn:spdx.dev:srap-ex8-trigger-analysis-link",
      "urn:spdx.dev:srap-ex8-change-impact-analysis",
      "urn:spdx.dev:srap-ex8-assumption",
      "urn:spdx.dev:srap-ex8-verification",
      "urn:spdx.dev:srap-ex8-evaluation",
      "urn:spdx.dev:srap-ex8-evidence"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:srap-ex8-change-trigger",
    "name": "Environmental report ENV-2026-044",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "ENV-2026-044",
      "identifierLocator": ["https://qms.example.invalid/environment/ENV-2026-044"],
      "issuingAuthority": "Example Site Reliability Team"
    }],
    "rationale": "A deployment environment reports higher EMI than the original validation envelope."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex8-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex8-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex8-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex8-change-impact-analysis",
    "name": "Change impact analysis for ENV-2026-044",
    "impactAnalysisStatus": "draft",
    "impactLevel": "high",
    "impactedElement": ["urn:spdx.dev:assumption-emi-envelope", "urn:spdx.dev:test-emi-susceptibility"],
    "addedElement": ["urn:spdx.dev:srap-ex8-assumption", "urn:spdx.dev:test-emi-site-condition"],
    "rationale": "The environment may exceed the original assumption, so a revised assumption and site-condition test are needed."
  },
  {
    "type": "functionalSafety_Assumption",
    "spdxId": "urn:spdx.dev:srap-ex8-assumption",
    "assumptionUID": {"type": "ExternalIdentifier", "externalIdentifierType": "other", "identifier": "ASSUME-EMI-SITE-REV-A"},
    "assumptionStatement": "The deployment site EMI exposure shall remain within the site-specific validated envelope."
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex8-verification",
    "verificationMethod": "analysis",
    "rationale": "Analyze whether the reported EMI environment affects the safety case."
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex8-evaluation",
    "evaluation": "inconclusive",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex8-verification",
    "rationale": "The EMI analysis was performed, but the available measurements do not conclusively map to the validated envelope.",
    "comment": "Additional site measurements are required before a pass or fail conclusion."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex8-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex8-evaluation",
    "to": ["urn:spdx.dev:emi-observation-ENV-2026-044"],
    "evidenceCategory": "observation"
  }
]
```

## Example 9: Hardware or supplier change

A supplier part-change notice may affect a safety requirement, validation, or
design artifact. SRAP links the supplier notice to the impact analysis and shows
which design and verification elements were reviewed or added.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex9-bundle",
    "name": "SRAP change record for supplier notice PCN-2026-051",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex9-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:srap-ex9-change-trigger",
      "urn:spdx.dev:srap-ex9-trigger-analysis-link",
      "urn:spdx.dev:srap-ex9-change-impact-analysis",
      "urn:spdx.dev:srap-ex9-verification",
      "urn:spdx.dev:srap-ex9-evaluation",
      "urn:spdx.dev:srap-ex9-evidence"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:srap-ex9-change-trigger",
    "name": "Supplier part change notice PCN-2026-051",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "PCN-2026-051",
      "identifierLocator": ["https://supplier.example.invalid/pcn/PCN-2026-051"],
      "issuingAuthority": "Example Sensor Supplier"
    }],
    "rationale": "A pressure sensor supplier changed an internal component used by a safety-related measurement path."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex9-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex9-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex9-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex9-change-impact-analysis",
    "name": "Change impact analysis for PCN-2026-051",
    "impactAnalysisStatus": "complete",
    "impactLevel": "low",
    "impactedElement": ["urn:spdx.dev:design-pressure-sensor-path", "urn:spdx.dev:test-pressure-sensor-accuracy"],
    "addedElement": ["urn:spdx.dev:verification-supplier-equivalence-PCN-2026-051"],
    "rationale": "The supplier evidence supports equivalence, but the affected sensor path is recorded for traceability."
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex9-verification",
    "verificationMethod": "analysis",
    "rationale": "Assess supplier equivalence data against the pressure-sensor safety requirement."
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex9-evaluation",
    "evaluation": "pass",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex9-verification",
    "rationale": "Supplier equivalence analysis confirms the pressure-sensor safety requirement remains satisfied."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex9-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex9-evaluation",
    "to": ["urn:spdx.dev:supplier-equivalence-report-PCN-2026-051"],
    "evidenceCategory": "report"
  }
]
```

## Example 10: Regulatory or safety bulletin

A regulator or safety bulletin introduces a new safety-case expectation. SRAP
communicates the bulletin as the trigger, the change impact analysis, and any
new requirement, verification, or evidence needed to show the safety case was
reviewed.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srap-ex10-bundle",
    "name": "SRAP change record for regulatory bulletin REG-2026-014",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srap-ex10-change-impact-analysis"],
    "element": [
      "urn:spdx.dev:srap-ex10-change-trigger",
      "urn:spdx.dev:srap-ex10-trigger-analysis-link",
      "urn:spdx.dev:srap-ex10-change-impact-analysis",
      "urn:spdx.dev:req-sbom-safety-trace-v1",
      "urn:spdx.dev:req-sbom-safety-trace-v2",
      "urn:spdx.dev:srap-ex10-amended-by",
      "urn:spdx.dev:srap-ex10-verification",
      "urn:spdx.dev:srap-ex10-evaluation",
      "urn:spdx.dev:srap-ex10-evidence"
    ]
  },
  {
    "type": "functionalSafety_ChangeTrigger",
    "spdxId": "urn:spdx.dev:srap-ex10-change-trigger",
    "name": "Regulatory bulletin REG-2026-014",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "REG-2026-014",
      "identifierLocator": ["https://regulator.example.invalid/bulletins/REG-2026-014"],
      "issuingAuthority": "Example Safety Regulator"
    }],
    "rationale": "A safety bulletin introduces a new traceability expectation for software components used in safety functions."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex10-trigger-analysis-link",
    "relationshipType": "other",
    "from": "urn:spdx.dev:srap-ex10-change-impact-analysis",
    "to": ["urn:spdx.dev:srap-ex10-change-trigger"]
  },
  {
    "type": "functionalSafety_ChangeImpactAnalysis",
    "spdxId": "urn:spdx.dev:srap-ex10-change-impact-analysis",
    "name": "Change impact analysis for REG-2026-014",
    "impactAnalysisStatus": "reviewable",
    "impactLevel": "high",
    "impactedElement": ["urn:spdx.dev:req-sbom-safety-trace-v1", "urn:spdx.dev:safety-case-index"],
    "removedElement": ["urn:spdx.dev:req-sbom-safety-trace-v1"],
    "addedElement": ["urn:spdx.dev:req-sbom-safety-trace-v2", "urn:spdx.dev:verification-regulatory-traceability"],
    "rationale": "The bulletin requires an updated safety-traceability requirement and a review of the safety case index."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srap-ex10-amended-by",
    "relationshipType": "amendedBy",
    "from": "urn:spdx.dev:req-sbom-safety-trace-v1",
    "to": ["urn:spdx.dev:req-sbom-safety-trace-v2"]
  },
  {
    "type": "functionalSafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srap-ex10-verification",
    "verificationMethod": "assessment",
    "rationale": "Assess current safety traceability against the new regulatory bulletin."
  },
  {
    "type": "functionalSafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srap-ex10-evaluation",
    "evaluation": "fail",
    "evaluationBasedOn": "urn:spdx.dev:srap-ex10-verification",
    "rationale": "The current safety case does not yet include the bulletin-required traceability expectation."
  },
  {
    "type": "functionalSafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srap-ex10-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srap-ex10-evaluation",
    "to": ["urn:spdx.dev:regulatory-bulletin-REG-2026-014"],
    "evidenceCategory": "report"
  }
]
```
