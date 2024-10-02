![ClashAI Wide-Banner](https://i.ibb.co/5czjY5n/Clash-AI-Wide-Banner-No-Background.png)
# 🚀 | ClashAI Python Package
**ClashAI Python Package for easy API integration!**

## Installation
```python
pip install clashai
```

## 💭 | Chat Completions
```python
import clashai

client = clashai.Client(api_key="[YOUR API KEY]")
completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Hello, World!",
        }
    ]
)

print(completion['choices'][0]['message']['content'])
```

## 📷 | Image Recognition
```py
import clashai
client = clashai.Client(api_key="[YOUR API KEY]")

response = client.chat.completions.create(
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ]
)

print(response['choices'][0]['message']['content'])
```