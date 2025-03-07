SPDX-License-Identifier: Community-Spec-1.0

# ApplicationType

## Summary

The ApplicationType defines a list of known distribution/deployment contexts
as central reference.

## Description

The field can be used to document the base, temporal, threat, or environmental
severity.

## Metadata

- name: ApplicationType

## Entries

- embeddedSystemAndOrApplicationsSoftwareInMassProduction: BT01 Embedded system and or application software in mass production.
- embeddedApplicationSoftwareInMassProductionWithFOTA: BT02 Embedded application software in mass production with Firmware Over-The-Air.
- embeddedSystemSoftwareOnSmartDevicesWithFOTA: BT03 Embedded system software on smart devices with Firmware Over-The-Air.
- embeddedApplicationSoftwareOnSmartDevicesWithFOTA: BT04 Embedded application software on smart devices with Firmware Over-The-Air.
- clientApplication: BT05 Client application.
- webApplication: BT06 Web application - the software is typically provided on a web-server and is interacting with the user via a browser. 
- serverBasedSystemSoftware: BT07 Server-based system software.
- serverBasedApplicationSoftware: BT08 Server-based application software.
- cloudServiceOnPremise: BT09 Cloud service on premise in private cloud.
- cloudServiceInTheInternet: BT10 Cloud service in the Internet.
- openSourceDevelopmentService: BT11 Open source development services.
- sourceCodeSharing: BT12 Source code sharing.
