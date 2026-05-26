SPDX-License-Identifier: Community-Spec-1.0

# agentType

## Summary

Indicates the functional capability type of the AI agent.

## Description

Specifies the primary functional type of an AI agent, that is, the kind of
work it performs or the mechanism by which it acts.

Common values include:

- `codeAgent`: Generates and executes code (e.g., Python) as its primary
  action mechanism, rather than emitting structured tool-call blobs.
- `toolCallingAgent`: Invokes tools by emitting structured calls (e.g., JSON)
  that are parsed and dispatched by the framework.
- `retrievalAgent`: Retrieves and synthesizes information from knowledge bases
  or document corpora using Retrieval-Augmented Generation (RAG) patterns.
- `webSearchAgent`: Queries external search engines or web APIs to gather
  up-to-date information from the internet.
- `browserAgent`: Navigates and interacts with live web pages by driving a
  headless browser, optionally using vision capabilities to interpret rendered
  content.
- `visionAgent`: Processes and reasons over visual inputs using a
  Vision-Language Model (VLM) as its core perception component.

An agent may declare multiple values when it combines capabilities
(e.g., a `codeAgent` that also acts as a `webSearchAgent`).

## Metadata

- name: agentType
- Nature: DataProperty
- Range: xsd:string
