"""

MIT License

Copyright (c) 2023 CheatBetter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import discord
from discord.ext import commands
from discord import app_commands
from bot.bot import DiscordBot
from discord.utils import get
from datetime import datetime

"""
def random_string(letter_count, digit_count):  
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) # it converts the string to list.  
    random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
    final_string = ''.join(sam_list)  
    return final_string  
"""



class Shop(commands.Cog):
    def __init__(self, bot: DiscordBot):
        self.bot = bot

    
    @app_commands.command(name="buy")
    @app_commands.describe(request="Request(Website, Discord Bot, Minecraft)")
    async def buy(self, ctx: discord.Interaction, request: str):
        # If it is not sent in the buy channel, it just stops working
        if ctx.channel.id != 1150555676469366824:
            await ctx.response.send_message(f"Please do these requests in the {ctx.guild.get_channel(1150555676469366824).mention} channel")
            await ctx.response.defer()
        requestl = ["Discord Bot", "Website", "Minecraft"]
        if request not in requestl:
            await ctx.response.send_message("Please provide a correct option (Website, Discord Bot, Minecraft)")
            await ctx.response.defer()
        embed = discord.Embed(title="Buy Order",
                        colour=0x00b0f4,
                        timestamp=datetime.now())

        embed.set_author(name="CheatBetters Clone", url="https://github.com/CheatBetter/My-Bot")

        embed.add_field(name="Author",
                value=f"{ctx.user.mention}",
                inline=True)
        embed.add_field(name="Request",
                value=f"{request}",
                inline=True)

        embed.set_footer(text="Written by .cheatbetter",
                icon_url="https://slate.dan.onl/slate.png")
        channel_name = "order-" + ctx.user.display_name
        channel = await ctx.guild.create_text_channel(name=channel_name, category=get(ctx.guild.categories, id=1150587203722952746))
        await ctx.response.send_message(f"Go check out your ticket in {channel.mention}", ephemeral=True)
        await channel.set_permissions(ctx.user, send_messages=True, read_messages=True, add_reactions=False, #Set the Permissions for the User
                                                        embed_links=True, attach_files=True, read_message_history=True,
                                                        external_emojis=True)
        await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=1150553026789130241), send_messages=False, read_messages=False, view_channel=False)
        await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=1150552432456257566), send_messages=False, read_messages=False, view_channel=False)
        await channel.set_permissions(discord.utils.get(ctx.guild.roles, id=1150552694008852521), send_messages=False, read_messages=False, view_channel=False)
        if self.bot.get_channel(channel.id) in self.bot.get_all_channels():
            role = discord.utils.get(ctx.guild.roles, id=1150552354966491146)
            await channel.send("\n", embed=embed)
            await channel.send(f"{role.mention}")
            await ctx.response.defer()
            

async def setup(bot):
    await bot.add_cog(Shop(bot), guilds=[discord.Object(id=1150551992272420999)])
