SPDX-License-Identifier: Community-Spec-1.0

# Changes in `add-ai-agent-v2` Branch

## New Class: `AI/AIAgent`

**Subclass of:** `/Core/SoftwareAgent`

Represents an AI agent, a software entity that uses artificial intelligence techniques to perceive its environment, reason about its state, and take actions to achieve specified goals. It typically implements a perception-action cycle employing AI models, heuristics, or planning algorithms to guide autonomous or semi-autonomous behavior.

AI agents may be characterized by the modalities through which they perceive input and produce output, the capabilities they provide, the external tools or services they invoke, the memory mechanisms they employ to retain information across interactions, and their degree of automation relative to human oversight.

### Properties on `AIAgent`

#### Native Properties

| Field Name | Type | Required/Optional | Description |
|---|---|---|---|
| `agentCapability` | `xsd:string` | Optional (0..*) | A functional capability the agent can perform |
| `agentCommunicationProtocol` | `/Core/DictionaryEntry` | Optional (0..*) | A standardized communication protocol implemented by the agent for interacting with tools, data sources, or other agents |
| `agentExternalTool` | `/Core/DictionaryEntry` | Optional (0..*) | An external tool or service the agent can invoke |
| `agentMemoryMode` | `AgentMemoryMode` | Optional (0..*) | Memory category or storage mechanism used by the agent |
| `agentPermissionScope` | `xsd:string` | Optional (0..*) | A permission granted to the AI agent |
| `agentTrustLevel` | `AgentTrustLevel` | Optional (0..1) | Degree of external verification applied to the agent's identity, behavioral claims, and declared capabilities |
| `agentType` | `AgentType` | Optional (0..*) | Communication and interaction role of the agent within a multi-agent system |
| `limitation` | `xsd:string` | Optional (0..1) | A known limitation of the AI agent or its underlying model |
| `safetyRiskAssessment` | `SafetyRiskAssessmentType` | Optional (0..1) | Results of general safety risk assessment of the AI system |

#### External Properties Restrictions

| Field Name | Type | Required/Optional | Description |
|---|---|---|---|
| `/Core/isoAutomationLevel` | `/Core/IsoAutomationLevel` | Optional (0..1) | Level of automation relative to human oversight, based on ISO/IEC 22989:2022 |
| `/Software/inputModality` | `/Core/Modality` | Optional (0..*) | Fundamental data or sensory type accepted as input |
| `/Software/outputModality` | `/Core/Modality` | Optional (0..*) | Fundamental data or sensory type produced as output |

### Relationship types used with `AIAgent`

| Relationship | Direction | Description |
|---|---|---|
| `hasPersistentMemory` | `AIAgent` → `Element` | The AIAgent uses the target Element as a persistent or long-term memory store (e.g., a database, vector store, or file system that retains information across sessions or reasoning steps) |
| `invokedBy` | `Element` → `Agent` | The Element was invoked by the target Agent (e.g., a Package is `invokedBy` an AIAgent; an AIAgent is `invokedBy` a Person) |
| `usesTool` | `AIAgent` → `Element` | The AIAgent uses the target Element as a tool to extend its capabilities |
| `usesModel` | `AIAgent` → `/AI/AIPackage` | The AIAgent uses the target AIPackage as its underlying AI model, enabling BOM consumers to trace from an agent to its associated model weights, training data, and safety assessments |

---

## New Properties (AI Profile)

### `agentCapability`
- **Nature:** DataProperty
- **Range:** `xsd:string`
- **Cardinality:** 0..*

A free-form string that identifies a user-facing task ability of the AI agent — what it can accomplish for an integrator or end-user, regardless of the architectural pattern used to fulfill it. Each value should capture one distinct task or goal. This is distinct from `agentType`, which classifies the agent's internal action-execution mechanism.

Use one `agentCapability` entry per distinct ability. Descriptions should be concise and human-readable. External tools or services invoked to fulfill a capability are recorded separately using the `agentExternalTool` property.

