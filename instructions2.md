# Lab: Turn your web page into a phone app

Today you'll turn the web page you made last week into a **Progressive Web App (PWA)**: a website your phone can install like an app, with its own icon, opening full screen and even working offline. You don't have to register it in an App Store, and it works on both iPhone and Android.

The purpose of this lab is to help you learn how to prompt a generative AI well, and to let you make something you can show your friends and family!

Your app needs two new files:
- **manifest.json** tells the phone your app's name, icon, and colors.
- **sw.js** (a "service worker") saves a copy of your app on the phone so it can run offline.

Together these let your phone understand and show your page like a normal app.

## 1. Decide where your app will live, and find its address
You can either update last week's repository, or keep it as it is and make a new one.

> **To keep your old repository:** create a new repository and upload your files from last week into it. Then click **Settings**, click **Pages** in the menu on the left, and under **Branch** change **None** to **main** and click **Save**.

Your site's address is either:
- `https://USERNAME.github.io/` if your repository is named `USERNAME.github.io`, or
- `https://USERNAME.github.io/REPOSITORY-NAME/` for any other repository name.

Open it in a browser to make sure it works. Write the address down; you'll need it twice.

## 2. Ask an AI to make the files
Open your `index.html` on GitHub and copy all of it. You'll paste it into the AI along with your request. (Don't just give the AI a link: many AIs can't open GitHub links and will make up a file instead.)

**Write your own prompt first.** A good prompt tells the AI:
- **what you have:** your index.html, pasted in
- **what you want:** a manifest.json, a sw.js, and an updated index.html
- **where it will live:** your address from step 1
- **your rules:** use relative paths (`./`) so it works in a folder; make the service worker "network-first" so your updates show up; don't change how the page looks or works
- **what to tell you:** the exact file names and sizes of the icon images it expects

When you're done, compare your prompt with this one. Did you leave anything out?

> Here is my index.html. Turn it into a Progressive Web App hosted on GitHub Pages at [YOUR ADDRESS FROM STEP 1]. Give me manifest.json, sw.js, and an updated index.html. Use relative paths (./) everywhere. Make the service worker network-first so updates show up. Don't change how my page looks or works. Tell me the exact file names and sizes of the icon images I need.

Save each file the AI gives you with exactly the name it uses. Before you go on, ask the AI: "Explain what each new line in index.html does."

## 3. Make your icon
Make a square image, at least 512×512 pixels, saved as a PNG. You can draw it, use Canva, or ask an image AI. Save it with **exactly** the file names the AI told you (usually `icon-192.png` and `icon-512.png`; the same image at both sizes is fine). If the AI's files put icons in a folder (like `icons/icon-192.png`), put them in a folder with that name.

## 4. Upload everything
On your repository's main page, click **Add file → Upload files** (the `+` button just left of the green **Code** button). Drag in manifest.json, sw.js, your icons, **and** the new index.html. GitHub replaces your old index.html with the new one. Click **Commit changes**.

## 5. Wait for it to build
Click the **Actions** tab. When the newest run shows a green check (usually 1–2 minutes), your site is updated.

## 6. Install it on your phone
Open your site's address on your phone, then:
- **iPhone:** tap Share (a box with an arrow sticking out) → **Add to Home Screen**. If you see "Open as Web App," turn it on.
- **Android (Chrome):** tap the ⋮ menu → **Install app** or **Add to Home screen**.

## 7. Test it
Open the app from your home screen. Now turn on **airplane mode** and open it again. It still works! That's the service worker.

## 8. Share it
Anyone can install your app: send them your address and have them do step 6.

## 9. Make a bigger app
Using what you learned in this lab and the last one, make a new app that's more complex than your first. One way to extend it is to use an API in your app. There is a list of free APIs [here](https://github.com/public-apis/public-apis). Pick one with **No** in the Auth column and **Yes** in the CORS column, so it works with our setup:
- **Auth: No** means you don't need a secret key. (Your repository is public, so anyone could see a key you put in it.)
- **CORS: Yes** means the API lets a web page in your browser ask it for data.

> An API (Application Programming Interface) is a fancy name for a connection between computer programs. You call the API from one program in a specific way, and another program returns data in a specific way.

Your app can only get new data from an API while it's online, so in airplane mode that part won't load. That's expected.

## If something goes wrong
- **Blank page or wrong icon:** check that your file names match the manifest exactly (capital letters count) and that they're in the right folder.
- **No "Install" or "Add to Home Screen" option:** the manifest or icons aren't loading. Paste your manifest.json into the AI and tell it what happened.
- **Your changes don't show up:** close the app completely and reopen it, or delete it from your home screen and add it again.
