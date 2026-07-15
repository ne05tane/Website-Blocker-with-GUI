---
title: Website Blocker with GUI
author: ne05tane
description:  A software application that allows users to restrict access to specific websites through a visual interface
created_at: 7-15-2026
---
### Submitted as a guide for jus'Study - A Hack Club "You Ship We Ship" event

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

## SetUp -


