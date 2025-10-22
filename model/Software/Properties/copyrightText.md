SPDX-License-Identifier: Community-Spec-1.0

# copyrightText

## Summary

Identifies the text of one or more copyright notices for a software Package,
File or Snippet, if any.

## Description

A copyrightText consists of the text(s) of the copyright notice(s) found
for a software Package, File or Snippet, if any.

If a copyrightText contains text, then it may contain any text related to
one or more copyright notices (even if not complete) for that software
Package, File or Snippet.

If a copyrightText has a "NONE" value, this indicates that the software
Package, File or Snippet contains no copyright notice whatsoever.

If a copyrightText has a "NOASSERTION" value, this indicates that one of the
following applies:

- the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
- the SPDX data creator has made no attempt to determine this field; or
- the SPDX data creator has intentionally provided no information (no
  meaning shall be implied by doing so).

If a copyrightText is present, but consists of solely an empty string or a
string with no substantive content (e.g., a string that contains only
whitespace), then this shall be interpreted as equivalent to a "NOASSERTION"
value as described above.

## Metadata

- name: copyrightText
- Nature: DataProperty
- Range: xsd:string

## Summary @zh-Hans

标识软件包、文件或代码片段的一个或多个版权声明的文本（如果有的话）。

## Description @zh-Hans

版权文本（ `copyrightText`）由软件包、文件或代码片段中找到的一个或多个版权声明的文本组成（如果有的话）。如果版权文本包含文本，则可能包含与该软件包、文件或代码片段的一个或多个版权声明相关的任何文本（即使不完整）。

如果版权文本的值为“NONE”，则表示该软件包、文件或代码片段根本不包含任何版权声明。

如果版权文本的值为“NOASSERTION”，则表示以下情况之一适用：

- SPDX数据创建者已尝试但无法达到合理的客观判断；
- SPDX数据创建者没有尝试确定此字段；
- SPDX数据创建者故意没有提供信息（这样做不应推断任何含义）。

如果版权文本存在，但仅由空字符串或没有实质内容的字符串组成（例如，只包含空格的字符串），那么这应该被解释为等同于上述“NOASSERTION”值。
