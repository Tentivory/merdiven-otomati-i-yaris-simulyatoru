import unittest

import yaris


class TestYaris(unittest.TestCase):
    def test_zemin_yasak(self):
        with self.assertRaises(ValueError):
            yaris.cikis_suresi(0, 0, False)

    def test_poset_yavaslatir(self):
        hafif = yaris.cikis_suresi(5, 0, False)
        agir = yaris.cikis_suresi(5, 4, False)
        self.assertGreater(agir, hafif)

    def test_karar_metni(self):
        self.assertIn("ZAFER", yaris.karar(9))
        self.assertIn("HEZİMET", yaris.karar(-8))


if __name__ == "__main__":
    unittest.main()
