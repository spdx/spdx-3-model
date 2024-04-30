# JSON Serialization

## Parsing JSON-LD as JSON

This is a description of how to deserialize JSON-LD as a pure JSON format without any knowledge of RDF.
On top-level, JSON-LD has two keys, "@context" and "@graph".

### Parsing "@context"

The context is a list of a string and an object. You can ignore the string.
The object consists of key-value pairs that allow the shortening of IDs and which we will call "namespace map" in the following.

For deserialization purposes, follow this process:

- For every string that is an ID (that includes values of the keys "spdxId" and "@id", 
  as well as all strings where you would expect objects according to the SPDX-3 model),
  split that string at the first colon into "prefix:suffix".
- If the suffix does not start with "//" and the prefix is a key in the namespace map,
  replace "prefix:" with the value found under that key in the namespace map.
- Else do nothing to that string.
After you are done applying this process to all IDs, you can ignore the "@context".

### Parsing "@graph"

You will find an array of objects under the "@graph" key.
Every one of these objects has a "type" key that tells you the class of the SPDX-3 model that the object is an instance of.
The rest of the keys then correspond to the properties of that SPDX class.
Take special note of the "spdxId" key which specifies the ID by which the object can be referenced from other places.

One thing to note is that not all objects in that list have to be subclasses of Element.
As only Elements have an spdxId, there is no "spdxId" key in these cases but an "@id" key.
However, the value of "@id" serves the same function of identifying and referencing that object from within other objects.

Last but not least, whenever you encounter a string where you would expect an object according to the SPDX-3 model,
you can substitute that string with the object that has that string as its "spdxId" or "@id".
