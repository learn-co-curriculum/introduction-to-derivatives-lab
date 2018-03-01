import unittest
from ipynb.fs.full.index import (derivative_of_graphed_function,
derivative_at_x_value_provided_tangent, output_at, df_dx,
polynomial_function_trace, tangent_line_delta, four_x_cubed_plus)

class IntroToDerivatives (unittest.TestCase):
    def test_derivative_of_graphed_function(self):
        self.assertEqual(derivative_of_graphed_function, 3)

    def test_derivative_at_x_value_provided_tangent(self):
        point_1 = {'x': 3.0, 'y': 5}
        point_2 = {'x': 3.5, 'y': 7}
        self.assertEqual(derivative_at_x_value_provided_tangent(point_1, point_2), 4.0)
        point_3 = {'x': 4.0, 'y': 9}
        point_4 = {'x': 4.5, 'y': 15}
        self.assertEqual(derivative_at_x_value_provided_tangent(point_3, point_4), 12.0)

    def test_four_x_cubed_plus(self):
        self.assertEqual(four_x_cubed_plus, [(4, 3), (11, 2)])

    def test_output_at(self):
        second_terms = [(3, 2), (-11, 0)]
        self.assertEqual(output_at(second_terms, 1), -8)
        self.assertEqual(output_at(second_terms, 3), 16)

    def test_df_dx(self):
        third_terms = [(2, 3), (7, 1)]
        delta_value = .001
        x_value = 2
        self.assertEqual(df_dx(third_terms, x_value, delta_value), 31.012)






    def test_polynomial_trace(self):
        three_x_cubed_plus = [(3, 3), (-11, 0)]
        three_x_cubed_plus_trace = {'x': [-4, -3, -2, -1, 0, 1, 2, 3],
        'y': [-203, -92, -35, -14, -11, -8, 13, 70]}
        self.assertEqual(polynomial_function_trace(three_x_cubed_plus, list(range(-4, 4))), three_x_cubed_plus_trace)

    def test_tangent_line_delta(self):
        three_x_cubed_plus = [(3, 3), (-11, 0)]
        self.assertEqual(tangent_line_delta(three_x_cubed_plus, 3, line_length = 4, delta = .00001), {'x': [-1, 3, 7], 'y': [-254.0, 70, 394.0]})
