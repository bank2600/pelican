Title: sed
Date: 2016-11-30 12:00
Category: Notes
Authors: Reese
Cover: http://cdn.computerhope.com/linux/sed.gif

I just found a cool way to find and replace with sed. I wanted to change the name of my author for my blog posts from trexor to Reese with one swoop. I was not going to make a post on this but found a intricacy between GNU/Linux and FreeBSD's sed. Figured I would just for notes for myself or anyone that locates this. Below are the examples of the differences.

GNU/Linux:`find . -type f | xargs sed -i  's/trexor/Reese/g'`

FreeBSD:`find . -type f | xargs sed -i '' 's/trexor/Reese/g'`

I found the original command and soultion on stackoverflow.

