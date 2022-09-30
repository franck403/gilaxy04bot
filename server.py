# import flask and discord
from flask import Flask, request
from discord_webhook import DiscordWebhook
# definit the app
app = Flask(__name__)

# api adress
@app.route('/')
def spawn():
    return '''<h1>webhook api</h1>'''

@app.route('/error/')
def error():
    return '''<h1>the program have a error please retry</h1>'''

@app.route('/message/')
def message():
    return '''<h1>webhook api</h1>'''
@app.route('/message/push')
def push():
    print(request.args)
    mes = request.args.get('message', '')
    url = request.args.get('url', '')
    print(url)
    print(mes)
    message = str(mes)
    webhook = DiscordWebhook(url=url, content=message)
    webhook.execute()
    return "message push"

if __name__ == "__main__":
    app.run()
