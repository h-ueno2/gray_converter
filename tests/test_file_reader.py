from gray_encorder.file_info import FileInfo
import unittest
from tempfile import TemporaryDirectory
import os


class IsExistsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = TemporaryDirectory()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_is_exsits(self):
        from gray_encorder.file_reader import FileReader
        test_dir = os.path.join(self.tmp.name, 'test')
        os.mkdir(test_dir)
        reader = FileReader(test_dir)
        self.assertEqual(True, reader.is_exists)

    def test_not_is_exists(self):
        from gray_encorder.file_reader import FileReader
        test_dir = os.path.join(self.tmp.name, 'test')
        reader = FileReader(test_dir)
        self.assertEqual(False, reader.is_exists)


class IsImageFileTest(unittest.TestCase):
    def test_is_image_file(self):
        from gray_encorder.file_reader import FileReader

        params = (
            {'target': 'test.JPG'},
            {'target': 'test.jpg'},
            {'target': 'test.PNG'},
            {'target': 'test.png'},
            {'target': 'test.GIF'},
            {'target': 'test.gif'},
        )
        reader = FileReader('')
        for param in params:
            with self.subTest(**param):
                actual = reader.is_image_file(param['target'])
                self.assertEqual(True, actual)

    def test_not_is_image_file(self):
        from gray_encorder.file_reader import FileReader

        params = (
            {'target': 'test.JP'},
            {'target': 'test.txt'},
            {'target': 'test.md'},
            {'target': ''},
            {'target': None},
        )
        reader = FileReader('')
        for param in params:
            with self.subTest(**param):
                actual = reader.is_image_file(param['target'])
                self.assertEqual(False, actual)


class ListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = TemporaryDirectory()
        self.test_img_1 = os.path.join(self.tmp.name, 'test_img_1.png')
        self.test_img_2 = os.path.join(self.tmp.name, 'test_img_2.png')
        self.test_text = os.path.join(self.tmp.name, 'test_text.txt')
        test_paths = [
            self.test_img_1,
            self.test_img_2,
            self.test_text,
        ]
        for file in test_paths:
            with open(file,  'w') as f:
                f.write('')

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_dir_list(self):
        from gray_encorder.file_reader import FileReader

        reader = FileReader(self.tmp.name)
        actuals = reader.list(True)
        expecteds = [
            FileInfo(self.test_img_1, True),
            FileInfo(self.test_img_2, True),
        ]

        self.assertEqual(len(expecteds), len(actuals))
        for expected, actual in zip(expecteds, actuals):
            self.assertEqual(expected.file_name, actual.file_name)
            self.assertEqual(expected.output_file_path,
                             actual.output_file_path)

    def test_file_list(self):
        from gray_encorder.file_reader import FileReader

        reader = FileReader(self.test_img_1)
        actuals = reader.list(True)
        expecteds = [
            FileInfo(self.test_img_1, True),
        ]

        self.assertEqual(len(expecteds), len(actuals))
        for expected, actual in zip(expecteds, actuals):
            self.assertEqual(expected.file_name, actual.file_name)
            self.assertEqual(expected.output_file_path,
                             actual.output_file_path)

    def test_not_image_file(self):
        from gray_encorder.file_reader import FileReader

        reader = FileReader(self.test_text)
        actuals = reader.list(True)
        expecteds = []

        self.assertEqual(len(expecteds), len(actuals))
