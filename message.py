from twilio.rest import Client

account_sid = 'AC8aade6112a16d7da59e6de736277a904'

auth_token = '210411cefe0a53233886a395c3b9c4b1'

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886 982 722 942",
    from_="+13522928947",
    body="嗨")

print(message.sid)
