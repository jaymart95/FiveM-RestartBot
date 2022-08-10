from disnake.ext.commands import Cog
import config

class Events(Cog):
    def __init__(self, bot):
        self.bot = bot


    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up('Events')
    
    @Cog.listener()
    async def on_message(self, message):
        rRole = config.ROLE_ID
        role = message.guild.get_role(rRole)
        if message.channel.id != config.CHANNEL_ID or message.author.id == config.BOT_ID:
            return
    
        channel = message.channel
        if "restarting" in message.content:
            await message.delete()
            await channel.send(f"||{role.mention}||\n🚨**SERVER IS UP!**🚨\n\n**You can join back now!!\n\nHow to Join:\n\n`1.`Open FiveM and press F8\n`2.`Type `connect {connect}`\n`3.`Press ENTER and you are done! It's as simple as that**")
            return
        await message.delete()

def setup(bot):
    bot.add_cog(Events(bot))