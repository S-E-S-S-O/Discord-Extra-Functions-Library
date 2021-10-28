import discord
import requests
from colorama import Fore

class Guild():
  def delete_all_channels(ctx):
    for DelAll in ctx.guild.channels:
      try:
        await DelAll.delete()
      except:
        pass

  def create_channels(Number, *ChannelName):
    for CreateChannels in range(Number):
      try:
        await CreateChannels.guild.create_text_channel(ChannelName)
      except:
        pass
      if Number == None:
        raise Exception(f"[{Fore.RED] ERROR{Fore.WHITE}] Nothing has been put in the {Fore.YELLOW}Number {Fore.WHITE}input.") 
      elif ChannelName == None
        raise Exception(f"[{Fore.RED] ERROR{Fore.WHITE}] Nothing has been put in the {Fore.YELLOW}ChannelName {Fore.WHITE}input.") 

class Call():
  def start_ringing(ID):
    #Still in developing

  def stop_ringing(ID):
    #Still in developing
