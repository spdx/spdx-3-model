SPDX-License-Identifier: Community-Spec-1.0

# intendedUse

## Summary

Describes what the given dataset should be used for.

## Description

A free-form text that describes what the given dataset should be used for.

Some datasets are collected to be used only for particular purposes.

For example, medical data collected from a specific demography might only be applicable
for training machine learning models to make predictions for that demography.
In such a case, the intendedUse field would capture this information.
Similarly, if a dataset is collected for building a facial recognition model,
the intendedUse field would specify that.

## Metadata

- name: intendedUse
- Nature: DataProperty
- Range: xsd:string
