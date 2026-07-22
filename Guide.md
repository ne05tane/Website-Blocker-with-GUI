---
title: Website Blocker with GUI
author: ne05tane
description:  A software application that allows users to restrict access to specific websites through a visual interface
created_at: 7-15-2026
---

## Intro - 

Let's first understand how it works.

A website blocker functions by intercepting your computer's request to connect to a website and stopping it before it leaves your device or immediately upon arrival. More advanced blockers install a local proxy/firewall. However, we can make a simpler one by having the blocker
edit a system's "host file".

In every major operating system, there sits a plain-text "host file" that maps hostnames to IP addresses. Usually, you can locate it on 
Windows at <mark>C:\Windows\System32\drivers\etc\hosts</mark> and on Mac/Linux at <mark>/etc/hosts</mark> 

For example, when you type www.wikipedia.com, the computer first checks the host file. If it finds an entry, it uses that IP address. If not,
it asks a DNS server (the internet's translator) for the correct IP.

Okay, now keep that in mind.

You might know that every device on a network has an IP address. In IPv4 networking, they look like four groups of numbers separated by three periods.
E.g, <mark>157.240.229.35</mark> for Facebook. 

Your computer has multiple addresses depending on context & one of them, is what you call a "Loopback address", which is strictly used 
for internal testing. 
<mark>127.0.0.1</mark> is the standard and most universally recognized loopback address, but it is technically just the first usable address in a 
massive reserved block that includes *16 million adresses* from <mark>127.0.0.1</mark> to <mark>127.255.255.254</mark>.

The GUI blocker automatically adds lines to this file mapping the unwanted domain to the loopback address. 
A simple way to do this is just by writing 127.0.0.1 next to the website like - 127.0.0.1 www.instagram.com

Your computer tries to connect to itself instead of the real website, and unless it is somehow running an instagram server locally, the connection fails and the site appears blocked.

The GUI simply provides an easy way to add or remove these lines without you needing to edit the text file manually.

So there you have it! Let's start building.

### Remember, you should make your own changes to your project. Question and find out when you're stuck. Do not blindly copy every step, that is the way to learm!


## SetUp -

To start, create a repo either by cloning or by running `git init` in a CLI tool. You must also track it using Hackatime so if you haven't added the extension to your IDE, do it first. PLease go through https://hackatime.hackclub.com/docs if you're new to Hackatime.

Also, we will be creating commits using git commands. If you've never heard of version control, I suggest making a quick search but I will also be explaining everything. The only thing you need to do is install Git first (if you haven't already).

Both Hackatime and Git are important to set up if you're doing the YSWS.


### Cloning a repo-

I will be using VScode as that is what I'm most familiar with. 

1)<img width="998" height="641" alt="Screenshot 2026-07-12 213132" src="https://github.com/user-attachments/assets/f9f51054-e3d1-4b94-8792-57a4a1407ed2" />

On GitHub, create a new repo and name it.
You can add a README later.
<br><br>

2)<img width="1267" height="632" alt="Screenshot 2026-07-12 213222" src="https://github.com/user-attachments/assets/bbcf082e-70d6-44f6-a781-3ae77073ada6" />
<br>
Copy the URL
<br><br>

3)<img width="1365" height="720" alt="Screenshot 2026-07-12 213631" src="https://github.com/user-attachments/assets/6bea7825-1ebf-432f-9480-5cd519dfe896" />
<br>
Click on clone repository
<br><br>

4)<img width="1365" height="721" alt="Screenshot 2026-07-12 214000" src="https://github.com/user-attachments/assets/dda73aff-d855-4677-bb3e-bec45b39a6bd" />
<br>
Paste the url in the search bar or alternatively, click on the correct repo from the dropdown menu.
<br><br>

5)<img width="1365" height="719" alt="Screenshot 2026-07-12 214415" src="https://github.com/user-attachments/assets/412a9cd3-7a52-4df5-ae36-875a46e78c95" />
<br>
If you've done it right, the command center will display the correct repo's name.
Click on new file and name it main.py
<br><br>

## Basics -

<img width="1365" height="719" alt="Screenshot 2026-07-12 214524" src="https://github.com/user-attachments/assets/3645e26f-0c16-4fc5-b9a4-32eb8be29556" />
<br><br>
Yay! Time to make your first commit.

Locate and click on Source Control (The Y-shaped icon). You will see that right now, your main.py file is unstaged so we have to do three steps-stage, commit and push.

