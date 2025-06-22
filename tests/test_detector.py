import unittest
import subprocess
from unittest import mock

from rpi_hw_info.models import RPIModel
from rpi_hw_info.detector import detect_rpi_model

class MockPopen(object):
	def __init__(self, stdout):
		self.stdout = stdout

class TestDetector(unittest.TestCase):
	@mock.patch('subprocess.run')
	def test_detect_rpi_model_3b(self, mock_run):
		# Mock the subprocess.run call
		mock_run.return_value = mock.Mock(
			stdout="processor       : 0\nmodel name      : ARMv7 Processor\nRevision        : a02082\n",
			returncode=0
		)
		
		# Call the function under test
		result = detect_rpi_model()
		
		# Verify the result
		self.assertIsInstance(result, RPIModel)
		self.assertEqual(result.model_name, "3B")
		self.assertEqual(result.cpu_target, "cortex-a53")
		self.assertEqual(result.fpu_target, "neon-fp-armv8")

if __name__ == '__main__':
	unittest.main()
