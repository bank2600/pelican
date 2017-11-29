Title: osTicket
Date: 2017-04-07 15:00
Authors: Reese
Summary: Getting organized
Cover: http://osticket.com/sites/default/files/osticket-supsys-sm.png
 
I have always been the type to have twenty projects going at the same time, and Ideas for more. It's been hard keeping up with all my projects and goals. I started thinking about using ticket software for at home stuff. If it works good in the office why can't it at home? I currently have osTicket running in a FreeBSD jail. I am still running FreeNAS 10.2, not updated to the Corral release train yet. I'll give it some more time for the quicks and edge cases to get worked out.
Sure that I'll have a blog post about my upgrade when that day comes. Currently I'm researching and planning the best option to move all my vm's and jails from one Virtualbox into bhyve or docker.

I've had the ticket system up for about a month and have over thirty tickets. I have knocked a few out and that always feels good. I like how I can rank them in priority also this is a handy feature. I have not setup the email system or any other plugins yet. This has been one of the most useful projects I've done in a while. If one could say this was a meta-project.

I setup a FEMP stack in the jail from [this](https://www.digitalocean.com/community/tutorials/how-to-install-an-nginx-mysql-and-php-femp-stack-on-freebsd-10-1) handy guide from DigitalOcean. I decided to use nginx and regretted this later (but I fixed it!). I searched for a specific tutorial on installing osTicket on FreeBSD. I found [this](https://jombsd.blogspot.com/2016/02/how-to-install-osticket-freebsd.html) one and used it was pretty nice. However I did need to install some
additional ports that the blog did not note. 

1. [devel/pecl-APCu](https://www.freshports.org/devel/pecl-APCu/) 
2. [databases/php56-mysqli](https://www.freshports.org/databases/php56-mysqli/)

I hope to find other projects that can be as useful as this.
