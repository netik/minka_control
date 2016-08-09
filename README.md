# minka_control

Controls a Minka Aire Fan with a Yardstick One or other compatible RFCat / SDR transmitter
These fans utiize a 306.1Mhz receiver.

Requires Python and RFCat libraries (aka rflib)

This code was written so that I could learn SDR and as a preliminary piece of code to connect my fans to my Insteon Home Automation system.
An Indigo module is forthcoming.

# Design notes

My remote was Minka Aire Remote model # TR110A FCC ID KUJCE10007 

This software does not account for the changing of the DIP switch settings.
It will only work with the switches set to:
```
SW8 = 0111 
SW9 = 1111
```

DIP Switches are located in the battery compartment of the remote.

# Resetting the DIP switches

If you change your DIP switches, you probably have to change the preamble. To do that, you have to reverse engineer the preamble again using an SDR as an analyzer and  The manual claims that the DIP switches control the 'frequency' but the FCCID and testing says otherwise. I don't see the frequency changing on my HackRF.

Also, if you change your DIP switches, the procedure to update the fan is:

1. Disable power to the fan via the circuit breaker or otherwise
1. Enable power
1. Within 60 seconds, hit stop, wait a second, then, 
1. Hold down stop for ten seconds. 

If you have a lamp on your fan the light will blink once to indicate that it's learned the transmitter ID.

