SPDX-License-Identifier: Community-Spec-1.0

# agentMemoryStore

## Summary

Indicates whether the AI agent uses persistent memory and, if so, where that memory is stored (e.g., file path, database/Vector DB URI, object store, or other addressable location).

## Description

Records a reference (URI or file path) to the storage used by the agent to retain information across steps/sessions (e.g., episodic logs, semantic embeddings, user/profile notes, tool interaction history). 
If the agent does not use persistent memory, set the value to NONE. If the presence or location of memory cannot be determined, set to NOASSERTION. 
For multiple memory backends, repeat this property once per backend.


## Metadata
- name: agentMemoryStore
-  Nature: DataProperty
-  Range: xsd:anyURI
