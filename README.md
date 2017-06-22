# harvest
Simple data values collector in MySQL for the Pimoroni's Enviro pHAT in Python3 for your Raspberry Pi. I use it personnaly with 2 Pi Zero.

First, to work with a MySQL database you need to install via pip3 the command : 
  sudo pip3 install PyMySQL

You must to adapt the m_dbb.py module to correctly insert the data in your own bdd tables, fields...

I use a Enviro pHat + Blinkt! staking to benefit from a luminous indication when the insertion request is executed, see the m_blinkt_pulse.py module.
Customs colors for Blinkt! are stored in m_color_list.py.
