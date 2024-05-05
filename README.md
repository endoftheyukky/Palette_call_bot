### READMEファイルの更新

```markdown
# Discord Voice State Bot

このDiscord Botは、特定のボイスチャンネルでユーザーの入退室を監視し、通話の開始と終了を通知します。このプログラムはGoogle Cloud Platform (GCP) の Google Compute Engine (GCE) 上で実行されており、Google Cloud Shellを使用してすべての設定とデプロイを完結させます。

## 機能

- ボイスチャンネルの入退室を監視。
- 通話開始時にはチャンネル名、始めた人、開始時間を通知。
- 通話終了時にはチャンネル名、通話時間（HH:MM:SS形式）を通知。

## 環境設定

### GCEインスタンスの設定

1. Google Cloud Consoleにアクセスし、「Compute Engine」に移動します。
2. 「VMインスタンス」をクリックして新しいインスタンスを作成します。
3. 必要な設定（リージョン、ゾーン、マシンタイプ、ブートディスクなど）を選択し、インスタンスを作成します。
4. VMが起動したら、Google Cloud Shellを開きます。

### 必要なソフトウェアのインストール

Google Cloud Shell上で以下のコマンドを実行し、必要なPython環境とライブラリをインストールします：

```bash
sudo apt update
sudo apt install python3-pip python3-dev
pip3 install discord.py pytz
```

### Botのセットアップとデプロイ

1. Google Cloud Shell内で、Botのスクリプトを直接編集するか、GitHubからクローンします。
2. 必要な環境変数（BotトークンやチャンネルID）をコード内に設定します。
3. Botをバックグラウンドで実行するには、次のコマンドを使用します：

```bash
nohup python3 palette_call_bot.py &
```

`nohup.out` ファイルに出力が保存されますので、何か問題が発生した場合にはこのファイルを確認します。

## 使用方法

設定を完了した後、インスタンスが起動している限りBotは自動的に動作します。再起動後も自動的に起動させたい場合は、`crontab` や `systemd` などを使用して設定してください。
