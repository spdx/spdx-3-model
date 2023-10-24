# Licensing profile conformance

For an `ElementCollection` to be conformant with the Licensing profile,
the following have to hold:

1. for every `SoftwareArtifact` there MUST exist exactly one `Relationship`
   of type `concludedLicense` having that element as its `from` property
   and an `AnyLicenseInfo` as its `to` property.


