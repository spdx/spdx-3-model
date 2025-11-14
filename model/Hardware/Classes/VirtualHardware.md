SPDX-License-Identifier: Community-Spec-1.0

# VirtualHardware

## Summary

Class that describes an instance of VirtualHardware.

## Description

A VirtualHardware is a distinct article related to simulation or emulation hardware.
This is used to assist in recording "Digital Twinning".

An FPGA simulation of hardware is a VirtualHardware.
Virtual hardware requires instantiation involving specific hardware and software.

## Metadata

- name: VirtualHardware
- SubclassOf: Hardware
- Instantiability: Concrete

## Properties

- virtualHardwareModel
  - type: VirtualHardwareModelType
  - minCount: 0
  - maxCount: 1
