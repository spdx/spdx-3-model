# Safety Relevance Assertion Capability examples

The following non-normative examples show how a Safety Relevance Assertion
Capability (SRAC) can be represented using SPDX Core, Security, and
FunctionalSafety elements.

SRAC is a usage pattern. It does not require a dedicated SRAC-specific
assessment class. Each example uses the same graph shape:

- a Core Bundle carries the delta or change record;
- AnalysisTrigger, or another source Artifact such as /Security/Vulnerability,
  records the source, reason, event, report, or external record that initiates
  the safety-relevant review;
- a Core Relationship links the SystemImpactAnalysis to the source using
  relationshipType hasInput, from the SystemImpactAnalysis to the source
  element;
- SystemImpactAnalysis records the analysis status, impact category,
  and the SPDX elements that are impacted, added, or removed from the analyzed
  safety context;
- when per-element decisions are represented, the SystemImpactAnalysis can use
  relationshipType hasOutput to link to each Decision, and each Decision can use
  relationshipType hasInput to identify the specific Element it decides on;
- RequirementVerification, EvaluationResult, and EvidenceRelationship are reused
  when downstream verification, result, and evidence need to be communicated.

When the work is still waiting on evidence, a decision, or a test rerun, use
impactAnalysisStatus with an inProgress value on SystemImpactAnalysis. Do not
use EvaluationResult with an inconclusive value to mean "not started". Use an
inconclusive EvaluationResult only when an evaluation was performed but cannot
be clearly classified as pass or fail, and include a comment or rationale.
Use impactAnalysisStatus with a complete value only after the analysis has
recorded its conclusion and any required downstream verification, evidence, or
per-element Decision records have been represented, or the rationale explains
why no downstream work is required.

SPDX elements are not edited in place. If a requirement, validation, test,
design artifact, or other work product changes, create a new SPDX element and
link the old element to the new element with a relationship such as amendedBy
when that relationship is appropriate.

When publishing the SRAC change record, use a Core Bundle to collect the
analysis graph. The Bundle rootElement can point to the SystemImpactAnalysis so
consumers can enter the graph at the analysis and follow the trigger, affected
elements, decisions, verification, results, and evidence.

The examples below omit some organization-specific records, such as detailed
QMS workflow data, when those records remain authoritative outside SPDX.
Examples 2 through 10 also reference requirements, tests, reports, and other
elements that are assumed to exist in the product's SPDX safety model. Example
1 is fully self-contained.

## Example 1: Product-line requirement value change

