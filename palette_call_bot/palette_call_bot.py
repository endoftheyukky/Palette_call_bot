import discord
from datetime import datetime, timedelta
import pytz

intents = discord.Intents.default()
intents.messages = True
intents.voice_states = True
client = discord.Client(intents=intents)

# チャンネルごとの通話開始時間を追跡するための辞書
call_start_times = {}

@client.event
async def on_voice_state_update(member, before, after):
    # 通話開始・終了の通知を送信するチャンネルのID
    botRoom = client.get_channel('YOUR_BOT_ROOM_ID')
    # 通話開始・終了を監視するチャンネルのID
    announceChannelIds = ['YOUR_ANNOUNCE_CHANNEL_ID1', 'YOUR_ANNOUNCE_CHANNEL_ID2', 'YOUR_ANNOUNCE_CHANNEL_ID3']

    # タイムゾーン設定
    jst = pytz.timezone('Asia/Tokyo')

    # 通話開始の検出
    if after.channel is not None and after.channel.id in announceChannelIds:
        if len(after.channel.members) == 1:  # このメンバーが最初に入ったとき
            start_time = datetime.now().astimezone(jst)
            call_start_times[after.channel.id] = start_time
            embed = discord.Embed(title="通話開始", color=0x3498db)
            embed.add_field(name="チャンネル", value=after.channel.name, inline=True)
            embed.add_field(name="始めた人", value=member.name, inline=True)
            embed.add_field(name="開始時間", value=start_time.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
            if member.avatar:
                embed.set_thumbnail(url=member.avatar.url)  # ユーザーのアイコン画像を設定
            await botRoom.send(embed=embed)

    # 通話終了の検出
    if before.channel is not None and before.channel.id in announceChannelIds:
        if len(before.channel.members) == 0:  # 最後の一人がチャンネルを抜けたとき
            end_time = datetime.now().astimezone(jst)
            start_time = call_start_times.pop(before.channel.id, end_time)
            call_duration = end_time - start_time
            call_duration_formatted = str(timedelta(seconds=int(call_duration.total_seconds())))
            embed = discord.Embed(title="通話終了", color=0xe74c3c)
            embed.add_field(name="チャンネル", value=before.channel.name, inline=True)
            embed.add_field(name="通話時間", value=call_duration_formatted, inline=True)
            await botRoom.send(embed=embed)

# Botのトークンを指定
client.run("YOUR_DISCORD_BOT_TOKEN")
