import unittest
from main import *

class TestGeometryFunctions(unittest.TestCase):
    def test_SCircle(self):
        """Тестирование площади круга"""
        self.assertEqual(SCircle(5), 79)
        self.assertEqual(SCircle(0), 0)

    def test_STriangle(self):
        """Тестирование площади треугольника"""
        # Прямоугольный треугольник
        self.assertEqual(STriangle(3, 4, 5), 6)
        # Не прямоугольный треугольник
        self.assertAlmostEqual(STriangle(2, 5, 6), 4.68)
        # Треугольник не существует
        self.assertEqual(STriangle(1, 2, 3), 'Треугольника с такими сторонами не существует')

    def test_SMnogogrannik(self):
        """Тестирование площади правильного многогранника"""
        self.assertAlmostEqual(SMnogogrannik(5, 6), 61.94)
        self.assertAlmostEqual(SMnogogrannik(3, 4), 6.93)

if __name__ == '__main__':
    unittest.main()