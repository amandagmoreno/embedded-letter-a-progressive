# Embedded Letter A – Progressive LED Matrix

This project demonstrates a progressive rendering of the letter **A** on a 5x5 WS2812 LED matrix using the **BitDogLab (RP2040)** board and **MicroPython**.

Each press of **Button A** lights the next segment of the letter until the full shape is completed.  
After completion, the next press clears the matrix and restarts the animation.

## Hardware
- BitDogLab (RP2040 / Pico W)
- 5x5 WS2812 LED Matrix
- Button A (GPIO5)

## Software
- MicroPython
- Thonny IDE

## Pin Mapping
| Component | GPIO |
|--------|------|
| Button A | GPIO5 |
| LED Matrix | GPIO7 |

## Project Logic
- Button input with internal pull-up
- Software debounce to avoid false triggers
- Predefined ordered pixel list forming the letter **A**
- Progressive rendering on each button press
- Coordinate remapping to correct physical LED orientation

## How It Works
1. Press Button A
2. One new LED segment of the letter appears
3. Repeat until the letter **A** is complete
4. Press again to reset and restart

## Author
Amanda Moreno
