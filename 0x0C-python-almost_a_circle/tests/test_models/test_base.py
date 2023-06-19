import unittest
import json
import csv
from unittest.mock import patch, MagicMock
from base import Base

class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        # Test when list_dictionaries is None
        self.assertEqual(Base.to_json_string(None), "[]")

        # Test when list_dictionaries is an empty list
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test when list_dictionaries contains dictionaries
        dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        expected_json = json.dumps(dicts)
        self.assertEqual(Base.to_json_string(dicts), expected_json)

    def test_save_to_file(self):
        # Test when list_objs is None
        with patch('builtins.open', MagicMock()) as mock_open:
            Base.save_to_file(None)
            mock_open.assert_called_with('Base.json', 'w')
            mock_open.return_value.write.assert_called_with("[]")

        # Test when list_objs is an empty list
        with patch('builtins.open', MagicMock()) as mock_open:
            Base.save_to_file([])
            mock_open.assert_called_with('Base.json', 'w')
            mock_open.return_value.write.assert_called_with("[]")

        # Test when list_objs contains objects
        obj1 = Base(1)
        obj2 = Base(2)
        objects = [obj1, obj2]
        expected_dicts = [obj1.to_dictionary(), obj2.to_dictionary()]
        expected_json = json.dumps(expected_dicts)
        with patch('builtins.open', MagicMock()) as mock_open:
            Base.save_to_file(objects)
            mock_open.assert_called_with('Base.json', 'w')
            mock_open.return_value.write.assert_called_with(expected_json)

    def test_from_json_string(self):
        # Test when json_string is None
        self.assertEqual(Base.from_json_string(None), [])

        # Test when json_string is an empty string
        self.assertEqual(Base.from_json_string(""), [])

        # Test when json_string represents a list of dictionaries
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        expected_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        self.assertEqual(Base.from_json_string(json_string), expected_dicts)

    def test_create(self):
        # Test when cls.__name__ is "Rectangle"
        with patch('base.Rectangle') as mock_Rectangle:
            dictionary = {'id': 1, 'width': 10, 'height': 20}
            obj = Base.create(**dictionary)
            mock_Rectangle.assert_called_with(1, 1)
            obj.update.assert_called_with(**dictionary)
            self.assertEqual(obj, mock_Rectangle.return_value)

        # Test when cls.__name__ is not "Rectangle"
        with patch('base.Square') as mock_Square:
            dictionary = {'id': 1, 'size': 10}
            obj = Base.create(**dictionary)
            mock_Square.assert_called_with(1)
            obj.update.assert_called_with(**dictionary)
            self.assertEqual(obj, mock_Square.return_value)

    def test_load_from_file(self):
        # Test when file exists
        expected_objs = [Base(1), Base(2), Base(3)]
        expected_dicts = [obj.to_dictionary() for obj in expected_objs]
        expected_json = json.dumps(expected_dicts)
        with patch('builtins.open', MagicMock()) as mock_open:
            mock_open.return_value.read.return_value = expected_json
            objs = Base.load_from_file()
            mock_open.assert_called_with('Base.json', 'r')
            self.assertEqual(objs, expected_objs)

        # Test when file does not exist
        with patch('builtins.open', MagicMock(side_effect=IOError())):
            objs = Base.load_from_file()
            self.assertEqual(objs, [])

    def test_save_to_file_csv(self):
        # Test when list_objs is None
        with patch('builtins.open', MagicMock()) as mock_open:
            Base.save_to_file_csv(None)
            mock_open.assert_called_with('Base.csv', 'w', newline='')
            mock_open.return_value.write.assert_called_with("")

        # Test when list_objs is an empty list
        with patch('builtins.open', MagicMock()) as mock_open:
            Base.save_to_file_csv([])
            mock_open.assert_called_with('Base.csv', 'w', newline='')
            mock_open.return_value.write.assert_called_with("")

        # Test when list_objs contains objects
        obj1 = Base(1)
        obj2 = Base(2)
        objects = [obj1, obj2]
        expected_dicts = [obj1.to_dictionary(), obj2.to_dictionary()]
        expected_header = "id,size,x,y\n"
        expected_csv = expected_header + "1,,0,0\n2,,0,0\n"
        with patch('builtins.open', MagicMock()) as mock_open:
            writer_mock = MagicMock()
            csv_mock = MagicMock(writer=writer_mock)
            mock_open.return_value.__enter__.return_value = csv_mock
            Base.save_to_file_csv(objects)
            mock_open.assert_called_with('Base.csv', 'w', newline='')
            writer_mock.writeheader.assert_called_with()
            writer_mock.writerow.assert_any_call(expected_dicts[0])
            writer_mock.writerow.assert_any_call(expected_dicts[1])

    def test_load_from_file_csv(self):
        # Test when file exists
        expected_objs = [Base(1), Base(2), Base(3)]
        expected_dicts = [obj.to_dictionary() for obj in expected_objs]
        expected_csv = "id,size,x,y\n1,,0,0\n2,,0,0\n3,,0,0\n"
        with patch('builtins.open', MagicMock()) as mock_open:
            reader_mock = MagicMock()
            csv_mock = MagicMock(reader=reader_mock)
            mock_open.return_value.__enter__.return_value = csv_mock
            reader_mock.__iter__.return_value = expected_dicts
            objs = Base.load_from_file_csv()
            mock_open.assert_called_with('Base.csv', 'r', newline='')
            self.assertEqual(objs, expected_objs)

        # Test when file does not exist
        with patch('builtins.open', MagicMock(side_effect=IOError())):
            objs = Base.load_from_file_csv()
            self.assertEqual(objs, [])

if __name__ == '__main__':
    unittest.main()
