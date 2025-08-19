SPDX-License-Identifier: Community-Spec-1.0
# hasRAG

## Summary
Indicates whether Retrieval-Augmented Generation (RAG) is used in constructing the prompt provided to the model.

## Description
When preparing a prompt for input to an LLM, it may be authored entirely by the user or automatically augmented with retrieved external content (e.g., from knowledge bases, APIs, or databases). This field specifies if RAG is employed during prompt construction. 
Allowed Values:
- Yes: The prompt includes externally retrieved content.
- No: The prompt is written directly without retrieval augmentation.
- NOASSERTION: No statement is made regarding the use of RAG.

## Metadata
- name: hasRAG
- Nature: ObjectProperty
- Range: /Core/PresenceType
