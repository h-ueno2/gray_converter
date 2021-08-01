import unittest


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
