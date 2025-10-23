SPDX-License-Identifier: Community-Spec-1.0

# vectorString

## Summary

Specifies the CVSS vector string for a vulnerability.

## Description

Specifies any combination of the CVSS Base, Temporal, Threat, Environmental,
and/or Supplemental vector string values for a vulnerability.

Supports vectorStrings specified in all CVSS versions.

*Constraints*

String values for the vectorString range shall only include the abbreviated form
of metric names specified in CVSS specifications, e.g.
[Common Vulnerability Scoring System Vector String](https://www.first.org/cvss/v4.0/specification-document#Vector-String).

## Metadata

- name: vectorString
- Nature: DataProperty
- Range: xsd:string

## Summary @zh-Hans

指定漏洞的CVSS向量字符串。

## Description @zh-Hans

指定漏洞的CVSS基本、时态、威胁、环境和/或补充向量字符串值的任意组合。

支持所有CVSS版本中指定的`vectorString`。

*约束条件*

`vectorString`范围内的字符串值只能包含CVSS规范中，例如[通用漏洞评分系统（CVSS）矢量字符串](https://www.first.org/cvss/v4.0/specification-document#Vector-String)，指定的度量名称的缩写形式，。
