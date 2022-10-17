import os

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines() [0]
        words = text.split()
    return words

def send_message(phoneNumber, message):
    os.system ('osascript send.scpt {} "{}"'.format(phoneNumber, message))

if __name__ == '__main__':
    words = get_words('nothere.txt') #Add the name of text file that will be sent
    number = 1234567890 #Put target number here
    for words in words:
        send_message(number, words)