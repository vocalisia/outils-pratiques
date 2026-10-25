"""Offline arithmetic and record checks. Python 3.10+, standard library only.

Inputs are user-supplied scenarios. No network, account, market-data or model API.
"""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
import math
from statistics import median
from xml.etree import ElementTree


def number(value, name, *, minimum=0, maximum=None, integer=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name}: finite numeric value required")
    if integer and abs(value) > 2**53:
        raise ValueError(f"{name}: integer exceeds exact floating-point range")
    try:
        value = float(value)
    except OverflowError as error:
        raise ValueError(f"{name}: number too large") from error
    if not math.isfinite(value) or value < minimum:
        raise ValueError(f"{name}: invalid range or non-finite value")
    if maximum is not None and value > maximum:
        raise ValueError(f"{name}: exceeds maximum {maximum}")
    if integer and not value.is_integer():
        raise ValueError(f"{name}: integer required")
    return int(value) if integer else value


def clean(value):
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("Result outside finite numeric range")
        return round(value, 6)
    if isinstance(value, dict):
        return {key: clean(item) for key, item in value.items()}
    if isinstance(value, list):
        return [clean(item) for item in value]
    return value


def records(items, name="records"):
    if not isinstance(items, list) or len(items) > 100000:
        raise ValueError(f"{name}: list of up to 100000 records required")
    if not all(isinstance(item, dict) for item in items):
        raise ValueError(f"{name}: objects required")
    return items


def identified_states(items, key, allowed):
    seen = set()
    counts = Counter({value: 0 for value in sorted(allowed)})
    for item in records(items):
        identity, state = item.get("id"), item.get(key)
        if not isinstance(identity, str) or not identity.strip() or identity in seen:
            raise ValueError("Each record needs a distinct nonempty string id")
        if not isinstance(state, str) or state not in allowed:
            raise ValueError(f"Invalid {key}; expected one of {sorted(allowed)}")
        seen.add(identity)
        counts[state] += 1
    return counts


def car_budget(purchase, initial_costs, monthly_running, months, resale):
    purchase = number(purchase, "purchase")
    initial = number(initial_costs, "initial_costs")
    running = number(monthly_running, "monthly_running")
    duration = number(months, "months", minimum=1, maximum=1200, integer=True)
    resale = number(resale, "resale")
    net = purchase + initial + running * duration - resale
    return {"net_scenario_cost": net, "monthly_equivalent": net / duration,
            "running_total": running * duration}


def test_summary(cases):
    counts = identified_states(cases, "status", {"PASS", "FAIL", "NOT_RUN"})
    tested = counts["PASS"] + counts["FAIL"]
    return {"counts": dict(counts), "tested": tested,
            "pass_fraction_of_run_cases": counts["PASS"] / tested if tested else None,
            "limitation": "Counts of supplied records, not independently observed product performance."}


def evidence_summary(records):
    counts = identified_states(records, "state", {"VERIFIED", "MISSING", "OUTDATED"})
    return {"counts": dict(counts), "needs_review": counts["MISSING"] + counts["OUTDATED"],
            "limitation": "VERIFIED is the user's declared state; this tool does not verify a source."}


def time_comparison(manual_minutes, automated_minutes, review_minutes, runs):
    manual = number(manual_minutes, "manual_minutes")
    automated = number(automated_minutes, "automated_minutes")
    review = number(review_minutes, "review_minutes")
    runs = number(runs, "runs", integer=True)
    total = automated + review
    return {"automated_plus_review_minutes": total, "net_minutes_per_run": manual-total,
            "net_minutes_for_all_runs": (manual-total)*runs,
            "relative_time_reduction": (manual-total)/manual if manual else None}


def weekly_hours(minutes):
    if not isinstance(minutes, list) or len(minutes) != 7:
        raise ValueError("minutes: exactly seven daily values required")
    total = sum(number(item, "daily minutes", maximum=1440) for item in minutes)
    return {"weekly_minutes": total, "weekly_hours": total/60}


def trading_fees(orders, amount_per_order, fixed_fee, proportional_rate, annual_custody):
    orders = number(orders, "orders", integer=True)
    amount = number(amount_per_order, "amount_per_order")
    fixed = number(fixed_fee, "fixed_fee")
    rate = number(proportional_rate, "proportional_rate", maximum=1)
    custody = number(annual_custody, "annual_custody")
    return {"order_fees": orders*(fixed+amount*rate), "custody": custody,
            "total_fees": orders*(fixed+amount*rate)+custody}


def fee_difference(capital, gross_return, fee_a, fee_b, years):
    capital = number(capital, "capital")
    growth = number(gross_return, "gross_return", minimum=-1, maximum=1)
    a = number(fee_a, "fee_a", maximum=1)
    b = number(fee_b, "fee_b", maximum=1)
    years = number(years, "years", maximum=1000, integer=True)
    if min(1+growth-a, 1+growth-b) < 0:
        raise ValueError("Net yearly growth factor must not be negative")
    end_a, end_b = capital*(1+growth-a)**years, capital*(1+growth-b)**years
    return {"scenario_a": end_a, "scenario_b": end_b, "difference_a_minus_b": end_a-end_b}


