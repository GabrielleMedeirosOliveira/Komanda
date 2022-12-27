import os
import unittest

from utils.json_handler import read_json, write_json


class TestReadingJSON(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.read_filepath = "tests/data/test_menu.json"
        cls.empty_json_filepath = "tests/data/empty.json"

    def test_reading_existing_json(self):
        result = read_json(self.read_filepath)
        expected = [
            {"id": 1, "name": "ADICIONAL FRANGO 50G", "price": 4.0},
            {"id": 2, "name": "SALADA", "price": 18.0},
            {"id": 3, "name": "ADICIONAL DE LEITE", "price": 1.0},
            {"id": 4, "name": "AMERICANO", "price": 5.0},
            {"id": 5, "name": "CAPUCCINO", "price": 7.0},
            {"id": 6, "name": "CARIOCA", "price": 5.0},
            {"id": 7, "name": "COADO", "price": 6.0},
            {"id": 8, "name": "COADO PEQUENO", "price": 3.0},
        ]

        self.assertIsInstance(
            result,
            list,
            "Verifique se sua função `read_json` está retornando uma lista",
        )

        self.assertListEqual(
            result,
            expected,
            "Verifique se sua função `read_json` está retornando adequadamente os items do menu",
        )

    def test_reading_non_existing_json(self):
        result = read_json("non_existing_path.json")
        expected = []

        self.assertListEqual(
            result,
            expected,
            "Verifique se sua função `read_json` está retornando uma lista vazia caso o arquivo não exista",
        )

    def test_reading_empty_json(self):
        result = read_json(self.empty_json_filepath)
        expected = []

        self.assertListEqual(
            result,
            expected,
            "Verifique se sua função `read_json` está retornando uma lista vazia caso o arquivo esteja vazio",
        )


class TestWritingJSON(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.write_filepath = "tests/data/test_write.json"

    def tearDown(self) -> None:
        if os.path.exists(self.write_filepath):
            os.remove(self.write_filepath)

    def test_writing_non_existing_json(self):
        new_item = {"name": "CHURROS DO M5", "price": 5.0}
        result = write_json(self.write_filepath, new_item)
        expected = {"name": "CHURROS DO M5", "price": 5.0, "id": 1}

        self.assertEqual(
            result["id"],
            expected["id"],
            "Verifique se quando o arquivo está vazio, o id 1 é alocado para o novo item adicionado",
        )
