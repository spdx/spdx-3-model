SPDX-License-Identifier: Community-Spec-1.0

# Location

## Summary

Location is used to define the location, address or coordinates of a place.

## Description

Location is used to define the location, address or coordinates of a place.  Location data may include latitude and longitude (for geographical locations), IP addresses for network locations, MAC addresses for computer networks, or other identifiers that specify where something exists within a system. There is often a need to provide context about where each one is located in relation to other things around it (e.g., which city, country).

## Metadata

- name: Location
- SubclassOf: Element
- Instantiability: Abstract

## Properties

- locationTime
  - type: DateTime
  - minCount: 0
  - maxCount: 1
