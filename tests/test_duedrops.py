import unittest

import duedrops


class DuedropsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = duedrops.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to DueDrops', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
