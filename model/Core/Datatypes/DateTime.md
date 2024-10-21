SPDX-License-Identifier: Community-Spec-1.0

# DateTime

## Summary

A string representing a specific date and time.

## Description

A DateTime is a string representation of a specific date and time.

It has resolution of seconds and is always expressed in UTC time zone.

The specific format is one of the most commonly used ISO-8601 formats.

## Metadata

- name: DateTime
- SubclassOf: xsd:dateTimeStamp

## Format

- pattern: ^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$

## Summary @jp

特定の日付と時刻を表す文字列。  

## Description @jp

DateTime は、特定の日付と時刻を表す文字列です。  

秒単位の解像度を持ち、常にUTCタイムゾーンで表されます。  

最も一般的に使用されている形式の1つである、ISO-8601 フォーマットで記述します。  