A product-line safety requirement is tightened for a deployed product context.
The previous requirement remains historically valid, the revised requirement is
created as a new element, and the delta Bundle communicates the trigger, impact
analysis, requirement revision, verification results, and evidence.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex1-bundle",
    "name": "SRAC change record for vehicle dynamics data VD-2026-040",
    "profileConformance": ["core", "software", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex1-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:srac-ex1-change-trigger",
      "urn:spdx.dev:srac-ex1-trigger-analysis-link",
      "urn:spdx.dev:srac-ex1-system-impact-analysis",
      "urn:spdx.dev:srac-ex1-analysis-decision-output",
      "urn:spdx.dev:srac-ex1-requirement-decision",
      "urn:spdx.dev:srac-ex1-decision-input",
      "urn:spdx.dev:agent-safety-review-board",
      "urn:spdx.dev:sop-system-impact-analysis",
      "urn:spdx.dev:req-brake-response-40ms",
      "urn:spdx.dev:req-brake-response-30ms",
      "urn:spdx.dev:srac-ex1-amended-by",
      "urn:spdx.dev:test-brake-response-t001",
      "urn:spdx.dev:test-brake-response-t002",
      "urn:spdx.dev:test-brake-response-t003",
      "urn:spdx.dev:srac-ex1-verification",
      "urn:spdx.dev:srac-ex1-verified-by",
      "urn:spdx.dev:srac-ex1-evaluation",
      "urn:spdx.dev:srac-ex1-evidence",
      "urn:spdx.dev:vehicle-dynamics-report-VD-2026-040",
      "urn:spdx.dev:srac-ex1-verification-30ms",
      "urn:spdx.dev:srac-ex1-verified-by-30ms",
      "urn:spdx.dev:srac-ex1-evaluation-30ms",
      "urn:spdx.dev:srac-ex1-evidence-30ms",
      "urn:spdx.dev:brake-response-test-report-30ms"
    ]
  },
  {
    "type": "functionalsafety_AnalysisTrigger",
    "spdxId": "urn:spdx.dev:srac-ex1-change-trigger",
    "name": "Vehicle dynamics data VD-2026-040",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "VD-2026-040",
      "identifierLocator": ["https://qms.example.invalid/vehicle-dynamics/VD-2026-040"],
      "issuingAuthority": "Example Mobility Safety Engineering"
    }],
    "description": "New vehicle dynamics data shows the previous braking response threshold is no longer sufficient for this product context."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex1-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex1-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex1-change-trigger"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex1-system-impact-analysis",
    "name": "System impact analysis for VD-2026-040",
    "functionalsafety_impactAnalysisProcess": ["urn:spdx.dev:sop-system-impact-analysis"],
    "functionalsafety_impactAnalysisStatus": "complete",
    "functionalsafety_impactLevel": "safetyImpact",
    "functionalsafety_impactedElement": ["urn:spdx.dev:req-brake-response-40ms", "urn:spdx.dev:test-brake-response-t001", "urn:spdx.dev:test-brake-response-t002"],
    "functionalsafety_removedElement": ["urn:spdx.dev:req-brake-response-40ms", "urn:spdx.dev:test-brake-response-t002"],
    "functionalsafety_addedElement": ["urn:spdx.dev:req-brake-response-30ms", "urn:spdx.dev:test-brake-response-t003", "urn:spdx.dev:srac-ex1-verification-30ms"],
    "rationale": "The active product context changes from a 40 ms requirement to a 30 ms requirement. The new requirement is verified before this analysis is closed."
  },
  {
    "type": "Specification",
    "spdxId": "urn:spdx.dev:sop-system-impact-analysis",
    "name": "System impact analysis procedure",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "SOP-system-impact-analysis",
      "identifierLocator": ["https://qms.example.invalid/sop/SOP-system-impact-analysis"],
      "issuingAuthority": "Example Mobility Safety Engineering"
    }]
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex1-analysis-decision-output",
    "relationshipType": "hasOutput",
    "from": "urn:spdx.dev:srac-ex1-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex1-requirement-decision"]
  },
  {
    "type": "Decision",
    "spdxId": "urn:spdx.dev:srac-ex1-requirement-decision",
    "name": "Decision for 30 ms braking response requirement",
    "originatedBy": ["urn:spdx.dev:agent-safety-review-board"],
    "decisionType": "approve",
    "decisionStatus": "recorded",
    "rationale": "Approve adding the 30 ms requirement for this product context after the linked verification rerun passes."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex1-decision-input",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex1-requirement-decision",
    "to": ["urn:spdx.dev:req-brake-response-30ms"]
  },
  {
    "type": "Agent",
    "spdxId": "urn:spdx.dev:agent-safety-review-board",
    "name": "Safety review board"
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
    "type": "software_File",
    "spdxId": "urn:spdx.dev:test-brake-response-t001",
    "name": "Brake response validation test T-001",
    "software_primaryPurpose": "test",
    "description": "Existing validation test rerun against the 30 ms braking command response threshold."
  },
  {
    "type": "software_File",
    "spdxId": "urn:spdx.dev:test-brake-response-t002",
    "name": "Brake response validation test T-002",
    "software_primaryPurpose": "test",
    "description": "Previous validation test retired for this product context."
  },
  {
    "type": "software_File",
    "spdxId": "urn:spdx.dev:test-brake-response-t003",
    "name": "Brake response validation test T-003",
    "software_primaryPurpose": "test",
    "description": "New validation test added for the 30 ms braking command response threshold."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex1-amended-by",
    "relationshipType": "amendedBy",
    "from": "urn:spdx.dev:req-brake-response-40ms",
    "to": ["urn:spdx.dev:req-brake-response-30ms"]
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex1-verification",
    "functionalsafety_verificationMethod": ["assessment"],
    "rationale": "Assess the previous threshold against the new product-line dynamics data."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex1-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-brake-response-40ms",
    "to": ["urn:spdx.dev:srac-ex1-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex1-evaluation",
    "functionalsafety_evaluation": "fail",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex1-verification",
    "rationale": "The 40 ms requirement is not met for the analyzed product context."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex1-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex1-evaluation",
    "to": ["urn:spdx.dev:vehicle-dynamics-report-VD-2026-040"],
    "functionalsafety_evidenceCategory": ["report"]
  },
  {
    "type": "software_File",
    "spdxId": "urn:spdx.dev:vehicle-dynamics-report-VD-2026-040",
    "name": "Vehicle dynamics report VD-2026-040",
    "software_primaryPurpose": "evidence",
    "description": "QMS report that triggered the braking response requirement reassessment.",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "VD-2026-040",
      "identifierLocator": ["https://qms.example.invalid/vehicle-dynamics/VD-2026-040"],
      "issuingAuthority": "Example Mobility Safety Engineering"
    }]
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex1-verification-30ms",
    "functionalsafety_verificationMethod": ["test"],
    "rationale": "Rerun T-001 and run T-003 against the new 30 ms requirement."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex1-verified-by-30ms",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-brake-response-30ms",
    "to": ["urn:spdx.dev:srac-ex1-verification-30ms"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex1-evaluation-30ms",
    "functionalsafety_evaluation": "pass",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex1-verification-30ms",
    "rationale": "The 30 ms requirement is met by the rerun validation evidence."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex1-evidence-30ms",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex1-evaluation-30ms",
    "to": ["urn:spdx.dev:brake-response-test-report-30ms"],
    "functionalsafety_evidenceCategory": ["report"]
  },
  {
    "type": "software_File",
    "spdxId": "urn:spdx.dev:brake-response-test-report-30ms",
    "name": "Brake response 30 ms test report",
    "software_primaryPurpose": "evidence",
    "description": "Report showing T-001 and T-003 passed against the 30 ms requirement.",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "evidenceUID",
      "identifier": "BRK-30MS-TEST-REPORT-2026-09",
      "identifierLocator": ["https://qms.example.invalid/test-reports/BRK-30MS-TEST-REPORT-2026-09"],
      "issuingAuthority": "Example Mobility Safety Engineering"
    }]
  }
]
```

## Example 2: CVE in a safety-relevant component

The Security profile carries the vulnerability and VEX status. FunctionalSafety
adds the safety context and the SRAC system impact analysis so the existing
Security vulnerability can be used as input to the safety analysis without
duplicating the Security/VEX layer.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex2-bundle",
    "name": "SRAC change record for CVE-2024-9999",
    "profileConformance": ["core", "security", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex2-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:vuln-cve-2024-9999",
      "urn:spdx.dev:vex-under-investigation-cve-2024-9999",
      "urn:spdx.dev:safety-context-openssl-sr12",
      "urn:spdx.dev:srac-ex2-trigger-analysis-link",
      "urn:spdx.dev:srac-ex2-system-impact-analysis",
      "urn:spdx.dev:srac-ex2-verification",
      "urn:spdx.dev:srac-ex2-verified-by",
      "urn:spdx.dev:srac-ex2-evaluation",
      "urn:spdx.dev:srac-ex2-evidence"
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
    "type": "functionalsafety_SafetyContextRelationship",
    "spdxId": "urn:spdx.dev:safety-context-openssl-sr12",
    "relationshipType": "hasRequirement",
    "from": "pkg:generic/openssl@3.0.8",
    "to": ["urn:spdx.dev:req-sr12-therapy-command-transport"],
    "scope": "runtime",
    "functionalsafety_safetyIntegrityLevel": "sil2"
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex2-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex2-system-impact-analysis",
    "to": ["urn:spdx.dev:vuln-cve-2024-9999"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex2-system-impact-analysis",
    "name": "System impact analysis for CVE-2024-9999",
    "functionalsafety_impactAnalysisProcess": ["urn:spdx.dev:sop-system-impact-analysis"],
    "functionalsafety_impactAnalysisStatus": "inProgress",
    "functionalsafety_impactLevel": "safetyAndSecurityImpact",
    "functionalsafety_impactedElement": [
      "pkg:generic/openssl@3.0.8",
      "urn:spdx.dev:req-sr12-therapy-command-transport",
      "urn:spdx.dev:safety-context-openssl-sr12"
    ],
    "functionalsafety_addedElement": ["urn:spdx.dev:srac-ex2-verification"],
    "rationale": "SafetyContextRelationship shows the vulnerable component is safety relevant at runtime."
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex2-verification",
    "functionalsafety_verificationMethod": ["assessment"],
    "rationale": "Assess whether the CVE affects the SIL-2 therapy command transport requirement."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex2-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-sr12-therapy-command-transport",
    "to": ["urn:spdx.dev:srac-ex2-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex2-evaluation",
    "functionalsafety_evaluation": "inconclusive",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex2-verification",
    "rationale": "The reachability analysis was performed, but exploitability of the affected TLS path in the safety function cannot yet be classified as pass or fail.",
    "comment": "Additional runtime tracing is needed before the safety impact conclusion is final."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex2-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex2-evaluation",
    "to": ["urn:spdx.dev:tls-reachability-report-2026-09"],
    "functionalsafety_evidenceCategory": ["report"]
  }
]
```

