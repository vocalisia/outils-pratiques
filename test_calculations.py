"""Known outcomes, boundary cases and invalid-input tests; no network."""
import json
from pathlib import Path
import subprocess
import sys
import unittest
from calculations import calculate, ENGINES


class ArithmeticTests(unittest.TestCase):
    def test_car_budget(self):
        result=calculate("car_budget",dict(purchase=12000,initial_costs=800,monthly_running=160,months=24,resale=7000))
        self.assertEqual(result["net_scenario_cost"],9640)

    def test_car_duration_cannot_be_zero(self):
        with self.assertRaises(ValueError):
            calculate("car_budget",dict(purchase=1,initial_costs=0,monthly_running=0,months=0,resale=0))

    def test_test_summary_excludes_unrun(self):
        result=calculate("test_summary",{"cases":[{"id":"a","status":"PASS"},{"id":"b","status":"FAIL"},{"id":"c","status":"NOT_RUN"}]})
        self.assertEqual(result["tested"],2)
        self.assertEqual(result["pass_fraction_of_run_cases"],0.5)

    def test_empty_summary_is_not_perfect_performance(self):
        self.assertIsNone(calculate("test_summary",{"cases":[]})["pass_fraction_of_run_cases"])

    def test_duplicate_case_rejected(self):
        with self.assertRaises(ValueError):
            calculate("test_summary",{"cases":[{"id":"a","status":"PASS"},{"id":"a","status":"FAIL"}]})

    def test_bad_test_status_rejected(self):
        with self.assertRaises(ValueError):
            calculate("test_summary",{"cases":[{"id":"a","status":"ok"}]})

    def test_evidence_summary(self):
        result=calculate("evidence_summary",{"records":[{"id":"a","state":"VERIFIED"},{"id":"b","state":"OUTDATED"},{"id":"c","state":"MISSING"}]})
        self.assertEqual(result["needs_review"],2)

    def test_time_comparison_counts_review(self):
        result=calculate("time_comparison",dict(manual_minutes=45,automated_minutes=12,review_minutes=8,runs=20))
        self.assertEqual(result["net_minutes_for_all_runs"],500)

    def test_automation_can_be_slower(self):
        result=calculate("time_comparison",dict(manual_minutes=10,automated_minutes=15,review_minutes=5,runs=2))
        self.assertEqual(result["net_minutes_for_all_runs"],-20)

    def test_zero_manual_duration_has_no_relative_gain(self):
        result=calculate("time_comparison",dict(manual_minutes=0,automated_minutes=0,review_minutes=0,runs=0))
        self.assertIsNone(result["relative_time_reduction"])

    def test_weekly_hours(self):
        self.assertEqual(calculate("weekly_hours",{"minutes":[60,45,0,90,30,0,60]})["weekly_hours"],4.75)

    def test_week_requires_seven_days(self):
        with self.assertRaises(ValueError): calculate("weekly_hours",{"minutes":[60]})

    def test_day_cannot_exceed_24_hours(self):
        with self.assertRaises(ValueError): calculate("weekly_hours",{"minutes":[1441,0,0,0,0,0,0]})

    def test_trading_fees(self):
        r=calculate("trading_fees",dict(orders=12,amount_per_order=1000,fixed_fee=3,proportional_rate=0.001,annual_custody=24))
        self.assertEqual(r["total_fees"],72)

    def test_fee_comparison_one_year(self):
        r=calculate("fee_difference",dict(capital=10000,gross_return=0.03,fee_a=0.002,fee_b=0.01,years=1))
        self.assertEqual(r["difference_a_minus_b"],80)

    def test_equal_fees_equal_outcomes(self):
        r=calculate("fee_difference",dict(capital=10000,gross_return=0,fee_a=0.01,fee_b=0.01,years=10))
        self.assertEqual(r["difference_a_minus_b"],0)

    def test_zero_years_preserves_capital(self):
        r=calculate("fee_difference",dict(capital=100,gross_return=0.03,fee_a=0.002,fee_b=0.01,years=0))
        self.assertEqual(r["scenario_a"],100)

    def test_negative_growth_factor_rejected(self):
        with self.assertRaises(ValueError):
            calculate("fee_difference",dict(capital=100,gross_return=-1,fee_a=0.1,fee_b=0.1,years=1))

    def test_gap_and_surplus(self):
        self.assertEqual(calculate("budget_gap",dict(expenses=4200,income=3500,buffer=250))["monthly_gap"],950)
        self.assertEqual(calculate("budget_gap",dict(expenses=100,income=300,buffer=20))["monthly_surplus"],180)

    def test_comparables_median(self):
        r=calculate("comparables",{"properties":[{"price":500000,"area":100},{"price":600000,"area":100},{"price":700000,"area":100}]})
        self.assertEqual(r["median_price_per_area"],6000)

    def test_even_median(self):
        r=calculate("comparables",{"properties":[{"price":10,"area":1},{"price":20,"area":1}]})
        self.assertEqual(r["median_price_per_area"],15)

    def test_zero_area_rejected(self):
        with self.assertRaises(ValueError): calculate("comparables",{"properties":[{"price":10,"area":0}]})

    def test_empty_comparables_rejected(self):
        with self.assertRaises(ValueError): calculate("comparables",{"properties":[]})

    def test_automation_payback(self):
        r=calculate("automation_balance",dict(minutes_saved=20,runs_per_month=40,hourly_cost=45,monthly_cost=100,setup_cost=900))
        self.assertEqual(r["monthly_net_scenario_value"],500)
        self.assertEqual(r["simple_payback_months"],1.8)

    def test_nonpositive_savings_have_no_payback(self):
        r=calculate("automation_balance",dict(minutes_saved=0,runs_per_month=40,hourly_cost=45,monthly_cost=100,setup_cost=900))
        self.assertIsNone(r["simple_payback_months"])

    def test_current_application_stage_counts(self):
        r=calculate("application_summary",{"applications":[{"id":"a","stage":"INTERVIEW"},{"id":"b","stage":"CLOSED"}]})
        self.assertEqual(r["total"],2)
        self.assertEqual(r["current_stage_counts"]["APPLIED"],0)

    def test_qualification_all_known_does_not_mean_yes(self):
        self.assertEqual(calculate("qualification",{"states":["NON"]*6})["state"],"PRÊT POUR REVUE HUMAINE")

    def test_qualification_unknown(self):
        self.assertEqual(calculate("qualification",{"states":["INCONNU"]*6})["missing"],6)

    def test_qualification_blank(self):
        self.assertEqual(calculate("qualification",{"states":[""]*6})["missing"],6)

    def test_qualification_invalid(self):
        self.assertEqual(calculate("qualification",{"states":["OUI"]*5+["yes"]})["state"],"SAISIE À CORRIGER")

    def test_qualification_size(self):
        with self.assertRaises(ValueError): calculate("qualification",{"states":[]})

    def test_funnel(self):
        r=calculate("funnel",dict(contacts=100,replies=20,meetings=8,held=6,sales=2))
        self.assertEqual(r["sale_per_contact"],0.02)
        self.assertEqual(r["held_per_meeting"],0.75)

    def test_zero_cohort_does_not_mean_zero_percent(self):
        r=calculate("funnel",dict(contacts=0,replies=0,meetings=0,held=0,sales=0))
        self.assertIsNone(r["sale_per_contact"])

    def test_non_nested_funnel_rejected(self):
        with self.assertRaises(ValueError): calculate("funnel",dict(contacts=1,replies=2,meetings=0,held=0,sales=0))

    def test_quotes(self):
        r=calculate("quote_total",dict(lines=[{"quantity":10,"unit_price":25},{"quantity":2,"unit_price":100}],fixed_cost=50))
        self.assertEqual(r["total"],500)

    def test_annual_scenario_is_not_insurance_model(self):
        r=calculate("annual_scenario",dict(monthly_premium=350,assumed_out_of_pocket=700))
        self.assertEqual(r["annual_scenario_total"],4900)
        self.assertNotIn("reimbursement",r)

    def test_fx_direction(self):
        r=calculate("fx_cost",dict(quantity=10,unit_price=100,fx_rate=0.9,commission=5))
        self.assertEqual(r["home_currency_total"],905)

    def test_weighted_matrix(self):
        r=calculate("weighted_matrix",{"weights":[2,1],"options":[{"id":"a","scores":[4,2]},{"id":"b","scores":[3,5]}]})
        self.assertEqual(r["highest_scoring_ids"],["b"])

    def test_matrix_ties_remain_ties(self):
        r=calculate("weighted_matrix",{"weights":[1],"options":[{"id":"a","scores":[4]},{"id":"b","scores":[4]}]})
        self.assertEqual(set(r["highest_scoring_ids"]),{"a","b"})
        self.assertTrue(r["tie"])

    def test_zero_matrix_weights_rejected(self):
        with self.assertRaises(ValueError): calculate("weighted_matrix",{"weights":[0],"options":[{"id":"a","scores":[4]}]})

    def test_matrix_missing_score_rejected(self):
        with self.assertRaises(ValueError): calculate("weighted_matrix",{"weights":[1,1],"options":[{"id":"a","scores":[4]}]})

    def test_matrix_out_of_range_rejected(self):
        with self.assertRaises(ValueError): calculate("weighted_matrix",{"weights":[1],"options":[{"id":"a","scores":[6]}]})

    def test_consumption(self):
        self.assertEqual(calculate("consumption",dict(distance_km=250,energy_kwh=47.5))["kwh_per_100km"],19)

    def test_zero_distance_rejected(self):
        with self.assertRaises(ValueError): calculate("consumption",dict(distance_km=0,energy_kwh=1))

    def test_panel_power_does_not_invent_energy(self):
        r=calculate("panel_power",dict(panels=12,watts_each=450))
        self.assertEqual(r["nominal_kw"],5.4)
        self.assertIsNone(r["annual_kwh"])

    def test_fractional_panel_count_rejected(self):
        with self.assertRaises(ValueError): calculate("panel_power",dict(panels=1.5,watts_each=450))

    def test_invoice(self):
        self.assertEqual(calculate("invoice_balance",dict(invoice=1200,payments=[300,450]))["outstanding"],450)

    def test_overpayment_not_negative_balance(self):
        r=calculate("invoice_balance",dict(invoice=10,payments=[15]))
        self.assertEqual((r["outstanding"],r["overpayment"]),(0,5))

    def test_negative_payment_rejected(self):
        with self.assertRaises(ValueError): calculate("invoice_balance",dict(invoice=10,payments=[-1]))

    def test_nan_and_bool_rejected(self):
        for value in [True,float("nan"),float("inf"),"100",None]:
            with self.subTest(value=value),self.assertRaises(ValueError):
                calculate("panel_power",dict(panels=value,watts_each=450))

    def test_unknown_parameters_rejected(self):
        with self.assertRaises(ValueError): calculate("panel_power",dict(panels=1,watts_each=450,unexpected=1))

    def test_missing_parameters_rejected(self):
        with self.assertRaises(ValueError): calculate("panel_power",dict(panels=1))

    def test_unknown_engine_rejected(self):
        for engine in ["unknown",[],None]:
            with self.subTest(engine=engine),self.assertRaises(ValueError): calculate(engine,{})

    def test_integer_above_exact_range_rejected(self):
        with self.assertRaises(ValueError): calculate("panel_power",dict(panels=2**53+1,watts_each=450))


