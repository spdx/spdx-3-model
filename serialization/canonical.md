# Canonical Serialization

Canonical serialization is single, consistent, normalized, deterministic, and reproducible form.

Such a canonical form normalizes things like ordering and formatting.

1. Canonical serialization is in JSON format, as defined in RFC 8259 (IETF STD 90)

1. no line breaks

1. key names MUST be wrapped in double quotes

1. no whitespace outside of strings

1. true, false and null: the literal names must be lowercase; no other literal names are allowed

1. integers: represented in base 10 using decimal digits. Contains an integer component that may be prefixed with an optional minus sign. Leading zeros are not allowed.

1. strings: UTF-8 representation without specific canonicalisation. A string begins and ends with quotation marks (%x22). Any Unicode characters may be placed within the quotation marks, except for the characters that MUST be escaped: quotation mark, reverse solidus, and the control characters (U+0000 through U+001F).

1. arrays: An array structure is represented as square brackets surrounding zero or more items. Items are separated by commas.

1. objects: An object structure is represented as a pair of curly brackets surrounding zero or more name/value pairs (or members). A name is a string containing only ASCII characters (0x21-0x7F). The names within an object must be unique. A single colon comes after each name, separating the name from the value. A single comma separates a value from a following name. The name/value pairs are ordered by name value.

1. DateTime is a signed integer of milliseconds since or before the Unix Epoch1. DateTime MUST be expressed as a series of base-10 digits, and MUST NOT be expressed with any leading zeroes, an exponent, a decimal point or a fractional part.