## Example 3: Field incident after deployment

A deployed device reports a safety-relevant incident. SRAC communicates the
incident reference, the analysis that decides which safety artifacts are
affected, and the resulting design or validation updates.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex3-bundle",
    "name": "SRAC change record for field incident INC-2026-0821",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex3-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:srac-ex3-change-trigger",
      "urn:spdx.dev:srac-ex3-trigger-analysis-link",
      "urn:spdx.dev:srac-ex3-system-impact-analysis",
      "urn:spdx.dev:req-dose-confirmation-v1",
      "urn:spdx.dev:req-dose-confirmation-v2",
      "urn:spdx.dev:srac-ex3-amended-by",
      "urn:spdx.dev:srac-ex3-verification",
      "urn:spdx.dev:srac-ex3-verified-by",
      "urn:spdx.dev:srac-ex3-evaluation",
      "urn:spdx.dev:srac-ex3-evidence",
      "urn:spdx.dev:srac-ex3-followup-verification",
      "urn:spdx.dev:srac-ex3-followup-verified-by"
    ]
  },
  {
    "type": "functionalsafety_AnalysisTrigger",
    "spdxId": "urn:spdx.dev:srac-ex3-change-trigger",
    "name": "Field incident INC-2026-0821",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "INC-2026-0821",
      "identifierLocator": ["https://servicenow.example.invalid/incident/INC-2026-0821"],
      "issuingAuthority": "Example Service Operations"
    }],
    "description": "A deployed system reported delayed confirmation of a safety command."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex3-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex3-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex3-change-trigger"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex3-system-impact-analysis",
    "name": "System impact analysis for INC-2026-0821",
    "functionalsafety_impactAnalysisStatus": "inProgress",
    "functionalsafety_impactLevel": "safetyImpact",
    "functionalsafety_impactedElement": ["urn:spdx.dev:req-dose-confirmation-v1", "urn:spdx.dev:test-dose-confirmation"],
    "functionalsafety_removedElement": ["urn:spdx.dev:req-dose-confirmation-v1"],
    "functionalsafety_addedElement": ["urn:spdx.dev:req-dose-confirmation-v2", "urn:spdx.dev:test-dose-confirmation-regression", "urn:spdx.dev:srac-ex3-followup-verification"],
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
    "spdxId": "urn:spdx.dev:srac-ex3-amended-by",
    "relationshipType": "amendedBy",
    "from": "urn:spdx.dev:req-dose-confirmation-v1",
    "to": ["urn:spdx.dev:req-dose-confirmation-v2"]
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex3-verification",
    "functionalsafety_verificationMethod": ["assessment"],
    "rationale": "Assess the field incident against the existing dose confirmation requirement and linked validation."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex3-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-dose-confirmation-v1",
    "to": ["urn:spdx.dev:srac-ex3-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex3-evaluation",
    "functionalsafety_evaluation": "fail",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex3-verification",
    "rationale": "The active requirement did not address the observed delayed-confirmation failure mode."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex3-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex3-evaluation",
    "to": ["urn:spdx.dev:device-log-INC-2026-0821", "urn:spdx.dev:field-service-report-INC-2026-0821"],
    "functionalsafety_evidenceCategory": ["log"]
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex3-followup-verification",
    "functionalsafety_verificationMethod": ["test"],
    "rationale": "Run regression validation against the revised dose confirmation requirement before closing the analysis."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex3-followup-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-dose-confirmation-v2",
    "to": ["urn:spdx.dev:srac-ex3-followup-verification"]
  }
]
```

## Example 4: Customer or hospital report with no safety impact

A hospital report is reviewed and the analysis concludes no safety-relevant
change is needed. SRAC still communicates the trigger, analysis, verification
result, and evidence so downstream consumers can see why no action was taken.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex4-bundle",
    "name": "SRAC change record for hospital report CAPA-2026-0134",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex4-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:srac-ex4-change-trigger",
      "urn:spdx.dev:srac-ex4-trigger-analysis-link",
      "urn:spdx.dev:srac-ex4-system-impact-analysis",
      "urn:spdx.dev:srac-ex4-analysis-decision-output",
      "urn:spdx.dev:srac-ex4-no-action-decision",
      "urn:spdx.dev:srac-ex4-decision-input",
      "urn:spdx.dev:agent-safety-review-board",
      "urn:spdx.dev:srac-ex4-verification",
      "urn:spdx.dev:srac-ex4-verified-by",
      "urn:spdx.dev:srac-ex4-evaluation",
      "urn:spdx.dev:srac-ex4-evidence"
    ]
  },
  {
    "type": "functionalsafety_AnalysisTrigger",
    "spdxId": "urn:spdx.dev:srac-ex4-change-trigger",
    "name": "Hospital report CAPA-2026-0134",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "CAPA-2026-0134",
      "identifierLocator": ["https://qms.example.invalid/capa/CAPA-2026-0134"],
      "issuingAuthority": "Example Hospital Quality System"
    }],
    "description": "A customer reported confusing alarm wording during routine operation."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex4-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex4-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex4-change-trigger"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex4-system-impact-analysis",
    "name": "System impact analysis for CAPA-2026-0134",
    "functionalsafety_impactAnalysisStatus": "complete",
    "functionalsafety_impactLevel": "noCriticalImpact",
    "functionalsafety_impactedElement": ["urn:spdx.dev:req-alarm-message-clarity", "urn:spdx.dev:user-manual-alarm-section"],
    "rationale": "The report was reviewed and does not change safety requirements, design, or validation."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex4-analysis-decision-output",
    "relationshipType": "hasOutput",
    "from": "urn:spdx.dev:srac-ex4-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex4-no-action-decision"]
  },
  {
    "type": "Decision",
    "spdxId": "urn:spdx.dev:srac-ex4-no-action-decision",
    "name": "No-action decision for alarm wording report",
    "originatedBy": ["urn:spdx.dev:agent-safety-review-board"],
    "decisionType": "noAction",
    "decisionStatus": "recorded",
    "rationale": "No safety requirement, design, or validation change is required for the reviewed report."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex4-decision-input",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex4-no-action-decision",
    "to": ["urn:spdx.dev:req-alarm-message-clarity"]
  },
  {
    "type": "Agent",
    "spdxId": "urn:spdx.dev:agent-safety-review-board",
    "name": "Safety review board"
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex4-verification",
    "functionalsafety_verificationMethod": ["assessment"],
    "rationale": "Assess whether the reported alarm wording creates a safety requirement or validation change."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex4-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-alarm-message-clarity",
    "to": ["urn:spdx.dev:srac-ex4-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex4-evaluation",
    "functionalsafety_evaluation": "pass",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex4-verification",
    "rationale": "The assessment found the existing requirement and validation evidence remain sufficient."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex4-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex4-evaluation",
    "to": ["urn:spdx.dev:hospital-report-CAPA-2026-0134", "urn:spdx.dev:human-factors-review-CAPA-2026-0134"],
    "functionalsafety_evidenceCategory": ["report"]
  }
]
```

