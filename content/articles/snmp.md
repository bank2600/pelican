Title: SNMP Fun
Date: 2016-11-27 18:00
Category: Labs
Authors: Reese
Summary: SNMP for all
Cover: http://terraltech.com/wp-content/uploads/2015/01/snmp.png?76a024

#Cacti


For quite some time on the podcasts I listen to I've heard talk about server monitoring for example Nagios and Zabbix. Having no experience in this and it sounded pretty intriguing. I created a fresh jail on my FreeNAS Mini and got busy. Not knowing where to start I did a google search for `network monitoring`. I seen a lot of information about Cacti and it seemed to be a good starting point.


I started out with [this guide](https://dnaeon.github.io/cacti-freebsd/). I failed to realise that the binary package for cacti did not install `mysql56-server`. I found a great [guide](https://www.digitalocean.com/community/tutorials/how-to-install-an-apache-mysql-and-php-famp-stack-on-freebsd-10-1) from the good folks at Digital Ocean, they have great tutorials. After I got Cacti up and running the next logical step was to add devices. I found a [
FreeBSD](http://docs.cacti.net/usertemplate:host:freebsd) it took a few times messing with the template and forgetting to add the cron script. *Eventually I had Graphs!*. I was able to find a template for my [Mikrotik switch](http://docs.cacti.net/usertemplate:host:mikrotik) also. After figuring out how to enable snmp on OpenWRT as described [here](https://wiki.openwrt.org/doc/howto/snmp.server) I had many data sources for the graphs.


After getting all my SNMP devices enabled and graph I was looking for more things to add. I figured all the systems log so why not try [a syslog plugin](http://docs.cacti.net/plugin:syslog). Under the Prerequisites I noticed > Cacti Settings plugin is required. After installing both plugins I was unable to get the logs from the remote system showing. I could see the logs coming across the network from a packet capture and verify they got wrote in the cacti host. Strange thing is when I
went to install the syslog plugin I got a error saying I needed more plugins. One was [settings](http://docs.cacti.net/plugin:settings) the other was [PIA](http://docs.cacti.net/manual:087:1_installation.9_pia). While troubleshooting this I skimmed the release notes and noticed [this](http://cacti.net/release_notes_0_8_8.php) *Plugin Architecture is now part of Cacti*?? are the plugins or directions not up to date? pretty confusing. Before figuring out the
culpret I talked with a comrade about the Cacti issue. His response: >>Fuck Cacti, look at LibreNMS.


##LibreNMS


The landing page for LibreNMS looked more updated then Cacti, when I seen the [live demo](http://www.librenms.org/#try) I was sold. There is no hassle with template in Cacti. By default LibreNMS has auto discovery that will scan the networks you define in the config file every 6 hours for new devices. The mouse over graphs are very nice. The website UI is way more user friendly. I have played with the alerts to send to Slack. I'm sure that I'll add more extensions down the road. That's all for
now!


Thanks for reading
