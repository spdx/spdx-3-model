SPDX-License-Identifier: Community-Spec-1.0

# Threat

## Summary

A threat is the potential of a negative circumstance or event.

## Description

A threat is a concept of a potential danger or origin of damage.

In security, threats are used to describe scenarios where an adversary actor attempts to compromise a system and exploit
protected resources.

In SPDX a Threat element is linked to different other elements to describe the Threat.
As such the Threat is expressed by other existing concepts such as:

* Weaknesses,
* Attack Patterns,
* Attack Techniques,
* Attack Procedures,
* Attack Paths.

A Threat may also be expressed by a need to protect. I.e. a threat can be inversely described by concepts intending to
establish protection from a threat.

SPDX explicitly differentiates Threats from Threat Actors or Threat Agents. A Threat is regarded permanent. It never
goes away. A Threat Actor anticipates to exploit a Threat in order to cause an impact on the system or its users.

Based on a Threat regarded as an impact potential, Risks can be concluded. A risk is the evaluation of the Threat in
the context of a selected and concrete Asset. This implies that one Threat can be evaluated to multiple Risks with
different impact and likelihood depending on the target asset.

E.g. the loss of confidential data (Threat) is evaluated as critical risk on the database storing secrets, while the
Risk is moderate on the database storing audit logs (with given policies controlling the allowed content).

## Metadata

- name: Threat
- SubclassOf: /Core/Element
- Instantiability: Concrete

## Properties

- context
  - type: String
  - minCount: 1
  - maxCount: 1
- genericImpactAssessment
  - type: Assessment
  - minCount: 0