## Example 5: Lab finding

A lab test finding identifies a new hazard-control gap. SRAC records the lab
finding as the trigger, the safety impact analysis, the new requirement and
test elements, and the failed assessment result that justifies the change.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex5-bundle",
    "name": "SRAC change record for lab finding LAB-2026-077",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex5-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:srac-ex5-change-trigger",
      "urn:spdx.dev:srac-ex5-trigger-analysis-link",
      "urn:spdx.dev:srac-ex5-system-impact-analysis",
      "urn:spdx.dev:req-occlusion-detect-v1",
      "urn:spdx.dev:req-occlusion-detect-v2",
      "urn:spdx.dev:srac-ex5-amended-by",
      "urn:spdx.dev:srac-ex5-verification",
      "urn:spdx.dev:srac-ex5-verified-by",
      "urn:spdx.dev:srac-ex5-evaluation",
      "urn:spdx.dev:srac-ex5-evidence",
      "urn:spdx.dev:srac-ex5-followup-verification",
      "urn:spdx.dev:srac-ex5-followup-verified-by"
    ]
  },
  {
    "type": "functionalsafety_AnalysisTrigger",
    "spdxId": "urn:spdx.dev:srac-ex5-change-trigger",
    "name": "Lab finding LAB-2026-077",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "LAB-2026-077",
      "identifierLocator": ["https://qms.example.invalid/lab/LAB-2026-077"],
      "issuingAuthority": "Example Reliability Lab"
    }],
    "description": "Bench testing found an occlusion detection edge case under a new waveform."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex5-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex5-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex5-change-trigger"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex5-system-impact-analysis",
    "name": "System impact analysis for LAB-2026-077",
    "functionalsafety_impactAnalysisStatus": "inProgress",
    "functionalsafety_impactLevel": "safetyImpact",
    "functionalsafety_impactedElement": ["urn:spdx.dev:hazard-occlusion", "urn:spdx.dev:req-occlusion-detect-v1", "urn:spdx.dev:test-occlusion-detection"],
    "functionalsafety_removedElement": ["urn:spdx.dev:req-occlusion-detect-v1"],
    "functionalsafety_addedElement": ["urn:spdx.dev:req-occlusion-detect-v2", "urn:spdx.dev:test-occlusion-edge-waveform", "urn:spdx.dev:srac-ex5-followup-verification"],
    "rationale": "The lab finding requires a revised occlusion detection requirement and a new targeted validation."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex5-amended-by",
    "relationshipType": "amendedBy",
    "from": "urn:spdx.dev:req-occlusion-detect-v1",
    "to": ["urn:spdx.dev:req-occlusion-detect-v2"]
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex5-verification",
    "functionalsafety_verificationMethod": ["assessment"],
    "rationale": "Assess the current occlusion detection requirement against the lab waveform finding."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex5-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-occlusion-detect-v1",
    "to": ["urn:spdx.dev:srac-ex5-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex5-evaluation",
    "functionalsafety_evaluation": "fail",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex5-verification",
    "rationale": "The existing requirement does not cover the edge waveform observed in the lab."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex5-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex5-evaluation",
    "to": ["urn:spdx.dev:lab-report-LAB-2026-077"],
    "functionalsafety_evidenceCategory": ["report"]
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex5-followup-verification",
    "functionalsafety_verificationMethod": ["test"],
    "rationale": "Run the targeted edge-waveform validation against the revised occlusion detection requirement before closing the analysis."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex5-followup-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-occlusion-detect-v2",
    "to": ["urn:spdx.dev:srac-ex5-followup-verification"]
  }
]
```

## Example 6: Validation test failure

A validation run fails after a regression signal. SRAC communicates that the
test failure triggers a system impact analysis, which then identifies the
affected validation and the new rerun or corrective verification.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex6-bundle",
    "name": "SRAC change record for validation failure VAL-FAIL-2026-019",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex6-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:srac-ex6-change-trigger",
      "urn:spdx.dev:srac-ex6-trigger-analysis-link",
      "urn:spdx.dev:srac-ex6-system-impact-analysis",
      "urn:spdx.dev:srac-ex6-verification",
      "urn:spdx.dev:srac-ex6-verified-by",
      "urn:spdx.dev:srac-ex6-evaluation",
      "urn:spdx.dev:srac-ex6-evidence"
    ]
  },
  {
    "type": "functionalsafety_AnalysisTrigger",
    "spdxId": "urn:spdx.dev:srac-ex6-change-trigger",
    "name": "Validation failure VAL-FAIL-2026-019",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "verificationUID",
      "identifier": "VAL-FAIL-2026-019",
      "identifierLocator": ["https://validation.example.invalid/runs/VAL-FAIL-2026-019"]
    }],
    "description": "The latest validation run failed after a regression in the watchdog timeout path."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex6-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex6-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex6-change-trigger"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex6-system-impact-analysis",
    "name": "System impact analysis for VAL-FAIL-2026-019",
    "functionalsafety_impactAnalysisStatus": "inProgress",
    "functionalsafety_impactLevel": "safetyImpact",
    "functionalsafety_impactedElement": ["urn:spdx.dev:test-watchdog-timeout", "urn:spdx.dev:req-watchdog-timeout"],
    "functionalsafety_removedElement": ["urn:spdx.dev:evaluation-watchdog-timeout-pass-2026-08"],
    "functionalsafety_addedElement": ["urn:spdx.dev:verification-watchdog-timeout-rerun"],
    "rationale": "The previous passing validation evidence no longer applies to the analyzed build and a rerun is required."
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex6-verification",
    "functionalsafety_verificationMethod": ["test"],
    "rationale": "Rerun watchdog timeout validation on the affected build."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex6-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-watchdog-timeout",
    "to": ["urn:spdx.dev:srac-ex6-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex6-evaluation",
    "functionalsafety_evaluation": "fail",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex6-verification",
    "rationale": "The watchdog timeout validation failed on the affected build."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex6-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex6-evaluation",
    "to": ["urn:spdx.dev:validation-log-VAL-FAIL-2026-019"],
    "functionalsafety_evidenceCategory": ["log"]
  }
]
```

