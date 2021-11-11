#!/usr/bin/python3
"""Test for Place class"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestBaseModel(unittest.TestCase):
    """Unit test for Place class"""

    @classmethod
    def setUp(cls):
        print('SetupClass')

    @classmethod
    def tearDown(cls):
        print('TearDownClass')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.p1 = Place()
        self.p2 = Place()

    def tearDown(self):
        """Unit test tear down"""
        del self.p1
        del self.p2

    def test_init(self):
        """Test for init method"""
        print("testing init...")
        self.assertIsNotNone(self.p1)
        self.assertIsInstance(self.p1, BaseModel)
        self.assertIs(type(self.p1), Place)

    def test_uuid(self):
        """Test for uuid attribute"""
        self.assertTrue(hasattr(self.p1, "id"))
        self.assertNotEqual(self.p1.id, self.p2.id)
        self.assertIsInstance(self.p1.id, str)

    def test_city_id(self):
        """Test for city_id attribute"""
        self.assertTrue(hasattr(self.p1, "city_id"))
        self.assertEqual(self.p1.city_id, "")
        self.assertIsInstance(self.p1.city_id, str)

    def test_user_id(self):
        """Test for user_id attribute"""
        self.assertTrue(hasattr(self.p1, "user_id"))
        self.assertEqual(self.p1.user_id, "")
        self.assertIsInstance(self.p1.user_id, str)

    def test_name(self):
        """Test for name attribute"""
        self.assertTrue(hasattr(self.p1, "name"))
        self.assertEqual(self.p1.name, "")
        self.assertIsInstance(self.p1.name, str)

    def test_description(self):
        """Test for description attribute"""
        self.assertTrue(hasattr(self.p1, "description"))
        self.assertEqual(self.p1.description, "")
        self.assertIsInstance(self.p1.description, str)

    def test_number_rooms(self):
        """Test for number_rooms attribute"""
        self.assertTrue(hasattr(self.p1, "number_rooms"))
        self.assertEqual(self.p1.number_rooms, 0)
        self.assertIsInstance(self.p1.number_rooms, int)

    def test_number_bathrooms(self):
        """Test for number_bathrooms attribute"""
        self.assertTrue(hasattr(self.p1, "number_bathrooms"))
        self.assertEqual(self.p1.number_bathrooms, 0)
        self.assertIsInstance(self.p1.number_bathrooms, int)

    def test_max_guest(self):
        """Test for max_guest attribute"""
        self.assertTrue(hasattr(self.p1, "max_guest"))
        self.assertEqual(self.p1.max_guest, 0)
        self.assertIsInstance(self.p1.max_guest, int)

    def test_price_by_night(self):
        """Test for price_by_night attribute"""
        self.assertTrue(hasattr(self.p1, "price_by_night"))
        self.assertEqual(self.p1.price_by_night, 0)
        self.assertIsInstance(self.p1.price_by_night, int)

    def test_latitude(self):
        """Test for latitude attribute"""
        self.assertTrue(hasattr(self.p1, "latitude"))
        self.assertEqual(self.p1.latitude, 0.0)
        self.assertIsInstance(self.p1.latitude, float)

    def test_longitude(self):
        """Test for longitude attribute"""
        self.assertTrue(hasattr(self.p1, "longitude"))
        self.assertEqual(self.p1.longitude, 0.0)
        self.assertIsInstance(self.p1.longitude, float)

    def test_amenity_ids(self):
        """Test for amenity_ids attribute"""
        self.assertTrue(hasattr(self.p1, "amenity_ids"))
        self.assertEqual(self.p1.amenity_ids, "")
        self.assertIsInstance(self.p1.amenity_ids, str)

    def test_str(self):
        """Test for __str__ method"""
        result = len(self.p1.__str__())
        self.assertTrue(result, 172)

    def test_save(self):
        """Test for save method"""
        prechange = self.p1.updated_at
        self.p1.save()
        postchange = self.p1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_created_at(self):
        """Test for created at time"""
        self.assertTrue(hasattr(self.p1, "created_at"))

    def test_updated_at(self):
        """Test for the updated at time attr"""
        prechange = self.p1.updated_at
        self.p1.save()
        postchange = self.p1.updated_at
        self.assertNotEqual(prechange, postchange)

    def test_kwargs(self):
        """Test for kwargs"""
        self.p1.name = "Holberton"
        self.p1.my_number = 89
        p1_json = self.p1.to_dict()

        p2 = BaseModel(**p1_json)
        self.assertEqual(self.p1.id, p2.id)
        self.assertEqual(self.p1.created_at, p2.created_at)
        self.assertEqual(self.p1.updated_at, p2.updated_at)
        self.assertEqual(self.p1.name, p2.name)
        self.assertEqual(self.p1.my_number, p2.my_number)

    def test_module_docstring(self):
        """Test for existence of module docstring"""
        print("testing module docstring...")
        result = len(__import__('models.place').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """Place Class Docstring Test"""
        print("test_place_docstring")
        result = len(Place.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """Place init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test__str__docstring(self):
        """Place __str__ Docstring Test"""
        print("testing __str__ docstring...")
        result = len(Place.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_save_docstring(self):
        """Place save method Docstring Test"""
        print("testing save docstring...")
        result = len(Place.save.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dict_docstring(self):
        """Place to_dict Docstring Test"""
        print("testing to_dict docstring...")
        result = len(Place.to_dict.__doc__)
        self.assertTrue(result > 0, True)

    if __name__ == "__main__":
        unittest.main()
