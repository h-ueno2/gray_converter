from tempfile import TemporaryDirectory
import unittest
import os
from unittest.case import expectedFailure
from pathlib import Path


class FileNameTest(unittest.TestCase):
    def test_get_file_base_name(self):
        from gray_encorder.file_info import FileInfo
        path = os.path.join('test', 'sample.txt')
        file_info = FileInfo(path, True)
        actual = file_info.file_name
        expected = 'sample.txt'

        self.assertEqual(expected, actual)


class OutputFilePathTest(unittest.TestCase):
    def test_is_overwrite(self):
        from gray_encorder.file_info import FileInfo
        path = os.path.join('test', 'sample.txt')

        params = (
            {'is_overwrite': True,
             'expected': os.path.join('test', 'sample.txt')},
            {'is_overwrite': False,
             'expected': os.path.join('test', 'gray', 'sample.txt')}
        )

        for param in params:
            with self.subTest(**param):
                file_info = FileInfo(path, param['is_overwrite'])
                actual = file_info.output_file_path
                expected = param['expected']
                self.assertEqual(expected, actual)


class OutputDirPathTest(unittest.TestCase):
    def test_is_overwrite(self):
        from gray_encorder.file_info import FileInfo
        path = os.path.join('test', 'tst', 'sample.txt')

        params = (
            {'is_overwrite': True,
             'expected': os.path.join('test', 'tst')},
            {'is_overwrite': False,
             'expected': os.path.join('test', 'tst', 'gray')}
        )

        for param in params:
            with self.subTest(**param):
                file_info = FileInfo(path, param['is_overwrite'])
                actual = file_info.output_dir_path
                expected = param['expected']
                self.assertEqual(expected, actual)
