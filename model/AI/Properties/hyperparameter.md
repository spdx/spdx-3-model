SPDX-License-Identifier: Community-Spec-1.0

# hyperparameter

## Summary

Records a hyperparameter used to build the AI model contained in the AI package.

## Description

Records a hyperparameter value.

Hyperparameters are settings defined before the training process that control
the learning algorithm's behavior. They differ from model parameters,
which are learned from the data during training. Developers typically set
hyperparameters manually or through a process of hyperparameter tuning
(also known as trial and error).

Examples of hyperparameters include learning rate, batch size, and the number
of layers in a neural network.

## Metadata

- name: hyperparameter
- Nature: ObjectProperty
- Range: /Core/DictionaryEntry
