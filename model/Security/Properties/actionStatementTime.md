SPDX-License-Identifier: Community-Spec-1.0

# actionStatementTime

## Summary

Records the time when a recommended action was communicated in a VEX statement
to mitigate a vulnerability.

## Description

When a VEX statement communicates an affected status, the author shall
include an action statement with a recommended action to help mitigate the
vulnerability's impact. The actionStatementTime property records the time
when the action statement was first communicated.

## Metadata

- name: actionStatementTime
- Nature: DataProperty
- Range: /Core/DateTime

## Summary @zh-Hans

记录在VEX语句中传达的缓解漏洞建议措施的时间。

## Description @zh-Hans

当VEX语句传达已受影响（affected）状态时，作者必须包含一个措施语句，提供建议措施帮助减轻漏洞影响。`actionStatementTime`属性记录措施语句首次传达的时间。
