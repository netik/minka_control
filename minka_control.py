#!/usr/local/bin/python
#
# minka_control.py
# John Adams <jna@retina.net>
# 8/9/2016
#

# Controls a Minka Aire fan with a Yardstick One or other compatible
# RFCat device

# My remote was Minka air Remote model # TR110A FCC ID KUJCE10007
# 
# This software does not account for the DIP switch settings. 
# My DIP switches are set to
# 
# SW8 0111
# SW9 1111

# If you change your DIP switches, you probably have to change the
# preamble. The manual claims that the DIP switches control the
# 'frequency' but the FCCID and testing says otherwise. I don't see
# the frequency changing on my HackRF.
 
import sys
import time
from rflib import *
from struct import *

d = RfCat()
baudRate = 2950
repeats = 20
PREAMBLE = '\x96\xDB\x6D'

CMDS = { 'off':  '\xB2\xC8',
         'slow': '\x92\xC8',
         'medium': '\x96\x48',
         'fast': '\xB2\x48'
}

def initRadio(d):
  # set up the radio
  d.setFreq(306100000)            # 306.10 Mhz
  d.setMdmModulation(MOD_ASK_OOK) # on-off-keying, no PWM
  d.setMdmDRate(baudRate)         # 2950 Baud is strange but works
  d.makePktFLEN(5)                # 40 bits
  
  # no thanks, we'll send our own preamble
  d.setMdmSyncMode(0)

# do the thing.
initRadio(d)

try: 
  for i in range(0,repeats):
    d.RFxmit(PREAMBLE + CMDS[sys.argv[1]])
except KeyError:
  print "Unknown Command"