## Example 7: Post-deployment configuration change

A site-specific runtime configuration change alters a threshold after deployment.
SRAC uses the external configuration record as the trigger and captures the
context-specific reassessment without treating the configuration change as a
product-line requirement revision.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex7-bundle",
    "name": "SRAC change record for deployed configuration CFG-2026-310",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex7-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:srac-ex7-change-trigger",
      "urn:spdx.dev:srac-ex7-trigger-analysis-link",
      "urn:spdx.dev:srac-ex7-system-impact-analysis",
      "urn:spdx.dev:srac-ex7-safety-context",
      "urn:spdx.dev:srac-ex7-verification",
      "urn:spdx.dev:srac-ex7-verified-by",
      "urn:spdx.dev:srac-ex7-evaluation",
      "urn:spdx.dev:srac-ex7-evidence"
    ]
  },
  {
    "type": "functionalsafety_AnalysisTrigger",
    "spdxId": "urn:spdx.dev:srac-ex7-change-trigger",
    "name": "Site configuration change CFG-2026-310",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "CFG-2026-310",
      "identifierLocator": ["https://config.example.invalid/changes/CFG-2026-310"],
      "issuingAuthority": "Example Device Operations"
    }],
    "description": "A deployed site changed a runtime dosing threshold within a validated configuration range."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex7-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex7-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex7-change-trigger"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex7-system-impact-analysis",
    "name": "System impact analysis for CFG-2026-310",
    "functionalsafety_impactAnalysisStatus": "complete",
    "functionalsafety_impactLevel": "noCriticalImpact",
    "functionalsafety_impactedElement": ["urn:spdx.dev:req-dose-threshold-runtime", "urn:spdx.dev:config-dose-threshold"],
    "functionalsafety_addedElement": ["urn:spdx.dev:srac-ex7-safety-context"],
    "rationale": "The configuration remains within the validated range, and the site-specific safety context is recorded; no separate decision record is required."
  },
  {
    "type": "functionalsafety_SafetyContextRelationship",
    "spdxId": "urn:spdx.dev:srac-ex7-safety-context",
    "relationshipType": "configures",
    "from": "urn:spdx.dev:config-dose-threshold",
    "to": ["urn:spdx.dev:req-dose-threshold-runtime"],
    "scope": "runtime",
    "functionalsafety_safetyIntegrityLevel": "sil2"
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex7-verification",
    "functionalsafety_verificationMethod": ["assessment"],
    "rationale": "Assess whether the deployed threshold remains within the validated safety envelope."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex7-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-dose-threshold-runtime",
    "to": ["urn:spdx.dev:srac-ex7-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex7-evaluation",
    "functionalsafety_evaluation": "pass",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex7-verification",
    "rationale": "The configured threshold is within the validated range for the runtime context."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex7-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex7-evaluation",
    "to": ["urn:spdx.dev:configuration-record-CFG-2026-310"],
    "functionalsafety_evidenceCategory": ["report"]
  }
]
```

## Example 8: Environmental change

A new operating environment introduces latency, temperature, power, or EMI
conditions that were not part of the previous safety case. SRAC communicates
the environmental trigger, the impacted assumptions and tests, and any
inconclusive evaluation that needs follow-up.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex8-bundle",
    "name": "SRAC change record for environmental report ENV-2026-044",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex8-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:srac-ex8-change-trigger",
      "urn:spdx.dev:srac-ex8-trigger-analysis-link",
      "urn:spdx.dev:srac-ex8-system-impact-analysis",
      "urn:spdx.dev:srac-ex8-assumption",
      "urn:spdx.dev:srac-ex8-verification",
      "urn:spdx.dev:srac-ex8-verified-by",
      "urn:spdx.dev:srac-ex8-evaluation",
      "urn:spdx.dev:srac-ex8-evidence"
    ]
  },
  {
    "type": "functionalsafety_AnalysisTrigger",
    "spdxId": "urn:spdx.dev:srac-ex8-change-trigger",
    "name": "Environmental report ENV-2026-044",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "ENV-2026-044",
      "identifierLocator": ["https://qms.example.invalid/environment/ENV-2026-044"],
      "issuingAuthority": "Example Site Reliability Team"
    }],
    "description": "A deployment environment reports higher EMI than the original validation envelope."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex8-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex8-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex8-change-trigger"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex8-system-impact-analysis",
    "name": "System impact analysis for ENV-2026-044",
    "functionalsafety_impactAnalysisStatus": "inProgress",
    "functionalsafety_impactLevel": "safetyImpact",
    "functionalsafety_impactedElement": ["urn:spdx.dev:assumption-emi-envelope", "urn:spdx.dev:test-emi-susceptibility"],
    "functionalsafety_addedElement": ["urn:spdx.dev:srac-ex8-assumption", "urn:spdx.dev:test-emi-site-condition"],
    "rationale": "The environment may exceed the original assumption, so a revised assumption and site-condition test are needed."
  },
  {
    "type": "functionalsafety_Assumption",
    "spdxId": "urn:spdx.dev:srac-ex8-assumption",
    "functionalsafety_assumptionUID": {"type": "ExternalIdentifier", "externalIdentifierType": "other", "identifier": "ASSUME-EMI-SITE-REV-A"},
    "functionalsafety_assumptionStatement": "The deployment site EMI exposure shall remain within the site-specific validated envelope."
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex8-verification",
    "functionalsafety_verificationMethod": ["analysis"],
    "rationale": "Analyze whether the reported EMI environment affects the safety case."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex8-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:assumption-emi-envelope",
    "to": ["urn:spdx.dev:srac-ex8-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex8-evaluation",
    "functionalsafety_evaluation": "inconclusive",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex8-verification",
    "rationale": "The EMI analysis was performed, but the available measurements do not conclusively map to the validated envelope.",
    "comment": "Additional site measurements are required before a pass or fail conclusion."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex8-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex8-evaluation",
    "to": ["urn:spdx.dev:emi-observation-ENV-2026-044"],
    "functionalsafety_evidenceCategory": ["observation"]
  }
]
```

