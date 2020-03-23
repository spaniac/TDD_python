import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_upper(self):
        self.assertEqual('FOO', 'foo'.upper())

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)


# unittest.main(exit=False)
# suite = unittest.TestSuite([TestStringMethods()])
# result = unittest.TestResult()
# suite.run(result)
# print(result)
