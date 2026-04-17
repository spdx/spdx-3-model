SPDX-License-Identifier: Community-Spec-1.0

# Changes in `add-ai-agent-v2` Branch

## New Class: `AI/AIAgent`

**Subclass of:** `/Core/SoftwareAgent`  
**Instantiability:** Concrete

Represents an AI agent — a software entity that uses artificial intelligence techniques to perceive its environment, reason about its state, and take actions to achieve specified goals. It typically implements a perception-action cycle employing AI models, heuristics, or planning algorithms to guide autonomous or semi-autonomous behavior.

AI agents may be characterized by the modalities through which they perceive input and produce output, the capabilities they provide, the external tools or services they invoke, the memory mechanisms they employ to retain information across interactions, and their degree of automation relative to human oversight.

### Properties on `AIAgent`

| Field Name | Type | Required/Optional | Description |
|---|---|---|---|
| `/Core/suppliedBy` | `/Core/Agent` | Optional (0..*) | The Agent(s) that supplied the AI agent artifact |
| `/Software/inputModality` | `/Core/Modality` | Optional (0..*) | Fundamental data or sensory type accepted as input |
| `/Software/outputModality` | `/Core/Modality` | Optional (0..*) | Fundamental data or sensory type produced as output |
| `agentCapability` | `xsd:string` | Optional (0..*) | A functional capability the agent can perform |
| `agentExternalTool` | `/Core/DictionaryEntry` | Optional (0..*) | An external tool or service the agent can invoke |
| `agentMemoryMode` | `xsd:string` | Optional (0..*) | Memory category or storage mechanism used by the agent |
| `automationLevel` | `AutomationLevel` | Optional (0..1) | Degree of automation relative to human oversight |

### Relationship types used with `AIAgent`

| Relationship | Direction | Description |
|---|---|---|
| `hasPersistentMemory` | `AIAgent` → `Element` | The AIAgent uses the target Element as a persistent or long-term memory store (e.g., a database, vector store, or file system that retains information across sessions or reasoning steps) |
| `invokedBy` | `Element` → `Agent` | The Element was invoked by the target Agent (e.g., a Package is `invokedBy` an AIAgent; an AIAgent is `invokedBy` a Person) |
| `usesTool` | `AIAgent` → `Element` | The AIAgent uses the target Element as a tool to extend its capabilities |

---

## New Properties (AI Profile)

### `agentCapability`
- **Nature:** DataProperty
- **Range:** `xsd:string`
- **Cardinality:** 0..*

A free-form string that identifies and describes a specific functional capability of the agent — what it can do, what goal it serves, or what class of task it is designed to handle. Each value should capture one distinct capability.

Capabilities reflect the agent's behavioral repertoire and may include, but are not limited to: information retrieval, document summarization, code generation and execution, data analysis, planning and task decomposition, multi-step reasoning, multi-agent coordination, and domain-specific actions.

Use one `agentCapability` entry per distinct capability. External tools invoked to fulfill a capability are recorded separately via `agentExternalTool`.

**Examples:**

| Value | Meaning |
|---|---|
| `web-search` | Agent can search the web for information |
| `document-summarization: condenses retrieved documents into structured outputs` | Agent summarizes documents |
| `code-execution: runs Python snippets in a sandboxed environment` | Agent executes code |
| `multi-step-reasoning: decomposes complex queries into sub-tasks and plans execution order` | Agent performs step-by-step reasoning |
| `multi-agent-coordination: delegates sub-tasks to specialized agents and aggregates results` | Agent orchestrates other agents |

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
- **Nature:** DataProperty
- **Range:** `xsd:string`
- **Cardinality:** 0..*

A free-form string indicating the type of memory store or storage mechanism used by the agent to retain and recall information across interactions or reasoning steps.

Memory modes can be classified along two complementary dimensions:

**By cognitive function** (from cognitive science and BDI agent models):

| Value | Description |
|---|---|
| `episodic` | Records of past events, interactions, or task executions that provide experiential context for future reasoning |
| `semantic` | Factual or conceptual knowledge stored for retrieval and inference (e.g., vector embeddings, knowledge graphs) |
| `procedural` | Encoded skills, plans, or behavioral patterns that guide the agent's execution strategy |
| `working` | Short-lived, context-scoped information used within a single reasoning session or conversation turn |

**By storage location** (from language agent architectures, e.g., CoALA 2023):

| Value | Description |
|---|---|
| `in-context` | Information retained within the active context window of the underlying language model |
| `in-weights` | Knowledge encoded in model parameters through pretraining or fine-tuning; not updated at runtime |
| `in-cache` | Precomputed key-value attention caches enabling efficient reuse of prior computations |
| `external` | Information persisted in an external store (database, file system, vector store) and retrieved on demand |

Multiple values may be declared when an agent employs more than one memory mechanism.

---

### `automationLevel`
- **Nature:** ObjectProperty
- **Range:** `AutomationLevel`
- **Cardinality:** 0..1

The level of automation characterizes the degree to which an AI agent operates independently of human control or intervention, ranging from fully human-controlled systems to fully autonomous agents. This classification defines the respective roles and responsibilities of the human operator and the automated system, and is a critical component for risk assessment, regulatory compliance, human-machine interface design, and determining accountability boundaries.

---

## New Vocabulary: `AI/AutomationLevel`

A controlled vocabulary that categorizes a system's level of automation. The 7-level enumeration is based on [ISO/IEC 22989:2022](https://www.iso.org/standard/74296.html), aligned with [SAE J3016_202104](https://www.sae.org/standards/content/j3016_202104/), [Levels of Autonomy in Surgical Robotics (LASR)](https://doi.org/10.1038/s41746-024-01102-y), and [AutomationLevel in the Data Privacy Vocabulary](http://w3id.org/dpv/#AutomationLevel).

Systems at levels 0–5 are heteronomous: their goals and objectives are set by external entities, typically human operators. A system at level 6 is autonomous, capable of independently defining and pursuing its own goals.

| Entry | Level | Description |
|---|---|---|
| `notAutomated` | 0 | No automation. The human operator fully controls the system with no automated decision-making |
| `assistiveAutomation` | 1 | The system assists a human operator, who retains full decision-making authority and direct control at all times |
| `partialAutomation` | 2 | Some sub-functions are fully automated while the overall system remains under the control of an external agent; the system can act on an approved task without requiring continuous direct human control |
| `conditionalAutomation` | 3 | The system can propose strategies and automatically execute the approved plan, while an external agent remains ready to intervene when necessary |
| `highAutomation` | 4 | The system performs most of its mission without external intervention, but may require human oversight for exceptional conditions |
| `fullAutomation` | 5 | The system is capable of performing its entire mission without any external intervention, from start to completion |
| `autonomous` | 6 | The system is capable of independently modifying its intended domain of use or its goals without external intervention, control, or oversight |

---

## New Properties (Software Profile)

### `inputModality`
- **Nature:** ObjectProperty
- **Range:** `/Core/Modality`
- **Cardinality:** 0..*

Specifies the fundamental type of data that a software artifact or agent accepts and processes as input. Multiple values may be declared for multimodal software.

---

### `outputModality`
- **Nature:** ObjectProperty
- **Range:** `/Core/Modality`
- **Cardinality:** 0..*

Specifies the fundamental type of data that a software artifact or agent produces or emits as output. Multiple values may be declared for multimodal software.

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

Added entry:

| Entry | Description |
|---|---|
| `hasPersistentMemory` | The `from` Element uses each `to` Element as a persistent or long-term memory store (e.g., a database, vector store, or file system that retains information across sessions or reasoning steps) |
