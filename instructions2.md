Today in lab:
  We are going to make a "progressive web app" on your phone.  This acts like an app on your phone, but doesn't require you to register through the App Store and works automatically on both Android and iPhone. The purpose of this lab is to help you guys learn how to properly prompt a generative AI and to let you guys make something you can show your friends and family! Here are the instructions:
1. Open the GitHub page you made last week and copy the URL. Next, paste the link into the AI of your choice, and ask it to generate the files necessary to turn the web app there into a progressive web app. 
2. Download the files it creates. These should include a manifest file, a serviceworker.js or sw.js file, and icons for your app. It will also regenerate your index.html file to accommodate the changes needed.  
> Progressive web apps need a manifest to define certain metadata associated with the app and a service worker to cache content that the app needs when it is offline. These allow your phone to understand and render your page like a normal app, and allow it to run offline. 

3. Go back to the main page of your repository, then click the plus button immediately to the left of the green code button. Select Upload files in the dropdown that comes up, and upload all the files other than the new index.html
> If you want to keep your old repository you can, but it is not required. To do so, you must create a new repository, upload all of your files, the new ones from this week and your old from last week. Then click on the settings button, and click pages on the bottom left, then under where it says branch, click on None, then change the branch to main and hit save. You will be able to view your new site at [your-username].github.io/[your-repository-name].
4. Next, paste the new Index file into your repo. Open the new index.html file, and hit Control-A, Control-C to copy the contents. 
5. Go back to the main page of your repository, and click on the index.html link. 
6. In the upper right, click on the pencil icon, then once you are in the edit window, click on the contents of the file and hit Control-A, and then delete. Then hit Control-V to paste the new index.html into the box. Click the green commit changes button in the upper right, then click the commit changes button in the window that pops up. 
7. Give it about a minute or two to build all these changes, then open the [your-username].github.io url on your phone, hit the share button for the page (it should look something like a small box with an arrow sticking out of it) and scroll through the options until you see "add to home screen". Click on that and make sure that "Open as a Web App" is set to yes if it is an option. 
8. Use the app on your phone!
9. If you want to give this to a friend or a parent or a sibling, all they have to do is step 7.
10. Using what you have learned from this lab and the last, create a new app, thats more complex than your first one. A possible path of extension you can take is incorporting an API into your app. A list of free API's can be found [here](https://github.com/public-apis/public-apis). Make sure that they are a No in the Auth column and a Yes in the CORS column, so that they work with our setup for the project. 

> An API (Application Programming Interface) is a fancy name for a connection between computer programs. You call the API from one program in a specific way, and another program returns data in a specific way.


