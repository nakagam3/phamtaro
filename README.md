# phamtaro
 
## 必要な設定ファイル

slackbot_settings.py  
```python
API_TOKEN = '<your-slack-api-token>'

default_reply = 'くしくし、何を言ってるかわからないのだ'

PLUGINS = [
    'plugins'
]
```

config.ini
```ini
[talk]
endpoint = https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk
token = '<your-talk-api-token>'
```

## venvを有効にする
```bash
python3 -m venv 環境の名前
source 環境の名前/bin/activate
```

### いちいちvenvのアクティベートをしたくない。。。
.vscode/settings.json
```
{
    "python.pythonPath": "プロジェクトのパス/venv/bin/python3"
}
```
↑ vscodeで開くと自動でアクティベートされる