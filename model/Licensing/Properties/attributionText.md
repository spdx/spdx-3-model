SPDX-License-Identifier: Community-Spec-1.0

# attributionText

## Summary

An attributionText provides a place for the SPDX data creator to record
acknowledgement text for a software Package, File or Snippet.

## Description

An attributionText for a software Package, File or Snippet provides a consumer
of SPDX data with acknowledgement content, to assist redistributors of the
Package, File or Snippet with reproducing those acknowledgements.

For example, this field may include a statement that is required by a
particular license to be reproduced in end-user documentation, advertising
materials, or another form.

This field may describe where, or in which contexts, the acknowledgements
need to be reproduced, but it is not required to do so. The SPDX data creator
may also explain elsewhere (such as in a licenseComment field) how they intend
for data in this field to be used.

An attributionText is is not meant to include the software Package, File or
Snippet’s actual complete license text (see concludedLicense to identify the
corresponding license).

## Metadata

- name: attributionText
- Nature: DataProperty
- Range: xsd:string
