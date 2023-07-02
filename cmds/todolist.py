import discord
from discord.ext import commands
import json 
from core import Cog_Extension

class TodoList(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        self.todo = []

        '''
        todo 是一個 list 變數
        你可以在各個function中對self.todo做操作
        來當作模擬todolist

        你可能需要用到的function 
        list : append, remove, sort
        ctx.send(str)

        '''
        
    # Add todolist 
    # item 是要增加的待辨事項
    @commands.command()
    async def AddTodoList(self, ctx, item):
        self.todo.append(item) 
        size = str(len(self.todo))
        await ctx.send("目前有 " + size + " 項代辦事項")

    # Remove todolist
    # item 是要移除的待辨事項
    @commands.command()
    async def RemoveTodoList(self, ctx, item):
        if item in self.todo:
            self.todo.remove(item)
            await ctx.send("已移除 " + item + " 代辦事項")
        else:
            await ctx.send("此代辦事項不存在")

    # Sort todolist
    @commands.command()
    async def SortTodoList(self, ctx):
        self.todo.sort()
        size = len(self.todo)
        if size > 0:
            for item in self.todo:
                await ctx.send(item)
        else:
             await ctx.send("沒有任何代辦事項")

    # Clear todolist
    @commands.command()
    async def ClearTodoList(self, ctx):
        self.todo.clear()
    
    # Show todolist
    @commands.command()
    async def ShowTodoList(self, ctx):
        for item in self.todo:
            await ctx.send(item)

async def setup(bot):
    await bot.add_cog(TodoList(bot))