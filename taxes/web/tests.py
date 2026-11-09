from django.test import TestCase


class NetPayTests(TestCase):
    def pay(self, income):
        return self.client.post("/", {"income": income}).context

    def test_one_million_salary(self):
        # PAYE: 25,000 + 30% of (1,000,000 - 410,000) = 202,000
        # NSSF: employee's 5% = 50,000
        r = self.pay(1_000_000)
        self.assertEqual(r["total_paye"], 202_000)
        self.assertEqual(r["total_nssf"], 50_000)
        self.assertEqual(r["net_income"], 748_000)

    def test_income_at_tax_free_threshold_pays_no_paye(self):
        r = self.pay(235_000)
        self.assertEqual(r["total_paye"], 0)
        self.assertEqual(r["total_nssf"], 11_750)

    def test_top_band_adds_extra_ten_percent(self):
        # 25,000 + 30% of 11,590,000 + 10% of 2,000,000 = 3,702,000
        self.assertEqual(self.pay(12_000_000)["total_paye"], 3_702_000)

    def test_text_input_resets_to_zero(self):
        self.assertEqual(self.pay("abc")["net_income"], 0)
