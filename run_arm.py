#!/usr/bin/env python3
# run the arm program
from pathlib import Path
import subprocess
import tempfile

from elftools.elf.elffile import ELFFile
from unicorn import Uc, UC_ARCH_ARM, UC_MODE_ARM, UC_MODE_LITTLE_ENDIAN
from unicorn.arm_const import UC_ARM_REG_R2, UC_ARM_REG_R3

source = Path(__file__).with_name("unit5_arm_add_sub.s")
with tempfile.TemporaryDirectory() as temp:
    obj = Path(temp) / "program.o"
    subprocess.run(["clang", "--target=armv7-none-eabi", "-c", str(source),
                    "-o", str(obj)], check=True)
    with obj.open("rb") as stream:
        code = ELFFile(stream).get_section_by_name(".text").data()

emulator = Uc(UC_ARCH_ARM, UC_MODE_ARM | UC_MODE_LITTLE_ENDIAN)
emulator.mem_map(0x1000, 0x1000)
emulator.mem_write(0x1000, code)
emulator.emu_start(0x1000, 0x1000 + len(code))
print(f"R2 = 0x{emulator.reg_read(UC_ARM_REG_R2):08X}")
print(f"R3 = 0x{emulator.reg_read(UC_ARM_REG_R3):08X}")
