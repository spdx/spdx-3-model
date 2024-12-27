SPDX-License-Identifier: Community-Spec-1.0

# hyperparameter

## Summary

Records a hyperparameter used to build the AI model contained in the AI
package.

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

## Summary @zh-Hans

记录用于构建AI软件包中AI模型的超参数。

## Description @zh-Hans

记录超参数值。

超参数是在训练过程之前定义的设置，用于控制学习算法的行为。它们与模型参数不同，模型参数是在训练期间从数据中学习得来的。开发者通常手动设置超参数，或者通过超参数调优（也称为试错）过程来设定。

超参数的例子包括学习率、批量大小和神经网络中的层数。
