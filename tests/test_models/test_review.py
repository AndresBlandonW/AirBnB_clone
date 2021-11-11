#!/usr/bin/python3
"""Test for City class"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestBaseModel(unittest.TestCase):
    """Unit test for City class"""

    @classmethod
    def setUp(cls):
        print('Setup Class')

    @classmethod
    def tearDown(cls):
        print('TearDown Class')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.r1 = Review()
        self.r2 = Review()

    def tearDown(self):
        """Unit test tear down"""
        del self.r1
        del self.r2

    def test_init(self):
        """Test for init method"""
        self.assertIsNotNone(self.r1)
        self.assertIsInstance(self.r1, BaseModel)
        self.assertIs(type(self.r1), Review)

    def test_uuid(self):
        """Test for uuid attribute"""
        self.assertTrue(hasattr(self.r1, "id"))
        self.assertNotEqual(self.r1.id, self.r2.id)
        self.assertIsInstance(self.r1.id, str)

    def test_place_id(self):
        """Test for place_id attribute"""
        self.assertTrue(hasattr(self.r1, "place_id"))
        self.assertEqual(self.r1.place_id, "")
        self.assertIsInstance(self.r1.place_id, str)

    def test_user_id(self):
        """Test for user_id attribute"""
        self.assertTrue(hasattr(self.r1, "user_id"))
        self.assertEqual(self.r1.user_id, "")
        self.assertIsInstance(self.r1.user_id, str)

    def test_text(self):
        """Test for text attribute"""
        self.assertTrue(hasattr(self.r1, "text"))
        self.assertEqual(self.r1.text, "")
        self.assertIsInstance(self.r1.text, str)

    def test_str(self):
        """Test for __str__ method"""
        result = len(self.r1.__str__())
        self.assertTrue(result, 172)

    def test_save(self):
        """Test for save method"""
        prechange = self.r1.updated_at
        self.r1.save()
        postchange = self.r1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_created_at(self):
        """Test for created at time"""
        self.assertTrue(hasattr(self.r1, "created_at"))

    def test_updated_at(self):
        """Test for the updated at time attr"""
        prechange = self.r1.updated_at
        self.r1.save()
        postchange = self.r1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_kwargs(self):
        """Test for kwargs"""
        self.r1.name = "Holberton"
        self.r1.my_number = 89
        r1_json = self.r1.to_dict()

        r2 = BaseModel(**r1_json)
        self.assertEqual(self.r1.id, r2.id)
        self.assertEqual(self.r1.created_at, r2.created_at)
        self.assertEqual(self.r1.updated_at, r2.updated_at)
        self.assertEqual(self.r1.name, r2.name)
        self.assertEqual(self.r1.my_number, r2.my_number)

    def test_module_docstring(self):
        """Test for existence of module docstring"""
        print("testing module docstring...")
        result = len(__import__('models.review').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """Review Class Docstring Test"""
        print("test_class_docstring")
        result = len(Review.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """Review init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test__str__docstring(self):
        """Review __str__ Docstring Test"""
        print("testing __str__ docstring...")
        result = len(Review.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_save_docstring(self):
        """Review save method Docstring Test"""
        print("testing save docstring...")
        result = len(Review.save.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dict_docstring(self):
        """Review to_dict Docstring Test"""
        print("testing to_dict docstring...")
        result = len(Review.to_dict.__doc__)
        self.assertTrue(result > 0, True)

    if __name__ == "__main__":
        unittest.main()
