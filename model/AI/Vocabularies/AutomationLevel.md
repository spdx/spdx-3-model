SPDX-License-Identifier: Community-Spec-1.0

# AutomationLevel

## Summary

Defines the level of automation a system possesses.

## Description

AutomationLevel is an enumeration that categorizes a system's level of
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

A system with automation level 6 is autonomous, capable of independently
defining and pursuing its own goals without external intervention.

## Metadata

- name: AutomationLevel

## Entries

- autonomous: Level 6 - Autonomous. The system is capable of independently modifying its intended domain of use or its goals without external intervention, control, or oversight.
- fullAutomation: Level 5 - Full automation. The system is capable of performing its entire mission without any external intervention, from start to completion.
- highAutomation: Level 4 - High automation. The system performs most of its mission without external intervention, but may require human oversight for exceptional conditions.
- conditionalAutomation: Level 3 - Conditional automation. The system can propose strategies and automatically execute the approved plan, while an external agent remains ready to intervene when necessary.
- partialAutomation: Level 2 - Partial automation. Some sub-functions of the system are fully automated while the overall system remains under the control of an external agent; the system can act on an approved task without requiring continuous direct human control.
- assistiveAutomation: Level 1 - Assistive automation. The system assists a human operator, who retains full decision-making authority and direct control at all times.
- notAutomated: Level 0 - Not automated. No automation. The human operator fully controls the system with no automated decision-making.
