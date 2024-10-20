import clashai
client = clashai.Client(api_key="sk-r0A00DzpxGRLddtomPauVYs3RCOjzvk86nuDY4jgIpnuK1uX")
response = client.chat.completions.create(messages=[{"role": "user", "content": "Hallo du bist cool"}], model="gpt-4-turbo")
print(response)
