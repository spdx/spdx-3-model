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
* the SPDX data creator has attempted to but cannot reach a reasonable
  objective determination;
* the SPDX data creator has made no attempt to determine this field; or
* the SPDX data creator has intentionally provided no information (no
  meaning should be implied by doing so).

If a copyrightText is present, but consists of solely an empty string or a
string with no substantive content (e.g., a string that contains only
whitespace), then this should be interpreted as equivalent to a "NOASSERTION"
value as described above.

## Metadata

- name: copyrightText
- Nature: DataProperty
- Range: xsd:string
