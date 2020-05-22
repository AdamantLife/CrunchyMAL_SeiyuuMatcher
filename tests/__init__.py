if __name__ == "__main__":
    import unittest
    import pathlib

    loader = unittest.TestLoader()
    tests = loader.discover(".")
    runner = unittest.TextTestRunner()
    runner.run(tests)
