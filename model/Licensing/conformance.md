# Licensing profile conformance

For an element collection to be conformant with the `Licensing` profile,
the following have to hold:

1. for every `/Software/SoftwareArtifact` there MUST exist exactly one `/Core/Relationship`
   of type `concludedLicense` having that element as its `from` property
   and an `/SimpleLicensing/AnyLicenseInfo` as its `to` property.


