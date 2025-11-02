import unittest

class TestProjectStructure(unittest.TestCase):
    def test_import_main(self):
        try:
            import main
        except ImportError:
            self.fail("main.py could not be imported")

if __name__ == '__main__':
    unittest.main()
