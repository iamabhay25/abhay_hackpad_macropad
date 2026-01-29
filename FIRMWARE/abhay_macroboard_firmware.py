import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.neopixel import NeoPixel

keyboard = KMKKeyboard()

# --------------------
# KEY PIN DEFINITIONS
# --------------------
keyboard.col_pins = (
    board.GP26,  # SW1
    board.GP27,  # SW2
    board.GP28,  # SW3
    board.GP29,  # SW4
    board.GP6,   # SW5
    board.GP7,   # SW6
)

keyboard.row_pins = ()
keyboard.diode_orientation = None

# --------------------
# RGB (SK6812)
# --------------------
rgb = NeoPixel(
    pin=board.GP3,     # DIN pin
    num_pixels=2,
    brightness=0.3,
    auto_write=True,
)
keyboard.extensions.append(rgb)

# --------------------
# KEYMAP
# --------------------
keyboard.keymap = [
    [
        # 1️⃣ Screenshot (Selection)
        KC.LGUI(KC.LSHIFT(KC.N4)),

        # 2️⃣ Save As
        KC.LGUI(KC.LSHIFT(KC.S)),

        # 3️⃣ Reopen Closed Tab
        KC.LGUI(KC.LSHIFT(KC.T)),

        # 4️⃣ Force Quit
        KC.LGUI(KC.LALT(KC.ESC)),

        # 5️⃣ Lock Screen
        KC.LCTRL(KC.LGUI(KC.Q)),

        # 6️⃣ Screenshot Window (Cmd+Shift+4 then Space)
        KC.MACRO(
            KC.LGUI(KC.LSHIFT(KC.N4)),
            KC.SPACE
        ),
    ]
]

if __name__ == "__main__":
    keyboard.go()
