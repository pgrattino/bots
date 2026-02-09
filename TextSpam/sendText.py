import os
import sys

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines() [0]
        words = text.split()
    return words

def send_message(phoneNumber, message, service_type):
    os.system ('osascript send.scpt {} "{}" {}'.format(phoneNumber, message, service_type))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit("Usage: python sendText.py [phonenumber] [service] [textfile]")
    words = get_words(sys.argv[3])
    number = sys.argv[1]
    service_type = sys.argv[2]
    for words in words:
        send_message(number, words, service_type)
