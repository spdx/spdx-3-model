# JSON Serialization

Ideally JSON will be very similar (or even the same) to JSON-LD.

The JSON serialization will consist of two things: A context file and an array of element objects (the "payload").

The context file will be linked via the single property "@context": "https://spdx.github.io/spdx-3-model/rdf/context.json" at top-level of the JSON file.
You need not care about its specifics, it is simply there to ensure compatibility of JSON and JSON-LD (if you want to know more, see the "about" section below).
However, you can use it to substitute long namespaces with shorter identifiers of your choice. 
To utilise this feature, add an object to the "@context", the keys of which are the short identifiers you want to use and their values the full namespace.
For example, you can shorten URIs like "http://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#SPDXRef-DOCUMENT" to "spdx-example:SPDXRef-DOCUMENT"
(note the colon) by using the following context, which maps "spdx-example" to the namespace part of the URI:
```json
"@context": [
    "https://spdx.github.io/spdx-3-model/rdf/context.json",
    {
      "spdx-example": "http://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301#"
    }
]
```
Have a look at [this](json%2Fexamples%2Fconverted_from_spdx_2.json) and [this](json%2Fexamples%2Fspdx_document4.json) example to see how this looks in a full serialization.  
For deserialization, you can check whether a URI has to be expanded by splitting it at the first colon into "prefix:suffix": 
If the suffix does not start with "//" and the prefix is a key in the context, you replace "prefix:" with the value found under that key.

The rest of the serialized file will consist of an array of objects under the "@graph" key, also at top-level of the JSON file.
Each of these objects must have a property "@type", stating its class name which must be an instantiable subclass of Element.
It also needs a property "@id", which serves to capture the SPDX ID of the Element.
All other SPDX properties of the Element are stated via key-value pairs, where the key is the name of the property (e.g. "createdBy").
The type of the value depends on the type of the property in the SPDX model and can be a string, number, array or object.
Note, though, that inlining of objects is only allowed for "complex data type" classes (CreationInfo, ExternalReference, etc.).
If the object were an Element, a string containing its ID would be written instead (which can be subjected to the URI shortening described above), thereby referencing another object from the same or even another payload.


#### About the context file
The context file is a tool to abbreviate long URIs in keys or vocabulary types.
This allows for a readable serialized output while still maintaining concise definitions of all properties and classes according to the RDF standard.
For example, using the context file as a "translation tool", we shorten the property "https://spdx.org/rdf/Core/createdBy" to simply "createdBy".
The context file will be universal for all SPDX users and is accessible at "https://spdx.github.io/spdx-3-model/rdf/context.json".
Utilising the context is achieved by adding the property "@context": "https://spdx.github.io/spdx-3-model/rdf/context.json" at top-level of the JSON file.
The context also serves to omit the @type key in objects where the type is already known from the key of the object.
For example, the object behind the key "creationInfo" is always of type "CreationInfo", so the key-value pair "@type": "CreationInfo" is implied via the context.