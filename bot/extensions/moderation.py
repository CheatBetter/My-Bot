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
import asyncio
from discord.ext import commands
from discord import app_commands
from bot.bot import DiscordBot
from datetime import datetime


class Moderation(commands.Cog):
    def __init__(self, bot: DiscordBot):
        self.bot = bot

    @commands.Cog.listener("on_member_join")
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_guild(1150551992272420999).get_channel(1151277211408670790)
        verify = self.bot.get_guild(1150551992272420999).get_channel(1150554488638287922)
        chat = self.bot.get_guild(1150551992272420999).get_channel(1150555827351072768)
        buy = self.bot.get_guild(1150551992272420999).get_channel(1150555676469366824)

        embed = discord.Embed(title="Welcome!",
                      description=f"Welcome to our new member, {member.mention}. Go verify at {verify.mention} and then you can start chatting at {chat.mention} or buy a service at {buy.mention}.\n\n-----------------------------------\n\nMember Count: {self.bot.get_guild(1150551992272420999).member_count}",
                      colour=0x00b0f4,
                      timestamp=datetime.now())

        embed.set_author(name="Cheatbetters Clone")

        embed.set_footer(text="Written by .cheatbetter",
                        icon_url="https://slate.dan.onl/slate.png")

        await channel.send(embed=embed)
    
    #@app_commands.command(name="ban")
    async def ban(self, ctx: discord.Interaction, member: discord.Member, time: int, d: str, *, reason: str="No Reason"):
        if member == None:
            embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
            await ctx.response.send_message(embed=embed)
			

        else:

            embed = discord.Embed(title="Banned!", description=f"{member.mention} has been banned!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Reason: ", value=reason, inline=False)
            embed.add_field(name="Time left for the ban:", value=f"{time}{d}", inline=False)
            await ctx.response.send_message(embed=embed)
            await ctx.guild.ban(user=member)

            if d == "s":
                await asyncio.sleep(int(time))
                await ctx.guild.unban(user=member)
            if d == "m":
                await asyncio.sleep(int(time*60))
                await ctx.guild.unban(user=member)
            if d == "h":
                await asyncio.sleep(int(time*60*60))
                await ctx.guild.unban(user=member)
            if d == "d":
                await asyncio.sleep(int(time*60*60*24))
                await ctx.guild.unban(user=member)		
        


async def setup(bot):
    await bot.add_cog(Moderation(bot), guilds=[discord.Object(id=1150551992272420999)])
