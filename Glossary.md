# Glossary
*(Editor's Note: General feeling that we can not make progress without understanding and defining the following terms)*

### Profile
Sean in Chat

### Namespace
Sean in Chat,  - use that as a starting point 

### Class
(and maybe subclass / extend)

### Property

### DataType
DataTypes are types whose instances are distinguished only by their value.[^1]
Types whose instances are distinguished by an instance identifier (primary key / index) are not DataTypes.

**Datatype:** No property is an instance identifier.

|            DataType | value                                                                  |
|--------------------:|------------------------------------------------------------------------|
|          Coordinate | {"latitude": 38.88980, "longitude": -77.03523}                         |
| Weather_Observation | {"location": "DCA", "time": "2022-11-01T20:44:39Z", "temperature": 48} |
|              Person | {"name": "John Doe", "weight": 152, date_of_birth": "1983-04-01"}      |

**Datatype:** Three different values of the same DataType are three separate instances.
No property is treated as an instance identifier even if it has a name such as "id", "uuid", etc.

| DataType | value                                                                              |
|---------:|------------------------------------------------------------------------------------|
|   Person | {"id": 123456, "name": "John Doe", "weight": 152, date_of_birth": "1983-04-01"}    |
|   Person | {"id": 123456, "name": "John Doe", "weight": 240, date_of_birth": "1983-04-01"}    |
|   Person | {"id": 123456, "name": "John Q. Doe", "weight": 152, date_of_birth": "1983-04-01"} |

**Class:** For non-DataType types, three different values with the same identifier are either
a single instance if variants are allowed, or an error.

|  Class | value                                                                              |
|-------:|------------------------------------------------------------------------------------|
| Person | {"id": 123456, "name": "John Doe", "weight": 152, date_of_birth": "1983-04-01"}    |
| Person | {"id": 123456, "name": "John Doe", "weight": 240, date_of_birth": "1983-04-01"}    |
| Person | {"id": 123456, "name": "John Q. Doe", "weight": 152, date_of_birth": "1983-04-01"} |

### Shape

### Constraint
A statement in a profile, restricting the set of allowed values, e.g. for properties in the model.
Examples could be the requirement of a different hash algorithm to be present.

### Validate

### Union
Gary

### Canonicalization
A process that takes abstract model data and generates a deterministic (string) representation (Serialization)
normalizing all choices like ordering, formatting and representation choices (like direction of relations and inlining).
See also https://spdx.github.io/canonical-serialisation/

### Serialization
representation of SPDX data as a byte stream

## Footnotes
[^1]:
    [UML](https://www.omg.org/spec/UML/2.5.1/PDF) Section 10.2.1