#!/usr/bin/python3
"""Test for State class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestBaseModel(unittest.TestCase):
    """Unit test for State class"""

    @classmethod
    def setUp(cls):
        print('Setup Class')

    @classmethod
    def tearDown(cls):
        print('TearDown Class')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.s1 = State()
        self.s2 = State()

    def tearDown(self):
        """Unit test tear down"""
        del self.s1
        del self.s2

    def test_init(self):
        """Test for init method"""
        self.assertIsNotNone(self.s1)
        self.assertIsInstance(self.s1, BaseModel)
        self.assertIs(type(self.s1), State)

    def test_uuid(self):
        """Test for uuid attribute"""
        self.assertTrue(hasattr(self.s1, "id"))
        self.assertNotEqual(self.s1.id, self.s2.id)
        self.assertIsInstance(self.s1.id, str)

    def test_name(self):
        """Test for name attribute"""
        self.assertTrue(hasattr(self.s1, "name"))
        self.assertEqual(self.s1.name, "")
        self.assertIsInstance(self.s1.name, str)

    def test_str(self):
        """Test for __str__ method"""
        result = len(self.s1.__str__())
        self.assertTrue(result, 172)

    def test_save(self):
        """Test for save method"""
        prechange = self.s1.updated_at
        self.s1.save()
        postchange = self.s1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_created_at(self):
        """Test for created at time"""
        self.assertTrue(hasattr(self.s1, "created_at"))

    def test_updated_at(self):
        """Test for the updated at time attr"""
        prechange = self.s1.updated_at
        self.s1.save()
        postchange = self.s1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_kwargs(self):
        """Test for kwargs"""
        self.s1.name = "Holberton"
        self.s1.my_number = 89
        s1_json = self.s1.to_dict()

        s2 = State(**s1_json)
        self.assertEqual(self.s1.id, s2.id)
        self.assertEqual(self.s1.created_at, s2.created_at)
        self.assertEqual(self.s1.updated_at, s2.updated_at)
        self.assertEqual(self.s1.name, s2.name)
        self.assertEqual(self.s1.my_number, s2.my_number)

    def test_module_docstring(self):
        """Test for existence of module docstring"""
        print("testing module docstring...")
        result = len(__import__('models.state').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """State Class Docstring Test"""
        print("test_class_docstring")
        result = len(State.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """State init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test__str__docstring(self):
        """State __str__ Docstring Test"""
        result = len(State.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_save_docstring(self):
        """State save method Docstring Test"""
        print("testing save docstring...")
        result = len(State.save.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dict_docstring(self):
        """State to_dict Docstring Test"""
        print("testing to_dict docstring...")
        result = len(State.to_dict.__doc__)
        self.assertTrue(result > 0, True)

    if __name__ == "__main__":
        unittest.main()
