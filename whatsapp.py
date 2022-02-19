from twilio.rest import Client
from access import account_sid, auth_token

client = Client(account_sid, auth_token)

def send(midia, numero):
    numero = '+'+numero.strip()
    
    try:
        message = client.messages.create(
            media_url= midia,
            # body = midia,
            from_='whatsapp:+14155238886',
            to='whatsapp:' + str(numero)
        )

        print(message.sid)
        return True
    except:
        return False

# print(send('https://www.google.com', '258846461323'))