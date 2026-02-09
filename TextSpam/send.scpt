on run {targetPhoneNumber, targetMessageToSend, serviceType}
	tell application "Messages"
		if serviceType is "iMessage" then
			set targetService to 1st service whose service type = iMessage
		else if serviceType is "SMS" then
			set targetService to 1st service whose service type = SMS
		else if serviceType is "RCS" then
			set targetService to 1st service whose service type = RCS
		else
			error "Invalid service type. Use 'iMessage' or 'SMS'"
		end if
		set targetBuddy to buddy targetPhonenumber of targetService
		set targetMessage to targetMessageToSend
		send targetMessage to targetBuddy
	end tell
end run