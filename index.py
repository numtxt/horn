import discord
import random
import pickle
import os
import time
import datetime

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("내 이름은 [호른], 너도 대장장이가 되고 싶은 거지? 망치질")
    await client.change_presence(status=discord.Status.online, activity=game)

command = """."""

# {user.id} 이걸로 유저 식별
# user = message.author
# await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임\n{user.name}{user.id}{user.display_name}")
# user.id

@client.event
async def on_message(message):
    if message.content.startswith("호른, 명령어"):
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_gold(), title="대장장이가 되고싶어?", description="우선 내 이름을 불러! [호른], 이라고 말이야!!")
        embed.set_thumbnail(url="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/84a6d18b-9a48-4189-95fa-9f3a7f50c113/free-icon-manual-book-3963789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201224T073900Z&X-Amz-Expires=86400&X-Amz-Signature=669306eb317d7d5b786a133e4b34043935b22ae1bf7b70183bd9a8b68ed87fbd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22free-icon-manual-book-3963789.png%22")
        # embed.set_image(url="")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="무기 제작 방법", value="호른, 무기제작 (무기 이름)", inline=False)
        embed.add_field(name="무기 강화 방법", value="호른, 무기강화 (무기 이름)", inline=False)
        embed.add_field(name="인벤토리 보기", value="호른, 인벤토리", inline=False)
        embed.add_field(name="누가 만든 무기가 제일 강하지?", value="호른, 무기랭킹", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("호른, 무기제작"):
        name = message.content.split(" ")[2:]
        word = ' '.join(name)
        exits = 0

        if word == "":
            exits = 1

        cos = 0
        user = message.author

        if exits == 0:
            try:
                source_file = open("/mnt/d/discord/data/horn/" + str(user.id) + " " + word + ".pickle", "rb")
            except FileNotFoundError:
                source_file = open("/mnt/d/discord/data/horn/" + str(user.id) + " " + word + ".pickle", "wb")
                inputer = str(1)
                pickle.dump(inputer, source_file)
                embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_gold(), title=word + " (이)가 만들어졌어!!", description="얼마나 강해질지 벌써부터 기대되는걸!!")
                embed.set_thumbnail(url="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/868b33b2-5b22-4680-8ec0-33c7fbaaf046/free-icon-rpg-game-2619186.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201224T075448Z&X-Amz-Expires=86400&X-Amz-Signature=7434a3091fec0b55ef658d772711fa801626c958caf8fb9e14321681378bb271&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22free-icon-rpg-game-2619186.png%22")
                # embed.set_image(url="")
                embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                cos = 1
            finally:
                source_file.close()

            if cos == 0:
                await message.channel.send(word + "(은)는 이미 존재하는 이름이야. 다른 이름으로 지어줘!")
        else:
            await message.channel.send("그 이름은 사용이 불가능한 이름이야. 다른 이름으로 지어줘!")

    if message.content.startswith("호른, 무기강화"):
        user = message.author
        cos = 0

        try:
            time_file = open("/mnt/d/discord/data/time/" + str(user.id) + ".pickle", "rb")
        except FileNotFoundError:
            time_file = open("/mnt/d/discord/data/time/" + str(user.id) + ".pickle", "wb")
            a = datetime.datetime.now()
            b = a + datetime.timedelta(seconds=10)
            pickle.dump(b, time_file)
            cos = 1
        finally:
            b = pickle.load(time_file)
            time_file.close()

        if cos == 0:
            a = datetime.datetime.now()
            if a >= b:
                cos = 1
            else:
                c = (b - a)
                c = c.seconds
                await message.channel.send(f"아직 강화 쿨타임이 돌지않았어! (강화 쿨타임 : 10초)\n남은 시간 : {c}초")

        # print(type(a), a)
        # print(type(b), b)

        if cos == 1:
            name = message.content.split(" ")[2:]
            word = ' '.join(name)
            source_file = open("/mnt/d/discord/data/horn/" + str(user.id) + " " + word + ".pickle", "rb")
            source = pickle.load(source_file)
            source_file.close()
            user_id = str(user.id)
            levels = int(source.split(" ")[0])
            win = 0

            if str(user.id) == user_id:
                if levels < 10:
                    yes = 90
                    paos = 3
                    num = random.randint(1, 100)
                    if num < 90:
                        win = 1
                if 10 <= levels < 20:
                    yes = 85
                    paos = 5
                    num = random.randint(1, 100)
                    if num < 85:
                        win = 1
                if 20 <= levels < 30:
                    yes = 80
                    paos = 8
                    num = random.randint(1, 100)
                    if num < 80:
                        win = 1
                if 30 <= levels < 40:
                    yes = 75
                    paos = 10
                    num = random.randint(1, 100)
                    if num < 75:
                        win = 1
                if 40 <= levels < 50:
                    yes = 70
                    paos = 12
                    num = random.randint(1, 100)
                    if num < 70:
                        win = 1
                if 50 <= levels < 60:
                    yes = 65
                    paos = 15
                    num = random.randint(1, 100)
                    if num < 65:
                        win = 1
                if 60 <= levels < 70:
                    yes = 60
                    paos = 17
                    num = random.randint(1, 100)
                    if num < 60:
                        win = 1
                if 70 <= levels < 80:
                    yes = 55
                    paos = 20
                    num = random.randint(1, 100)
                    if num < 55:
                        win = 1
                if 80 <= levels < 90:
                    yes = 50
                    paos = 23
                    num = random.randint(1, 100)
                    if num < 50:
                        win = 1
                if 90 <= levels < 100:
                    yes = 45
                    paos = 25
                    num = random.randint(1, 100)
                    if num < 45:
                        win = 1
                if levels == 100:
                    win = 2
    # win = 2 # 만렙

                paos = int(paos / 2)

                # 검 파괴 확률
                num = random.randint(1, 100)
                if num <= paos:
                    win = 3

                if win == 1:
                    levels += 1

                    # 레벨 : str(levels)   강화 성공 확률 : str(yes)    검 파괴 확률 : str(paos)
                    
                    embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_blue(), title=word + " (이)가 강화에 성공했어!", description="")
                    embed.set_thumbnail(url="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/af887357-fb55-4dd2-a16f-cb2227b96ac3/free-icon-anvil-3067321.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201224T102033Z&X-Amz-Expires=86400&X-Amz-Signature=68ae94e04c096e29cb8a4804afbdf6e8590e876630762690faef807201bb8193&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22free-icon-anvil-3067321.png%22")
                    # embed.set_image(url="")
                    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                    embed.add_field(name="현재 레벨", value=str(levels), inline=False)
                    embed.add_field(name="강화 성공 확률", value=str(yes) + "%", inline=False)
                    embed.add_field(name="검 파괴 확률", value=str(paos) + "%", inline=False)
                    await message.channel.send(embed=embed)

                elif win == 2:
                    embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_gold(), title=word + " (은)는 더 이상 강화가 불가능하네!", description="")
                    embed.set_thumbnail(url="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/868b33b2-5b22-4680-8ec0-33c7fbaaf046/free-icon-rpg-game-2619186.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201224T075448Z&X-Amz-Expires=86400&X-Amz-Signature=7434a3091fec0b55ef658d772711fa801626c958caf8fb9e14321681378bb271&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22free-icon-rpg-game-2619186.png%22")
                    # embed.set_image(url="")
                    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                    embed.add_field(name="현재 레벨", value=str(levels), inline=False)
                    embed.add_field(name="이 검은 말일세!", value="전설의 대장장이가 손수 만든 명검이라네!", inline=False)
                    embed.add_field(name="레벨이 한계에 달하여 더 이상 강화를 할 수 없습니다", value="", inline=False)
                    await message.channel.send(embed=embed)
                elif win == 3:
                    embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_magenta(), title="이런!! " + word + " (이)가 깨져버렸군!!", description="")
                    embed.set_thumbnail(url="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/99336ddd-ff69-4317-b14e-d7fecf6af6dc/free-icon-broken-shield-3375186.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201224T102716Z&X-Amz-Expires=86400&X-Amz-Signature=b03388d1a58056266ef82042c1c0ca28ee109e27b6fd90593ccd909cd738d040&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22free-icon-broken-shield-3375186.png%22")
                    # embed.set_image(url="")
                    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                    embed.add_field(name="레벨", value=str(levels), inline=False)
                    embed.add_field(name="검 파괴 확률", value=str(paos) + "%", inline=False)
                    embed.add_field(name="작별 인사", value="잘가... " + word, inline=False)
                    await message.channel.send(embed=embed)

                    source_file = ("/mnt/d/discord/data/horn/" + str(user.id) + " " + word + ".pickle")
                    os.remove(source_file)
                else:
                    embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_red(), title=word + " (이)가 강화에 실패했군!", description="")
                    embed.set_thumbnail(url="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/af887357-fb55-4dd2-a16f-cb2227b96ac3/free-icon-anvil-3067321.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201224T102033Z&X-Amz-Expires=86400&X-Amz-Signature=68ae94e04c096e29cb8a4804afbdf6e8590e876630762690faef807201bb8193&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22free-icon-anvil-3067321.png%22")
                    # embed.set_image(url="")
                    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                    embed.add_field(name="현재 레벨", value=str(levels), inline=False)
                    embed.add_field(name="강화 성공 확률", value=str(yes) + "%", inline=False)
                    embed.add_field(name="검 파괴 확률", value=str(paos) + "%", inline=False)
                    await message.channel.send(embed=embed)

                source_file = open("/mnt/d/discord/data/horn/" + str(user.id) + " " + word + ".pickle", "wb")
                inputer = str(levels)
                pickle.dump(inputer, source_file)
                source_file.close()

                time_file = open("/mnt/d/discord/data/time/" + str(user.id) + ".pickle", "wb")
                a = datetime.datetime.now()
                b = a + datetime.timedelta(seconds=10)
                pickle.dump(b, time_file)
                time_file.close()
            else:
                await message.channel.send(word + " 라는 무기는 너한테 없는 것 같은데?")

    if message.content == "호른, 인벤토리":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_teal(), title="여기! 니 무기들이야!", description="")
        embed.set_thumbnail(url="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/02b8d5c6-ccf2-4382-bed8-3bfc65a7d84b/free-icon-delivery-box-3134347.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201224T090232Z&X-Amz-Expires=86400&X-Amz-Signature=a56ec3c67c8c0c3191c80deec8555ba7483167147276dc1becb6c9ec145573fc&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22free-icon-delivery-box-3134347.png%22")
        # embed.set_image(url="")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        user = message.author
        file_list = os.listdir("/mnt/d/discord/data/horn/")
        for i in file_list:
            if int(i.split(" ")[0]) == user.id:
                source_file = open("/mnt/d/discord/data/horn/" + i, "rb")
                source = pickle.load(source_file)
                source_file.close()
                levels = int(source.split(' ')[0])
                nam = ' '.join(i.split(" ")[1:])
                names = nam[:-7]
                embed.add_field(name=names, value=str(levels) + "레벨", inline=True)
        await message.channel.send(embed=embed)

    if message.content == "호른, 무기랭킹":
        file_list = os.listdir("/mnt/d/discord/data/horn/")
        st1 = 0
        st2 = 0
        st3 = 0
        st2_name = ""
        st1_name = ""

        for i in file_list:
            source_file = open("/mnt/d/discord/data/horn/" + i, "rb")
            source = pickle.load(source_file)
            source_file.close()
            if st1 <= int(source):
                st3 = st2
                st3_name = st2_name

                st2 = st1
                st2_name = st1_name

                st1 = int(source)
                st1_name_to = ''.join(i.split(" ")[1])
                st1_name = st1_name_to[:-7]

        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_green(), title="여기! 무기 랭킹이라네!", description="사소한 버그가 있어서 정확하진 않아!")
        embed.set_thumbnail(url="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4faca2bf-7a6e-4183-bc71-e231acfb54a4/free-icon-medal-of-honor-3314383.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201224T101341Z&X-Amz-Expires=86400&X-Amz-Signature=ffd8a26123fdea242676e5dc12904231daa78865bc2caf0a09cc9a987660e17d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22free-icon-medal-of-honor-3314383.png%22")
        # embed.set_image(url="")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="1위 " + st1_name, value=str(st1) + "레벨", inline=False)
        embed.add_field(name="2위 " + st2_name, value=str(st2) + "레벨", inline=False)
        embed.add_field(name="3위 " + st3_name, value=str(st3) + "레벨", inline=False)
        await message.channel.send(embed=embed)

    if message.content == "developer command one":
        user = message.author
        if user.id == 790192589269106698:
            embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.dark_green(), title="공지가 있어!!", description="여긴 베타테스터들을 위한 서버라네!!")
            embed.set_thumbnail(url="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/53d9ebb8-6266-4cd5-994c-b4dcbe9c1b38/free-icon-light-bulb-3942306.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201225T052324Z&X-Amz-Expires=86400&X-Amz-Signature=b214da172c87ab57666e4b9ec1b944e1ff55827bd53e0ea3a2edac1e0a34c3d3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22free-icon-light-bulb-3942306.png%22")
            # embed.set_image(url="")
            embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            embed.add_field(name="무기 만드는 법을 모르겠다고?", value="'호른, 명령어'를 입력해서 나를 불러봐!!", inline=False)
            embed.add_field(name="만약 문제가 생기면", value="아래에 있는 녀석에게 문의를 넣어! 분명 고쳐줄꺼야!", inline=False)
            await message.channel.send(embed=embed)

account_token = os.environ('BOT_TOKEN')
client.run(account_token)
