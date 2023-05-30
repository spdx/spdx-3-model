# JSON Serialization

Ideally JSON will be very similar (or even the same) to JSON-LD.

The JSON serialization will consist of two things: A context file and an array of element objects (the "payload").

The context file will be linked via the single property "@context": "https://spdx.github.io/spdx-3-model/rdf/context.json" at top-level of the JSON file.
You need not care about its specifics, it is simply there to ensure compatibility of JSON and JSON-LD (if you want to know more, see the "about" section below).

The rest of the serialized file will consist of an array of objects under the "@graph" key, also at top-level of the JSON file.
Each of these objects must have a property "@type", stating its class name which must be an instantiable subclass of Element.
It also needs a property "@id", which serves to capture the SPDX ID of the Element.
All other SPDX properties of the Element are stated via key-value pairs, where the key is the name of the property (e.g. "createdBy").
The type of the value depends on the type of the property in the SPDX model and can be a string, number, array or object.
Note, though, that inlining of objects is only allowed for "complex data type" classes (CreationInfo, ExternalReference, etc.).
If the object were an Element, a string containing its ID would be written instead, thereby referencing another object from the same or even another payload.


#### About the context file
The context file is a tool to abbreviate long URIs in keys or vocabulary types.
This allows for a readable serialized output while still maintaining concise definitions of all properties and classes according to the RDF standard.
For example, using the context file as a "translation tool", we shorten the property "https://spdx.org/rdf/Core/createdBy" to simply "createdBy".
The context file will be universal for all SPDX users and is accessible at "https://spdx.github.io/spdx-3-model/rdf/context.json".
Utilising the context is achieved by adding the property "@context": "https://spdx.github.io/spdx-3-model/rdf/context.json" at top-level of the JSON file.
The context also serves to omit the @type key in objects where the type is already known from the key of the object.
For example, the object behind the key "creationInfo" is always of type "CreationInfo", so the key-value pair "@type": "CreationInfo" is implied via the context.