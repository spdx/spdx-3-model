SPDX-License-Identifier: Community-Spec-1.0

# AutonomyLevel

## Summary

Defines the degrees of automation a system possesses.

## Description

AutonomyLevel is an enumeration that categorizes a system's level of automation.

Systems categorized with autonomy levels 0-5 are heteronomous. This means that while they may be fully automated, their goals and objectives are set by external entities, typically humans.

A system with autonomy level 6 is autonomous. Such a system can independently define and pursue its own goals.

## Metadata

- name: AutonomyLevel

## Entries

- level0: No automation. The operator fully controls the system.
- level1: Assistance. The system provides some mechanical guidance or assistance during a task while the operator has continuous control of the system.
- level2: Partial automation or deterministic task automation. Some sub-functions of the system are fully automated while the system remains under control of an external agent. The operator has discrete control of the system.
- level3: Conditional automation or strategic task automation. A system generates task strategies but relies on the human to select from among different strategies or to approve an autonomously selected strategy.
- level4: High automation. The system performs parts of its mission without external intervention.
- level5: Full automation. The system is capable of performing its entire mission without external intervention.
- level6: Autonomy. The system is capable of modifying its operation domain or its goals without external intervention, control, or oversight.
