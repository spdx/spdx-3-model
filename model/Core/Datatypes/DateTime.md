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

## Summary @zh-Hans

表示特定日期和时间的字符串。

## Description @zh-Hans

`DateTime`是表示特定日期和时间的字符串。

其精度为秒，并始终以UTC时区表示。

具体格式是最常用的ISO-8601格式之一。
