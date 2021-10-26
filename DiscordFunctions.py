import discord
import requests

class Guild():
  def delete_all_channels():
    for DelAll in ctx.guild.channels:
      await DelAll.delete()

  def create_channels(Number, *ChannelName):
    for CreateChannels in range(Number):
      await CreateChannels.guild.create_text_channel(ChannelName)

class Call():
  def start_ringing(ID):
    #Still in developing

  def stop_ringing(ID):
    #Still in developing