**Examples:**

```text
web-search
```

```text
document-summarization: condenses retrieved documents into structured outputs
```

```text
code-execution: runs Python snippets in a sandboxed environment
```

```text
multi-step-reasoning: decomposes complex queries into sub-tasks and plans execution order
```

```text
multi-agent-coordination: delegates sub-tasks to specialized agents and aggregates results
```

---

### `agentExternalTool`
- **Nature:** ObjectProperty
- **Range:** `/Core/DictionaryEntry`
- **Cardinality:** 0..*

Identifies an external tool, API, or service that the AI agent can invoke to perform actions beyond its built-in model. Each `DictionaryEntry` maps a short, human-readable tool identifier (the key) to a URI, package URL, or other reference that locates the tool's definition or specification (the value).

External tools enable agents to retrieve information, transform data, execute operations, or interact with external systems. Examples include: web search APIs, code execution sandboxes, database query interfaces, translation services, and domain-specific utilities.

**Examples:**

| Key | Value |
|---|---|
| `web-search` | `https://serpapi.com/` |
| `code-interpreter` | `pkg:pypi/jupyter-kernel-gateway@2.0.0` |
| `pubmed-query` | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/` |

---

### `agentMemoryMode`
- **Nature:** ObjectProperty
- **Range:** `AgentMemoryMode`
- **Cardinality:** 0..*

Classifies how an AI agent retains and recalls information across interactions or reasoning steps. Multiple values may be declared when an agent employs more than one memory mechanism.

**Values:** see `AI/AgentMemoryMode` vocabulary.

---

### `agentCommunicationProtocol`
- **Nature:** ObjectProperty
- **Range:** `/Core/DictionaryEntry`
- **Cardinality:** 0..*

Specifies the standardized communication protocol(s) that the AI agent implements, enabling consumers, integrators, and automated tooling to determine how the agent can be invoked, composed, or connected within a larger system.

Agent protocols define the rules, formats, and procedures for structured communication between an agent and external entities. Examples of widely adopted agent protocols include: Model Context Protocol (MCP), Agent2Agent (A2A), Agent Network Protocol (ANP), Agent Communication Protocol (AComP), Agent Connect Protocol (AConP), Agent Interaction and Transaction Protocol (AITP), Coral Protocol, and Agora.

Each entry maps a short, human-readable protocol identifier (the key) to the protocol version or a URI pointing to its specification (the value).

**Examples:**

| Key | Value |
|---|---|
| `MCP` | `1.2` |
| `A2A` | `https://github.com/google/A2A` |
| `ANP` | `https://www.agent-network-protocol.com/` |
| `AConP` | `https://spec.acp.agntcy.org/` |

---

### `agentType`
- **Nature:** ObjectProperty
- **Range:** `AgentType`
- **Cardinality:** 0..*

A controlled classification of the structural role an AI agent assumes in terms of how it communicates and interacts with other agents and orchestration systems. Analogous to `typeOfModel` for AI models, it answers "what kind of agent is this?" from an interaction standpoint — not from a capability or task standpoint.

An agent may declare multiple values when it simultaneously holds more than one role (e.g., a worker toward an upstream orchestrator that itself orchestrates a sub-group of specialist agents). Domain-level task abilities are recorded separately using `agentCapability`.

**Values:** see `AI/AgentType` vocabulary.

---

### `agentTrustLevel`
- **Nature:** ObjectProperty
- **Range:** `AgentTrustLevel`
- **Cardinality:** 0..1

Specifies the trust level assigned to an AI agent, reflecting how rigorously its identity and behavior have been verified by external parties. Trust level informs consumers, orchestrators, and access-control systems about the confidence they can place in the agent's declared properties and the scope of resources or operations the agent may be permitted to access.

An agent declares at most one trust level. When no value is present, consumers should treat the agent as unverified.

