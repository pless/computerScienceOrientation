from sense_hat import SenseHat

# This connects your code to the Sense HAT
sense = SenseHat()

# Scroll Hello world across the LED lights in green
sense.show_message("Hello world!", text_colour=[0, 255, 0])

# Read the temperature (in degrees Celsius) and scroll it
temp = sense.get_temperature()
sense.show_message("Temp: " + str(round(temp, 1)) + " C")

# Read the air pressure (in millibars) and scroll it
pressure = sense.get_pressure()
sense.show_message("Pressure: " + str(round(pressure)) + " mb")

# Read the humidity (percent) and scroll it
humidity = sense.get_humidity()
sense.show_message("Humidity: " + str(round(humidity)) + " %")
