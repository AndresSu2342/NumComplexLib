import NumComplexLib
from math import sqrt
import unittest
class TestCplxOperations(unittest.TestCase):

    def test_sumcomplejos(self):
        suma = NumComplexLib.SumaComplejos([5,2],[4,7])
        self.assertAlmostEqual(suma[0], 9)
        self.assertAlmostEqual(suma[1], 9)

    def test_procomplejos(self):
        producto = NumComplexLib.ProductoComplejos([-3,-5],[7,-9])
        self.assertAlmostEqual(producto[0], -66)
        self.assertAlmostEqual(producto[1], -8)

    def test_rescomplejos(self):
        resta = NumComplexLib.RestaComplejos([5,2],[4,7])
        self.assertAlmostEqual(resta[0], 1)
        self.assertAlmostEqual(resta[1], -5)

    def test_divcomplejos(self):
        division = NumComplexLib.DivisionComplejos([-4,5],[8,-2])
        self.assertAlmostEqual(division[0], -42)
        self.assertAlmostEqual(division[1], 32)
        self.assertAlmostEqual(division[2], 68)

    def test_modcomplejos(self):
        modulo = NumComplexLib.ModuloComplejos([-2,2])
        self.assertAlmostEqual(modulo, 8)

    def test_conjcomplejos(self):
        conj = NumComplexLib.ConjugadoComplejos([3,4])
        self.assertAlmostEqual(conj[0], 3)
        self.assertAlmostEqual(conj[1], -4)

    def test_fasecomplejos(self):
        fase = NumComplexLib.FaseComplejos([-2,2])
        self.assertAlmostEqual(fase, 135)

    def test_repocomplejos(self):
        repo = NumComplexLib.RepresentacionPolar([-2,2])
        self.assertAlmostEqual(repo[0], 8)
        self.assertAlmostEqual(repo[1], 135)

    def test_recacomplejos(self):
        reca = NumComplexLib.RepresentacionCartesiana([2,120])
        self.assertAlmostEqual(reca[0], -1)
        self.assertAlmostEqual(reca[1], sqrt(3))


if __name__ == '__main__':
    unittest.main()


