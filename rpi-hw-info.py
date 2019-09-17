
#!/usr/bin/env python
from __future__ import print_function

import subprocess
import sys

class RPIModel:
        def __init__(self, model_name, model_id, cpu_target, fpu_target ):
                """Create a representation of a Raspi hardware

                Arguments:
                model_name -- the human-readable model name, e.g. "3B"
                model_id   -- Hexadecimal identifier for the RPi model; see https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md
                cpu_target -- the gcc cpu target to -mtune to
                fpu_target -- the gcc fpu target to -mfpu to
                """

                self.model_name = model_name
                self.model_id = model_id
                self.cpu_target = cpu_target
                self.fpu_target = fpu_target

        def __repr__(self):
                return self.model_name + ":" + hex( self.model_id ) + ":" + self.cpu_target + ":" + self.fpu_target

rpi_models = [
        RPIModel( "3B", int("0x8",16), "cortex-a53", "neon-fp-armv8" ),
        RPIModel( "3B+", int("0xd",16), "cortex-a53", "neon-fp-armv8" ),
        RPIModel( "4B", int("0x11",16), "cortex-a72", "neon-fp-armv8" )
]

cpuinfo = subprocess.Popen(["cat", "/proc/cpuinfo"], stdout=subprocess.PIPE)
found = False

# see https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md
revision_format_bitmask = int( "0x800000", 16 )
model_id_bitmask = int( "0xFF0", 16 )

for line in cpuinfo.stdout.readlines():
        fields = line.strip().split()
        if fields and fields[0] == "Revision" :
                revision = fields[2]
                revision_hex = int( "0x" + revision, 16 )

                revision_format = ( revision_hex & revision_format_bitmask ) >> 23
                if revision_format == 0:
                        sys.exit( revision + ": older revision format `" + str( revision_format ) + "' is not supported." )

                model_id = ( revision_hex & model_id_bitmask ) >> 4
                for rpi in rpi_models :
                        if rpi.model_id == model_id:
                                found = True
                                print( str( rpi ) )
                                break

if not found:
        sys.exit( revision + ": unrecognized revision." )

