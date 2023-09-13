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

class VerificationButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label="Verify",custom_id = "Verify",style = discord.ButtonStyle.success)
    async def verify(self, ctx: discord.Interaction, button):
        role = 1150553026789130241
        user = ctx.user
        if role not in [y.id for y in user.roles]:
            await user.add_roles(user.guild.get_role(role))
            await user.send("You have been verified!")
            await ctx.response.defer()
        else:
            await user.send("You have already been verified!")
            await ctx.response.defer()

class Verification(commands.Cog):
    def __init__(self, bot: DiscordBot):
        self.bot = bot

    @app_commands.command(name="verify", description="Verifies you")
    async def verify(self, ctx: discord.Interaction):
        embed = discord.Embed(title = "Verification", description = "Click below to verify.")
        await ctx.response.send_message(embed = embed, view = VerificationButton())
        await ctx.response.defer()

    

    

async def setup(bot):
    await bot.add_cog(Verification(bot), guilds=[discord.Object(id=1150551992272420999)])
