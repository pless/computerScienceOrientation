1. Create a Github account if you do not have one. If you have one go to github.com 
2. Click on the plus button on the top right of the dashboard, and select create a new repository. Name it [Your username].github.io, make sure the visibility is set to public. Make sure it is your exact username, include any numbers and the exact spelling.
3. Click create a new file under quick setup in the bottom left of that box, name it index.md and in the body type "Hello World"
4. Click commit changes in the upper right hand corner, let it fill in the message, then click commit changes again.
5. After about a minute or two, at https://[yourusername].github.io you should see "Hello World!"
6. Come up with a idea for a web app
    - The best ideas will be: Specific, simple, not just a reinvention of a app you already use
7. Describe the app, in detail in a paragraph
    - Include things like: intended users, problem to solve, what the user needs to do in it, etc.
8. Edit your description down to around 3-5 features
    - You can add more as you iterate, but for a first go, simple is better
9. Paste this description into your LLM of choice, and ask it "Can I build this app in GitHub Pages"
10. If the answer is yes, ask it to generate you an index.html file, a style.css file, and a app.js file
11. It will either give you a zipped folder containing all 3 files, or 3 individual files, or just raw code seperated out.
    - If you got the first, unzip it to a folder and right click on the .html file and select open in your browser
    - If you got the second, download all 3, make sure they are named correctly and put them in a new folder named something distinctive
    - If you got the 3rd, open VS Code, select file -> create new file -> name it app.js, style.css, index.html depending on the code you are pasting -> hit enter and paste the code into the file and save it
12. Poke around the opened site from what you downloaded, make sure it works roughly how you expected.
    - If the style or scripting isnt loading open the html file in a text editor and look for the references to "style.css" and "app.js" and make sure they use a relative path (./) and referencing the right file names
    - If you have other errors beyond that, make sure theres no issues with open brackets, open parenthases or braces, etc as that can come up
    - If you can't diagnose the issue, describe it to your LLM and see if it can diagnose and fix it, and failing that talk to a TA or the professor 
13. Once you are satisifed that it works, go to your repository link from earlier. Click on the HelloWorld.md file you made earlier, and in the upper right hand corner select the three dots icon. In the drop down that comes up, select delete.
14. Go back to the main page of your repository, then click the plus button immediate to the left of the green code button. Select upload files in the dropdown that comes up, and upload your 3 files. 
15. It may take a second to build, but once it does you can go to https://[Your username].github.io
16. Once you have it live at URL, show a friend! See what they built
17. Once you have finished all these steps, look at any features you cut in step 3, describe them to your LLM and push the updated files and see what happens



