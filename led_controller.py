import RPi.GPIO as GPIO
from tkinter import Tk, IntVar
from tkinter.ttk import Button, Style

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setwarnings(False)  # Disable warnings

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
    """
    Turn off all connected LEDs by setting their GPIO output to LOW.
    """
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(BLUE_LED, GPIO.LOW)

# Function to control LEDs based on user selection
def control_leds():
    """
    Turn off all LEDs and turn on the selected LED based on the value
    stored in the led_choice variable. Change the button styles to reflect the selection.
    """
    turn_off_all_leds()  # Ensure all LEDs are off before setting the new one
    selected_led = led_choice.get()  # Get the current selection from IntVar

    # Update LED state and button styles
    if selected_led == 1:
        GPIO.output(RED_LED, GPIO.HIGH)
        red_button.configure(style="Red.TButton")
        green_button.configure(style="TButton")
        blue_button.configure(style="TButton")
    elif selected_led == 2:
        GPIO.output(GREEN_LED, GPIO.HIGH)
        red_button.configure(style="TButton")
        green_button.configure(style="Green.TButton")
        blue_button.configure(style="TButton")
    elif selected_led == 3:
        GPIO.output(BLUE_LED, GPIO.HIGH)
        red_button.configure(style="TButton")
        green_button.configure(style="TButton")
        blue_button.configure(style="Blue.TButton")

# Function to clean up GPIO and exit the program
def exit_program():
    """
    Clean up GPIO settings and close the Tkinter window.
    """
    GPIO.cleanup()  # Release GPIO resources
    window.quit()  # Close the GUI window

# Tkinter GUI setup
window = Tk()
window.title("Enhanced LED Controller")  # Set the title of the GUI window
window.geometry("400x300")  # Set the dimensions of the window
window.configure(bg="#f7f7f7")  # Set background color

# Configure button styles
style = Style()
style.configure("TButton", font=("Helvetica", 14), padding=10)  # Default button style
style.configure("Red.TButton", font=("Helvetica", 14), padding=10, background="red")  # Style for Red LED
style.configure("Green.TButton", font=("Helvetica", 14), padding=10, background="green")  # Style for Green LED
style.configure("Blue.TButton", font=("Helvetica", 14), padding=10, background="blue")  # Style for Blue LED

# Variable to store the selected LED choice
led_choice = IntVar()
led_choice.set(0)  # Default to no selection

# Create buttons for controlling LEDs
red_button = Button(window, text="Red LED", command=lambda: [led_choice.set(1), control_leds()])
red_button.pack(pady=10)  # Add vertical spacing

green_button = Button(window, text="Green LED", command=lambda: [led_choice.set(2), control_leds()])
green_button.pack(pady=10)

blue_button = Button(window, text="Blue LED", command=lambda: [led_choice.set(3), control_leds()])
blue_button.pack(pady=10)

# Create an exit button
exit_button = Button(window, text="Exit", command=exit_program)
exit_button.pack(pady=20)

# Run the Tkinter main loop
window.mainloop()