In very simplified terms, you essentially wanna take snapshots of your code. This helps you undo mistakes and revert to previous versions if errors occur and as mentioned above, you might need to install git first.

<mark>Stage</mark> means to choose specific changes from your working directory to include in the next snapshot. We have so far only created 
main.py and nothing else. You can choose to write some code or stage it now itself through two ways :-

1) Click on the plus icon as highlighted in the picture above.
                    OR
2) Open the terminal in your editor and run `git add main.py`

<br><br>

<img width="1365" height="722" alt="Screenshot 2026-07-12 214609" src="https://github.com/user-attachments/assets/706cf9da-3916-468e-9a72-aad236b8e91c" />

<br><br>
Notice in source control, the file you staged is now under staged changes. This prepares it for the next step - <mark>Commit</mark>. </n>
Committing saves a permanent snapshot to your *local* repository history. I say local becuse these changes remain private to your local machine.

However, we need to make our code visible to other developers. This is done through the next step <mark>push</mark> but first we learn to commit.

In the picture above, I wrote "init", short for initialization. Only committing those snapshots isn't helpful, so we write a message alongside it.
For example, you think a block of code you've written is not needed. So you delete it, save your modified file, run `git add` (staging) and write a concise message explaining your step - "remove redundant code".

This is what I did. I initialized a new python file and now I wanna save this snapshot in history so I explained my step - "init"
Once you write init, click on commit and tada! you've just made your first commit.

Just like `git add`, another way to commit is by using the terminal to run `git commit -m "Your message"` 

<br><br>

<img width="1365" height="477" alt="Screenshot 2026-07-12 214747" src="https://github.com/user-attachments/assets/882b727e-a3e5-450c-98c0-c5cd98173ca4" />
<br><br>

For this last step, you have to use the terminal. Locate the terminal in your editor and write `git push`. Earlier, I said committing only saves your changes locally, but <mark>pushing</mark> shares them to a remote repository like GitHub. This serves as cloud backup and other people can learn from your code. You should remember the following three commands in order and remember to commit frequently!

`git add .` The dot after `add` means stage *all* files and changes.
`git commit -m "message"` & 
`git push`

<br><br>

## Using tkinter - 

It is better to keep the blocking logic and graphical interface separate. Our main.py will contain the GUI. You can actually skip to the part where we initialize logic.py but I wanted to make a window first (The rectangle box that has all your widgets like buttons and images)
<br><br>

<img width="1365" height="710" alt="Screenshot 2026-07-12 215250" src="https://github.com/user-attachments/assets/06960285-2fcb-463b-b853-0467a67c9bf3" />
<br><br>

We start by importing tkinter to build our graphical interface. There are many ways you can do this:- 
1. `import tkinter`
2. `from tkinter import * ` (meaning from tkinter import all)
3. `import tkinter as tk` - tk is the alias or shorthand for tkinter. This is useful for when you need to  access the module's classes and functions using a shorter prefix.

Next, `window=Tk()` instantiates the root window (the main container that holds you buttons, widgets and labels)

Save your file, use the three git commands in order or use the source control sidebar to commit and push.
<br><br>

<img width="1365" height="691" alt="Screenshot 2026-07-12 215433" src="https://github.com/user-attachments/assets/97d10863-191b-4840-b0fb-d038d0e1c0eb" />
<br><br>
This is what the terminal looks like after everything
<br><br><br>

<img width="1365" height="641" alt="Screenshot 2026-07-12 215827" src="https://github.com/user-attachments/assets/10b13699-a600-4446-ac87-74717a48fb7b" />
<br><br>
You can check your remote repository to see if it shows up. 
<br><br><br>

<img width="1363" height="683" alt="Screenshot 2026-07-12 221111" src="https://github.com/user-attachments/assets/7acfdbd2-ff85-4275-bebd-ab10315a389a" />
<br><br>
To define the window's size, we use the method `window.geometry("widthxheight")`. You must enter the values in pixels. 

You can even define its position: `window.geometry("widthxheight+x+y)` for example,  `window.geometry("300x200+100+50")` sets the size to 300x200 and positions the top-left corner at x=100, y=50. 

Negative Coordinates: Using negative values (e.g., "-50-50") positions the window relative to the bottom-right edge of the screen.

Use `window.title('text')` to name the title.

