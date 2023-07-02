///ToDo list

    async def AddTodoList(self, ctx, item):
        self.todo.append(item) 
        size = str(len(self.todo))
        await ctx.send("目前有 " + size + " 項代辦事項")
#把輸入的東西存在self.todo裏，之後使用 str() 函式將這個長度轉換為字串，可以將其儲存在變數

    async def RemoveTodoList(self, ctx, item):
        if item in self.todo:
            self.todo.remove(item)
            await ctx.send("已移除 " + item + " 代辦事項")
        else:
            await ctx.send("此代辦事項不存在")
#用if else判斷item是否在self.todo裡面，有就移除並print"已移除 " + item + " 代辦事項"否則"此代辦事項不存在"

    async def SortTodoList(self, ctx):
        self.todo.sort()
        size = len(self.todo)
        if size > 0:
            for item in self.todo:
                await ctx.send(item)
        else:
             await ctx.send("沒有任何代辦事項")
#使用 self.todo.sort() 對 self.todo 清單進行排序，再判斷size是否為0，如果是就print"沒有任何代辦事項"否則把事項按照字母順序列印。

    # Clear todolist
    @commands.command()
    async def ClearTodoList(self, ctx):
        self.todo.clear()
＃使用.clear()清除所有再self.todo裡面的東西
    
    # Show todolist
    @commands.command()
    async def ShowTodoList(self, ctx):
        for item in self.todo:
            await ctx.send(item)
＃使用ctx.send把self.todo裡面的東西(item印出來)

/// (vote bot)投票機器人

import re
class vote(Cog_Extension):
    @commands.command()
    async def vote(self,ctx,*,cho):
        list = re.compile(r'\S+').findall(cho)
        options = ['(A)','(B)','(C)','(D)']
#使用了 re.compile(r'\S+').findall(cho) 的正則表達式操作，目的是將 cho 字串中的非空白字符分割成一個列表。也就是將 cho 字串中的單詞提取出來。這個列表存儲在 list 變數中。
接著創建 options 的列表，其中包含了四個選項 '(A)'、'(B)'、'(C)'、'(D)'。用於投票選擇的標記或標籤。
並將結果存儲在名為 list 的變數中。

        if len(list) >1:
            embed = discord.Embed(title= list[0],color=0x000982)
            list.pop(0)
            count = 0
            for ele in list:
                embed.add_field(name = f"{options[count]}{ele}",value = "\u200b",inline = False)
                count = count+1
            msg = await ctx.send(embed = embed)
            count = 0
            for ele in list:
                await msg.add_rection(options[count])
                count = count+1
＃如果 list 列表的長度大於1：
創建一個名為 embed 的 Discord 嵌入物件（Embed）也就是對話框，設置標題為 list[0]第一個輸入的東西為題目，顏色為 0x000982（十六進制表示）藍色。
之後從 list 中移除第一個元素（已經變題目了），即 list.pop(0)。
對於 list 中的每個元素 ele：
使用 embed.add_field() 將投票選項和相應的 ele 添加為一個嵌入物件的字段（field）也就是投票選項使用 options 列表中對應的標籤，例如 (A)。
value = "\u200b" 添加空格，確保字段的對齊。
inline = False 表示字段不需要內嵌顯示。

        else:
            embed = discord.Embed(title = "正確答案是",color = 0xFF0000)
            embed.add_field(name = list[0],value = "\u200b",inline = False)
            msg = await ctx.send(embed = embed)
            await msg.add_reaction("👍")
            await msg.add_reaction("💯")
        await ctx.message.delete()#刪掉訊息
＃如果 list 列表的長度為1：
創建一個名為 embed 的 Discord 嵌入物件（Embed）也就是對話框，設置標題為 "正確答案是"，顏色為 0xFF0000（紅色）。
使用 embed.add_field() 將 list[0]也就是正確答案 添加為一個嵌入物件的字段（field）。
使用 ctx.send(embed=embed) 發送帶有嵌入物件的訊息，並將返回的訊息 msg 存儲起來。
之後機器人傳送 "👍" 和 "💯" 這兩個反應來表示贊同和喜愛（讓你覺得有人回應你？其實沒有哈哈～。
最後把你在dc裡輸入正確答案的指令刪除，這樣才不會和問題的程式碼搞混，版面也較為精簡！！

///wordle

def __init__(self, bot):
        link = requests.get('https://gist.githubusercontent.com/cfreshman/d97dbe7004522f7bc52ed2a6e22e2c04/raw/633058e11743065ad2822e1d2e6505682a01a9e6/wordle-nyt-words-14855.txt')
        self.responselist = link.text.split('\n')
        
        self.ans = None
        self.count = 0
#從單字庫取得單字並以空白間分隔成清單，將答案和記數初始化

async def Play(self, ctx):
        n = random.randint(0, len(self.responselist))
        self.ans = self.responselist[n]
#隨機從清單選一個單字當作答案

async def Ask(self, ctx, ans):
        response = []
        c = 0
        self.count += 1
        for i in range(len(self.responselist)):
            if ans == self.responselist[i]:
                c = 1
        if self.ans == None:
            self.count -= 1
            await ctx.send('請先輸入 Play 指令')

        elif self.count == 7:
            await ctx.send(f'太嫩了, 答案是{self.ans}') 

        elif len(ans) != 5:
            self.count -= 1
            await ctx.send('請輸入5個字母的單字')

        elif c == 0:
            self.count -= 1
            await ctx.send('這好像不是個單字')

        elif ans == self.ans:
            await ctx.send('恭喜答對!!!') 
            
        else:
            for i in range(len(self.ans)):
                if ans[i] == self.ans[i]:
                    response.append(str(ans[i]).upper())
                elif ans[i] == self.ans[0] or ans[i] == self.ans[1] or ans[i] == self.ans[2] or ans[i] == self.ans[3] or ans[i] == self.ans[4]:
                    response.append(str(ans[i]).lower())
                else:
                    response.append("#")
            await ctx.send(response[0]+response[1]+response[2]+response[3]+response[4])
#如果答案還是初始狀態，回傳'請先輸入 Play 指令'
#如果輸入超過6次，回傳答案是什麼
#如果輸入的單字長度不是5，回傳'請輸入5個字母的單字'
#如果拿單字跟單字list裡一個個跑都沒有一樣的，回傳'這好像不是個單字'
#如果輸入答案和預設答案一樣，回傳'恭喜答對!!!'

///GuessGame

async def guess(self, ctx):
        # print(number)  
        await ctx.send('1-100，任意選一個數字')
        count = 0
        lowernumber = 1
        highernumber = 100
        number = random.randint(lowernumber, highernumber)
#將記數初始化，設定lowernumber = 1，highernumber = 100，答案為這區間的隨機整數

for i in range(0, 7):
            response = await self.bot.wait_for('message')
            if count == 7:
              await ctx.send("遊戲結束")

            try : 
                guess = int(response.content) 
            
            except:
                await ctx.send("請輸入數字，從新輸入$guess")
                break
                
            if guess == number : 
                await ctx.send("猜對了")
                break
                
            if guess > 100 :
                await ctx.send("超過100，格式錯誤")
                count -= 1
                break
                
            if guess < number:
                lowernumber = guess
                await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")
                
            if guess > number :
                highernumber = guess
                await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")
            count += 1
#將玩家答案存在response後如果他是數字就存在guess裡，否則回傳"請輸入數字，從新輸入$guess"
#如果超過7次，遊戲結束
#如果玩家猜對，回傳"猜對了"
#如果猜的數>100，回傳"超過100，格式錯誤
#否則回傳新的區間

