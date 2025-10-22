SPDX-License-Identifier: Community-Spec-1.0

# DatasetAvailabilityType

## Summary

Availability of dataset.

## Description

Describes the possible types of availability of a dataset, indicating whether
the dataset can be directly downloaded, can be assembled using a script for
scraping the data, is only available after a clickthrough or a registration
form.

## Metadata

- name: DatasetAvailabilityType

## Entries

- clickthrough: Dataset is not publicly available and can only be accessed after affirmatively accepting terms on a clickthrough webpage.
- directDownload: Dataset is publicly available and can be downloaded directly.
- query: Dataset is publicly available, but not all at once, and can only be accessed through queries which return parts of the dataset.
- registration: Dataset is not publicly available and an email registration is required before accessing the dataset, although without an affirmative acceptance of terms.
- scrapingScript: Dataset provider is not making available the underlying data and the dataset shall be reassembled, typically using the provided script for scraping the data.

## Summary @zh-Hans

数据集的可用性。

## Description @zh-Hans

描述数据集可能的可用性类型，指示数据集是否可以直接下载、可以使用脚本爬取数据后组装，或者仅在点击进入或填写注册表单后才可用。

## Entries @zh-Hans

- clickthrough: 数据集不公开可用，只能在点击进入网页并确认接受条款后访问。
- directDownload: 数据集公开可用，可以直接下载。
- query: 数据集公开可用，但不能一次性获取，只能通过查询访问返回数据集的部分内容。
- registration: 数据集不公开可用，不需要确认接受条款但需要进行电子邮件注册方可访问数据集。
- scrapingScript: 数据集提供者没有提供基础数据，必须重新组装数据集，通常使用提供的爬虫脚本抓取数据。
