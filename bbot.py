import discord
import asyncio
from captcha.image import ImageCaptcha
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["문의는 ∑」🔥  💎  바나나 💎 🔥#0001 에게 부탁드립니다.!", "BBOT봇은 Team MB에서 만들어졌어요!" , "제 접두사는 [ * ] 이에요!"]
        for (m) in range(2):
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(5)

@client.event
async def on_message(message):
    if message.content.startswith("*안녕"):
        await message.channel.send("안녕하세요!")
    
    if message.content.startswith("*꺼져"):
        await message.channel.send("님도 꺼져주실레요?")

    if message.content.startswith("*소개"):
        await message.channel.send("안녕하세요 저는 TEAM MB에서 만들어진 BBOT예요!")

    if message.content.startswith("*잘가"):
        await message.channel.send("당신도 잘 가요!!")

    if message.content.startswith("*누구야?"):
        await message.channel.send("BBOT이지!")

    if message.content.startswith("*죽어"):
        await message.channel.send("깨꼬닥")

    if message.content.startswith("*기절해"):
        await message.channel.send("50/100 죽음😵")

    if message.content.startswith("*기절해"):
        await message.channel.send("50/100 죽음😵")

    if message.content.startswith("*몇 살이야?"):
        await message.channel.send("음... 1살이네요!😂")
    
    if message.content.startswith("*초대"):
        embed = discord.Embed(title="BBOT 초대하기", description="[초대하기](https://discord.com/api/oauth2/authorize?client_id=734983344743252070&permissions=8&scope=bot) \n \n [서포트 서버 링크](https://discord.gg/uSjUzRb)", color=0x00ff00)
        embed.set_footer(text="봇 초대는 본인이 관리자인 서버에 한해서 봇을 초대할 수 있습니다.")
        await message.channel.send(embed=embed)

    if message.content.startswith("*킥"):
        if message.author.guild_permissions.administrator:
            kickusermention = message.content[4:]
            kickuserid = kickusermention[2:20]
            kickuser = message.guild.get_member(int(kickuserid))
            await message.guild.kick(kickuser)
            await message.channel.send( str(kickuser) + "님이 관리자에 인하여 킥 되었어요!")
        else:
            await message.channel.send("관리자 권한이 있으신가요? 다시 한번 확인해봐요!")

    if message.content.startswith("*언뮤트"):
        if message.author.guild_permissions.administrator:
            firstid = message.content[5:]
            author = message.guild.get_member(int(firstid[2:20]))
            role = discord.utils.get(message.guild.roles, name="뮤트")
            await author.remove_roles(role)
            await message.channel.send("**뮤트를 풀었어요!**")
        else:
            await message.channel.send("**관리자 권한 거부**")
            
    if message.content.startswith("*캡챠") or message.content.startswith("<캡차"):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = "Captcha.png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("**__Captcha__ 인증 시간이 끝났어요**")
            return

        if msg.content == a:
            await message.channel.send("**__Captcha__ 인증에 성공 했어요 M BOT 캡챠도 이용해주세요!**")
        else:
            await message.channel.send("**__Captcha__ 인증에 실패했어요 다시 한번 해보세요!**") 

                        
client.run('Token')
