# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACed732a3c49700934481addd5ce1659f0"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

trigger = client.usage.triggers.get("UT33c6aeeba34e48f38d6899ea5b765ad4")
print trigger.current_value