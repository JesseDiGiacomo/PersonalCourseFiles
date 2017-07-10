from twilio.rest import TwilioRestClient #chamada anterior pois a atual nao funcionou

#from twilio.rest import Client
#a linha a cima eh a forma indicada pelo site, porem da problema no import Client
#Ao utilizar o import TwilioRestClient, precisei mudar o codigo original de Client para TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = TwilioRestClient(account_sid, auth_token) #nesta linha precisou mudar de Client para TwilioRestClient

message = client.messages.create(
    to="+5521984484791",
    from_="+13479831515",
    body="Hello from Python! Teste do programa do Jesse. =) ")

print(message.sid)

#codigo funcionando perfeitamente desta forma.
