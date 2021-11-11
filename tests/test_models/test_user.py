#!/usr/bin/python3
"""Test for User class"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """Unit test for User class"""

    @classmethod
    def setUp(cls):
        print('SetupClass')

    @classmethod
    def tearDown(cls):
        print('TearDownClass')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.u1 = User()
        self.u2 = User()

    def tearDown(self):
        """Unit test tear down"""
        del self.u1
        del self.u2

    def test_init(self):
        """Test for init method"""
        self.assertIsNotNone(self.u1)
        self.assertIsInstance(self.u1, BaseModel)
        self.assertIs(type(self.u1), User)

    def test_uuid(self):
        """Test for uuid attribute"""
        self.assertTrue(hasattr(self.u1, "id"))
        self.assertNotEqual(self.u1.id, self.u2.id)
        self.assertIsInstance(self.u1.id, str)

    def test_email(self):
        """Test for email attribute"""
        self.assertTrue(hasattr(self.u1, "email"))
        self.assertEqual(self.u1.email, "")
        self.assertIsInstance(self.u1.email, str)

    def test_first_name(self):
        """Test for first_name attribute"""
        self.assertTrue(hasattr(self.u1, "first_name"))
        self.assertEqual(self.u1.first_name, "")
        self.assertIsInstance(self.u1.first_name, str)

    def test_last_name(self):
        """Test for last_name attribute"""
        self.assertTrue(hasattr(self.u1, "last_name"))
        self.assertEqual(self.u1.last_name, "")
        self.assertIsInstance(self.u1.last_name, str)

    def test_str(self):
        """Test for __str__ method"""
        result = len(self.u1.__str__())
        self.assertTrue(result, 172)

    def test_save(self):
        """Test for save method"""
        prechange = self.u1.updated_at
        self.u1.save()
        postchange = self.u1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_created_at(self):
        """Test for created at time"""
        self.assertTrue(hasattr(self.u1, "created_at"))

    def test_updated_at(self):
        """Test for the updated at time attr"""
        prechange = self.u1.updated_at
        self.u1.save()
        postchange = self.u1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_kwargs(self):
        """Test for kwargs"""
        self.u1.name = "Holberton"
        self.u1.my_number = 89
        u1_json = self.u1.to_dict()

        u2 = User(**u1_json)
        self.assertEqual(self.u1.id, u2.id)
        self.assertEqual(self.u1.created_at, u2.created_at)
        self.assertEqual(self.u1.updated_at, u2.updated_at)
        self.assertEqual(self.u1.name, u2.name)
        self.assertEqual(self.u1.my_number, u2.my_number)

    def test_module_docstring(self):
        """Test for existence of module docstring"""
        print("testing module docstring...")
        result = len(__import__('models.user').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """User Class Docstring Test"""
        print("test_class_docstring")
        result = len(User.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """User init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test__str__docstring(self):
        """User __str__ Docstring Test"""
        print("testing __str__ docstring...")
        result = len(User.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_save_docstring(self):
        """User save method Docstring Test"""
        print("testing save docstring...")
        result = len(User.save.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dict_docstring(self):
        """User to_dict Docstring Test"""
        print("testing to_dict docstring...")
        result = len(User.to_dict.__doc__)
        self.assertTrue(result > 0, True)

    if __name__ == "__main__":
        unittest.main()
