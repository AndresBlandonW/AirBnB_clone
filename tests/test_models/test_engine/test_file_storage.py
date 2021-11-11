#!/usr/bin/python3
"""Unit test for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unit test for FileStorage class"""

    @classmethod
    def setUp(cls):
        print('SetupClass')

    @classmethod
    def tearDown(cls):
        print('TearDownClass')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.fs1 = FileStorage()
        self.fs2 = FileStorage()

    def tearDown(self):
        """Unit test tear down"""
        del self.fs1
        del self.fs2

    def test_objects_dict(self):
        """Test for __objects"""
        print("testing __objects...")
        self.assertIsInstance(self.fs1, FileStorage)
        self.assertTrue(hasattr(self.fs1, "__objects"))
        self.assertIsInstance(self.fs1.__objects, dict)

    def test_file_path(self):
        """Test for __file_path"""
        print("testing __file_path...")
        self.assertIsInstance(self.fs1, FileStorage)
        self.assertTrue(hasattr(self.fs1, "__file_storage"))
        self.assertIsInstance(self.fs1.__file_path, str)

    def test_all(self):
        """Test for all method"""
        print("testing all method...")
        pass

    def test_new(self):
        """Test for new method"""
        print("Testing new method...")
        pass

    def test_save(self):
        """Test for save method"""
        print("Testing save method...")
        pass

    def test_reload(self):
        """Test for reload method"""
        print("Testing reload method...")
        pass

    if __name__ == "__main__":
        unittest.main()
