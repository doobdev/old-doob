import discord
from discord.ext import commands
doob_logo = "https://cdn.discordapp.com/avatars/680606346952966177/ada47c5940b5cf8f7e12f61eefecc610.webp?size=1024"

class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Gives user some info about Doob
    @commands.command(aliases=['botinfo'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def info(self, ctx):
        embed = discord.Embed(title="Doob's Info", description="Some of Doob's info that might be useful for you to know!", colour=discord.Color.blue())

        embed.add_field(name="Name", value="Doob", inline=False)
        embed.add_field(name="Description", value="A Discord bot made by mmatt using discord.py, he felt like making it so he did B)", inline=False)
        embed.add_field(name="Developer", value="The creator of Doob is <@308000668181069824>", inline=False)
        embed.add_field(name="Bot's Server Count", value=f"{str(len(self.client.guilds))}", inline=False)
        embed.add_field(name="Bot's Member Count", value=f"{str(len(self.client.users))}", inline=False)
        embed.add_field(name="The ping for Doob is...", value=f" :ping_pong: {round(self.client.latency * 1000)} ms", inline=False)
        embed.add_field(name="Library", value="discord.py", inline=False)
        embed.add_field(name="Top.gg Link", value="https://top.gg/bot/680606346952966177", inline=False)
        embed.add_field(name="Invite Link", value="https://discordapp.com/oauth2/authorize?client_id=680606346952966177&scope=bot&permissions=271674430", inline=False)
        embed.add_field(name="GitHub Repository", value="https://github.com/doobdev/doob", inline=False)
        embed.add_field(name="Docs", value="http://docs.doobbot.com/", inline=False)
        embed.set_thumbnail(url=doob_logo)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(info(client))
