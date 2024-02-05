# Author: Michael Crum
# Date: 2/4/24

from skidl import *

set_default_tool(KICAD7)

# TEMPLATES

R_0603 = Part(
    "./kicad/balance_stick/balance_stick_symbols",
    "R",
    dest=TEMPLATE,
    footprint="balance_stick:R_0603_hand_solder",
)

C_0603 = Part(
    "./kicad/balance_stick/balance_stick_symbols",
    "C",
    dest=TEMPLATE,
    footprint="balance_stick:C_0603_hand_solder",
)

ESP_C3_MINI = Part(
    "./kicad/balance_stick/balance_stick_symbols",
    "ESP32-C3-MINI-1",
    dest=TEMPLATE,
    footprint="balance_stick:ESP32-C3-MINI-1_HandSoldering",
)

# INTERFACES



# SUBCIRCUIT

# EXPORTING
ERC()
generate_netlist()
