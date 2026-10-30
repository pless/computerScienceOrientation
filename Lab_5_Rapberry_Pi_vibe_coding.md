# Lab 5: Raspberry Pi vibe coding
In this lab, you will use AI to help you make a program for your Raspberry Pi and Sense HAT.
Your program must react to something happening around it. For example, it could react to the room temperature or to you moving the Pi.

You do not need to know how to code everything yourself. You will explain your idea to an AI assistant, copy the code it gives you, and test it.

## Step 1: Connect to the Pi ##
>These are the steps we used last week!
1. Look at the monitor connected to your Raspberry Pi. You should see the Raspberry Pi desktop, which looks similar to a regular computer desktop.
2. You need to open a program called the **Terminal**.
   1. Look at the top-left corner of the Raspberry Pi desktop.
   2. Click the Raspberry icon to open the main menu.
   3. Find and click Accessories.
   4. Click Terminal. 
3. Find the Raspberry Pi's IP address
   1. Click inside the Terminal window.
   2. type `hostname -I` and press Enter
   3. You should see a set of numbers that look something like this: 192.168.1.25. This number is just like a mailing address.
    It tells your computer where to go to do stuff. The same way your home address tells the mailman where to deliver stuff.
4. Open a terminal on your laptop
   1. If you are using **Windows**:
    Go to your laptop's desktop.
    Press the Windows key on your keyboard.
    Type PowerShell into the search bar.
    Click Windows PowerShell in the search results.
    If you are using **macOS** or **Linux**: Open the Terminal application on your laptop.
    A new window should open where you can type commands.
    *If youre not sure what you have, ask us and we can tell you*
    2. In the terminal on your laptop, type the following command: `ssh csci1010@IP_ADDRESS` and replace the IP_ADDRESS with the IP address you found on step 3.
    3. The first time you connect, your laptop may ask whether you trust the Raspberry Pi. Type `yes` and press Enter.
    4. You will see a prompt to enter a password. The password is password (I know it's very secure). ** IMPORTANT: ** The password may not appear on the screen as you type. You will not see letters, dots, or stars. This is normal. Type the password anyway and press Enter. 
5. Check you're connected by typing `hostname` in your laptop's terminal. It should say "Lab"
Congratulations! You have connected to a Raspberry Pi remotely using SSH. You will use this same terminal for the rest of the lab.

## Step 2: Come up with a project! ##
Here's a little bit more about what the SenseHat on the Pi can do. 
### The Sense HAT: What can it sense?

| Sensor | What it does | Example project |
|---|---|---|
| Temperature | Measures temperature near the board | Change the lights based on temperature |
| Humidity | Measures moisture in the air | Display a humidity warning |
| Air pressure | Measures atmospheric pressure | Show changing pressure readings |
| Accelerometer | Detects movement and tilting | Control a game by tilting the Pi |
| Gyroscope | Measures how quickly the board rotates | Detect twisting or turning |
| Magnetometer | Detects magnetic fields and direction | Make a digital compass |

### The Sense HAT: What can it do?

| Feature | What it does | Example project |
|---|---|---|
| 8×8 LED display | Shows 64 colored lights | Display faces, arrows, colors, or animations |
| Joystick | Detects up, down, left, right, and middle-button presses | Make a small game |
| Continuous display updates | Changes what appears on the LEDs while a program runs | Create an interactive animation |

Using this information, come up with a project idea that uses the Sense HAT to interact with your environment:

Before asking AI to write code, think about these questions.
1. What do you want to build?
>Write one sentence describing your idea.
2. What will your program respond to?
>Examples: temperature, humidity, movement, joystick presses, magnetic field.
3. What should happen when it responds?
>Examples: change the lights, display a message, play a game, or show an animation.
4. What would make your project more interesting?
>Think of one extra feature you might want to add later. It's ok if you don't have time for it.

**NOTE** This should most likely be the longest part of the lab. Do NOT ask AI to come up with the project idea itself. We want to teach you how to vibe code and use AI properly, not to skip utilizing your own mind. 

## Step 3: Prompting AI ## 
There are a few ways to prompt an AI agent and one of the ways is by persona prompting. You do this by assigning the AI a character, job title, or area of expertise before giving it a task. 
This helps prime the model to draw from a specific subset of its training data, steering its tone, vocabulary, depth, and perspective to better match that role. 

>For example: If you are trying to write a food blog post, you can start your prompt by saying, "You are a Michelin star food critic" to get a better, more nuanced response from the AI.

How do you think you can use this kind of prompting to help you more effectively prompt for this project? Come up with a role for the agent, describe the project you want to make, and ask it for one `.py` file (or specify you want it to be a Python file)

## Step 4: Running ##
The next step is to copy and run the code!
Last week, we made the folder `projects` with files `Hello_world.py`, `Flappy_bird.py` and `flappy_bird_accl.py` (or something similar)
1. Check your current directory (where you are in the terminal) with the `pwd` command, which stands for print working directory. You should see csci1010@LAB{dir} ###### Change
2. If you see {directory} great! If not, run this command to put youin the right place [dir]
3. Create a new file called lab 5 and paste your code; you do that by running `nano lab5.py`  and pressing Enter
     1. Click inside the Nano editor.
     2. Paste the code using Ctrl + Shift + V in most Windows terminals, or right-click and select Paste if that option is available.
     3. Check that the code appears in the editor. Important: Do not press Ctrl + V automatically. In Nano, that shortcut may trigger a different command depending on your terminal.
4. You need to save the code before you can run it. To do that:
     1. Press Ctrl + O (the letter O, not zero).
     2. Nano will show the filename at the bottom. It should say lab5.py.
     3. Press Enter to confirm the filename.
     4. Press Ctrl + X to exit Nano.
     5. Now the fun part. Type python3 lab5.py into the terminal to run your code.
  
Does it work how you expected? Are there any errors? If there are, feed them into the AI model of your choice, explain what you are trying to do, what is currently happening, and any errors you encountered. 

## Step 5: Submitting ##

Answer the following questions on the submission form for credit. 
Use this link: {LINK} and answer the following questions: 
1. What was the project you made? What sensor did you utilize?
2. Did you use persona prompting? Did you notice any difference between persona prompting and non-persona prompting?
3. Can we share your projects with some of the faculty in the department (Does not affect grade, we just want to show off to other professors)
























