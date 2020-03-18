# phamtaro
 
## 必要な設定ファイル

slackbot_settings.py  
```python
API_TOKEN = "<your-slack-api-token>"

default_reply = 'くしくし、何を言ってるかわからないのだ'

PLUGINS = [
    'plugins'
]
```

config.ini
```ini
[talk]
endpoint = https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk
token = "<your-talk-api-token>"
```