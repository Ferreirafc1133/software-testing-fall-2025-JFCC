# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    celsius_to_fahrenheit,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")


class TestWhiteBoxCheckNumberStatus(unittest.TestCase):
    """Unit tests for 1: check_number_status"""

    def test_positive_number(self):
        """Return Positive when number > 0"""
        self.assertEqual(check_number_status(5), "Positive")

    def test_negative_number(self):
        """Return Negative when number < 0"""
        self.assertEqual(check_number_status(-3), "Negative")

    def test_zero(self):
        """Return Zero when number == 0"""
        self.assertEqual(check_number_status(0), "Zero")


class TestWhiteBoxCelsiusToFahrenheit(unittest.TestCase):
    """Unit tests for 10: celsius_to_fahrenheit"""

    def test_valid_temperatures(self):
        """Valid range: should convert Celsius to Fahrenheit."""
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_invalid_low_temperature(self):
        """Invalid: below -100"""
        self.assertEqual(celsius_to_fahrenheit(-150), "Invalid Temperature")

    def test_invalid_high_temperature(self):
        """Invalid: above 100"""
        self.assertEqual(celsius_to_fahrenheit(150), "Invalid Temperature")


class TestWhiteBoxTrafficLight(unittest.TestCase):
    """Unit tests for 23: TrafficLight"""

    def test_initial_state(self):
        """Initial state should be Red"""
        tl = TrafficLight()
        self.assertEqual(tl.get_current_state(), "Red")

    def test_cycle_once(self):
        """Red = Green"""
        tl = TrafficLight()
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Green")

    def test_cycle_twice(self):
        """Red = Green = Yellow"""
        tl = TrafficLight()
        tl.change_state()
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Yellow")

    def test_cycle_three_times(self):
        """Red = Green = Yellow = Red"""
        tl = TrafficLight()
        tl.change_state()
        tl.change_state()
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Red")

    def test_multiple_full_cycles(self):
        """Two full cycles should return to Red"""
        tl = TrafficLight()
        for _ in range(6):
            tl.change_state()
        self.assertEqual(tl.get_current_state(), "Red")
