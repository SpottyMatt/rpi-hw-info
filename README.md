
Raspberry Pi Hardware Info Detector
==============================

`./rpi-hw-info.py` will return useful information about a Raspberry Pi that cannot be easily obtained through other means.
It will print a colon (`:`)-separated list of data to stdout.

If the hardware info cannot be detected, it will print an error message to stderr.

You might use this to make scripts compatible with multiple Raspberry Pi models.

Detection is based on decoding the hardware "revision" per the [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md).

Output Format
==============================

Example:

        3B+:0xd:cortex-a53:neon-fp-armv8

| Column # | Contents                   | Example       |
| -------- | -------------------------- | ------------- |
| 1        | Short human-readable model | 3B+           |
| 2        | Hexadecimal model ID       | 0xd           |
| 3        | CPU target                 | cortex-a53    |
| 4        | FPU target                 | neon-fp-armv8 |

Usage
==============================

You might use `awk` to easily grab a column:

        CPU_TARGET=$(./rpi-hw-info.py | awk -F ':' '{print $3}')
        gcc -mtune=${CPU_TARGET} ...

