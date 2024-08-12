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

    templist = empty list of strings

    for all files in the package {
        if file is a packageVerificationCodeExcludedFile
            skip it  /* exclude SPDX analysis file */
        else
            append "algorithm(file)/n" to templist
    }

    sort templist in ascending order by value
    
    valueslist = remove "/n"s from templist  /* ordered sequence with no separators */
     
    if valuelist is empty
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
