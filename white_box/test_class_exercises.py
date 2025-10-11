# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    calculate_total_discount,

    celsius_to_fahrenheit,
    White-box-tests
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_password,
    validate_credit_card,
    validate_date,
    check_flight_eligibility,
    validate_url,
    calculate_quantity_discount,
    check_file_size,
    check_loan_eligibility,
    calculate_shipping_cost,
    grade_quiz,
    authenticate_user,
    get_weather_advisory,
    UserAuthentication,
    DocumentEditingSystem,
    ElevatorSystem,
    calculate_total_discount,
    calculate_order_total,
    calculate_items_shipping_cost,
    validate_login,
    verify_age,
    categorize_product,
    validate_email,
    White-box-tests
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


class TestCheckNumberStatus(unittest.TestCase):
    """
    Check number status unit tests.
    """

    def test_check_number_status_negative(self):
        """
        Checks negative number.
        """
        self.assertEqual(check_number_status(-5), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_check_number_status_positive_even(self):
        """
        Checks positive even number.
        """
        self.assertEqual(check_number_status(8), "Positive")

    def test_check_number_status_positive_odd(self):
        """
        Checks positive odd number.
        """
        self.assertEqual(check_number_status(7), "Positive")


class TestValidatePassword(unittest.TestCase):
    """
    Validate password unit tests.
    """

    def test_validate_password_too_short(self):
        """
        Checks password length.
        """
        self.assertFalse(validate_password("short"))

    def test_validate_password_no_number(self):
        """
        Checks password for numbers.
        """
        self.assertFalse(validate_password("NoNumber"))

    def test_validate_password_no_uppercase(self):
        """
        Checks password for uppercase letters.
        """
        self.assertFalse(validate_password("nouppercase1"))

    def test_validate_password_no_special_characters(self):
        """
        Checks password for special characters.
        """
        self.assertFalse(validate_password("NoSpecial1"))

    def test_validate_password_valid(self):
        """
        Checks valid password.
        """
        self.assertTrue(validate_password("Valid1Password!"))


class TestCalculateTotalDiscount(unittest.TestCase):
    """
    Calculate total discount unit tests.
    """

    def test_calculate_total_discount_no_discount(self):
        """
        Checks no discount applied.
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_10_percent_lower_limit(self):
        """
        Checks 10 percent discount applied for lower limit.
        """
        self.assertEqual(calculate_total_discount(100), 10)

    def test_calculate_total_discount_10_percent_upper_limit(self):
        """
        Checks 10 percent discount applied for upper limit.
        """
        self.assertEqual(calculate_total_discount(500), 50)

    def test_calculate_total_discount_20_percent(self):
        """
        Checks 20 percent discount applied.
        """
        self.assertEqual(calculate_total_discount(501), 100.2)


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

# 11 a 21 

class TestValidateCreditCard(unittest.TestCase):
    def test_valid_lengths_and_digits(self):
        self.assertEqual(validate_credit_card("0" * 13), "Valid Card")
        self.assertEqual(validate_credit_card("1" * 16), "Valid Card")

    def test_invalid_by_length_or_chars(self):
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")
        self.assertEqual(validate_credit_card("1234abcd5678"), "Invalid Card")


class TestValidateDate(unittest.TestCase):
    def test_valid_bounds(self):
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_invalid_bounds(self):
        self.assertEqual(validate_date(1899, 12, 31), "Invalid Date")
        self.assertEqual(validate_date(2101, 1, 1), "Invalid Date")
        self.assertEqual(validate_date(2000, 0, 10), "Invalid Date")
        self.assertEqual(validate_date(2000, 13, 10), "Invalid Date")
        self.assertEqual(validate_date(2000, 5, 0), "Invalid Date")
        self.assertEqual(validate_date(2000, 5, 32), "Invalid Date")


class TestCheckFlightEligibility(unittest.TestCase):
    def test_age_in_range(self):
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_out_of_range_without_ff(self):
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")
        self.assertEqual(check_flight_eligibility(70, False), "Not Eligible to Book")

    def test_frequent_flyer_overrides_age(self):
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")


class TestValidateUrl(unittest.TestCase):
    def test_valid_http_https(self):
        self.assertEqual(validate_url("http://example.com"), "Valid URL")
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_invalid_scheme(self):
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_https_length_ignores_limit_due_to_logic(self):
        long_host = "a" * 260
        self.assertEqual(validate_url(f"https://{long_host}.com"), "Valid URL")


class TestCalculateQuantityDiscount(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_five_percent(self):
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_ten_percent(self):
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")


class TestCheckFileSize(unittest.TestCase):
    def test_valid_limits(self):
        self.assertEqual(check_file_size(0), "Valid File Size")
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_invalid_limits(self):
        self.assertEqual(check_file_size(-1), "Invalid File Size")
        self.assertEqual(check_file_size(1048577), "Invalid File Size")


class TestCheckLoanEligibility(unittest.TestCase):
    def test_not_eligible_low_income(self):
        self.assertEqual(check_loan_eligibility(25000, 800), "Not Eligible")

    def test_mid_income_secured_or_standard(self):
        self.assertEqual(check_loan_eligibility(40000, 650), "Secured Loan")
        self.assertEqual(check_loan_eligibility(40000, 720), "Standard Loan")

    def test_high_income(self):
        self.assertEqual(check_loan_eligibility(80000, 760), "Premium Loan")
        self.assertEqual(check_loan_eligibility(80000, 700), "Standard Loan")


class TestCalculateShippingCost(unittest.TestCase):
    def test_small_package(self):
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_medium_package(self):
        self.assertEqual(calculate_shipping_cost(5, 11, 11, 11), 10)
        self.assertEqual(calculate_shipping_cost(2, 30, 30, 30), 10)

    def test_otherwise_20(self):
        self.assertEqual(calculate_shipping_cost(0.5, 15, 10, 10), 20)
        self.assertEqual(calculate_shipping_cost(2, 10, 11, 11), 20)


class TestGradeQuiz(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(grade_quiz(7, 2), "Pass")
        self.assertEqual(grade_quiz(10, 0), "Pass")

    def test_conditional_pass(self):
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(8, 3), "Conditional Pass")

    def test_fail(self):
        self.assertEqual(grade_quiz(6, 4), "Fail")
        self.assertEqual(grade_quiz(4, 0), "Fail")


class TestAuthenticateUser(unittest.TestCase):
    def test_admin(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_user(self):
        self.assertEqual(authenticate_user("userx", "password8"), "User")

    def test_invalid(self):
        self.assertEqual(authenticate_user("usr", "password8"), "Invalid")
        self.assertEqual(authenticate_user("userx", "short"), "Invalid")


class TestGetWeatherAdvisory(unittest.TestCase):
    def test_heat_and_humidity(self):
        self.assertEqual(
            get_weather_advisory(31, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_cold(self):
        self.assertEqual(
            get_weather_advisory(-1, 50), "Low Temperature. Bundle Up!"
        )

    def test_neutral(self):
        self.assertEqual(
            get_weather_advisory(20, 50), "No Specific Advisory"
        )



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


class TestWhiteBoxValidatePassword(unittest.TestCase):
    """Unit tests for 2: validate_password"""

    def test_valid_password(self):
        self.assertTrue(validate_password("Ab1!bcde"))

    def test_too_short(self):
        self.assertFalse(validate_password("Aa1!a"))

    def test_missing_uppercase(self):
        self.assertFalse(validate_password("aa1!aaaa"))

    def test_missing_lowercase(self):
        self.assertFalse(validate_password("AA1!AAAA"))

    def test_missing_digit(self):
        self.assertFalse(validate_password("Aa!aaaaa"))

    def test_missing_special(self):
        self.assertFalse(validate_password("Aa1aaaaa"))


class TestWhiteBoxCalculateTotalDiscount(unittest.TestCase):
    """Unit tests for 3: calculate_total_discount"""

    def test_no_discount_below_100(self):
        self.assertEqual(calculate_total_discount(99), 0)

    def test_10_percent_at_100(self):
        self.assertEqual(calculate_total_discount(100), 10)

    def test_10_percent_at_500(self):
        self.assertEqual(calculate_total_discount(500), 50)

    def test_20_percent_above_500(self):
        self.assertEqual(calculate_total_discount(750), 150)


class TestWhiteBoxCalculateOrderTotal(unittest.TestCase):
    """Unit tests for 4: calculate_order_total"""

    def test_no_discount_qty_1_5(self):
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_5_percent_qty_6_10(self):
        items = [{"quantity": 6, "price": 10}]
        self.assertEqual(calculate_order_total(items), 6 * 10 * 0.95)

    def test_10_percent_qty_over_10(self):
        items = [{"quantity": 11, "price": 10}]
        self.assertEqual(calculate_order_total(items), 11 * 10 * 0.9)

    def test_mixed_items(self):
        items = [
            {"quantity": 2, "price": 50},   
            {"quantity": 7, "price": 20},   
            {"quantity": 12, "price": 5},  
        ]
        expected = (2 * 50) + (0.95 * 7 * 20) + (0.9 * 12 * 5)
        self.assertAlmostEqual(calculate_order_total(items), expected, places=2)


class TestWhiteBoxShippingCost(unittest.TestCase):
    """Unit tests for 5: calculate_items_shipping_cost"""

    def test_standard_tiers(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 5}], "standard"), 10)
        self.assertEqual(calculate_items_shipping_cost([{"weight": 9}], "standard"), 15)
        self.assertEqual(calculate_items_shipping_cost([{"weight": 11}], "standard"), 20)

    def test_express_tiers(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 5}], "express"), 20)
        self.assertEqual(calculate_items_shipping_cost([{"weight": 9}], "express"), 30)
        self.assertEqual(calculate_items_shipping_cost([{"weight": 11}], "express"), 40)

    def test_invalid_method(self):
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost([{"weight": 2}], "fast")


class TestWhiteBoxValidateLogin(unittest.TestCase):
    """Unit tests for 6: validate_login"""

    def test_successful_login(self):
        self.assertEqual(validate_login("user123", "Password1!"), "Login Successful")

    def test_username_too_short(self):
        self.assertEqual(validate_login("usr", "Password1!"), "Login Failed")

    def test_username_too_long(self):
        self.assertEqual(validate_login("u" * 21, "Password1!"), "Login Failed")

    def test_password_too_short(self):
        self.assertEqual(validate_login("username", "P1short"), "Login Failed")

    def test_password_too_long(self):
        self.assertEqual(validate_login("username", "X" * 16), "Login Failed")


class TestWhiteBoxVerifyAge(unittest.TestCase):
    """Unit tests for 7: verify_age"""

    def test_bounds_eligible(self):
        self.assertEqual(verify_age(18), "Eligible")
        self.assertEqual(verify_age(65), "Eligible")

    def test_underage(self):
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_overage(self):
        self.assertEqual(verify_age(66), "Not Eligible")


class TestWhiteBoxCategorizeProduct(unittest.TestCase):
    """Unit tests for 8: categorize_product"""

    def test_category_a(self):
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")

    def test_category_b(self):
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")

    def test_category_c(self):
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")

    def test_category_d(self):
        self.assertEqual(categorize_product(9), "Category D")
        self.assertEqual(categorize_product(201), "Category D")


class TestWhiteBoxValidateEmail(unittest.TestCase):
    """Unit tests for 9: validate_email"""

    def test_valid_email(self):
        self.assertEqual(validate_email("user@example.com"), "Valid Email")

    def test_too_short(self):
        self.assertEqual(validate_email("a@b"), "Invalid Email")

    def test_too_long(self):
        long_email = ("u" * 49) + "@a.co"
        self.assertEqual(validate_email(long_email), "Invalid Email")

    def test_missing_at(self):
        self.assertEqual(validate_email("userexample.com"), "Invalid Email")

    def test_missing_dot(self):
        self.assertEqual(validate_email("user@examplecom"), "Invalid Email")