But most importantly, you must call `window.loop(`) to start the event loop aka, keeping the application responsive and to actually display the window. If you try running main.py and for some reason, your root window does not show up, make sure to check if you've called it correctly.
<br><br>

<img width="1365" height="721" alt="Screenshot 2026-07-12 221125" src="https://github.com/user-attachments/assets/5c2d9e19-7b56-42f7-a375-1ff684948ccc" />
<br><br>
This is what it looks like when you run it and as you can see, it kind of looks weird
so you can modify the dimensions in `window.geometry()`
<br><br>

<img width="1365" height="682" alt="Screenshot 2026-07-12 221219" src="https://github.com/user-attachments/assets/c7cba96d-ba78-4e97-94b3-4eea673fbb22" />
<br><br>
If you're happy with how it looks, you can go ahead and stage and commit.
<br><br>

<img width="964" height="308" alt="Screenshot 2026-07-12 224853" src="https://github.com/user-attachments/assets/88c1dc88-5157-4c74-a2f5-c7284378dbca" />
<br><br>
Next we're gonna initialise logic.py and import datetime and time modules.
Create two variables as in the picture. One will hold the directory to our hosts file and the second - the loopback address.
<br><br>

<img width="1348" height="665" alt="Screenshot 2026-07-12 225010" src="https://github.com/user-attachments/assets/30d6d8b5-22d5-4ab5-83f0-dbd4744cc1a7" />
<br><br>
Locate the hosts file in your system and copy the path. 
<br><br>

<img width="1360" height="525" alt="Screenshot 2026-07-12 233524" src="https://github.com/user-attachments/assets/490b089d-afce-4f2c-9473-dfb6434b7032" />
<br><br>
Next write the blocking logic. I did this by creating a function with the same name that will take two arguments- `duration_hours` & `website_list`
As the name says, one will hold a list of websites and the other will ask for the time duration that you want them blocked. 

Then we define <mark>endtime</mark> to be a difference between your current local time and the duration that you enter. 
Simply add `datetime.datetime.now` to `datetime.timedelta()`

`datetime.datetime.now` is a class method that returns a datetime object representing the current local date and time based on the system clock. 
`datetime.timedelta()` represents a duration or difference between two dates or times, rather than a specific point in time.

Name the variable that will hold duration_hours for example, hours like I did above.

If you know how to work with file handling operations in python, the next steps are easy,

In the `While True:` block, it basically says,

IF the current date and time (`datetime.datetime.now`) is less than our defined endtime, open the hosts file in "read and write" mode (`r+`) using a shorthand (`fh` as I named it but you can use `fo`, short for file object) and run the following instructions:-

 1. <mark> Read the whole thing </mark> {`content = fh.read()` OR `fo.read()`}
 2. <mark> Ignore if a site we want blocked is already there</mark> (`for site in website_list:`....`pass`)
 3. <mark> Else write it down in the hosts file so we can block it</mark>

If you remember in the intro, I explained we could do the last step by writing "127.0.0.1 www.instagram.com" for example.

Can you try to figure out how `fh.write(redirect  + " " + site "\n"` does that? 

Also note, `r` opens the file in "read mode", `w` in "write mode", `a` in "append mode", `r+` in "read and write" mode etc. 
We want to be able to both read and write in our file.
<br><br>

<img width="919" height="520" alt="Screenshot 2026-07-12 235646" src="https://github.com/user-attachments/assets/3870ca9e-6602-4662-8ce8-86dacd2c2bc4" />
<br><br>

Then the else block (`datetime.datetime.now > end_time`) will execute the unblocking phase, you can see how it's done above but I encourage you try to figure it out yourself FIRST.

Hints:-

