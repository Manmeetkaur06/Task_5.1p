import RPi.GPIO as GPIO
from tkinter import Tk, IntVar, Label, Frame
from tkinter.ttk import Button, Style

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering system for GPIO
GPIO.setwarnings(False)  # Disable GPIO warnings to avoid clutter in the output

# Define GPIO pins for the LEDs
RED_LED = 17    # GPIO pin connected to the Red LED
GREEN_LED = 27  # GPIO pin connected to the Green LED
YELLOW_LED = 22 # GPIO pin connected to the Yellow LED

# Set up GPIO pins as output and initialize to LOW (off)
GPIO.setup(RED_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW_LED, GPIO.OUT, initial=GPIO.LOW)

# Function to turn off all LEDs
def turn_off_all_leds():
    """
    Turn off all connected LEDs by setting their GPIO output to LOW.
    """
    GPIO.output(RED_LED, GPIO.LOW)     # Turn off Red LED
    GPIO.output(GREEN_LED, GPIO.LOW)   # Turn off Green LED
    GPIO.output(YELLOW_LED, GPIO.LOW)  # Turn off Yellow LED

# Function to control LEDs based on user selection
def control_leds():
    """
    Turn off all LEDs and turn on the selected LED based on the value
    stored in the led_choice variable. Update button styles dynamically.
    """
    turn_off_all_leds()  # Ensure all LEDs are off before activating the selected one
    selected_led = led_choice.get()  # Get the current selection (0=None, 1=Red, 2=Green, 3=Yellow)

    # Reset all button styles to inactive
    red_button.configure(style="Inactive.TButton")
    green_button.configure(style="Inactive.TButton")
    yellow_button.configure(style="Inactive.TButton")

    # Determine which LED to turn on and update the button style
    if selected_led == 1:
        GPIO.output(RED_LED, GPIO.HIGH)  # Turn on Red LED
        red_button.configure(style="Red.TButton")  # Highlight Red button
    elif selected_led == 2:
        GPIO.output(GREEN_LED, GPIO.HIGH)  # Turn on Green LED
        green_button.configure(style="Green.TButton")  # Highlight Green button
    elif selected_led == 3:
        GPIO.output(YELLOW_LED, GPIO.HIGH)  # Turn on Yellow LED
        yellow_button.configure(style="Yellow.TButton")  # Highlight Yellow button
    # If selected_led == 0, no LED is turned on and buttons remain inactive

# Function to clean up GPIO and exit the program
def exit_program():
    """
    Clean up GPIO settings to release resources and close the Tkinter window.
    """
    GPIO.cleanup()  # Release GPIO resources and reset all GPIO pins
    window.quit()   # Close the GUI window and terminate the program

# Tkinter GUI setup
window = Tk()
window.title("LED Controller")  # Set the title of the GUI window
window.configure(bg="white")  # Set the background color to white

# Set window size and center it on the screen
window_width = 800
window_height = 500
# Get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# Find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
# Set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Configure button styles using ttk.Style
style = Style()
style.theme_use('default')  # Use default theme for better control over styles

# Inactive button style
style.configure("Inactive.TButton",
                font=("Helvetica", 16),
                padding=10,
                foreground="black",
                background="#dcdcdc",
                borderwidth=1,
                relief="flat")

# Active button styles
style.configure("Red.TButton",
                font=("Helvetica", 16),
                padding=10,
                foreground="white",
                background="red",
                borderwidth=1,
                relief="flat")

style.configure("Green.TButton",
                font=("Helvetica", 16),
                padding=10,
                foreground="white",
                background="green",
                borderwidth=1,
                relief="flat")

style.configure("Yellow.TButton",
                font=("Helvetica", 16),
                padding=10,
                foreground="black",
                background="yellow",
                borderwidth=1,
                relief="flat")

# Main title label
title_label = Label(window,
                    text="LED Controller",
                    font=("Helvetica", 28, 'bold'),
                    bg="white",
                    fg="black")
title_label.pack(pady=30)

# Description label
description_label = Label(
    window,
    text="Select an LED to turn on. The active LED will light up, and its button will be highlighted.",
    font=("Helvetica", 14),
    bg="white",
    fg="gray"
)
description_label.pack(pady=10)

# Create a frame for the LED buttons
button_frame = Frame(window, bg="white")
button_frame.pack(pady=30)

# Variable to store the selected LED choice
led_choice = IntVar()
led_choice.set(0)  # Default to no LED selected

# Create buttons for controlling LEDs
button_width = 15

red_button = Button(
    button_frame,
    text="Red LED",
    command=lambda: [led_choice.set(1), control_leds()],
    style="Inactive.TButton",
    width=button_width
)
red_button.grid(row=0, column=0, padx=30, pady=10)

green_button = Button(
    button_frame,
    text="Green LED",
    command=lambda: [led_choice.set(2), control_leds()],
    style="Inactive.TButton",
    width=button_width
)
green_button.grid(row=0, column=1, padx=30, pady=10)

yellow_button = Button(
    button_frame,
    text="Yellow LED",
    command=lambda: [led_choice.set(3), control_leds()],
    style="Inactive.TButton",
    width=button_width
)
yellow_button.grid(row=0, column=2, padx=30, pady=10)

# Initialize the LEDs and button styles
control_leds()

# Create an Exit button to close the program
exit_button = Button(
    window,
    text="Exit",
    command=exit_program,
    style="TButton",
    width=10
)
exit_button.pack(pady=40)

# Run the Tkinter main loop
window.mainloop()
