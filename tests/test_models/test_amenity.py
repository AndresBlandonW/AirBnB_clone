#!/usr/bin/python3
"""Test for Amenity class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
    """Unit test for Amenitity class """

    @classmethod
    def setUp(cls):
        print('SetupC lass')

    @classmethod
    def tearDown(cls):
        print('TearDown Class')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.a1 = Amenity()
        self.a2 = Amenity()

    def tearDown(self):
        """Unit test tear down"""
        del self.a1
        del self.a2

    def test_init(self):
        """Test for init method"""
        self.assertIsNotNone(self.a1)
        self.assertIsInstance(self.a1, BaseModel)
        self.assertIs(type(self.a1), Amenity)

    def test_uuid(self):
        """Test for uuid attribute"""
        self.assertTrue(hasattr(self.a1, "id"))
        self.assertNotEqual(self.a1.id, self.a2.id)
        self.assertIsInstance(self.a1.id, str)

    def test_name(self):
        """Test for name attribute"""
        self.assertTrue(hasattr(self.a1, "name"))
        self.assertEqual(self.a1.name, "")
        self.assertIsInstance(self.a1.name, str)

    def test_str(self):
        """Test for __str__ method"""
        result = len(self.a1.__str__())
        self.assertTrue(result, 172)

    def test_save(self):
        """Test for save method"""
        prechange = self.a1.updated_at
        self.a1.save()
        postchange = self.a1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_created_at(self):
        """Test for created at time"""
        self.assertTrue(hasattr(self.a1, "created_at"))

    def test_updated_at(self):
        """Test for the updated at time attr"""
        prechange = self.a1.updated_at
        self.a1.save()
        postchange = self.a1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_kwargs(self):
        """Test for kwargs"""
        self.a1.name = "Holberton"
        self.a1.my_number = 89
        a1_json = self.a1.to_dict()

        a2 = BaseModel(**a1_json)
        self.assertEqual(self.a1.id, a2.id)
        self.assertEqual(self.a1.created_at, a2.created_at)
        self.assertEqual(self.a1.updated_at, a2.updated_at)
        self.assertEqual(self.a1.name, a2.name)
        self.assertEqual(self.a1.my_number, a2.my_number)

    def test_module_docstring(self):
        """Test for existence of module docstring"""
        result = len(__import__('models.amenity').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """Amenity Class Docstring Test"""
        print("test_class_docstring")
        result = len(Amenity.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """Amenity init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test__str__docstring(self):
        """Amenity __str__ Docstring Test"""
        print("testing __str__ docstring...")
        result = len(Amenity.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_save_docstring(self):
        """Amenity save method Docstring Test"""
        print("testing save docstring...")
        result = len(Amenity.save.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dict_docstring(self):
        """Amenity to_dict Docstring Test"""
        print("testing to_dict docstring...")
        result = len(Amenity.to_dict.__doc__)
        self.assertTrue(result > 0, True)

    if __name__ == "__main__":
        unittest.main()
