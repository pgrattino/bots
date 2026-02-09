# Spam Texter

Spam Texter is a fun project I made after watching someone explain how to use Apple Automator.

Given a text file, this script uses Automator and the Messages app on macOS to send text messages using a messaging protocol of your choice.

The fun part of this project is that it doesn’t just send the file, it sends every word as an individual text message.

**⚠️ PLEASE USE WITH CAUTION ⚠️**

I am not responsible for how this code is used. By pulling or running this code, you agree that I have no control over what you do with it.

## Requirements

* macOS
* Python 3
* Apple Automator
* Messages app (iMessage or SMS configured)

## Usage
Once you pull the code, run the following command in your CLI:
``python3 sendText.py [targetPhoneNumber] [messageProtocol] [path/to/text/file]``

### Example

``python3 sendText.py 7205551234 iMessage test.txt``

## Notes
Each word in the provided text file will be sent as a separate message.

This can easily overwhelm or annoy the recipient. **Use responsibly**.

## Disclaimer
This project is for educational and experimental purposes only.

Do not use this to harass, spam, or violate any messaging policies or laws.