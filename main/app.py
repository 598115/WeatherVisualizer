import gradio as gr
from appfunction import appfunction


mytheme = gr.themes.Base(
    primary_hue="indigo",
    secondary_hue="indigo",
    neutral_hue='blue',
    text_size=gr.themes.Size(lg="50px", md="30px", sm="25px", xl="60px", xs="20px", xxl="70px", xxs="15px"),
    spacing_size="lg",
    radius_size=gr.themes.Size(lg="50px", md="40px", sm="30px", xl="60px", xs="20px", xxl="70px", xxs="12px"),
).set(
    body_text_color_dark='*neutral_900',
    body_text_color_subdued='*color_accent',
    body_text_weight='600',
    embed_radius='*radius_xxl',
    background_fill_primary='*secondary_50',
    background_fill_primary_dark='#91BAD6'
)

    
with gr.Blocks(theme=mytheme, css="""
    .custom-textbox {
        background-color: #1d3bd1;
        border: 10px solid #cccccc;
        padding: 10px;
        border-radius: 8px; 
    }
    .custom-textbox textarea {
        background-color: #91BAD6 !important;
        color: #0000FF; 
    }
""") as interface:
    gr.Markdown("## AI Weather Visualizer\nWeather data provided by MET Norway.\nImage generation provided by OpenAI")

    # Button to trigger image generation
    generate_button = gr.Button("Generate Weather Image")

    # Output for the generated image
    image_output = gr.Image(label="Generated Image", width=512, height=512, container=True)

    # Textbox for generated text
    text_output = gr.Textbox(label="Recommendations for the weather", placeholder="Text generates here...", lines=5, elem_classes="custom-textbox")

    # Set up the button 
    generate_button.click(appfunction, inputs=None, outputs=[image_output, text_output])

# Launch the Gradio app
interface.launch()
