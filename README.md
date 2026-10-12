# Skylight math

Skylight math weighs the sky a roof lets in: glass area against floor area on a
labeled daylight scale, catalog units against a target, and the sunshine priced
in kilowatt-hours of summer heat.

Live site: https://ilanis-agent.github.io/skylightmath/

## The three tools

- **Daylight plan** - room length x width and glass area become a daylight
  percentage (rounded to one decimal) and a labeled verdict: dim under 3%,
  soft 3-7%, bright 7-15%, glare beyond 15%.
- **Unit plan** - a target glass area and a unit size in cm become the unit
  count (ceiling of target over unit area) and the achieved area.
- **Heat plan** - glass area x hours of direct sun x a labeled 0.6 kW a sq m
  becomes kilowatt-hours of heat a day, rounded to one decimal.

## Limits

Every norm is labeled and illustrative. Orientation, shaft depth and climate
move the real numbers, and roof structure, flashing and waterproofing belong
to a roofer, never to a calculator.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (12 cases, 57 checks)

Run the tests: `python3 oracle.py && node test.js`
