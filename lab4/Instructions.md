# Lab 4: A Raspberry Pi #

Computer Science Orientation · Raspberry Pi + Sense HAT
You'll be using a tiny computer called a **Raspberry Pi**. Attached to the top of it is a **Sense HAT**: a board with a square grid of colored lights (the **LED matrix**) and sensors that can feel temperature, air pressure, humidity, and movement.

By the end of this lab you will have:
Made the Pi say "Hello world" with its lights, followed by a reading from one of its sensors (temperature, humidity, air pressure)
Played a Flappy Bird game that you control by blowing on the Pi 
Used an AI assistant to change the game so you control it by moving the Pi
Answered 2 short questions



## Part 1: Connect to the Raspberry Pi using SSH

What is SSH? SSH stands for Secure Shell. It lets you control another computer by typing commands from your own computer.
In this lab, you will use a laptop to connect to a Raspberry Pi. First, you will find the Pi's IP address. Then, you will use that address to connect to it remotely.

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
    It tells your computer where to go to send data. Just like your home address tells the mailman where to deliver mail.
      > If you see multiple IP addresses, run `ip -4 addr` and look for the one named eth0
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
   
## Part 2: Say "Hello world" on the LED board ##
You will make the Pi scroll "Hello world!" across its lights, then show you the temperature, pressure, and humidity of the room.
1. Type the following command: `mkdir -p ~/projects` and press Enter
2. Next, type: `cd ~/projects` and press Enter
3. Now type: `nano hello_world.py` and press enter. This is a way for you to type code to make the Raspberry Pi do the thing you want.
4. Copy the Hello World code that's in the hello_world.py file in this folder.
5.To paste the code into the text editor:
  1.  Click inside the Nano editor.
  2.  Paste the code using Ctrl + Shift + V in most Windows terminals, or right-click and select Paste if that option is available.
  3.  Check that the code appears in the editor
Important: Do not press Ctrl + V automatically. In Nano, that shortcut may trigger a different command depending on your terminal.
6. You need to save the code before you can run it. To do that:
   1. Press Ctrl + O (the letter O, not zero).
   2. Nano will show the filename at the bottom. It should say hello_world.py.
   3. Press Enter to confirm the filename.
   4. Press Ctrl + X to exit Nano.
7. Now the fun part. Type `python3 hello_world.py` into the terminal.

What do you see?
#### Want to customize it? Change the words inside the quotation marks, or change [0, 255, 0] to [255, 0, 0] for red or [0, 0, 255] for blue. Save, then run it again with python3 hello_world.py.

## Part 3: Play Flappy Bird (controlled by your breath) ##
Now you will create another Python file. This time, you will play the Flappy Bird game.

How to play:
- The yellow light is your bird. The green lights are pipes that scroll in from the right, each with a gap you need to fly through.
- Blow on the Sense HAT from 1 or 2 inches away, and the bird goes up while you blow and sinks when you stop.
- **To stop the game**, click in the Terminal and press **Ctrl + C**.

1. Type `nano flappy_bird.py` into your laptop's terminal
2. Find the complete Flappy Bird Python code provided in this folder and copy it.
3. Return to the terminal window with Nano open and paste using the previous steps from Hello World
4. Save the file using the previous steps for hello world
5. Now the more fun part: type `python3 flappy_bird.py` and press Enter in your terminal

### What did you notice?
>Did you notice a delay between blowing and the bird moving? The humidity sensor takes time to detect moisture from your breath.
>In Part 4, you will use an AI assistant to modify the game so that you can control the bird by tilting the Raspberry Pi instead.

## Part 4: Fix it with AI (vibe coding) ##
You will ask an AI to change the game so it uses the Pi's **accelerometer** instead of the humidity sensor.
> An accelerometer is a tiny sensor that feels movement, like the one in your phone that rotates the screen when you turn it.
The goal: the bird goes up and down every time you move the Pi.

You don't need to understand every single line of Python. You just need to explain what you want, test the result, and ask the AI to fix anything that does not work. The goal is for you to understand 
(1) How cool a Raspberry Pi is. (2) See how strong generative AI can be (and also see its major weak points) and finally (3) Know how to effectively use and prompt these models


### Step by step ###

1. On your laptop **Copy the code** again and Open an AI assistant.
2. Write your prompt. Use Prompt 1 below as a format. Then paste your copied code at the end.
5. Copy the AI's answer
6. Make a new Python file using the steps above called `flappy_bird_accl.py`
7. Paste it into nano using the previous steps on how to do that. 
8. Run it! 
9. **Move the Pi** and see what happens. Move it gently: it is still plugged in, so don't yank the cables, and hold it by the edges instead of pressing on the LED board.

Is it working as expected?
Does tilting the Pi move the bird?
Does the bird move in the direction you expected?
Is the bird too sensitive, or do you have to tilt the Pi too far?
Does the game still behave like Flappy Bird?

If something does not work as expected, you can ask the AI to fix it using prompt 2!
   
##### Prompt 1: ask for the change #####
Describe the situation. For example, the Raspberry Pi, the game, the humidity
Describe your desired outcome: Using the accelerometer 
Make the AI describe what it did in a way that you understand
[paste your code here]

##### Prompt 2: if something goes wrong or feels off #####
Thanks! I ran the code and ______. Can you fix that? Please give me the complete updated code again.
You can finish that sentence with an error message you copied from the Terminal, or with a problem you noticed, like "the bird moves too much" or "I have to shake it really hard." You can also ask for changes like making it more or less sensitive.
**Tip**: AI isn't perfect. If the first try doesn't work, that's normal. Use Prompt 2 and try again.

**Remember:** Vibe coding is an iterative process. You describe what you want, test the code, notice what needs improvement, and ask the AI to make changes. You do not have to get everything right on the first try.

## Part 5: Submit ##
Go to the submission link: {}
Answer these 2 questions:
Which version was easier to play, blowing on the Pi or moving the Pi? Why? (1 or 2 sentences)
(q2)



