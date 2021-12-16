import unittest
# from MyClass import CircleArea as CA
import MyClass
from math import pi
import warehouse as WH


class TestWH(unittest.TestCase):
    def test_Add(self):
        self.assertRaises(TypeError, WH.ContainerManagment.add, 1)
        self.assertRaises(TypeError, WH.ContainerManagment.add, WH.Container(1, 1, 1))

    # def test_Delete(self):
    #     self.assertRaises(TypeError, WH.ContainerManagment.delete, "!")
        # self.assertRaises(KeyError, WH.ContainerManagment.delete, "23")






# class TestMyClass(unittest.TestCase):
#     def test_area(self):
#         self.assertEqual(MyClass.Circle.CircleArea(3), pi*3**2)
#         self.assertEqual(MyClass.Circle.CircleArea(1), pi)
#         self.assertEqual(MyClass.Circle.CircleArea(0), 0)
#         self.assertEqual(MyClass.Circle.CircleArea(2.5), pi * 2.5 ** 2)
#
#     def test_value(self):
#         self.assertRaises(ValueError, MyClass.Circle.CircleArea, -3)
#         self.assertRaises(ValueError, MyClass.Circle.CircleArea, -2)
#
#     def test_type(self):
#         self.assertRaises(TypeError, MyClass.Circle.CircleArea, 5+2j)


if __name__ == '__main__':
    unittest.main()
