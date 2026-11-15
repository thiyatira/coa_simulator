# COA Simulator

Computer Organization and Architecture lab programs by Thiyatira Reni N.

- Unit 1: Binary to decimal conversion
- Unit 2: Unsigned 8-bit addition with carry
- Unit 3: Full-adder truth table
- Unit 4: RAW data hazard detection
- Unit 5: ARM32 addition and subtraction

## Run

Install Python 3, then run any of Units 1–4:

```sh
python unit1_binary_to_decimal.py
python unit2_add_8bit.py
python unit3_full_adder.py
python unit4_data_hazards.py
```

For Unit 5, also install Clang with ARM target support and make sure `clang` is on your PATH. Then:

```sh
python -m pip install -r requirements.txt
python run_arm.py
```

The runner assembles `unit5_arm_add_sub.s` and executes it with the Unicorn ARM emulator.
On macOS/Linux, use `python3` if `python` is unavailable.