1.`fo.seek()` OR `fh.seek()` changes the position of the cursor by a specified no. of bytes. The syntax is {fo.seek(offset, from_what}.
We want the file handle/cursor at the beginning so we put the reference as 0 in `fo.seek(0)` because 0 puts the cursor at the beginning, 1 lets it stay in its current position and 2 shifts the cursor at the end.

2. `time.sleep()` pauses the execution of the current thread for a specified number of seconds. I later changed it from 30 seconds to something shorter. I recommend you do this to pause execution between checks or the script would consume 100% of the CPU cause the while loop would run infinitely fast!

This is the only instance in the code where time module is used. So if you don't want to implement `time.sleep()`, you don't need to `import time`. However, for the reasons I mentioned, it is highly suggested you do use this.

3. `fo.truncate(size)` sets the file to exactly size bytes. If size is smaller than the current file, data is lost. Without arguments, it shrinks the file to the current position of the file pointer.

Also, understand the difference between `read()` and `readlines()`. The first returns a string, the latter returns a *list* of strings. Use `read()` when you need the whole content as a block and `readlines()` when you need to process individual lines.

Remember to commit!
<br><br>

## GUI -

<img width="993" height="686" alt="Screenshot 2026-07-13 003742" src="https://github.com/user-attachments/assets/0a23dd0c-2c11-4f90-a580-086851f6acb1" />

<br><br>
Back to main.py, we will `import threading` and our logic.py file.

To plagiarize, <mark> "the threading module is a built-in Python library that provides a higher-level interface for creating and managing threads, allowing multiple operations to run concurrently within the same process.  It is designed primarily for I/O-bound tasks (like web scraping or file operations) where the program spends time waiting for external resources" </mark>

Then we define a class `App` that will encapsulate the logic, state and widgets. The dunder (double underscore) method right below it is a special function that Python automatically executes the moment you create a new instance of the class.

In the context of Tkinter, root is the main window or the top-level container for your entire application. Notice though, that in
`def __init__(self, window)`, I named my root variable `window` because I didn't need to differentiate between a main window or other windows. 
However, the standard is to just name it `root`.

If you name it root, you will write `self.root` instead of `self.window`. 

Also, if you had earlier created the window, the methods you used to change its size and position will all have `self` added in front. (see above) 

<br><br>
<img width="1189" height="680" alt="Screenshot 2026-07-13 073910" src="https://github.com/user-attachments/assets/164ab4a6-c777-4d8a-9037-7f6ce03923fa" />

<br><br>

Thus, you must also put `window.mainloop()` inside the `if__name__== "__main__"` block to the very end.

*It is `root.mainloop()` if you have named your root variable root!*

The rest is easy to understand:-
1. Write `window=Tk()` or `root=Tk()` to initialize the main application window. Basically, this will contain all your widgets and labels.
2. `app=App(window)` or `app=App(root)`
3. Finally, `window.mainloop()` or `root.mainloop()` to run the window. 

`def _setup_ui(self):` _setup_ui only has single underscores, not to be confused with special functions like `__init__` which have double underscores.

Then `tk.label()` creates a label, basically a button which im going to name focus. Then you can modify that button using attributes such as `font=(<fontname>, <fontsize>, <style>)`, `background` & `foreground`. Then you need to pack all these attributes using   `self.timer.pack`. Use pady to make changes in the y direction aka make the button have greater width for example 20px. Similarly, use padx aka padding in the x direction to change the length of the label.
<br><br>

<img width="1365" height="567" alt="Screenshot 2026-07-13 080225" src="https://github.com/user-attachments/assets/4e3d6386-639d-495f-81ee-421ddd7ccf9a" />
<br><br>
You can make as many labels as you want and modify them using the above attributes.
<br><br>

<img width="1365" height="687" alt="Screenshot 2026-07-13 075746" src="https://github.com/user-attachments/assets/e01080dd-85b8-4490-9c84-94d62f4d7311" />
<br><br>
You can save and run to see how it looks so far. 
It's very basic and you can change it to your liking
<br><br>

<img width="1365" height="588" alt="Screenshot 2026-07-13 081006" src="https://github.com/user-attachments/assets/2afea515-8588-4fb2-8161-c62422f043a3" />
<br><br>
We're gonna import another scrolledtext from tkinter as well. 
<br><br>

<img width="720" height="542" alt="Screenshot 2026-07-13 081506" src="https://github.com/user-attachments/assets/4d74e93a-997b-4d1d-8216-af8415c92922" />
<br><br>
Copy what I've written to create a text box that can scroll.
<br><br>

<img width="1182" height="574" alt="Screenshot 2026-07-13 082144" src="https://github.com/user-attachments/assets/40196ae4-9a1a-4c95-a24b-2c96ac4eff35" />
<br><br>
I would like to change the box's dimensions
<br><br>

<img width="1365" height="650" alt="Screenshot 2026-07-13 092206" src="https://github.com/user-attachments/assets/2adc24e1-70b2-4ce9-8fb6-47f6c67d60eb" />
<br><br>
You can make your own changes to settle on what you like.
<br><br><br>

## Time to Ship -


















































