import RPi.GPIO as GPIO
from tkinter import Tk, Radiobutton, Button, IntVar

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins for the LEDs
RED_LED = 17
GREEN_LED = 27
BLUE_LED = 22

# Set up GPIO pins as output
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

# Function to turn off all LEDs
def turn_off_all_leds():
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)

# Function to control LEDs based on the selected radio button
def control_leds():
    turn_off_all_leds()
    selected_led = led_choice.get()
    
    if selected_led == 1:
        GPIO.output(RED_LED, GPIO.HIGH)
    elif selected_led == 2:
        GPIO.output(GREEN_LED, GPIO.HIGH)
    elif selected_led == 3:
        GPIO.output(BLUE_LED, GPIO.HIGH)

# Cleanup GPIO on exit
def exit_program():
    GPIO.cleanup()
    window.quit()

# Tkinter GUI setup
window = Tk()
window.title("LED Controller")

# IntVar to store selected radio button value
led_choice = IntVar()
led_choice.set(0)  # Default to no selection

# Create radio buttons for each LED
Radiobutton(window, text="Red LED", variable=led_choice, value=1, command=control_leds).pack()
Radiobutton(window, text="Green LED", variable=led_choice, value=2, command=control_leds).pack()
Radiobutton(window, text="Blue LED", variable=led_choice, value=3, command=control_leds).pack()

# Exit button
Button(window, text="Exit", command=exit_program).pack()

# Run the Tkinter event loop
window.mainloop()