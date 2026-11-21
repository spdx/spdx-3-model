SPDX-License-Identifier: Community-Spec-1.0

# Modality

## Summary

A controlled vocabulary used to classify the nature of the data channel
(or sensory type) for content or interaction within a system.

## Description

The Modality defines a standardized classification for the distinct data
channels or sensory types through which information is communicated, perceived,
or processed by agents and software.

This vocabulary enables system components to describe the specific modality or
form in which information is exchanged, serving functions such as:

- Human-computer interaction (HCI): Defining the sensory channels for input and
  output.
- Foundation models: Specifying the nature of input data and the expected
  output.
- Data classification: Categorizing data and collections of data based on
  data's inherent form.

## Metadata

- name: Modality

## Entries

- audio: Spoken language and sound (e.g., voice commands, recorded dialog, music, environmental sounds, audio alerts).
- gesturePose: Body movement, hand gestures, facial expressions, or full-body pose estimation.
- hapticTactile: Touch, force, or tactile feedback data (e.g., vibrations, surface pressure, grip data).
- image: Still visual data (e.g., photographs, drawings, diagrams, charts).
- noAssertion: The modality is not known or cannot be reasonably determined, or the creator has made no attempt to determine this field, or the creator has intentionally provided no information (no meaning shall be implied by doing so).
- other: Any other modality not defined in this list.
- text: A sequence of characters intended to convey meaning in a natural human language.
- video: Temporal visual data (sequences of still visual data), which can associated time-synchronized data such as audio tracks or transcriptions.
