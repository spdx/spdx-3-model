SPDX-License-Identifier: Community-Spec-1.0

# autonomyType

## Summary

**DEPRECATED in SPDX 3.1.**
Use [/Core/isoAutomationLevel](../../Core/Properties/isoAutomationLevel.md)
instead.

Indicates whether the system can perform a decision or action without human
involvement or guidance.

## Description

**NOTE:**
This property is deprecated and only included for backward compatibility.
New documents should use
[/Core/isoAutomationLevel](../../Core/Properties/isoAutomationLevel.md)
instead.

Indicates if the system is fully automated or a human is involved in any of the
decisions of the AI system.

- yes: Indicates that the system is fully automated.
- no: Indicates that a human is involved in any of the decisions of the AI
  system.
- noAssertion: Makes no assertion about the autonomy.

## Metadata

- name: autonomyType
- Nature: ObjectProperty
- Range: /Core/PresenceType
