import RPi.GPIO as GPIO
from tkinter import Tk, IntVar
from tkinter.ttk import Button, Style

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering system for GPIO
GPIO.setwarnings(False)  # Disable GPIO warnings to avoid clutter in the output

# Define GPIO pins for the LEDs
RED_LED = 17  # GPIO pin connected to the Red LED
GREEN_LED = 27  # GPIO pin connected to the Green LED
YELLOW_LED = 22  # GPIO pin connected to the Yellow LED

# Set up GPIO pins as output
GPIO.setup(RED_LED, GPIO.OUT)  # Configure Red LED pin as output
GPIO.setup(GREEN_LED, GPIO.OUT)  # Configure Green LED pin as output
GPIO.setup(YELLOW_LED, GPIO.OUT)  # Configure Yellow LED pin as output

# Function to turn off all LEDs
def turn_off_all_leds():
    """
    Turn off all connected LEDs by setting their GPIO output to LOW.
    This ensures that only one LED is active at a time.
    """
    GPIO.output(RED_LED, GPIO.LOW)  # Turn off Red LED
    GPIO.output(GREEN_LED, GPIO.LOW)  # Turn off Green LED
    GPIO.output(YELLOW_LED, GPIO.LOW)  # Turn off Yellow LED

# Function to control LEDs based on user selection
def control_leds():
    """
    Turn off all LEDs and then turn on the selected LED based on the value
    stored in the led_choice variable. Also, update button styles dynamically
    to indicate the active LED.
    """
    turn_off_all_leds()  # Ensure all LEDs are off before activating the selected one
    selected_led = led_choice.get()  # Get the current selection from the GUI (1=Red, 2=Green, 3=Yellow)

    # Determine which LED to turn on and update the button style
    if selected_led == 1:  # Red LED selected
        GPIO.output(RED_LED, GPIO.HIGH)  # Turn on Red LED
        red_button.configure(style="Red.TButton")  # Highlight Red button
        green_button.configure(style="TButton")  # Reset Green button style
        yellow_button.configure(style="TButton")  # Reset Yellow button style
    elif selected_led == 2:  # Green LED selected
        GPIO.output(GREEN_LED, GPIO.HIGH)  # Turn on Green LED
        red_button.configure(style="TButton")  # Reset Red button style
        green_button.configure(style="Green.TButton")  # Highlight Green button
        yellow_button.configure(style="TButton")  # Reset Yellow button style
    elif selected_led == 3:  # Yellow LED selected
        GPIO.output(YELLOW_LED, GPIO.HIGH)  # Turn on Yellow LED
        red_button.configure(style="TButton")  # Reset Red button style
        green_button.configure(style="TButton")  # Reset Green button style
        yellow_button.configure(style="Yellow.TButton")  # Highlight Yellow button

# Function to clean up GPIO and exit the program
def exit_program():
    """
    Clean up GPIO settings to release resources and close the Tkinter window.
    This ensures that GPIO pins are properly reset when the program exits.
    """
    GPIO.cleanup()  # Release GPIO resources and reset all GPIO pins
    window.quit()  # Close the GUI window and terminate the program

# Tkinter GUI setup
window = Tk()  # Initialize the main Tkinter window
window.title("Enhanced LED Controller")  # Set the title of the window
window.geometry("400x300")  # Set the dimensions of the window
window.configure(bg="#f7f7f7")  # Set the background color of the window

# Configure button styles using ttk.Style
style = Style()  # Create a Style object to define button appearances
style.configure("TButton", font=("Helvetica", 14), padding=10)  # Default button style with font and padding
style.configure("Red.TButton", font=("Helvetica", 14), padding=10, background="red")  # Style for Red button
style.configure("Green.TButton", font=("Helvetica", 14), padding=10, background="green")  # Style for Green button
style.configure("Yellow.TButton", font=("Helvetica", 14), padding=10, background="yellow")  # Style for Yellow button

# Variable to store the selected LED choice
led_choice = IntVar()  # IntVar is used to store integer values for radio button selections
led_choice.set(0)  # Default to no LED selection (value = 0)

# Create buttons for controlling LEDs
red_button = Button(
    window,
    text="Red LED",  # Button label
    command=lambda: [led_choice.set(1), control_leds()]  # Update selection and control LEDs
)
red_button.pack(pady=10)  # Add vertical spacing between buttons

green_button = Button(
    window,
    text="Green LED",
    command=lambda: [led_choice.set(2), control_leds()]
)
green_button.pack(pady=10)

yellow_button = Button(
    window,
    text="Yellow LED",
    command=lambda: [led_choice.set(3), control_leds()]
)
yellow_button.pack(pady=10)

# Create an Exit button to close the program
exit_button = Button(
    window,
    text="Exit",  # Button label
    command=exit_program  # Action to perform on button click
)
exit_button.pack(pady=20)  # Add spacing below the Exit button

# Run the Tkinter main loop
window.mainloop()  # Start the GUI event loop, keeping the window responsive
