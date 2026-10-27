SPDX-License-Identifier: Community-Spec-1.0

# ObservablePropertyType

## Summary

Recommended observable properties for observations of resource use and
environmental impact.

## Description

The `ObservablePropertyType` vocabulary provides identifiers for commonly
observed properties that are not fully identified by a QUDT quantity kind
alone, for example because the measurement boundary needs to be specified.

The IRI of an entry of this vocabulary may be used as the value of
the `observedProperty` property of an `Observation`.
The `observedProperty` property is not restricted to this vocabulary:
a QUDT quantity kind IRI shall be used instead when it fully identifies
the observed property (for example,
<http://qudt.org/vocab/quantitykind/Temperature> for the temperature of
a shipment), and IRIs from other vocabularies may also be used.

Each entry is a QUDT quantity kind that is a specialization (`skos:broader`)
of a QUDT quantity kind or of another entry.
The unit of the observed value shall have the same dimension as the broader
QUDT quantity kind (for example, <http://qudt.org/vocab/unit/KiloW-HR>
for energy).
The lists of applicable units in QUDT are not complete, so a unit not listed
there may still be used if its dimension matches.

For entries that are counts, the unit shall be applicable to the QUDT
quantity kind `Count` (for example, <http://qudt.org/vocab/unit/COUNT>).

Entries for greenhouse gas emissions specialize the QUDT quantity kind
`CO2Equivalent`: the observed value is a mass of carbon dioxide equivalent
(CO2e), recorded with a mass unit such as <http://qudt.org/vocab/unit/KiloGM>,
<http://qudt.org/vocab/unit/TONNE>, or <http://qudt.org/vocab/unit/MegaTONNE>
(for example, a value of 3.2 with `MegaTONNE` means 3.2 Mt CO2e).
The set of characterization factors used (for example, IPCC AR6 GWP100)
should be identified in the observation procedure or by a `conformsTo`
relationship to a Specification.
Removals of greenhouse gases are recorded as negative values.

## Metadata

- name: ObservablePropertyType
- entryType: http://qudt.org/schema/qudt/QuantityKind

## Entries

- biogenicCarbonContent: Mass of biogenic carbon contained in a product, expressed as mass of carbon (not CO2e).
  - broader: http://qudt.org/vocab/quantitykind/Mass
- carbonEmission: Net greenhouse gas emissions and removals, expressed as carbon dioxide equivalent (CO2e) using 100-year global warming potentials (GWP100), unless the observation procedure states otherwise.
  - broader: http://qudt.org/vocab/quantitykind/CO2Equivalent
- carbonEmissionAircraft: Greenhouse gas emissions from aircraft transportation, reported separately as required by ISO 14067; these emissions are also included in the total.
  - broader: /Core/ObservablePropertyType/carbonEmission
- carbonEmissionBiogenic: Greenhouse gas emissions and removals from biogenic sources (ISO 14067 biogenic GHG emissions and removals; PEF "Climate change - biogenic").
  - broader: /Core/ObservablePropertyType/carbonEmission
- carbonEmissionFossil: Greenhouse gas emissions and removals from fossil sources (ISO 14067 net fossil GHG emissions and removals; PEF "Climate change - fossil").
  - broader: /Core/ObservablePropertyType/carbonEmission
- carbonEmissionLandUseChange: Greenhouse gas emissions and removals from land use change; the observation procedure should state whether only direct land use change (ISO 14067 dLUC) or also land use (PEF "Climate change - land use and land use change") is included.
  - broader: /Core/ObservablePropertyType/carbonEmission
- carbonEmissionLocationBased: Mass of greenhouse gas emissions from purchased electricity, calculated with the average emission factor of the grid where consumption occurs (GHG Protocol Scope 2 location-based method).
  - broader: /Core/ObservablePropertyType/carbonEmission
- carbonEmissionMarketBased: Mass of greenhouse gas emissions from purchased electricity, calculated with the emission factors of contractual instruments (GHG Protocol Scope 2 market-based method).
  - broader: /Core/ObservablePropertyType/carbonEmission
- computeOperations: Number of arithmetic operations (for example, floating-point operations) performed; the operation type and precision should be stated in the observation procedure.
  - broader: http://qudt.org/vocab/quantitykind/Count
- energyConsumption: Energy consumed, with the measurement boundary unspecified.
  - broader: http://qudt.org/vocab/quantitykind/Energy
- energyConsumptionAccelerator: Energy consumed by accelerators only (for example, GPUs, TPUs, or NPUs).
  - broader: /Core/ObservablePropertyType/energyConsumption
- energyConsumptionFacility: Energy consumed at the facility boundary, including IT equipment and facility overhead such as cooling and power distribution.
  - broader: /Core/ObservablePropertyType/energyConsumption
- energyConsumptionItEquipment: Energy consumed by IT equipment (for example, processors, memory, storage, accelerators, and networking), excluding facility overhead.
  - broader: /Core/ObservablePropertyType/energyConsumption
- requestCount: Number of requests served.
  - broader: http://qudt.org/vocab/quantitykind/Count
- waterConsumption: Volume of water consumed (withdrawn and not returned to the source), including water used for cooling.
  - broader: http://qudt.org/vocab/quantitykind/Volume
