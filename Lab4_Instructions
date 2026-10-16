# Lab 4: A Raspberry Pi #

Computer Science Orientation · Raspberry Pi + Sense HAT
You'll be using a tiny computer called a **Raspberry Pi**. Attached to the top of it is a **Sense HAT**: a board with a square grid of colored lights (the **LED matrix**) and sensors that can feel temperature, air pressure, humidity, and movement.

By the end of this lab you will have:
Made the Pi say "Hello world" with its lights, followed by a reading from one of its sensors (temperature, humidity, air pressure)
Played a Flappy Bird game that you control by blowing on the Pi 
Used an AI assistant to change the game so you control it by moving the Pi
Answered 2 short questions

## Part 1: Get connected and find where to code ##
Your Pi is already set up for you. You just need to find the place where the coding happens.

Use the Laptops provided for you. The Pi is plugged into it. You should see the Raspberry Pi desktop, which looks like a normal computer screen. If the screen is black or asks you to log in, ask your GTA.

1. Open the code editor: click the **Raspberry icon** in the top-left corner, choose **Programming**, then click **Geany**. Geany is the program where you will see and edit code.
2. In Geany, find the panel with tabs named **Status, Compiler, Messages, Scribble, and Terminal**.
3. Click the **Terminal** tab. The Terminal is a place where you type commands to run your programs. You will use it a lot today.

   
## Part 2: Say "Hello world" on the LED board ##
You will make the Pi scroll "Hello world!" across its lights, then show you the temperature, pressure, and humidity of the room.
1. In Geany, click **File**, then **New**. You get a blank page.
2. Copy the code below onto the blank page (The comments are just for your understanding. you don’t have to type those)
```
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
````
3. Save the file: click **File**, then **Save As**. Type the name `hello.py`, open the projects folder, and click Save.
4. Click in the **Terminal** tab and type these two lines, pressing Enter after each one:
`cd ~/projects` then `python3 hello.py`
5. Watch the LED board on the Sense HAT. The words scroll across from right to left. The whole thing takes less than a minute.

#### Want to customize it? #### Change the words inside the quotation marks, or change [0, 255, 0] to [255, 0, 0] for red or [0, 0, 255] for blue. Save, then run it again with python3 hello.py.

## Part 3: Play Flappy Bird (controlled by your breath) ##
How to play:
- The yellow light is your bird. The green lights are pipes that scroll in from the right, each with a gap you need to fly through.
- Blow on the Sense HAT from 1 or 2 inches away and the bird goes up while you blow and sinks when you stop.
- **To stop the game**, click in the Terminal and press **Ctrl + C**.

In Geany, click **File**, then **Open**.
Open the folder called **projects**.
Click the folder called **FlappyBird**.
Click the file called **Flappybird.py**, then click Open. This is the code for a Flappy Bird game that uses the humidity sensor.
Click in the **Terminal** tab and type these two lines, pressing Enter after each one:
`cd ~/projects/FlappyBird`
`python3 Flappybird.py`
Play with it for a bit!
**Did you notice something?** There is a delay between when you blow and when the bird goes up. That happens because the humidity sensor is slow. It takes a couple of seconds for your breath's moisture to reach it. That's pretty annoying, right? Let's fix it.

## Part 4: Fix it with AI (vibe coding) ##
You will ask an AI to change the game so it uses the Pi's **accelerometer** instead of the humidity sensor.
> An accelerometer is a tiny sensor that feels movement, like the one in your phone that rotates the screen when you turn it.
The goal: the bird goes up and down every time you move the Pi.

#### Step by step ####

1. **Copy the code**. Click inside the code, press Ctrl + A, then Ctrl + C.
2. In Geany, click **File**, then **New** and paste the flappyBird code in that file
3. Open an AI assistant. Open the web browser (the globe icon at the top of the screen) and go to your preferred AI, such as ChatGPT, Claude, or Gemini. Log in if it asks.
4. Write your prompt. Use Prompt 1 below as a format. Then paste your copied code at the end.
5. Copy the AI's answer. Look for the code box in its reply. Click the Copy button on the code box.
6. Paste it into Geany. Click inside the code in Geany, press Ctrl + A, then Ctrl + V (paste), then Ctrl + S (save).
7. Run it. In the Terminal, type:
     `cd ~/projects/FlappyBird`
     `python3 Flappybird_accel.py`
   
8. **Move the Pi** and see what happens. Move it gently: it is still plugged in, so don't yank the cables, and hold it by the edges instead of pressing on the LED board.
   
##### Prompt 1: ask for the change #####
Describe the situation. For example, the Raspberry Pi, the game, the humidity
Describe your desired outcome: Using the accelerometer 
Make the AI describe what it did in a way that you understand
[paste your code here]

##### Prompt 2: if something goes wrong or feels off #####
Thanks! I ran the code and ______. Can you fix that? Please give me the complete updated code again.
You can finish that sentence with an error message you copied from the Terminal, or with a problem you noticed, like "the bird moves too much" or "I have to shake it really hard." You can also ask for changes like making it more or less sensitive.
**Tip**: AI isn't perfect. If the first try doesn't work, that's normal. Use Prompt 2 and try again.

## Part 6: Submit ##
Go to the submission link: {}
Answer these 2 questions:
Which version was easier to play, blowing on the Pi or moving the Pi? Why? (1 or 2 sentences)
Name one everyday device (other than the Pi) that has an accelerometer in it.
