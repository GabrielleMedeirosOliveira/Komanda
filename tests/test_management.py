import unittest

from freezegun import freeze_time
from management.tab_handler import calculate_tab


class TestTabHandler(unittest.TestCase):
    @freeze_time("2011-10-11 12:00:00")
    def test_calculate_tab_subtotal_and_created_at(self):
        table_1 = [{"id": 7, "amount": 3}, {"id": 3, "amount": 2}]
        result = calculate_tab(table_1)
        expected = {"subtotal": 20.0, "created_at": "11/10/2011 12:00:00"}

        self.assertEqual(
            result["subtotal"],
            expected["subtotal"],
            "Verifique se o cálculo do subtotal está sendo feito corretamente",
        )

        self.assertEqual(
            result["created_at"],
            expected["created_at"],
            "Verifique se o formato da data retornada em `created_at` é `dd/mm/yyyy HH:MM:SS`",
        )
