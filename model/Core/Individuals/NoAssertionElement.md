SPDX-License-Identifier: Community-Spec-1.0

# NoAssertionElement

## Summary

An Individual Value for Element representing a set of Elements of unknown
identify or cardinality (number).

## Description

NoAssertionElement should be used if

- the SPDX creator has attempted to but cannot reach a reasonable objective
  determination;
- the SPDX creator has made no attempt to determine this field; or
- the SPDX creator has intentionally provided no information (no meaning should
  be implied by doing so).

For example, a Relationship with
`relationshipType`="ancestorOf",
`from`=Element1,
and
`to`=NoAssertionElement
is explicitly expressing that
no assertion is being made about any potential descendants of Element1.

## Metadata

- name: NoAssertionElement
- type: IndividualElement

## Property Values

- name: "NOASSERTION"

## Summary @ja

不明な識別子やカーディナリティ (数) を持つ要素の集合を表す個別の値。  

## Description @ja

NoAssertionElement は、以下の場合に利用されるべきです。  

- SPDX ドキュメントの作成者が、合理的、客観的な判断を試みたが解決できなかった場合  
- SPDX ドキュメントの作成者が、この部分を判断しなかった場合  
- SPDX ドキュメントの作成者が、意図的に情報を提供しなかった場合（その行為に意味を含ませるべきではありません）  

例えば、  
`relationshipType`="ancestorOf"、  
`from`=Element1  
の時に、  
`to`=NoAssertionElement  
という関係は、Element1 が子エレメントを持つかどうかは分からないということを明示的に表しています。  
