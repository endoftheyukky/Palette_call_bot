GitHubのリポジトリ用に、このDiscord botのREADMEファイルをMarkdown形式で作成します。以下はそのサンプルです：

```markdown
# Discord Voice State Bot

このDiscord Botは、指定されたボイスチャンネルでのユーザーの入退室を監視し、通話の開始と終了を通知します。通話が開始されると、参加したチャンネル名、通話を開始したユーザー名、開始時間を通知します。通話が終了すると、チャンネル名と通話の継続時間を通知します。

## 機能

- ボイスチャンネルの入退室を監視。
- 通話開始時にはチャンネル名、始めた人、開始時間を通知。
- 通話終了時にはチャンネル名、通話時間（HH:MM:SS形式）を通知。
- ユーザーのアバター画像を含む通知メッセージを埋め込みで表示。

## 前提条件

このBotを使用する前に、次のものが必要です：

- Python 3.8 以上
- discord.py ライブラリ
- pytz ライブラリ

## セットアップ

### 依存関係のインストール

このプロジェクトに必要な依存関係をインストールするには、次のコマンドを実行します：

```bash
pip install discord.py pytz
```

### Botの設定

1. [Discord Developer Portal](https://discord.com/developers/applications)で新しいアプリケーションを作成。
2. Botをアプリケーションに追加し、生成されたトークンをコピー。
3. `palette_call_bot.py` ファイルにトークンを貼り付けます：

```python
client.run("YOUR_BOT_TOKEN_HERE")
```

### Botをサーバーに招待

Botをサーバーに招待するには、アプリケーションページでOAuth2 URLジェネレータを使用し、適切な権限を選択してリンクを生成し、サーバーにアクセスします。

## 使用方法

Botを実行するには、以下のコマンドを使用します：

```bash
python palette_call_bot.py
```
