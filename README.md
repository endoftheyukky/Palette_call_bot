# Discord Voice State Bot

このDiscord Botは、特定のボイスチャンネルでユーザーの入退室を監視し、通話の開始と終了を通知します。このプログラムはGoogle Cloud Platform (GCP) の Google Compute Engine (GCE) 上で実行されています。

## 主な機能

- ボイスチャンネルの入退室を監視します。
- 通話開始時にはチャンネル名、始めた人、開始時間を通知します。
- 通話終了時にはチャンネル名と通話時間（HH:MM:SS形式）を通知します。

## システム要件

- Google Cloud Platform アカウント
- Google Compute Engine インスタンス
- Python 3.8 以上
- 必要な Python パッケージ: discord.py, pytz

## セットアップ手順

### 1. GCEインスタンスの設定

1. Google Cloud Consoleにアクセスし、Compute Engineのセクションに移動します。
2. 新しいインスタンスを作成し、適切なマシンタイプとOSイメージを選択します。
3. ネットワーク設定が完了したら、インスタンスにSSHで接続します。

### 2. 必要なソフトウェアのインストール

```bash
sudo apt update
sudo apt install python3-pip python3-dev
pip3 install discord.py pytz
```

### 3. Botスクリプトの準備

- スクリプトを直接エディタで作成するか、既存のファイルを転送します。
- スクリプトには、適切なトークンとチャンネルIDが含まれていることを確認してください。

### 4. プロセスの持続性の確保

ターミナルを閉じてもプロセスが継続するように、以下のコマンドを実行します。

```bash
echo 'shopt -u huponexit' >> ~/.bashrc
source ~/.bashrc
```

### 5. Botの実行

プロセスをバックグラウンドで持続的に実行するには、`nohup` コマンドを使用します。

```bash
nohup python3 palette_call_bot.py &
```

このコマンドはプロセスをバックグラウンドで実行し、出力を `nohup.out` ファイルに保存します。

## 使用方法

Botが正常に設定され、実行されると、指定したDiscordチャンネルでユーザーの入退室を監視し、通話の開始と終了情報を自動的に通知します。
