class require():
    def install(time="10"):
        import subprocess
        print("installing flask. max time = 1 minute in a not good wifi")
        subprocess.run("pip install flask", shell=True)
        print("installing webhook api. max time = 1 minute in a not good wifi")
        subprocess.run("pip install discord_webhook", shell=True)
        print("install finish")
    def server(time="10"):
        import requests
        URL = "https://raw.githubusercontent.com/franck403/gilaxy04bot/main/server.py"
        file = requests.get(URL, stream=True)
        with open("server.py", "wb") as files:
            for chunk in file.iter_content(chunk_size=1024):

                if chunk:
                    files.write(chunk)
class message():
    def webhook(message="nothing", url="localhost"):
        import requests
        link = 'http://127.0.0.1:5000/message/push?message=' + message + "&url=" + url
        r = requests.get(link)
        r.status_code
        print("message is push")


if __name__ == "__main__":
    print("for prevent so the program verfiy if the require import and libray are install")
    question2 = input("do you have install the serve flask on you're local computer (you can only acces to the server with you're localhost). Yes or No")
    if question2 != "no":
        pass
    else:
        require.server()
        print("the server file is in the directory of the program you need to start its because if you don't start it the program will don't work so please start its.")
    require.install()
    question = input("please verfiy if the flask are open. yes if its not start or all thing for no")
    if question != "yes":
        message.webhook(message = input("type the message here : "), url = input("type the url of the webhook : "))
    else:
        print("the server is not open. \n please start it")
