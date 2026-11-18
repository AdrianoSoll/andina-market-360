import unittest
from src.resumen import calcular_resumen
class TestResumenVentas(unittest.TestCase):
    def setUp(self):
        self.datos = calcular_resumen()
    def test_cantidad_operaciones(self):
        self.assertEqual(self.datos["operaciones"], 12)
    def test_total_general(self):
        self.assertAlmostEqual(self.datos["total"], 1845.00, places=2)
    def test_total_lima(self):
        self.assertAlmostEqual(self.datos["sedes"]["Lima"], 814.00, places=2)
    def test_totales_ica_arequipa(self):
        self.assertAlmostEqual(self.datos["sedes"]["Ica"], 555.00, places=2)
        self.assertAlmostEqual(self.datos["sedes"]["Arequipa"], 476.00, places=2)
if __name__ == "__main__":
    unittest.main()
