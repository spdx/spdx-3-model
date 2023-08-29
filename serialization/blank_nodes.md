

# What are blanknodes?

According to the W3C, blank nodes are nodes in an RDF graph that have no URI label. They are existential variables that describe a thing without naming it.

`"You can identify BlankNodes locally with a NodeId. that ID can be used to talk about the node inside your particular file/store of information, but you can't use it to ID the node externally."`

# Known issues with blank nodes

There is broad consensus in the rdf community on the existence of significant issues and challenges with using blank nodes.
A very brief time searching will yield scores of papers, blog posts, articles, etc. calling out various reasons that blank nodes are problematic and should be avoided wherever possible in the large majority of situations. 
Semantics and the standards specifications regarding blank nodes are inconsistent and contradictory leading to inconsistency between tools, ambiguity in how they will be processed, interpreted or queried.

When blank nodes are used it is typically for the convenience of the producer but if maintained in the graph comes at significant cost to the consumer in the form of ambiguity, uncertainty, complexity, and resources (time and computing resources).

If they are decided to be used they are ONLY for a single scope of a single datastore or single serialized document and NOT for global or cross-scope use. This is explicitly stated in all of the W3C specifications dealing with blank nodes. Using them for cross-scope or deserialized in-graph use as SPDX 3.0 is intended leads to significant potential data integrity issues.

Blank nodes also have significant issues for SPARQL, the definitive standard mechanism for querying rdf graphs. The two do NOT play well together due to inherent issues in blank node design and inconsistencies in the rdf specifications related to blank nodes. Many queries can lead to inconsistent and non-integrous results. Various academics and companies have offered workarounds and schemes to attempt to address this disconnect but they all come at significant compute complexity and cost. These issues increase significantly with the volume of blank nodes in the overall graph being queried.

Blank nodes also cause significant issues with semantic entailment (ability to determine full semantic integrity and correctness) of the graph. Entailment is required for any higher-order semantic inferencing and analysis. A couple of academics have offered papers that purport to mathematically prove that entailment using blank nodes is NPComplete though there is broad consensus that while it is likely possible it is almost always impractical and problematic.

# Discussion that occurred within the SPDX Tech committee and the SPDX Serialization Working Group

The topic of blank nodes, their challenges and their desired value in the form of serialization brevity were discussed over the course of multiple weeks in the SPDX Tech committee and SPDX Serialization Working Group meetings.

These discussions included the fact that almost all of the identified challenges exist when trying to use blank nodes in the deserialized graph or across multiple serializations.

The topic of skolemisation was discussed as a potential solution for these issues. According to the W3C characterization of skolemisation:
`Blank nodes do not have an intrinsic name in the RDF abstract syntax. In situations where such a name is required, implementations MAY systematically replace blank nodes in an RDF graph with IRIs. Systems wishing to do this SHOULD mint a new, globally unique IRI for each blank node. Such IRIs are known as Skolem IRIs.`
Skolemisation is inherently performed by many graph database engines upon ingestion of blank node content to avoid complexity and integrity issues but skolemisation is not universally applied, can have varying implementations and comes at additional processign cost.

There was not 100% agreement among all members of the SPDX Tech committee and the SPDX Serialization Working Group on the tradeoffs on allowing blank nodes in SPDX but a clear compromise consensus did develop that for the sake of serialization brevity blank nodes should be allowed under very specific conditions of use.

# Consensus agreement for use of blank nodes within SPDX 3.X
* blank nodes MAY be used only in single-scope content serialization
* only non-Element class objects may utilize blank nodes
* blank nodes will be serialized as embedded in their relational/property position within the Elements they characterize
* blank nodes will not use identifiers in serialized content
* serializated content may NOT contain compaction use of blank nodes (multiple blank node locations in the serialized referencing the same blank node definition which should be implicitly prevented by the previous two bullet points above)
* skolemisation MUST be performed upon any deserialization
