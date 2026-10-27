SPDX-License-Identifier: Community-Spec-1.0

# DatasetObservablePropertyType

## Summary

Recommended observable properties for observations of the size of
the content of a dataset or other artifact.

## Description

The `DatasetObservablePropertyType` vocabulary provides identifiers for
measures of the size of content, other than its size in bytes.
The size in bytes shall be recorded using the `/Software/byteSize` property
instead of a `/Core/Observation`.

The IRI of an entry of this vocabulary may be used as the value of
the `/Core/observedProperty` property of a `/Core/Observation`.
These entries may be used for any `/Core/Artifact`, including
`/Software/File` and `/Software/Package`, not only for `DatasetPackage`.

Counts of tokens, words, lines, and characters depend on the procedure
used to produce them (for example, the tokenizer and its version,
or the word segmentation method for a given language).
An observation using one of these entries should identify the procedure
using the `/Core/observationProcedure` property or a `usesTool` relationship,
since counts produced by different procedures are not comparable.

Each entry is a QUDT quantity kind that is a specialization (`skos:broader`)
of a QUDT quantity kind.
For entries that are counts, the unit shall be applicable to the QUDT
quantity kind `Count` (for example, <http://qudt.org/vocab/unit/COUNT>).

## Metadata

- name: DatasetObservablePropertyType
- entryType: http://qudt.org/schema/qudt/QuantityKind

## Entries

- characterCount: Number of characters; Unicode code points, unless the observation procedure states otherwise.
  - broader: http://qudt.org/vocab/quantitykind/Count
- contentDuration: Playback duration of time-based content, such as audio or video.
  - broader: http://qudt.org/vocab/quantitykind/Time
- imageCount: Number of distinct images.
  - broader: http://qudt.org/vocab/quantitykind/Count
- lineCount: Number of lines, as delimited by the procedure identified in the observation.
  - broader: http://qudt.org/vocab/quantitykind/Count
- recordCount: Number of records, rows, or instances.
  - broader: http://qudt.org/vocab/quantitykind/Count
- tokenCount: Number of tokens, as produced by the tokenizer identified in the observation.
  - broader: http://qudt.org/vocab/quantitykind/Count
- wordCount: Number of words, as segmented by the procedure identified in the observation.
  - broader: http://qudt.org/vocab/quantitykind/Count