## Example 9: Hardware or supplier change

A supplier part-change notice may affect a safety requirement, validation, or
design artifact. SRAC links the supplier notice to the impact analysis and shows
which design and verification elements were reviewed or added.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex9-bundle",
    "name": "SRAC change record for supplier notice PCN-2026-051",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex9-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:srac-ex9-change-trigger",
      "urn:spdx.dev:srac-ex9-trigger-analysis-link",
      "urn:spdx.dev:srac-ex9-system-impact-analysis",
      "urn:spdx.dev:srac-ex9-verification",
      "urn:spdx.dev:srac-ex9-verified-by",
      "urn:spdx.dev:srac-ex9-evaluation",
      "urn:spdx.dev:srac-ex9-evidence"
    ]
  },
  {
    "type": "functionalsafety_AnalysisTrigger",
    "spdxId": "urn:spdx.dev:srac-ex9-change-trigger",
    "name": "Supplier part change notice PCN-2026-051",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "PCN-2026-051",
      "identifierLocator": ["https://supplier.example.invalid/pcn/PCN-2026-051"],
      "issuingAuthority": "Example Sensor Supplier"
    }],
    "description": "A pressure sensor supplier changed an internal component used by a safety-related measurement path."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex9-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex9-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex9-change-trigger"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex9-system-impact-analysis",
    "name": "System impact analysis for PCN-2026-051",
    "functionalsafety_impactAnalysisStatus": "complete",
    "functionalsafety_impactLevel": "qualityImpact",
    "functionalsafety_impactedElement": ["urn:spdx.dev:design-pressure-sensor-path", "urn:spdx.dev:test-pressure-sensor-accuracy"],
    "functionalsafety_addedElement": ["urn:spdx.dev:verification-supplier-equivalence-PCN-2026-051"],
    "rationale": "The supplier evidence supports equivalence and no safety requirement or validation change is required, so the impact is recorded as qualityImpact; no separate decision record is required."
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex9-verification",
    "functionalsafety_verificationMethod": ["analysis"],
    "rationale": "Assess supplier equivalence data against the pressure-sensor safety requirement."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex9-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:design-pressure-sensor-path",
    "to": ["urn:spdx.dev:srac-ex9-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex9-evaluation",
    "functionalsafety_evaluation": "pass",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex9-verification",
    "rationale": "Supplier equivalence analysis confirms the pressure-sensor safety requirement remains satisfied."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex9-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex9-evaluation",
    "to": ["urn:spdx.dev:supplier-equivalence-report-PCN-2026-051"],
    "functionalsafety_evidenceCategory": ["report"]
  }
]
```

## Example 10: Regulatory or safety bulletin

A regulator or safety bulletin introduces a new safety-case expectation. SRAC
communicates the bulletin as the trigger, the system impact analysis, and any
new requirement, verification, or evidence needed to show the safety case was
reviewed.

```json
[
  {
    "type": "Bundle",
    "spdxId": "urn:spdx.dev:srac-ex10-bundle",
    "name": "SRAC change record for regulatory bulletin REG-2026-014",
    "profileConformance": ["core", "functionalSafety"],
    "rootElement": ["urn:spdx.dev:srac-ex10-system-impact-analysis"],
    "element": [
      "urn:spdx.dev:srac-ex10-change-trigger",
      "urn:spdx.dev:srac-ex10-trigger-analysis-link",
      "urn:spdx.dev:srac-ex10-system-impact-analysis",
      "urn:spdx.dev:req-sbom-safety-trace-v1",
      "urn:spdx.dev:req-sbom-safety-trace-v2",
      "urn:spdx.dev:srac-ex10-amended-by",
      "urn:spdx.dev:srac-ex10-verification",
      "urn:spdx.dev:srac-ex10-verified-by",
      "urn:spdx.dev:srac-ex10-evaluation",
      "urn:spdx.dev:srac-ex10-evidence"
    ]
  },
  {
    "type": "functionalsafety_AnalysisTrigger",
    "spdxId": "urn:spdx.dev:srac-ex10-change-trigger",
    "name": "Regulatory bulletin REG-2026-014",
    "externalIdentifier": [{
      "type": "ExternalIdentifier",
      "externalIdentifierType": "other",
      "identifier": "REG-2026-014",
      "identifierLocator": ["https://regulator.example.invalid/bulletins/REG-2026-014"],
      "issuingAuthority": "Example Safety Regulator"
    }],
    "description": "A safety bulletin introduces a new traceability expectation for software components used in safety functions."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex10-trigger-analysis-link",
    "relationshipType": "hasInput",
    "from": "urn:spdx.dev:srac-ex10-system-impact-analysis",
    "to": ["urn:spdx.dev:srac-ex10-change-trigger"]
  },
  {
    "type": "functionalsafety_SystemImpactAnalysis",
    "spdxId": "urn:spdx.dev:srac-ex10-system-impact-analysis",
    "name": "System impact analysis for REG-2026-014",
    "functionalsafety_impactAnalysisStatus": "inProgress",
    "functionalsafety_impactLevel": "safetyImpact",
    "functionalsafety_impactedElement": ["urn:spdx.dev:req-sbom-safety-trace-v1", "urn:spdx.dev:safety-case-index"],
    "functionalsafety_removedElement": ["urn:spdx.dev:req-sbom-safety-trace-v1"],
    "functionalsafety_addedElement": ["urn:spdx.dev:req-sbom-safety-trace-v2", "urn:spdx.dev:verification-regulatory-traceability"],
    "rationale": "The bulletin requires an updated safety-traceability requirement and a review of the safety case index."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex10-amended-by",
    "relationshipType": "amendedBy",
    "from": "urn:spdx.dev:req-sbom-safety-trace-v1",
    "to": ["urn:spdx.dev:req-sbom-safety-trace-v2"]
  },
  {
    "type": "functionalsafety_RequirementVerification",
    "spdxId": "urn:spdx.dev:srac-ex10-verification",
    "functionalsafety_verificationMethod": ["assessment"],
    "rationale": "Assess current safety traceability against the new regulatory bulletin."
  },
  {
    "type": "Relationship",
    "spdxId": "urn:spdx.dev:srac-ex10-verified-by",
    "relationshipType": "verifiedBy",
    "from": "urn:spdx.dev:req-sbom-safety-trace-v1",
    "to": ["urn:spdx.dev:srac-ex10-verification"]
  },
  {
    "type": "functionalsafety_EvaluationResult",
    "spdxId": "urn:spdx.dev:srac-ex10-evaluation",
    "functionalsafety_evaluation": "fail",
    "functionalsafety_evaluationBasedOn": "urn:spdx.dev:srac-ex10-verification",
    "rationale": "The current safety case does not yet include the bulletin-required traceability expectation."
  },
  {
    "type": "functionalsafety_EvidenceRelationship",
    "spdxId": "urn:spdx.dev:srac-ex10-evidence",
    "relationshipType": "hasEvidence",
    "from": "urn:spdx.dev:srac-ex10-evaluation",
    "to": ["urn:spdx.dev:regulatory-bulletin-REG-2026-014"],
    "functionalsafety_evidenceCategory": ["report"]
  }
]
```
