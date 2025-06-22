import unittest
import subprocess
from unittest import mock
from io import BytesIO

from rpi_hw_info.models import RPIModel
from rpi_hw_info.detector import detect_rpi_model

class TestDetector(unittest.TestCase):
	@mock.patch('subprocess.Popen')
	def test_detect_rpi_model_3b(self, mock_popen):
		# Create a proper iterable object for the stdout
		mock_stdout = BytesIO(
			b"processor       : 0\n"
			b"model name      : ARMv7 Processor\n"
			b"Revision        : a02082\n"
		)
		
		# Configure the mock process
		mock_process = mock.Mock()
		mock_process.stdout = mock_stdout
		mock_popen.return_value = mock_process
		
		# Call the function under test
		result = detect_rpi_model()
		
		# Verify the result
		self.assertIsInstance(result, RPIModel)
		self.assertEqual(result.model_name, "3B")
		self.assertEqual(result.cpu_target, "cortex-a53")
		self.assertEqual(result.fpu_target, "neon-fp-armv8")

if __name__ == '__main__':
	unittest.main()
