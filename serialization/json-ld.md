# JSON-LD serialization

## JSON-LD context file
The context file includes most profile names, class names, property names, 
and vocabulary names from all profiles, as well as the "xsd" namespace and maps them to their respective URIs.
It also defines the aliases "spdxId" and "type" for "@id" and "@type", respectively.  
Exceptions have to be made for property names that are duplicated across different namespaces.
If one of these namespaces is "https://spdx.org/rdf/v3/Core", it takes precedence in the context over other namespaces (TODO: What if the Core namespace is not among them?).
If the duplicated property name is from a different namespace, it has to be prepended with the namespace when used in the body of JSON-LD (e.g. "security:locator": "https://some.locator").

For properties, the range of their values is also denoted.
Note that context expansion of the type only works for Literals and not Object nodes.
This especially means that all Element objects and complex data types (CreationInfo, ExternalReference etc.) must explicitly state their type in the object.
For vocabularies, a local @vocab is defined to prepend any value with the URI of the correct vocabulary type.
Note that this does not check that the given vocabulary value and the resulting URI is actually defined in SPDX.
