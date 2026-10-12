import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)
def round2(x): return jsnum(math.floor(x * 100 + 0.5) / 100)

def day_plan(roomLengthM, roomWidthM, glassAreaM2):
    if not (roomLengthM > 0) or not (roomWidthM > 0) or not (glassAreaM2 > 0):
        return {"error": "length, width and glass area must be positive"}
    floor = round1(roomLengthM * roomWidthM)
    pct = round1(glassAreaM2 / (roomLengthM * roomWidthM) * 100)
    if pct < 3: verdict = "a dim corner on the labeled scale"
    elif pct < 7: verdict = "a soft daylight balance on the labeled scale"
    elif pct <= 15: verdict = "a bright room on the labeled scale"
    else: verdict = "glare territory on the labeled scale"
    return {"floor": floor, "pct": pct, "verdict": verdict}

def unit_plan(targetAreaM2, unitWidthCm, unitHeightCm):
    if not (targetAreaM2 > 0) or not (unitWidthCm > 0) or not (unitHeightCm > 0):
        return {"error": "target, width and height must be positive"}
    unitA = unitWidthCm * unitHeightCm / 10000
    units = math.ceil(targetAreaM2 / unitA)
    return {"unitArea": round2(unitA), "units": units, "achieved": round2(units * unitA)}

def gain_plan(glassAreaM2, sunHours):
    if not (glassAreaM2 > 0) or not (sunHours > 0):
        return {"error": "area and hours must be positive"}
    kwh = round1(glassAreaM2 * sunHours * 0.6)
    if kwh < 2: verdict = "a gentle warm-up on the labeled scale"
    elif kwh < 6: verdict = "a noticeable summer load on the labeled scale"
    else: verdict = "a serious summer load on the labeled scale - shading belongs in the plan"
    return {"kwh": kwh, "verdict": verdict}

def render_day(r, roomLengthM, roomWidthM, glassAreaM2):
    return ("A " + fmt(roomLengthM) + " x " + fmt(roomWidthM) + " m room (" + fmt(r["floor"]) + " sq m) with "
            + fmt(glassAreaM2) + " sq m of glass: " + fmt(r["pct"]) + "% daylight glass - " + r["verdict"] + ".")

def render_unit(r, targetAreaM2, unitWidthCm, unitHeightCm):
    return ("For " + fmt(targetAreaM2) + " sq m of glass with " + fmt(unitWidthCm) + " x " + fmt(unitHeightCm)
            + " cm units (" + fmt(r["unitArea"]) + " sq m each): " + plural(r["units"], "unit") + ", "
            + fmt(r["achieved"]) + " sq m achieved on the labeled plan.")

def render_gain(r, glassAreaM2, sunHours):
    return (fmt(glassAreaM2) + " sq m of glass under " + plural(sunHours, "hour")
            + " of sun takes in about " + fmt(r["kwh"]) + " kWh of heat a day at a labeled 0.6 kW a sq m - "
            + r["verdict"] + ".")

cases = []
for a in [(4.5, 3.2, 1), (5, 4, 0.4), (6, 5, 5), (0, 3, 1)]:
    r = day_plan(*a)
    cases.append({"fn": "dayPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_day(r, *a)})
for a in [(2, 60, 90), (1, 50, 50), (3, 80, 80), (0, 60, 90)]:
    r = unit_plan(*a)
    cases.append({"fn": "unitPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_unit(r, *a)})
for a in [(2, 6), (1, 3), (2, 4), (0, 6)]:
    r = gain_plan(*a)
    cases.append({"fn": "gainPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_gain(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
