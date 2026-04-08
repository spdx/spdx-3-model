SPDX-License-Identifier: Community-Spec-1.0

# Changes in `add-ai-prompt-v2` Branch

## New Class: `AI/Prompt`

**Subclass of:** `/Software/SoftwareArtifact`  
**Instantiability:** Concrete

Represents a prompt — instructions and directly accompanying content (natural language text, documents, code, and/or media) provided to an AI system by an external entity (human or AI agent) to guide its output.

Prompts are categorized by their role:
- A **user prompt** is provided by a user (human or AI agent) and is associated with a single query.
- A **system prompt** is provided by the system's owner or administrator to inform the system's overall behavior for every query or instruction. In agentic contexts, system prompts are sometimes referred to as "instructions."

### Properties on `Prompt`

| Field Name | Type | Required/Optional | Description |
|---|---|---|---|
| `promptRole` | `PromptRoleType` | Optional (0..1) | Whether the prompt is a `user` prompt (scoped to a single query) or a `system` prompt (governing overall behavior for every query) |
| `promptPattern` | `xsd:string` | Optional (0..*) | Design pattern or structured prompting strategy used to guide the model (e.g., `chain-of-thought`, `persona`, `tree-of-thought`, `decomposition`) |
| `isContextAugmented` | `xsd:boolean` | Optional (0..1) | `true` if the prompt was automatically augmented with external content (RAG, API lookup, database query, etc.); `false` otherwise |

## Properties

- /Core/inLanguage
  - type: /Core/LanguageTag
  - minCount: 0
- /Core/contentModality
  - type: /Core/Modality
  - minCount: 0
- /Core/contentType
  - type: /Core/MediaType
  - minCount: 0
- /Dataset/dataCollectionProcess
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- /Dataset/dataPreprocessing
  - type: xsd:string
  - minCount: 0
  - maxCount: 1
- /Dataset/hasSensitivePersonalInformation
  - type: /Core/PresenceType
  - minCount: 0
  - maxCount: 1
- /Dataset/confidentialityLevel
  - type: /Dataset/ConfidentialityLevelType
  - minCount: 0
  - maxCount: 1
- isContextAugmented
  - type: xsd:boolean
  - minCount: 0
  - maxCount: 1
- promptPattern
  - type: xsd:string
  - minCount: 0
- promptRole
  - type: /AI/PromptRoleType
  - minCount: 0
  - maxCount: 1



---

## New Properties (AI Profile)

### `promptRole`
- **Nature:** ObjectProperty
- **Range:** `PromptRoleType`
- **Cardinality:** 0..1

Specifies the role of a prompt within an AI interaction. Prompts are categorized into two distinct roles:
- `user`: Provided by a user (human or AI agent), associated with a single query or instruction.
- `system`: Provided by the system's owner, maintainer, or administrator to inform the system's overall behavior for every query or instruction. Sometimes referred to as "instructions" in agentic contexts.

---

### `promptPattern`
- **Nature:** DataProperty
- **Range:** `xsd:string`
- **Cardinality:** 0..*

Identifies a design pattern or structured prompting strategy used within a prompt to guide a foundation model toward a desired output or enhance its performance. Although free-form, standardized terminology is recommended where possible.

**Suggested values:**

| Value | Description |
|---|---|
| `simple` | A prompt without any specific pattern |
| `chain-of-thought` | Explicitly requires sequential, step-by-step reasoning before the answer |
| `decomposition` | Breaks a complex task into a collection of simpler sub-tasks |
| `flipped-interaction` | Reverses roles, instructing the model to ask clarifying questions first |
| `persona` | Instructs the model to adopt a specific role or character |
| `self-consistency` | Generates multiple outputs and selects the most common (consensual) answer |
| `self-reflection` | Asks the model to critique and refine its own output or steps |
| `tree-of-thought` | Explores and evaluates multiple branching lines of reasoning |

---

### `isContextAugmented`
- **Nature:** DataProperty
- **Range:** `xsd:boolean`
- **Cardinality:** 0..1

Specifies whether an automated grounding mechanism is employed during prompt construction (e.g., Retrieval-Augmented Generation, API results, or database lookups).
- `true`: The prompt includes automatically sourced external context or supporting content.
- `false`: The prompt is constructed directly without automated external augmentation.

When set to `true`, a Relationship of type `usesTool` can optionally be used to describe the context augmentation mechanism or tool employed.

---

## New Vocabulary: `AI/PromptRoleType`

A controlled vocabulary for classifying the role of a prompt within an AI system interaction.

| Entry | Description |
|---|---|
| `user` | A prompt provided by a user (human or AI agent) of the AI system, associated with a single query or instruction |
| `system` | A prompt provided by the system's owner, maintainer, or administrator to inform the system's overall behavior for every query or instruction. Sometimes referred to as "instructions" in agentic contexts |

---

## New Property (Core Profile)

### `contentModality`
- **Nature:** ObjectProperty
- **Range:** `Modality`
- **Cardinality:** 0..*

Provides information about the content modality of an Element or a property. A content modality describes the nature of the information channel or sensory type through which content is communicated, perceived, or processed by agents and software.

Use `other` if the modality is not listed, and optionally provide the specific modality in the `comment` property.

---

## New Vocabulary: `Core/Modality`

A controlled vocabulary used to classify the nature of the data channel (or sensory type) for content or interaction within a system.

| Entry | Description |
|---|---|
| `audio` | Spoken language and sound (e.g., voice commands, recorded dialog, music, environmental sounds, audio alerts) |
| `gesturePose` | Body movement, hand gestures, facial expressions, or full-body pose estimation |
| `hapticTactile` | Touch, force, or tactile feedback data (e.g., vibrations, surface pressure, grip data) |
| `image` | Still visual data (e.g., photographs, drawings, diagrams, charts) |
| `text` | A sequence of characters intended to convey meaning in a natural human language |
| `video` | Temporal visual data (sequences of still visual data), which can have associated time-synchronized data such as audio tracks or transcriptions |
| `other` | Any other modality not defined in this list |
| `noAssertion` | The modality is not known or cannot be reasonably determined, or the creator has made no attempt to determine this field |

---

## Changes to Existing Classes

### `AI/AIPackage`

Added property:

| Field Name | Type | Required/Optional | Description |
|---|---|---|---|
| `/Core/isoAutomationLevel` | `IsoAutomationLevel` | Optional (0..1) | ISO automation level classification for the AI package |