def budget_gap(expenses, income, buffer):
    need = number(expenses, "expenses") + number(buffer, "buffer")
    income = number(income, "income")
    return {"monthly_need": need, "monthly_gap": max(0, need-income),
            "monthly_surplus": max(0, income-need)}


def comparables(properties):
    properties = records(properties, "properties")
    if not properties:
        raise ValueError("At least one comparable required")
    ratios = [number(item.get("price"), "price") / number(item.get("area"), "area", minimum=0.000001)
              for item in properties]
    return {"count": len(ratios), "price_per_area": ratios, "median_price_per_area": median(ratios),
            "limitation": "Unadjusted arithmetic of supplied observations, not a property appraisal."}


def automation_balance(minutes_saved, runs_per_month, hourly_cost, monthly_cost, setup_cost):
    minutes = number(minutes_saved, "minutes_saved", minimum=-1440)
    runs = number(runs_per_month, "runs_per_month", integer=True)
    hourly = number(hourly_cost, "hourly_cost")
    recurring = number(monthly_cost, "monthly_cost")
    setup = number(setup_cost, "setup_cost")
    hours = minutes*runs/60
    net = hours*hourly-recurring
    return {"monthly_hours_saved": hours, "monthly_net_scenario_value": net,
            "simple_payback_months": setup/net if net > 0 else None}


def application_summary(applications):
    counts = identified_states(applications, "stage", {"DRAFT", "APPLIED", "INTERVIEW", "OFFER", "CLOSED"})
    return {"current_stage_counts": dict(counts), "total": sum(counts.values()),
            "limitation": "Current stage counts, not cumulative conversion rates."}


def qualification(states):
    if not isinstance(states, list) or len(states) != 6:
        raise ValueError("Exactly six qualification states required")
    if not all(isinstance(state, str) and state in {"OUI", "NON", "INCONNU", ""} for state in states):
        return {"state": "SAISIE À CORRIGER", "missing": None}
    missing = sum(state in {"INCONNU", ""} for state in states)
    return {"state": "INFORMATIONS À COMPLÉTER" if missing else "PRÊT POUR REVUE HUMAINE", "missing": missing}


def funnel(contacts, replies, meetings, held, sales):
    values = [number(value, name, integer=True) for value, name in
              zip([contacts,replies,meetings,held,sales], ["contacts","replies","meetings","held","sales"])]
    if any(later > earlier for earlier, later in zip(values, values[1:])):
        raise ValueError("Nested stages of the same cohort must not increase")
    def fraction(numerator, denominator):
        return numerator/denominator if denominator else None
    c,r,m,h,s = values
    return {"reply_fraction": fraction(r,c), "meeting_per_reply": fraction(m,r),
            "held_per_meeting": fraction(h,m), "sale_per_held": fraction(s,h),
            "sale_per_contact": fraction(s,c)}


def quote_total(lines, fixed_cost):
    totals = [number(row.get("quantity"), "quantity")*number(row.get("unit_price"), "unit_price")
              for row in records(lines, "lines")]
    fixed = number(fixed_cost, "fixed_cost")
    return {"line_totals": totals, "fixed_cost": fixed, "total": sum(totals)+fixed}


def annual_scenario(monthly_premium, assumed_out_of_pocket):
    premium = number(monthly_premium, "monthly_premium")
    residual = number(assumed_out_of_pocket, "assumed_out_of_pocket")
    return {"twelve_premiums": premium*12, "assumed_out_of_pocket": residual,
            "annual_scenario_total": premium*12+residual}


class DocumentReader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_depth = 0
        self.h1_depth = 0
        self.title_parts = []
        self.h1_parts = []
        self.h1 = []
        self.canonicals = []
        self.robots = []
        self.lang = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html": self.lang = attrs.get("lang")
        if tag == "title": self.title_depth += 1
        if tag == "h1": self.h1_depth += 1
        if tag == "link" and "canonical" in (attrs.get("rel") or "").lower().split():
            self.canonicals.append(attrs.get("href"))
        if tag == "meta" and (attrs.get("name") or "").lower() in {"robots", "googlebot"}:
            self.robots.append(attrs.get("content", ""))

    def handle_endtag(self, tag):
        if tag == "title": self.title_depth = max(0, self.title_depth-1)
        if tag == "h1" and self.h1_depth:
            self.h1_depth -= 1
            if not self.h1_depth:
                self.h1.append(" ".join(" ".join(self.h1_parts).split()))
                self.h1_parts = []

    def handle_data(self, text):
        if self.title_depth: self.title_parts.append(text)
        if self.h1_depth: self.h1_parts.append(text)


