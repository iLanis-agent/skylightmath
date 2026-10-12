(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }
  function round2(x) { return Math.round(x * 100) / 100; }

  function dayPlan(roomLengthM, roomWidthM, glassAreaM2) {
    if (!(roomLengthM > 0) || !(roomWidthM > 0) || !(glassAreaM2 > 0)) return { error: "length, width and glass area must be positive" };
    var floor = round1(roomLengthM * roomWidthM);
    var pct = round1(glassAreaM2 / (roomLengthM * roomWidthM) * 100);
    var verdict;
    if (pct < 3) verdict = "a dim corner on the labeled scale";
    else if (pct < 7) verdict = "a soft daylight balance on the labeled scale";
    else if (pct <= 15) verdict = "a bright room on the labeled scale";
    else verdict = "glare territory on the labeled scale";
    return { floor: floor, pct: pct, verdict: verdict };
  }

  function unitPlan(targetAreaM2, unitWidthCm, unitHeightCm) {
    if (!(targetAreaM2 > 0) || !(unitWidthCm > 0) || !(unitHeightCm > 0)) return { error: "target, width and height must be positive" };
    var unitA = unitWidthCm * unitHeightCm / 10000;
    var units = Math.ceil(targetAreaM2 / unitA);
    var achieved = round2(units * unitA);
    return { unitArea: round2(unitA), units: units, achieved: achieved };
  }

  function gainPlan(glassAreaM2, sunHours) {
    if (!(glassAreaM2 > 0) || !(sunHours > 0)) return { error: "area and hours must be positive" };
    var kwh = round1(glassAreaM2 * sunHours * 0.6);
    var verdict;
    if (kwh < 2) verdict = "a gentle warm-up on the labeled scale";
    else if (kwh < 6) verdict = "a noticeable summer load on the labeled scale";
    else verdict = "a serious summer load on the labeled scale - shading belongs in the plan";
    return { kwh: kwh, verdict: verdict };
  }

  function renderDay(r, roomLengthM, roomWidthM, glassAreaM2) {
    return "A " + roomLengthM + " x " + roomWidthM + " m room (" + r.floor + " sq m) with " + glassAreaM2 + " sq m of glass: " + r.pct + "% daylight glass - " + r.verdict + ".";
  }

  function renderUnit(r, targetAreaM2, unitWidthCm, unitHeightCm) {
    return "For " + targetAreaM2 + " sq m of glass with " + unitWidthCm + " x " + unitHeightCm + " cm units (" + r.unitArea + " sq m each): " + plural(r.units, "unit") + ", " + r.achieved + " sq m achieved on the labeled plan.";
  }

  function renderGain(r, glassAreaM2, sunHours) {
    return glassAreaM2 + " sq m of glass under " + plural(sunHours, "hour") + " of sun takes in about " + r.kwh + " kWh of heat a day at a labeled 0.6 kW a sq m - " + r.verdict + ".";
  }

  var api = { dayPlan: dayPlan, unitPlan: unitPlan, gainPlan: gainPlan, renderDay: renderDay, renderUnit: renderUnit, renderGain: renderGain };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.SkylightMath = api;
})(this);
