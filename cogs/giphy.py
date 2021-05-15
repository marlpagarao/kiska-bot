import discord
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import random


class giphy(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command(name="giphy", help="Search a gif")
    async def giphy(self,ctx,*,q="Smile"):

        api_key = 'rADqWsxAnjWXRrIk9WlNAtiYH2W1MZUV'
        api_instance = giphy_client.DefaultApi()

        try:

            api_responce = api_instance.gifs_search_get(api_key, q, limit=5, rating ='r')
            lst = list(api_responce.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=q)
            emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=emb)
    


            
        except  ApiException as e:
            print("Exception when calling Api")    

def setup(client):
    client.add_cog(giphy(client))