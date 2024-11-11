import gradio as gr
from openai import OpenAI
from openai.types import Image, ImageModel, ImagesResponse
from util.apikey import OPENAI_IMAGE_KEY as iapi

client = OpenAI(
    api_key = iapi
)

def generateImage(userprompt):
    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=userprompt,
            size="512x512",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        return f"Error: {str(e)}"
    
interface = gr.Interface(
    fn=generateImage,
    inputs=gr.Textbox(label="Image Description"),
    outputs=gr.Image(label="Generated Images"),
    title="AI weather visualizer.\nWeather data provided by MET Norway.\nImage generation provided by OpenAI",
)

interface.launch(share=True)
