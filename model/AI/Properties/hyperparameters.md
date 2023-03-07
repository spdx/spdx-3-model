SPDX-License-Identifier: Community-Spec-1.0

# hyperparameters

## Summary

Field captures the record of the hyperparameters used to build the AI model contained in the AI package

## Description

The field records all or the important hyperparameters of each model. The hyperparmeters are listed as hyperparameter1_name:hyperparameter1_value, hyperparameter2_name: hyperparameter2_value etc. If there are multiple models, the hyperparameters of each model are listed in a separate line. 

## Metadata

- name: hyperparameters
- Nature: DataProperty
- Range: xsd:string
