# Units of measurement

We adhere to the International System of Units (SI) for consistency and accuracy in all technical documentation. [Source: BIPM](https://www.bipm.org)

* Additional units not part of SI are also included on this page.
* For conversion of non-SI units to SI units, refer to the Conversion Table.
* Refer to RMF pages 31, 32, and 38 for specific instructions on unit usage.
* The uppercase 'K' and lowercase 'k' are distinguished as follows:
  * 'K' represents 1024.
  * 'k' represents 1000.

## Formatting guidelines

* Always include a space between the numeric value and the unit symbol.
  * Example: 15 g, 15 mm
* **Exceptions**:
  * Temperature: When using abbreviations for degrees Celsius or Fahrenheit, do not add a space before or after the degree symbol (RMF p. 38). Example: 15°C.
  * Percent sign: Example: 50%
  * Units do not need to be spelled out in running text; the abbreviation is acceptable.
* Always spell out 'bit' and 'byte'; do not abbreviate as 'b' or 'B'.
* When spelling out the unit name, use a hyphen to separate the number from the unit. [Source: BIPM](https://www.bipm.org)
  * Example: a 16-bit address, a 35-millimeter film.
* When the value is used as an adjective, leave a space between the numerical value and the unit symbol. [Source: BIPM](https://www.bipm.org)
  * Example: a 10 kΩ resistor, a 35 mm film.

## Prefixes for binary powers (Source: Read Me First)

| Factor | Abbreviation | Unit      | Value        | Note                        |
| ------ | ------------ | --------- | ------------ | --------------------------- |
| 2^10   | Kb (Kib)     | kilobit   | 1024 b       | Prohibited                  |
| 2^10   | KB (KiB)     | kilobyte  | 1024 B       | Prohibited (RMF pg. 381)    |
| 2^20   | MB (MiB)     | megabyte  | 1048576 B    | Prohibited                  |
| 2^30   | GB (GiB)     | gigabyte  | 1073741824 B | Prohibited (RMF pg. 376)    |

Base 2 is assumed for these prefixes. Although these prefixes are not part of SI, they are commonly used in information technology to avoid incorrect usage of SI prefixes.

## SI prefixes

SI prefixes represent powers of 10. **They should not be used to indicate powers of 2**. For binary powers, the IEC has adopted separate prefixes, as defined in IEC 60027-2: 2005, third edition - *Letter symbols to be used in electrical technology – Part 2: Telecommunications and electronics.*

### Positive powers of 10

| Factor | Name  | Symbol |
| ------ | ----- | ------ |
| 10^1   | deca  | da     |
| 10^2   | hecto | h      |
| 10^3   | kilo  | k      |
| 10^6   | mega  | M      |
| 10^9   | giga  | G      |
| 10^12  | tera  | T      |
| 10^15  | peta  | P      |
| 10^18  | exa   | E      |
| 10^21  | zetta | Z      |
| 10^24  | yotta | Y      |

### Negative powers of 10

| Factor | Name  | Symbol |
| ------ | ----- | ------ |
| 10^-1  | deci  | d      |
| 10^-2  | centi | c      |
| 10^-3  | milli | m      |
| 10^-6  | micro | μ      |
| 10^-9  | nano  | n      |
| 10^-12 | pico  | p      |
| 10^-15 | femto | f      |
| 10^-18 | atto  | a      |
| 10^-21 | zepto | z      |
| 10^-24 | yocto | y      |

## SI base units

| Name      | Symbol | Quantity       | Notes                           |
| --------- | ------ | -------------- | ------------------------------- |
| meter     | m      | length         |                                 |
| kilogram  | kg     | mass           |                                 |
| second    | s      | time           | 'sec' is also acceptable (RMF p. 393). |
| ampere    | A      | electric current |                               |
| kelvin    | K      | thermodynamic temperature  |                       |
| mole      | mol    | amount of substance |                            |
| candela   | cd     | luminous intensity |                             |

## SI coherent derived units

| Name              | Symbol | Quantity              |
| ----------------- | ------ | --------------------- |
| square meter      | m²     | area                  |
| cubic meter       | m³     | volume                |
| meter per second  | m/s    | speed, velocity       |
| meter per second squared | m/s² | acceleration     |
| reciprocal meter  | m⁻¹    | wavenumber            |
| kilogram per cubic meter | kg/m³ | density, mass density |
| kilogram per square meter | kg/m² | surface density  |
| cubic meter per kilogram | m³/kg | specific volume   |
| ampere per square meter | A/m² | current density    |
| ampere per meter  | A/m    | magnetic field strength |
| mole per cubic meter | mol/m³ | amount concentration |
| candela per square meter | cd/m² | luminance         |
| one               | 1      | refractive index      |
| one               | 1      | relative permeability |

## SI coherent derived units with special names and symbols

| Name          | Symbol | Derived quantity              |
| ------------- | ------ | ----------------------------- |
| radian        | rad    | plane angle                   |
| steradian     | sr     | solid angle                   |
| hertz         | Hz     | frequency                     |
| newton        | N      | force                         |
| pascal        | Pa     | pressure, stress              |
| joule         | J      | energy, work, amount of heat  |
| watt          | W      | power, radiant flux           |
| coulomb       | C      | electric charge, amount of electricity |
| volt          | V      | electric potential difference, electromotive force |
| farad         | F      | capacitance                   |
| ohm           | Ω      | electric resistance           |
| siemens       | S      | electric conductance          |
| weber         | Wb     | magnetic flux                 |
| tesla         | T      | magnetic flux density         |
| henry         | H      | inductance                    |
| degree Celsius | °C    | Celsius temperature           |
| lumen         | lm     | luminous flux                 |
| lux           | lx     | illuminance                   |
| becquerel     | Bq     | activity of a radionuclide    |
| gray          | Gy     | absorbed dose, kerma         |
| sievert       | Sv     | dose equivalent               |
| katal         | kat    | catalytic activity            |

## Non-SI units accepted for use within SI

| Name          | Symbol | Value in SI units          |
| ------------- | ------ | -------------------------- |
| minute        | min    | 1 min = 60 s               |
| hour          | h      | 1 h = 60 min = 3600 s      |
| day           | d      | 1 d = 24 h = 86400 s       |
| degree        | °      | 1° = (π/180) rad           |
| minute (angle) | ′     | 1′ = (1/60)° = (π/10800) rad |
| second (angle) | ″     | 1″ = (1/60)′ = (π/648000) rad |
| hectare       | ha     | 1 ha = 1 hm² = 10⁴ m²      |
| litre         | L or l | 1 L = 1 l = 1 dm³ = 10⁻³ m³ |
| tonne         | t      | 1 t = 10³ kg               |

## Other non-SI units

| Quantity            | Name        | Symbol | Value in SI units           |
| ------------------- | ----------- | ------ | --------------------------- |
| pressure            | bar         | bar    | 1 bar = 0.1 MPa = 100 kPa = 10⁵ Pa |
| pressure            | millimeter of mercury | mmHg | 1 mmHg ≈ 133.322 Pa |
| length              | ångström    | Å      | 1 Å = 0.1 nm = 100 pm = 10⁻¹⁰ m |
| length              | nautical mile | M     | 1 M = 1852 m               |
| area                | barn        | b      | 1 b = 100 fm² = (10⁻¹² cm)² = 10⁻²⁸ m² |
| speed               | knot        | kn     | 1 kn = (1852/3600) m/s     |
| logarithmic ratio quantities | neper | Np |                             |
| logarithmic ratio quantities | bel | B |                             |
| logarithmic ratio quantities | decibel | dB |                         |

## Other units used in Nordic documentation

| Abbreviation | Unit          | Value                   |
| ------------ | ------------- | ----------------------- |
| dBc          | decibels relative to the carrier (See [Glossary](https://wiki.spaces/TECHDOC/pages/120292720)) | |
| kHz          | kilohertz     | 1,000 Hz                |
| MHz          | megahertz     | 1,000,000 Hz            |
| GHz          | gigahertz     | 1,000,000,000 Hz        |
| kbps         | kilobits per second | 1,000 b/s         |
| kBps         | kilobytes per second | 1,000 B/s        |
| Mbps         | megabits per second | 1,000,000 b/s     |
| MBps         | megabytes per second | 1,000,000 B/s    |
| (k)sps       | (kilo) samples per second | 1,000 samples/s |
| ppm          | parts per million |                       |

## Proper notation versus keyboard approximations

Standard keyboards lack many technical symbols. Avoid substituting available characters for proper notation:

**Inappropriate substitutions**:
* Using hashtag/number sign (#) for pound-mass or pound-force
* Using apostrophe (') for arcminute or foot
* Using quotation mark (") for arcsecond or inch

**Appropriate notation**:
* Spell out: pound, foot, inch when proper symbols aren't available
* Use abbreviations: lb, ft, in when space constraints exist
* Insert proper symbols: ′ for arcminute, ″ for arcsecond when documenting angular measurements

Modern documentation tools support Unicode. Configure your environment to access proper technical symbols rather than approximating with keyboard substitutes.

## Measurement system bridging

Technical audiences span geographies with different measurement traditions:

**Strategy selection**:
* **SI-primary contexts** (circuit design, electrical specifications): Use SI units exclusively. Don't add imperial conversions.
  * Example: "Supply voltage: 3.3 V" (no imperial equivalent needed)
* **Physical dimension contexts** (enclosure size, cable length): Include both systems when either might aid understanding.
  * Example: "Antenna length: 65 mm (2.56 in)"
* **Mixed-audience contexts**: Lead with SI, follow with imperial in parentheses.

**Conversion placement**:
* Keep conversions together on first mention: "Operating range: 15 m (49 ft)"
* Don't repeat conversions throughout—establish the relationship once per context

The goal isn't mathematical precision in conversions but helping readers visualize scale regardless of their familiar system.

## Temporal interval formatting

Express time durations consistently across your documentation:

**System displays and logs**:
* Use colon-separated notation for machine-generated timestamps
* Example: "Process duration: 02:15:33"
* Define component meaning: first pair = hours, second = minutes, third = seconds

**Human-readable text**:
* Spell out time units in explanatory content
* Example: "Compilation typically requires 3 to 5 minutes"
* Use natural language rather than numeric codes

**API responses and data formats**:
* Follow ISO 8601 duration format: PT3H15M22S
* Document your format choice in API specifications

Consistency within output types matters more than consistency across all contexts—match reader expectations for each format.

## Industry convention conflicts

Electrical component ratings sometimes diverge from standard SI spacing conventions:

**Standard SI practice**: Include space between value and unit
* Correct: 5 V, 100 mA, 4.7 kΩ

**Component marking practices**: Manufacturers often omit spacing on physical labels
* Common on hardware: "12V", "500mA", "3V3" (meaning 3.3V)

**Documentation approach**:
* Follow SI standards in technical writing: use spacing
* When documenting physical markings exactly as they appear, note the deviation
* Example: "Locate the component marked '5V' on the board (5 V supply rail)"

Consistency within your documentation takes priority—pick SI-compliant spacing and maintain it throughout, even when describing non-compliant labels.
