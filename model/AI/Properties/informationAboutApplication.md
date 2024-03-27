SPDX-License-Identifier: Community-Spec-1.0

# informationAboutApplication

## Summary

Provides relevant information about the AI software, not including the model description.

## Description

A free-form text description of how the AI model is used within the software.
It should include any relevant information, such as pre-processing steps,
third-party APIs, and other pertinent details.

It can also include:

- Functionality provided by the AI model within the software application,
  including: any specific tasks or decisions it is designed to perform;
  any pre-processing steps that are applied to the input data before it is
  fed into the AI model for inference, such as data cleaning, normalization,
  or feature extraction;
  and any third-party APIs or services that are used in conjunction with
  the AI model, such as data sources, cloud services, or other AI models.
- Description of any dependencies or requirements needed to run the AI model
  within the software application, including: specific hardware,
  software libraries, and operating systems.

## Metadata

- name: informationAboutApplication
- Nature: DataProperty
- Range: xsd:string
