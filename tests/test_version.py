import unittest
import re
import rpi_hw_info

class TestVersion(unittest.TestCase):
	def test_version_exists(self):
		"""Test that __version__ exists and is in the correct format."""
		self.assertTrue(hasattr(rpi_hw_info, '__version__'))
		# Check that version follows semantic versioning (or development version)
		version_pattern = r'^(\d+\.\d+\.\d+(-[a-zA-Z0-9]+)?|\d+\.\d+\.\d+\.\w+|\d+\.\d+\.\d+\.post\d+\+[a-f0-9]+|0\.0\.0-dev)$'
		self.assertTrue(re.match(version_pattern, rpi_hw_info.__version__))

if __name__ == '__main__':
	unittest.main()
