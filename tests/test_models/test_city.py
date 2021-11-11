#!/usr/bin/python3
"""Test for City class"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Unit test for City class"""

    @classmethod
    def setUp(cls):
        print('SetupClass')

    @classmethod
    def tearDown(cls):
        print('TearDownClass')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.c1 = City()
        self.c2 = City()

    def tearDown(self):
        """Unit test tear down"""
        del self.c1
        del self.c2

    def test_init(self):
        """Test for init method"""
        self.assertIsNotNone(self.c1)
        self.assertIsInstance(self.c1, BaseModel)
        self.assertIs(type(self.c1), City)

    def test_uuid(self):
        """Test for uuid attribute"""
        self.assertTrue(hasattr(self.c1, "id"))
        self.assertNotEqual(self.c1.id, self.c2.id)
        self.assertIsInstance(self.c1.id, str)

    def test_state_id(self):
        """Test for state_id attribute"""
        self.assertTrue(hasattr(self.c1, "state_id"))
        self.assertEqual(self.c1.state_id, "")
        self.assertIsInstance(self.c1.state_id, str)

    def test_name(self):
        """Test for name attribute"""
        self.assertTrue(hasattr(self.c1, "name"))
        self.assertEqual(self.c1.name, "")
        self.assertIsInstance(self.c1.name, str)

    def test_str(self):
        """Test for __str__ method"""
        result = len(self.c1.__str__())
        self.assertTrue(result, 172)

    def test_save(self):
        """Test for save method"""
        prechange = self.c1.updated_at
        self.c1.save()
        postchange = self.c1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_created_at(self):
        """Test for created at time"""
        self.assertTrue(hasattr(self.c1, "created_at"))

    def test_updated_at(self):
        """Test for the updated at time attr"""
        prechange = self.c1.updated_at
        self.c1.save()
        postchange = self.c1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_kwargs(self):
        """Test for kwargs"""
        self.c1.name = "Holberton"
        self.c1.my_number = 89
        c1_json = self.c1.to_dict()

        c2 = BaseModel(**c1_json)
        self.assertEqual(self.c1.id, c2.id)
        self.assertEqual(self.c1.created_at, c2.created_at)
        self.assertEqual(self.c1.updated_at, c2.updated_at)
        self.assertEqual(self.c1.name, c2.name)
        self.assertEqual(self.c1.my_number, c2.my_number)

    def test_module_docstring(self):
        """Test for existence of module docstring"""
        print("testing module docstring...")
        result = len(__import__('models.city').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """City Class Docstring Test"""
        print("test_class_docstring")
        result = len(City.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """City init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test__str__docstring(self):
        """City __str__ Docstring Test"""
        print("testing __str__ docstring...")
        result = len(City.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_save_docstring(self):
        """City save method Docstring Test"""
        print("testing save docstring...")
        result = len(City.save.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dict_docstring(self):
        """City to_dict Docstring Test"""
        print("testing to_dict docstring...")
        result = len(City.to_dict.__doc__)
        self.assertTrue(result > 0, True)

    if __name__ == "__main__":
        unittest.main()
