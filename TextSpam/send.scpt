on run {targetPhoneNumber, targetMessageToSend}
	tell application "Messages"
		set targetService to 1st service whose service type = iMessage
		set targetBuddy to buddy targetPhonenumber of targetService
		set targetMessage to targetMessageToSend
		send targetMessage to targetBuddy
	end tell
end run