SPDX-License-Identifier: Community-Spec-1.0

# PackageVerificationCode

## Summary

An SPDX version 2.X compatible verification method for software packages.

## Description

This verification method is provided for compatibility with SPDX 2.X.

This verification method provides an independently reproducible mechanism identifying specific contents of a package based on the actual files (except the SPDX document itself, if it is included in the package) that make up each package and that correlates to the data in this SPDX document. 
This identifier enables a recipient to determine if any file in the original package (that the analysis was done on) has been changed and permits inclusion of an SPDX document as part of a package.

Algorithm:

verificationcode = 0

filelist = templist = ""

for all files in the package {

    if file is an "excludes" file, skip it /* exclude SPDX analysis file(s) */

        append templist with "SHA1(file)/n"
        
    }
    
sort templist in ascending order by SHA1 value

filelist = templist with "/n"s removed. /* ordered sequence of SHA1 values with no separators */

verificationcode = SHA1(filelist)

Where SHA1(file) applies a SHA1 algorithm on the contents of file and returns the result in lowercase hexadecimal digits.

Required sort order: '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f' (ASCII order)

## Metadata

- name: PackageVerificationCode
- SubclassOf: /Core/IntegrityMethod

## Properties

- /Core/hashValue
  - type: xsd:string
  - minCount: 1
  - maxCount: 1
- packageVerificationCodeExcludedFile
  - type: xsd:string
