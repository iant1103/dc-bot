'''
可以複製todolist的架構, 但請記得更改class & function的名稱
這個檔案的名字也可以改
'''
import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import re
class vote(Cog_Extension):
    @commands.command()
    async def vote(self,ctx,*,cho):
        list = re.compile(r'\S+').findall(cho)
        options = ['(A)', '(B)', '(C)', '(D)']
        
        if len(list) >1:
            embed = discord.Embed(title = list[0], color=0x000982)
            list.pop(0)
            count = 0
            for ele in list:
                embed.add_field(name = f"{options[count]}{ele}", value = "\u200b",inline = False)
                count = count+1
            msg = await ctx.send(embed = embed)
            count = 0
            for ele in list:
                await msg.add_rection(options[count])
                count = count+1

        else:
            embed = discord.Embed(title = "正確答案是",color = 0xFF0000)
            embed.add_field(name = list[0], value = "\u200b", inline = False)
            msg = await ctx.send(embed = embed)
            await msg.add_reaction("👍")
            await msg.add_reaction("💯")

        await ctx.message.delete()#刪掉訊息

async def setup(bot):
    await bot.add_cog(vote(bot))