def html_audit(html):
    if not isinstance(html, str) or len(html) > 5000000:
        raise ValueError("html: string of up to 5 million characters required")
    parser = DocumentReader()
    parser.feed(html)
    parser.close()
    return {"title": " ".join(" ".join(parser.title_parts).split()), "h1": parser.h1,
            "lang": parser.lang, "declared_canonicals": parser.canonicals,
            "declared_robots": parser.robots, "indexation": "NOT_TESTED"}


def sitemap_audit(xml):
    if not isinstance(xml, str) or len(xml) > 5000000:
        raise ValueError("xml: string of up to 5 million characters required")
    if "<!DOCTYPE" in xml.upper() or "<!ENTITY" in xml.upper():
        raise ValueError("XML document type and entity declarations are not accepted")
    try:
        root = ElementTree.fromstring(xml)
    except ElementTree.ParseError as error:
        raise ValueError("Malformed XML") from error
    local = lambda tag: tag.rsplit("}",1)[-1]
    kind = local(root.tag)
    if kind not in {"urlset", "sitemapindex"}:
        raise ValueError("Expected a urlset or sitemapindex root")
    entry_tag = "url" if kind == "urlset" else "sitemap"
    locations = []
    for entry in root:
        if local(entry.tag) == entry_tag:
            location = next((child.text.strip() for child in entry if local(child.tag) == "loc" and child.text and child.text.strip()), None)
            if location is None:
                raise ValueError("Every sitemap entry needs a nonempty loc")
            locations.append(location)
    counts = Counter(locations)
    return {"kind": kind, "entries": len(locations), "unique_locations": len(counts),
            "duplicates": sorted(location for location,count in counts.items() if count > 1),
            "indexation": "NOT_TESTED", "child_sitemaps_fetched": False}


def fx_cost(quantity, unit_price, fx_rate, commission):
    qty = number(quantity, "quantity")
    price = number(unit_price, "unit_price")
    rate = number(fx_rate, "fx_rate", minimum=0.000000001)
    fee = number(commission, "commission")
    return {"quote_currency_notional": qty*price, "home_currency_notional": qty*price*rate,
            "home_currency_total": qty*price*rate+fee}


def weighted_matrix(weights, options):
    if not isinstance(weights, list) or not weights:
        raise ValueError("Nonempty weights required")
    weights = [number(weight, "weight") for weight in weights]
    denominator = sum(weights)
    if denominator <= 0:
        raise ValueError("Total weight must be positive")
    seen = set()
    scores = []
    for option in records(options, "options"):
        identity, values = option.get("id"), option.get("scores")
        if not isinstance(identity,str) or not identity.strip() or identity in seen:
            raise ValueError("Distinct nonempty option ids required")
        if not isinstance(values,list) or len(values) != len(weights):
            raise ValueError("Every option needs one score per weight")
        values = [number(value,"score",maximum=5) for value in values]
        seen.add(identity)
        scores.append({"id":identity,"weighted_score":sum(w*s for w,s in zip(weights,values))/denominator})
    if not scores:
        raise ValueError("At least one option required")
    best = max(row["weighted_score"] for row in scores)
    winners = [row["id"] for row in scores if math.isclose(row["weighted_score"],best,rel_tol=1e-12,abs_tol=1e-12)]
    return {"scores":scores,"highest_scoring_ids":winners,"tie":len(winners)>1}


def consumption(distance_km, energy_kwh):
    distance = number(distance_km,"distance_km",minimum=0.000001)
    energy = number(energy_kwh,"energy_kwh")
    return {"kwh_per_100km":100*energy/distance}


def panel_power(panels, watts_each):
    count = number(panels,"panels",integer=True)
    watts = number(watts_each,"watts_each")
    return {"nominal_watts":count*watts,"nominal_kw":count*watts/1000,"annual_kwh":None}


def invoice_balance(invoice, payments):
    total = number(invoice,"invoice")
    if not isinstance(payments,list):
        raise ValueError("payments: list required")
    paid = sum(number(value,"payment") for value in payments)
    return {"paid":paid,"outstanding":max(0,total-paid),"overpayment":max(0,paid-total)}


ENGINES = {name:globals()[name] for name in (
    "car_budget","test_summary","evidence_summary","time_comparison","weekly_hours",
    "trading_fees","fee_difference","budget_gap","comparables","automation_balance",
    "application_summary","qualification","funnel","quote_total","annual_scenario",
    "html_audit","sitemap_audit","fx_cost","weighted_matrix","consumption","panel_power","invoice_balance")}


def calculate(engine, inputs):
    if not isinstance(engine,str) or engine not in ENGINES or not isinstance(inputs,dict):
        raise ValueError("Known engine and JSON object inputs required")
    try:
        return clean(ENGINES[engine](**inputs))
    except (TypeError,OverflowError) as error:
        raise ValueError("Invalid input shape or numeric overflow") from error
