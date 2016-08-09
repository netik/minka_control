# minka_control
Controls a Minka Aire Fan with a Yardstick One or other compatible RFCat / SDR transmitter

John Adams <jna@retina.net>                                                                                                                                   
8/9/2016                                                                                                                                                      

This code was written so that I could learn SDR and as a preliminary piece of code to connect my fans to my Insteon Home Automation system.
An Indigo module is forthcoming.

# Design notes

My remote was Minka air Remote model # TR110A FCC ID KUJCE10007                                                                                               
                                                                                                                                                               
This software does not account for the DIP switch settings.                                                                                                   
My DIP switches are set to                                                                                                                                    

```
SW8 0111                                                                                                                                                      
SW9 1111                                                                                                                                                      
```

If you change your DIP switches, you probably have to change the                                                                                              
preamble. The manual claims that the DIP switches control the                                                                                                 
'frequency' but the FCCID and testing says otherwise. I don't see                                                                                             
the frequency changing on my HackRF.     
