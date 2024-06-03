from asyncio import run as arun
from collections import UserDict
from highrise import BaseBot, __main__
from highrise import *
from highrise.models import SessionMetadata, User
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
from highrise import BaseBot, User, Position, SessionMetadata
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition,Item,Position,User,)
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (AnchorPosition,CurrencyItem,Item,Position,SessionMetadata,User,)
from highrise.__main__ import BotDefinition

class BotDefinition:

  def __init__(self, bot, room_id, api_token):
    self.bot = bot
    self.room_id = room_id
    self.api_token = api_token


class MyBot(BaseBot):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.following_user = None
    self.banned_users = {}
    self.following_username = None
    super().__init__()
    self.user_positions = {}

  async def on_user_leave(self, user: User) -> None:
    print(f"{user.username}")
    await self.highrise.chat(f" Yeah gtfo {user.username}")


  async def on_user_join(self, user: User,position: Position | AnchorPosition):
    await self.highrise.chat(f"  Hi {user.username}, welcom in \n Wait \n Who tf are you ?")
    

  async def run(self, room_id, token):
    definitions = [BotDefinition(self, room_id, token)]
    await __main__.main(definitions)

 
  async def on_chat(self, user: User, message: str):

    if message.startswith("!come") and user.username in ["T9s", "_Rolex_x","xXLoveLoopXx"]:
      response = await self.highrise.get_room_users()
      your_pos = None
      for content in response.content:
        if content[0].id == user.id:
          if isinstance(content[1], Position):
            your_pos = content[1]
            break
      if not your_pos:
        await self.highrise.send_whisper(user.id, f"احداثيات غير صالحه")
        return
      await self.highrise.chat("I,m coming ")
      await self.highrise.walk_to(your_pos)

    if message.startswith("Float"):
      await self.highrise.send_emote("emote-float", user.id)
    if message.startswith("Tiktok2"):
      await self.highrise.send_emote("dance-tiktok2", user.id)
    if message.startswith("pose1"):
      await self.highrise.send_emote("emote-pose1", user.id)
    if message.startswith("Russian"):
      await self.highrise.send_emote("dance-russian", user.id)
    if message.startswith("Sing"):
      await self.highrise.send_emote("idle_singing", user.id)
    if message.startswith("Enth"):
      await self.highrise.send_emote("idle-enthusiastic", user.id)
    if message.startswith("Casual"):
      await self.highrise.send_emote("idle-dance-casual", user.id)
    if message.startswith("sit"):
      await self.highrise.send_emote("idle-loop-sitfloor", user.id)
    if message.startswith("Lust"):
      await self.highrise.send_emote("emote-lust", user.id)
    if message.startswith("Creedy"):
      await self.highrise.send_emote("emote-greedy", user.id)
    if message.startswith("Bow"):
      await self.highrise.send_emote("emote-bow", user.id)
    if message.startswith("Curtsy"):
      await self.highrise.send_emote("emote-curtsy", user.id)
    if message.startswith("Snow"):
      await self.highrise.send_emote("emote-snowball", user.id)
    if message.startswith("Angel"):
      await self.highrise.send_emote("emote-snowangel", user.id)
    if message.startswith("Confused"):
      await self.highrise.send_emote("emote-confused", user.id)
    if message.startswith("Teleport"):
      await self.highrise.send_emote("emote-teleporting", user.id)
    if message.startswith("Swordfight"):
      await self.highrise.send_emote("emote-swordfight", user.id)
    if message.startswith("Energy"):
      await self.highrise.send_emote("emote-energyball", user.id)
    if message.startswith("Tiktok8"):
      await self.highrise.send_emote("dance-tiktok8", user.id)
    if message.startswith("Blackpink"):
      await self.highrise.send_emote("dance-blackpink", user.id)
    if message.startswith("Model"):
      await self.highrise.send_emote("emote-model", user.id)
    if message.startswith("Penny"):
      await self.highrise.send_emote("dance-pennywise", user.id)
    if message.startswith("Tiktok10"):
      await self.highrise.send_emote("dance-tiktok10", user.id)
    if message.startswith("Telekinesis"):
      await self.highrise.send_emote("emote-telekinesis", user.id)
    if message.startswith("Hot"):
      await self.highrise.send_emote("emote-hot", user.id)
    if message.startswith("Weird"):
      await self.highrise.send_emote("dance-weird", user.id)
    if message.startswith("Pose7"):
      await self.highrise.send_emote("emote-pose7", user.id)
    if message.startswith("Pose8"):
      await self.highrise.send_emote("emote-pose8", user.id)
    if message.startswith("Pose3"):
      await self.highrise.send_emote("emote-pose3", user.id)
    if message.startswith("Pose5"):
      await self.highrise.send_emote("emote-pose5", user.id)
    if message.startswith("kiss"):
      await self.highrise.send_emote("emote-kiss", user.id)

    if message.startswith("Laughing"):
      await self.highrise.send_emote("emote-laughing", user.id)
    if message.startswith("cursing"):
      await self.highrise.send_emote("emoji-cursing", user.id)
    if message.startswith("flex"):
      await self.highrise.send_emote("emoji-flex", user.id)
    if message.startswith("gagging"):
      await self.highrise.send_emote("emoji-gagging", user.id)
    if message.startswith("celebrate"):
      await self.highrise.send_emote("emoji-celebrate", user.id)
    if message.startswith("macarena"):
      await self.highrise.send_emote("dance-macarena", user.id)
    if message.startswith("charging"):
      await self.highrise.send_emote("emote-charging", user.id)
    if message.startswith("shopp"):
      await self.highrise.send_emote("dance-shoppingcart", user.id)
    if message.startswith("maniac"):
      await self.highrise.send_emote("emote-maniac", user.id)
    if message.startswith("snake"):
      await self.highrise.send_emote("emote-snake", user.id)
    if message.startswith("frog"):
      await self.highrise.send_emote("emote-frog", user.id)
    if message.startswith("superpose"):
      await self.highrise.send_emote("emote-superpose", user.id)
    if message.startswith("cute"):
      await self.highrise.send_emote("emote-cute", user.id)
    if message.startswith("tiktok9"):
      await self.highrise.send_emote("dance-tiktok9", user.id)
    if message.startswith("weird"):
      await self.highrise.send_emote("dance-weird", user.id)
    if message.startswith("cutey"):
      await self.highrise.send_emote("emote-cutey", user.id)
    if message.startswith("punkguitar"):
      await self.highrise.send_emote("emote-punkguitar", user.id)
    if message.startswith("zombierun"):
      await self.highrise.send_emote("emote-zombierun", user.id)
    if message.startswith("fashi"):
      await self.highrise.send_emote("emote-fashionista", user.id)
    if message.startswith("gravity"):
      await self.highrise.send_emote("emote-gravity", user.id)
    if message.startswith("icecream"):
      await self.highrise.send_emote("dance-icecream", user.id)
    if message.startswith("wrong"):
      await self.highrise.send_emote("dance-wrong", user.id)
    if message.startswith("uwu"):
      await self.highrise.send_emote("idle-uwu", user.id)
    if message.startswith("tiktok4"):
      await self.highrise.send_emote("idle-dance-tiktok4", user.id)
    if message.startswith("shy2"):
      await self.highrise.send_emote("emote-shy2", user.id)
    if message.startswith("anime"):
      await self.highrise.send_emote("dance-anime", user.id)

    if message.lower().startswith("!help"):
      dance_list = [
          "Float",
          "Tiktok2",
          "pose1",
          "Russian",
          "Sing",
          "Enth",
          "Casual",
          "sit",
          "Lust",
          "Creedy",
          "Bow",
          "Curtsy",
          "Snow",
          "Angel",
          "Confused",
          "Teleport",
          "Swordfight",
          "Energy",
      ]

      # Convert the list to a comma-separated string
      dance_list_str = ", ".join(dance_list)
      await self.highrise.send_whisper(user.id, dance_list_str)

    if message.lower().startswith("!help"):
      await self.highrise.send_whisper(
          user.id,
          "Model , Penny , Tiktok10 , Telekinesis , Hot , Weird , Pose7 , Pose8 , Pose3 , Pose5 , kis , Laughing , cursing , flex , gagging , Blackpink , Tiktok8"
      )

    if message.lower().startswith("!help"):
      await self.highrise.send_whisper(
          user.id,
          " celebrate , macarena , charging , shopp , maniac , snake  , frog , superpose , cute , tiktok9 , weird , cutey ,  punkguitar , zombierun , fashi , gravity , icecream , wrong , uwu , tiktok4 , shy2 , anime"
      )


if __name__ == "__main__":
  room_id = "6642999dd78c92aa3c494b17"
  token = "d765dff2980f9300fcc4f7f5dfd3b9d9cda7668e6c7d3bfd9a07bc7cd0b88d5a"
  arun(MyBot().run(room_id, token))
