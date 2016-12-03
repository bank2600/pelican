Title: RF and more Arduino
Date: 2016-06-26 14:35
Category: SDR, Arduino
Tags: SDR, Arduino
Slug: rflayer0
Authors: Reese
Summary: More Arduino labs and SDR RF fun.

# SDR and Arduino

I have got my [SDR](https://en.wikipedia.org/wiki/Software-defined_radio) back out, the local repeaters have been pretty active. I seem to keep hearing the same people. Had a strom come in and they gave good updates. I got out my HamItUp Upconverter and heard some traffic on the HAM bands. I did this [lab](http://oomlout.com/a/products/ardx/circ-08/) it was very cool messing with analog inputs. I also learned what a [potentiometer](https://en.wikipedia.org/wiki/Potentiometer) is. I did a couple more labs and now I'm done with CIRC-09. Reversing the code in
this one was fun it let me turn it into a night light. 



#int sensorPin = 0;    // select the input pin for the potentiometer
#int ledPin = 13;      // select the pin for the LED
#int sensorValue = 0;  // variable to store the value coming from the sensor
#
#void setup() {
#  // declare the ledPin as an OUTPUT:
#  pinMode(ledPin, OUTPUT);  
#}
#
#void loop() {
#  // read the value from the sensor:
#  sensorValue = analogRead(sensorPin);    
#  // turn the ledPin on
#  digitalWrite(ledPin, HIGH);  
#  // stop the program for  milliseconds:
#  delay(sensorValue);          
#  // turn the ledPin off:        
#  digitalWrite(ledPin, LOW);   
#  // stop the program for for  milliseconds:
#  delay(sensorValue);                  
#}

This was a test for codeblock in markdown. I can't tell if it worked as of writing this.

## Hyper-V

Yes I still do run Windows for some of the video games I enjoy playing. I have been loving what the Linux guys did with KVM. So I figured I'd try out Hyper-V. The setup was quite simple. All I had to do was check a box and then was told I needed to reboot the computer so the service would be started. I have installed a rolling release of Gentoo and I was not able to change the resolution to a higher more native one. Maybe I should have tried a more popular distro for starting with. In all A
good weekend I got some side work done.
