SPDX-License-Identifier: Community-Spec-1.0

# intendedUse

## Summary

**DEPRECATED in SPDX 3.1.**
Use [/Core/intendedUse](../../Core/Properties/intendedUse.md) instead.

The intended use of a given dataset.

## Description

**NOTE:**
This property is deprecated and only included for backward compatibility.
New documents should use
[/Core/intendedUse](../../Core/Properties/intendedUse.md)
instead.

A free-form text that describes what the given dataset should be used for.

Some datasets are collected to be used only for particular purposes.

For example, medical data collected from a specific demography should only be applicable
for training machine learning models to make predictions for that demography.
In such a case, the intendedUse field would capture this information.
Similarly, if a dataset is collected for building a facial recognition model,
the intendedUse field would specify that.

## Metadata

- name: intendedUse
- Nature: DataProperty
- Range: xsd:string
