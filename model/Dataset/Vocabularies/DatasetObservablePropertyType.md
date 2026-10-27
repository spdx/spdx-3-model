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

An observation of one of these entries covers all the content of its subject.
When the size of each modality of a dataset is needed (for example, the
duration of its audio and the duration of its video), the content of each
modality should be described by its own `DatasetPackage`, with its own
observations, and the whole dataset should be linked to each of them using
a `contains` relationship.

`contentDuration` specializes the QUDT quantity kind
<http://qudt.org/vocab/quantitykind/Time>, and its unit shall be a unit of
time.
The other entries are counts, and specialize the QUDT quantity kind
<http://qudt.org/vocab/quantitykind/Count>; their unit shall be applicable
to it (for example, <http://qudt.org/vocab/unit/COUNT>).

<!--
TODO: When spec-parser supports vocabulary entry attributes, add back:
- in Metadata: `- entryType: http://qudt.org/schema/qudt/QuantityKind`
  (emitted as rdf:type of each entry);
- under each entry: `  - broader: <IRI or /Namespace/Vocabulary/entry>`
  (emitted as skos:broader), using the quantity kinds listed above.
Removed from PR #1246 because spec-parser main rejects them.
-->

## Metadata

- name: DatasetObservablePropertyType

## Entries

- characterCount: Number of characters; Unicode code points, unless the observation procedure states otherwise.
- contentDuration: Playback duration of time-based content, such as audio or video.
- imageCount: Number of still pictures, such as photographs, illustrations, or drawings; not container images or disk images, and not frames of a video.
- lineCount: Number of lines, as delimited by the procedure identified in the observation.
- recordCount: Number of records, rows, or instances.
- tokenCount: Number of tokens, as produced by the tokenizer identified in the observation.
- wordCount: Number of words, as segmented by the procedure identified in the observation.
