# Discord Voice State Bot

このDiscord Botは、指定されたボイスチャンネルでのユーザーの入退室を監視し、通話の開始と終了を通知します。このプログラムは、Google Cloud Platform (GCP) の Google Compute Engine (GCE) 上で実行しています。

## 機能

- 指定したボイスチャンネルのみの入退室を監視。
- 通話開始時にはチャンネル名、始めた人、開始時間を通知。
- 通話終了時にはチャンネル名、通話時間（HH:MM:SS形式）を通知。

## 環境

このBotはGoogle Cloud PlatformのCompute Engineインスタンス上で実行されています。以下はそのセットアッププロセスです。

### GCEでの設定

1. GCPコンソールにログインします。
2. 「Compute Engine」に移動し、「VMインスタンス」をクリックして新しいインスタンスを作成します。
3. 必要な設定（リージョン、ゾーン、マシンタイプ、ブートディスクなど）を行い、インスタンスを作成します。
4. VMが起動したら、SSHを使ってインスタンスに接続します。
5. 必要なPython環境やライブラリをインストールします（`discord.py`、`pytz`など）。

### 依存関係のインストール

このプロジェクトに必要な依存関係をインストールするには、次のコマンドを実行します：

```bash
pip install discord.py pytz
```

## セットアップ

1. `YOUR_DISCORD_BOT_TOKEN` にあなたのDiscord Botのトークンを設定してください。
2. `YOUR_BOT_ROOM_ID` にメッセージを送信するチャンネルのIDを設定してください。
3. `YOUR_ANNOUNCE_CHANNEL_ID1`, `YOUR_ANNOUNCE_CHANNEL_ID2`, `YOUR_ANNOUNCE_CHANNEL_ID3` に、通話の監視を行いたいボイスチャンネルのIDを設定してください。

## 使用方法

Botを実行するには、設定したトークンとチャンネルIDをコードに適切に配置し、次のコマンドを実行します：

```bash
python palette_call_bot.py
```