**Values:** see `AI/AgentTrustLevel` vocabulary.

---

### `agentPermissionScope`
- **Nature:** DataProperty
- **Range:** `xsd:string`
- **Cardinality:** 0..*

A free-form string that identifies a permission granted to the AI agent. Captures the permissions assigned to the agent and their delegation source, enabling consumers to assess what resources or operations the agent is authorized to access.

**Examples:**

```text
read:files
```

```text
execute:code-interpreter
```

```text
write:external-api delegated-by:orchestrator
```

---

### `limitation`
- **Nature:** DataProperty
- **Range:** `xsd:string`
- **Cardinality:** 0..1

A free-form text that captures a known limitation of the AI agent or its underlying model. Note that this is not guaranteed to be exhaustive.

**Examples:**

```text
Poor accuracy for non-English languages
```

```text
Context window limited to 128k tokens; long documents may be truncated
```

---

### `safetyRiskAssessment`
- **Nature:** ObjectProperty
- **Range:** `SafetyRiskAssessmentType`
- **Cardinality:** 0..1

Results of general safety risk assessment of the AI system. Uses categorization according to the EU general risk assessment methodology (Article 20, Regulation (EC) No 765/2008). Note that this categorization differs from the one proposed in the EU AI Act's provisional agreement.

**Values:** see `AI/SafetyRiskAssessmentType` vocabulary.

---

## New Vocabulary: `AI/AgentType`

A controlled vocabulary that classifies the communication and interaction role of an AI agent within a multi-agent system. Analogous to `typeOfModel` for AI models, it answers "what kind of agent is this?" from an interaction standpoint: whether the agent initiates and coordinates work, executes delegated tasks, or participates as a peer. Informed by inter-agent protocol specifications including A2A, ANP, AConP, the Coral Protocol, and Agora, and consistent with the taxonomy in Yang et al. (2025), "A Survey of AI Agent Protocols," arXiv:2504.16736.

An agent may hold more than one role simultaneously.

| Entry | Description |
|---|---|
| `orchestrator` | Initiates and decomposes high-level goals into sub-tasks, delegates those sub-tasks to other agents, and aggregates their results. Controls the overall workflow and is responsible for task assignment and result synthesis. Corresponds to the client agent role in A2A and the coordinator role in the Coral Protocol |
| `worker` | Receives a delegated task from an orchestrator or controller, executes it using its own capabilities and tools, and returns the result. Does not direct other agents in the context of the delegated task. Corresponds to the remote agent role in A2A and the invoked agent role in AConP |
| `peer` | Participates in symmetric, decentralized multi-agent collaboration without a fixed coordinator or worker hierarchy. Any peer may initiate interactions with any other peer; protocols and task assignments are negotiated dynamically. Corresponds to agents-on-the-internet in ANP and networked LLM nodes in Agora |

---

## New Vocabulary: `AI/AgentTrustLevel`

A controlled vocabulary that categorizes the trust level of an AI agent based on the degree of external verification applied to its identity, behavioral claims, and declared capabilities. Informed by the NIST AI Agent Standards Initiative trust framework.

An agent declares at most one trust level.

| Entry | Description |
|---|---|
| `unverified` | Level 0 — The agent has not been reviewed or assessed by any party. No claims about its identity, capabilities, or behavior have been independently examined. Access and operational scope should be maximally restricted |
| `selfDeclared` | Level 1 — Trust is based solely on claims made by the agent's developer or operator. No external review has been conducted. Suitable for low-stakes, sandboxed, or internal-only deployments where the declaring party is known and accountable |
| `thirdPartyReviewed` | Level 2 — The agent has been independently reviewed or audited by a third party, but has not undergone formal certification against a recognized standard. Provides higher confidence than self-declaration for use in controlled production environments |
| `certified` | Level 3 — The agent has been formally certified by a recognized standards or certification body against defined criteria for identity, capability accuracy, and behavioral compliance. Suitable for high-stakes deployments requiring verified accountability and regulatory alignment |

