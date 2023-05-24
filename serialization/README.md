# Notes on Serialization

## Serialization info

One approach to serialization is to define format-specific SPDX data models.
The other is to define an abstract (format-agnostic) SPDX Information Model
along with application-independent serialization rules for each data format.
The information-based approach allows:
1. a single SPDX information model to apply to all serialization formats
2. simple (non-LD) JSON and YAML messages to be defined
3. serialized data in any format to be losslessly converted to, and combined with,
data in any other format.
    - For an extreme example, a Person instance serialized in
XML/RDF can be linked in a Relationship instance serialized in JSON to an Artifact
instance serialized in tag:value, because the IM models information needed by
applications, not data objects.
    - A more plausible use case would allow a signed collection of Packages in JSON
   format to be included in and validated by an SBOM in XML/RDF format.

## Serialization formats

The files in the [Information Model](InformationModel) directory describe the abstract
modeling approach.

The files in this directory provide some notes on the specific serialization formats.

The notes are numbered for easier referencing -- the order is **not** significant.


