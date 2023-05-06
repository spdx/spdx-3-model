
*LicenseInfo*	<- /Core/Element
  NoneLicense
  NoAssertionLicense
  *LicenseExpression*
     ConjuctiveSet
     	member: LicenseExpression[2..*]
     DisjunctiveSet
     	member: LicenseExpression[2..*]
     OrLaterOperator
     	license: License
     WithOperator
     	license: License
     	addition: Addition
     SingleLicense
	license: License


*LicensingText*	<- /Core/Element
	[id, name, comment] come from Element
	text: xsd:string[1]
	seeAlso: URI[0..*]
	standardTemplate: xsd:string[0..1]
	isDeprecatedId: bool[0..1]
	obsoletedBy: LicensingText[0..1]
  *License*
  	isOsiApproved: bool[0..1]
	isFsfLibre: bool[0..1]
	standardHeader: xsd:string[0..1]
    ListedLicense
    	listVersionAdded: LicenseListVersion
	deprecatedVersion: LicenseListVersion
    CustomLicense
  *Addition*
    ListedException
    	listVersionAdded: LicenseListVersion
	deprecatedVersion: LicenseListVersion
    CustomAddition



CopyrightText	<- xsd:string
  NoneCopyrightText
  NoAssertionCopyrightText


AttributionText	<- xsd:string

LicenseListVersion <- xsd:string
  format: \d+\.\d+

