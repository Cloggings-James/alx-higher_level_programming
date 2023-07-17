import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)
        self.s4 = Square(4, 2, 1, 10)

    def tearDown(self):
        pass

    def test_id(self):
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)

    def test_size(self):
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 3)
        self.assertEqual(self.s4.size, 4)

    def test_x(self):
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.x, 1)
        self.assertEqual(self.s4.x, 2)

    def test_y(self):
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s4.y, 1)

    def test_update_args(self):
        self.s1.update(10)
        self.assertEqual(self.s1.id, 10)
        self.s2.update(5, 3)
        self.assertEqual(self.s2.id, 5)
        self.assertEqual(self.s2.size, 3)
        self.s3.update(1, 1, 1)
        self.assertEqual(self.s3.id, 1)
        self.assertEqual(self.s3.size, 1)
        self.assertEqual(self.s3.x, 1)
        self.s4.update(2, 2, 2, 2)
        self.assertEqual(self.s4.id, 2)
        self.assertEqual(self.s4.size, 2)
        self.assertEqual(self.s4.x, 2)
        self.assertEqual(self.s4.y, 2)

    def test_update_kwargs(self):
        self.s1.update(id=5)
        self.assertEqual(self.s1.id, 5)
        self.s2.update(size=4, x=1)
        self.assertEqual(self.s2.size, 4)
        self.assertEqual(self.s2.x, 1)
        self.s3.update(y=5, size=2, id=2)
        self.assertEqual(self.s3.id, 2)
        self.assertEqual(self.s3.size, 2)
        self.assertEqual(self.s3.y, 5)
        self.s4.update(x=0, y=0, id=1, size=1)
        self.assertEqual(self.s4.id, 1)
        self.assertEqual(self.s4.size, 1)
        self.assertEqual(self.s4.x, 0)
        self.assertEqual(self.s4.y, 0)

    def test_area(self):
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 9)
        self.assertEqual(self.s4.area(), 16)

    def test_display(self):
        expected_output = "\n#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(self.s1.display(), expected_output)
        expected_output = "  ##\n  ##\n"
        self.assertEqual(self.s2.display(), expected_output)
        expected_output = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(self.s3.display(), expected_output)
        expected_output = "  ##\n  ##\n"
        self.assertEqual(self.s4.display(), expected_output)

    def test_str(self):
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(self.s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(self.s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(str(self.s4), "[Square] (10) 2/1 - 4")

    def test_to_dictionary(self):
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 0,
            'y': 0
        }
        self.assertEqual(self.s1.to_dictionary(), expected_dict)
        expected_dict = {
            'id': 2,
            'size': 2,
            'x': 2,
            'y': 0
        }
        self.assertEqual(self.s2.to_dictionary(), expected_dict)
        expected_dict = {
            'id': 3,
            'size': 3,
            'x': 1,
            'y': 3
        }
        self.assertEqual(self.s3.to_dictionary(), expected_dict)
        expected_dict = {
            'id': 10,
            'size': 4,
            'x': 2,
            'y': 1
        }
        self.assertEqual(self.s4.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()

