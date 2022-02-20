from twilio.rest import Client
from access import account_sid, auth_token, from_number

client = Client(account_sid, auth_token)

def send(midia, numero):
    numero = '+'+numero.strip()
    
    try:
        message = client.messages.create(
            media_url= midia,
            # body = midia,
            from_= from_number,
            to='whatsapp:' + str(numero)
        )

        print(message.sid)
        return True
    except:
        return False

# print(send('https://images.unsplash.com/photo-1645192598815-df5a445ba803?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60', '258846461323'))