SPDX-License-Identifier: Community-Spec-1.0

# DatasetType

## Summary

Enumeration of dataset types.

## Description

Describes the different structures of data within a given dataset. A dataset
can have multiple types of data, or even a single type of data but still match
multiple types, for example sensor data could also be timeseries or labeled
image data could also be considered categorical.

## Metadata

- name: DatasetType

## Entries

- audio: Data is audio based, such as a collection of music from the 80s.
- categorical: Data that is classified into a discrete number of categories, such as the eye color of a population of people.
- graph: Data is in the form of a graph where entries are somehow related to each other through edges, such a social network of friends.
- image: Data is a collection of images such as pictures of animals.
- noAssertion: Data type is not known.
- numeric: Data consists only of numeric entries.
- other: Data is of a type not included in this list.
- sensor: Data is recorded from a physical sensor, such as a thermometer reading or biometric device.
- structured: Data is stored in tabular format or retrieved from a relational database.
- syntactic: Data describes the syntax or semantics of a language or text, such as a parse tree used for natural language processing.
- text: Data consists of unstructured text, such as a book, a Wikipedia article (without images), or a transcript.
- timeseries: Data is recorded in an ordered sequence of timestamped entries, such as the price of a stock over the course of a day.
- timestamp: Data is recorded with a timestamp for each entry, but not necessarily ordered or at specific intervals, such as when a taxi ride starts and ends.
- video: Data is video based, such as a collection of movie clips featuring Tom Hanks.
