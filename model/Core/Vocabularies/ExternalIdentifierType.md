SPDX-License-Identifier: Community-Spec-1.0

# ExternalIdentifierType

## Summary

Specifies the type of an external identifier.

## Description

ExternalIdentifierType specifies the type of an external identifier.

## Metadata

- name: ExternalIdentifierType

## Entries

- cpe22: [Common Platform Enumeration Specification 2.2](https://cpe.mitre.org/files/cpe-specification_2.2.pdf)
- cpe23: [Common Platform Enumeration: Naming Specification Version 2.3](https://csrc.nist.gov/publications/detail/nistir/7695/final)
- cve: Common Vulnerabilities and Exposures identifiers, an identifier for a specific software flaw defined within the official CVE Dictionary and that conforms to the [CVE specification](https://csrc.nist.gov/glossary/term/cve_id).
- email: Email address, as defined in [RFC 3696](https://datatracker.ietf.org/doc/rfc3696/) Section 3.
- gitoid: [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid), stands for [Git Object ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects). A gitoid of type blob is a unique hash of a binary artifact. A gitoid may represent either an [Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types) for the software artifact or an [Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier) for the software artifact's associated [Artifact Input Manifest](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-input-manifest); this ambiguity exists because the Artifact Input Manifest is itself an artifact, and the gitoid of that artifact is its valid identifier. Gitoids calculated on software artifacts (Snippet, File, or Package Elements) should be recorded in the SPDX 3.0 SoftwareArtifact's contentIdentifier property. Gitoids calculated on the Artifact Input Manifest (Input Manifest Identifier) should be recorded in the SPDX 3.0 Element's externalIdentifier property. See [OmniBOR Specification](https://github.com/omnibor/spec/), a minimalistic specification for describing software [Artifact Dependency Graphs](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg).
- other: Used when the type does not match any of the other options.
- packageUrl: Package URL, as defined in the corresponding [Annex](../../../annexes/pkg-url-specification.md) of this document.
- securityOther: Used when there is a security related identifier of unspecified type.
- swhid: SoftWare Hash IDentifier, a persistent intrinsic identifier for digital artifacts, such as files, trees (also known as directories or folders), commits, and other objects typically found in version control systems. The format of the identifiers is defined in the [SWHID specification](https://www.swhid.org/specification/v1.1/4.Syntax) (ISO/IEC DIS 18670). They typically look like `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`.
- swid: Concise Software Identification (CoSWID) tag, as defined in [RFC 9393](https://datatracker.ietf.org/doc/rfc9393/) Section 2.3.
- urlScheme: [Uniform Resource Identifier (URI) Schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). The scheme used in order to locate a resource.

## Summary @zh-Hans

指定`ExternalIdentifier`的类型。

## Description @zh-Hans

`ExternalIdentifierType`指定`ExternalIdentifier`的类型。

## Entries @zh-Hans

- cpe22: [通用平台枚举规范 第2.2版](https://cpe.mitre.org/files/cpe-specification_2.2.pdf)
- cpe23: [通用平台枚举：命名规范 第2.3版](https://csrc.nist.gov/publications/detail/nistir/7695/final)
- cve: 公共漏洞和暴露标识符，是在官方CVE词典中定义的特定软件缺陷的标识符，符合[CVE规范](https://csrc.nist.gov/glossary/term/cve_id)。
- email: 电子邮件地址，如[RFC 3696](https://datatracker.ietf.org/doc/rfc3986/)第3节中定义。
- gitoid: [Gitoid](https://www.iana.org/assignments/uri-schemes/prov/gitoid)，代表[Git对象ID](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)。类型为blob的`gitoid`是二进制工件的唯一哈希值。`gitoid`可以表示软件工件的[Artifact Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-identifier-types)，或者其关联的[Input Manifest Identifier](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#input-manifest-identifier)。由于Artifact Input Manifest本身就是一个工件，其`gitoid`是其有效标识符，这导致了歧义。在软件工件（代码片段、文件或包元素）上计算的`gitoid`应记录在SPDX 3.0 `SoftwareArtifact`的`contentIdentifier`属性中。在Artifact Input Manifest上计算的`gitoid`应记录在SPDX 3.0 `Element`的`externalIdentifier`属性中。详见[OmniBOR规范](https://github.com/omnibor/spec/)，这是用于描述软件[工件依赖图](https://github.com/omnibor/spec/blob/eb1ee5c961c16215eb8709b2975d193a2007a35d/spec/SPEC.md#artifact-dependency-graph-adg)的极简规范。
- other: 用于类型与其他选项不匹配的情况。
- packageUrl: 包URL，如本规范相应[附件](../../../annexes/pkg-url-specification.md)中定义。
- securityOther: 用于存在未指定类型的安全相关标识符的情况。
- swhid: 软件哈希标识符（SoftWare Hash IDentifier），用于数字工件（如文件、目录、提交和版本控制系统中常见的其他对象）的持久性内在标识符。标识符的格式定义在[SWHID规范](https://www.swhid.org/specification/v1.1/4.Syntax)（ISO/IEC DIS 18670）中。通常格式为`swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`。
- swid: 简洁软件标识（Concise Software Identification， CoSWID）标签，如[RFC 9393](https://datatracker.ietf.org/doc/rfc9393/)第2.3节中定义。
- urlScheme: [统一资源标识符（URI）方案](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml)。用于定位资源的方案。
