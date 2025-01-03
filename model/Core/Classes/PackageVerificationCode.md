SPDX-License-Identifier: Community-Spec-1.0

# PackageVerificationCode

## Summary

An SPDX version 2.X compatible verification method for software packages.

## Description

This verification method is provided for compatibility with SPDX 2.X.

Use of this verification code method is discouraged except for scenarios where the `contentIdentifier` property on `Artifact` can not be used.

This verification method provides an independently reproducible mechanism identifying specific contents of a package based on the actual files (except the SPDX document itself, if it is included in the package) that make up each package and that correlates to the data in this SPDX document.

This identifier enables a recipient to determine if any file in the original package (that the analysis was done on) has been changed and permits inclusion of an SPDX document as part of a package.

Algorithm:

    templist = ""

    for all files in the package {
        if file is a packageVerificationCodeExcludedFile
            skip it  /* exclude SPDX analysis file */
        else
            append "algorithm(file)/n" to templist
    }

    sort templist in ascending order by value
    
    /* remove separators from ordered sequence */
    valueslist = remove "/n"s from templist
     
    if valueslist is empty
       hashValue = 0
    else
       hashValue = algorithm(valueslist)

where `algorithm(string)` applies a hash algorithm on a string and returns the result in lowercase hexadecimal digits.

Required sort order: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' (ASCII order)

## Metadata

- name: PackageVerificationCode
- SubclassOf: /Core/IntegrityMethod

## Properties

- algorithm
  - type: HashAlgorithm
  - minCount: 1
  - maxCount: 1
- hashValue
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- packageVerificationCodeExcludedFile
  - type: xsd:string

## Summary @zh-Hans

SPDX 2.X版本兼容的软件包校验方法。

## Description @zh-Hans

此验证方法是为兼容SPDX 2.X而提供的。

除非`Artifact`中的`contentIdentifier`属性无法使用，否则不建议使用此校验码方法。

此校验方法提供了一种独立可复现的机制，根据构成每个软件包且与此SPDX文档中的数据相关联的实际文件（如果SPDX文档包含在软件包中，则排除SPDX文档本身）来识别软件包的特定内容。

此标识符使接收者能够确定原始软件包（进行分析的软件包）中的任何文件是否已更改，并允许将SPDX文档作为软件包的一部分包含在内。

算法：

    templist = ""

    对于软件包中的所有文件 {
        如果文件是 packageVerificationCodeExcludedFile
            跳过文件  /* 排除 SPDX 分析文件 */
        否则
            将"algorithm(file)/n"追加到templist
    }

    按值升序排列templist

    /* 从有序序列中删除分隔符 */
    valueslist = 从templist中删除"/n"

    如果valueslist为空
       hashValue = 0
    否则
       hashValue = algorithm(valueslist)

其中`algorithm(string)`将哈希算法应用于字符串，并以小写十六进制数字返回结果。

所需排序顺序：'0'，'1'，'2'，'3'，'4'，'5'，'6'，'7'，'8'，'9'，'a'，'b'，'c'，'d'，'e'，'f'（ASCII顺序）