class DocumentTests(unittest.TestCase):
    def test_html(self):
        html='<html lang="fr"><title>A &amp; B</title><link rel="canonical" href="https://example.org/"><meta name="ROBOTS" content="noindex"><h1>Titre <span>utile</span></h1></html>'
        r=calculate("html_audit",{"html":html})
        self.assertEqual(r["title"],"A & B")
        self.assertEqual(r["h1"],["Titre utile"])
        self.assertEqual(r["declared_robots"],["noindex"])
        self.assertEqual(r["indexation"],"NOT_TESTED")

    def test_html_without_h1(self):
        self.assertEqual(calculate("html_audit",{"html":"<p>texte</p>"})["h1"],[])

    def test_sitemap_duplicates(self):
        r=calculate("sitemap_audit",{"xml":"<urlset><url><loc>https://example.org/a</loc></url><url><loc>https://example.org/a</loc></url></urlset>"})
        self.assertEqual(r["entries"],2)
        self.assertEqual(r["duplicates"],["https://example.org/a"])

    def test_sitemap_index_does_not_become_url_count(self):
        r=calculate("sitemap_audit",{"xml":"<sitemapindex><sitemap><loc>https://example.org/child.xml</loc></sitemap></sitemapindex>"})
        self.assertEqual(r["kind"],"sitemapindex")
        self.assertFalse(r["child_sitemaps_fetched"])

    def test_xml_entities_rejected(self):
        with self.assertRaises(ValueError): calculate("sitemap_audit",{"xml":"<!DOCTYPE a [<!ENTITY x 'test'>]><urlset/>"})

    def test_invalid_xml(self):
        for xml in ["<urlset>","<notasitemap/>","<urlset><url/></urlset>"]:
            with self.subTest(xml=xml),self.assertRaises(ValueError): calculate("sitemap_audit",{"xml":xml})

    def test_catalog_examples_and_domain_isolation(self):
        catalog=json.loads((Path(__file__).parent/"catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(len(catalog),35)
        self.assertEqual(len({row["domain"] for row in catalog}),35)
        for row in catalog:
            with self.subTest(resource=row["id"]):
                self.assertIn(row["engine"],ENGINES)
                json.dumps(calculate(row["engine"],row["inputs"]),allow_nan=False)
                self.assertTrue(row["purpose"] and row["limit"] and len(row["fields"])>=6)

    def test_cli_error_is_nonzero(self):
        result=subprocess.run([sys.executable,str(Path(__file__).parent/"run.py"),"funnel","no-such-input.json"],capture_output=True,text=True)
        self.assertEqual(result.returncode,2)
        self.assertIn("error",json.loads(result.stderr))


if __name__ == "__main__":
    unittest.main()
