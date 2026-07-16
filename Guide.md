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

Also, we will be creating commits using git commands. If you've never heard of version control, I suggest making a quick search but I will be explaining everything. The only thing you need to do is install Git first (if you haven't already).

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
Notice in source control, the file you staged is now under staged changes. This prepares it for the next step - <mark>Commit</mark>
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

<img width="1365" height="710" alt="Screenshot 2026-07-12 215250" src="https://github.com/user-attachments/assets/06960285-2fcb-463b-b853-0467a67c9bf3" />
<br><br>
The `*` in `from tkinter import *` means all.
To instantiate a window, write `window = Tk()`

Save your file, use the three git commands in order or use the source control sidebar to commit and push.
<br><br>

<img width="1365" height="691" alt="Screenshot 2026-07-12 215433" src="https://github.com/user-attachments/assets/97d10863-191b-4840-b0fb-d038d0e1c0eb" />
<br>
This is what the terminal looks like after everything
<br><br>



















