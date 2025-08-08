SPDX-License-Identifier: Community-Spec-1.0

# ApplicationType

## Summary

The ApplicationType defines a list of known distribution/deployment contexts as central reference.

## Description

The field can be used to document the type of application for the business context.

## Metadata

- name: ApplicationType

## Entries

- embeddedSystemAndOrApplicationsSoftwareInMassProduction: BT01 Embedded system and or application software in mass production.
- embeddedApplicationSoftwareInMassProductionWithFOTA: BT02 Embedded application software in mass production with FOTA.
- embeddedSystemSoftwareOnSmartDevicesWithFOTA: BT03 Embedded system software on smart devices with FOTA.
- embeddedApplicationSoftwareOnSmartDevicesWithFOTA: BT04 Embedded application software on smart devices with FOTA.
- clientApplication: BT05 Client Application.
- webApplication: BT06 Web Application - The Software is typically provided on a web-server and is interacting with the user via a browser. 
- serverBasedSystemSoftware: BT07 Server-based system software.
- serverBasedApplicationSoftware: BT08 Server-based application software.
- cloudServiceOnPremise: BT09 Cloud Service on premise in private cloud.
- cloudServiceInTheInternet: BT10 Cloud Service in the internet.
- openSourceDevelopmentService: BT11 Open Source Development Services.
- sourceCodeSharing: BT12 Source Code Sharing.
