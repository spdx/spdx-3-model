SPDX-License-Identifier: Community-Spec-1.0

# IsoAutomationLevel

## Summary

Defines the level of automation a system possesses.

## Description

IsoAutomationLevel is an enumeration that categorizes a system's level of
automation, helping to define the roles and responsibilities of both the
human operator and the automated system.

The 7-level enumeration is based on
[ISO/IEC 22989:2022 Artificial intelligence concepts and terminology](https://www.iso.org/standard/74296.html),
aligned with
[SAE J3016_202104 Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles](https://www.sae.org/standards/content/j3016_202104/),
[Levels of Autonomy in Surgical Robotics (LASR)](https://doi.org/10.1038/s41746-024-01102-y),
and
[AutomationLevel in Data Privacy Vocabulary](http://w3id.org/dpv/#AutomationLevel).

Systems categorized with automation levels 0-5 are heteronomous.
This means that while they can be fully automated, their goals and objectives
are set by external entities, typically human operators.

A system with automation level 6 is autonomous, capable of independently define
and pursue its own goals.

## Metadata

- name: IsoAutomationLevel

## Entries

- autonomous: Level 6 - Autonomous. The system is capable of modifying its intended domain of use or its goals without external intervention, control or oversight.
- fullAutomation: Level 5 - Full automation. The system is capable of performing its entire mission without external intervention.
- highAutomation: Level 4 - High automation. The system performs parts of its mission without external intervention.
- conditionalAutomation: Level 3 - Conditional automation. The system can propose strategies and then automatically execute the approved plan, with an external agent being ready to take over when necessary.
- partialAutomation: Level 2 - Partial automation or task automation. Some sub-functions of the system are fully automated while the system remain under control of an external agent. The system can perform actions for an approved task without requiring the agent's continuous direct control.
- assistiveAutomation: Level 1 - Assistive automation. The system assists an operator.
- notAutomated: Level 0 - Not automated. No automation. The operator fully controls the system.