---

## New Vocabulary: `AI/AgentMemoryMode`

A controlled vocabulary classifying how an AI agent retains and recalls information across interactions or reasoning steps. Multiple values may be declared when an agent employs more than one mechanism.

| Entry | Description |
|---|---|
| `episodic` | Records of past events, interactions, or task executions that provide experiential context for future reasoning |
| `semantic` | Factual or conceptual knowledge stored for retrieval and inference (e.g., vector embeddings, knowledge graphs) |
| `procedural` | Encoded skills, plans, or behavioral patterns that guide the agent's execution strategy |
| `working` | Short-lived, context-scoped information used within a single reasoning session or conversation turn |
| `inContext` | Information retained within the active context window of the underlying language model |
| `inWeights` | Knowledge encoded in model parameters through pretraining or fine-tuning; not updated at runtime |
| `inCache` | Precomputed key-value attention caches enabling efficient reuse of prior computations |
| `external` | Information persisted in an external store (database, file system, vector store) and retrieved on demand |

---

## New Vocabulary: `AI/SafetyRiskAssessmentType`

A controlled vocabulary listing the general safety risk levels for an AI system, using categorization according to the EU general risk assessment methodology (Article 20, Regulation (EC) No 765/2008).

| Entry | Description |
|---|---|
| `serious` | The highest level of risk posed by an AI system |
| `high` | The second-highest level of risk posed by an AI system |
| `medium` | The third-highest level of risk posed by an AI system |
| `low` | Low/no risk is posed by an AI system |

---

## New Properties (Software Profile)

### `inputModality`
- **Nature:** ObjectProperty
- **Range:** `/Core/Modality`
- **Cardinality:** 0..*

Specifies the fundamental type of data that a software artifact or agent accepts and processes as input. This includes the sensory or representational form of data, such as natural language text, images, audio, or structured records. Multiple `inputModality` values may be declared when a software artifact or agent processes more than one type of input.

---

### `outputModality`
- **Nature:** ObjectProperty
- **Range:** `/Core/Modality`
- **Cardinality:** 0..*

Specifies the fundamental type of data that a software artifact or agent produces or emits as output. This includes the sensory or representational form of data, such as natural language text, images, audio, or structured records. Multiple `outputModality` values may be declared when a software artifact or agent produces more than one type of output.

---

## New Vocabulary: `Core/Modality`

A controlled vocabulary classifying the fundamental data or sensory type of content accepted or produced by software artifacts and agents.

| Entry | Description |
|---|---|
| `text` | Natural language text, structured text, or source code |
| `image` | Raster or vector image data (e.g., photographs, diagrams, screenshots) |
| `audio` | Sound recordings, speech, or music |
| `video` | Temporally sequenced visual data, with or without associated audio |
| `tabular` | Structured data organized in rows and columns (e.g., CSV, relational tables) |
| `timeSeries` | Sequences of values indexed by time (e.g., sensor readings, financial data) |
| `graph` | Data represented as nodes and edges (e.g., knowledge graphs, molecular structures) |
| `pointCloud` | Three-dimensional spatial data represented as sets of points (e.g., LiDAR, 3D scans) |
| `multimodal` | Combinations of two or more distinct modalities processed jointly |
| `other` | A modality not covered by the categories above |

---

## Changes to Existing Vocabularies

### `Core/RelationshipType`

Added entries:

| Entry | Description |
|---|---|
| `hasPersistentMemory` | The `from` Element uses each `to` Element as a persistent or long-term memory store (e.g., a database, vector store, or file system that retains information across sessions or reasoning steps) |
| `usesModel` | The `from` Element (typically an AIAgent) uses each `to` `/AI/AIPackage` as its underlying AI model, enabling BOM consumers to trace from an agent to its associated model weights, training data, and safety assessments |
