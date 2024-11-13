from openai import OpenAI
from openai.types import Image, ImageModel, ImagesResponse
from util.apikey import OPENAI_IMAGE_KEY as iapi

client = OpenAI(
    api_key = iapi
)

def generateImage(userprompt):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=userprompt,
            size="1792x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        return f"Error: {str(e)}"
    
def generateText(userprompt):
    # Create a chat completion using GPT-4
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
          {
             "role": "user",
              "content": userprompt,
         }
        ],
    )
    # Extract
    return chat_completion.choices[0].message.content
