import gradio as gr
from appfunction import appfunction
from urllib.parse import urlparse, parse_qs

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
    .textbox-custom input, .textbox-custom textarea {
    color: white !important;  /* Sets text color to white */
}
""") as interface:
    gr.Markdown("## AI Weather Visualizer\nWeather data provided by MET Norway.\nImage generation provided by OpenAI")
    gr.Markdown(""" This service gives you current weather information on a 
                given location. AI is used to generate a picture of how you can expect the weather to look like at the location. 
                AI is also used to give you advice like what to wear according to the weather.
                To start, input the coordinates of your desired location. 
                You can use the interactive map to find the coordinates. Then click the get weather data button.
                The coordinates must be formatted as a decimal number with two decimal places or else the default location of Bergen is used""")

    map_component = gr.HTML(f"""
        <iframe src="https://598115.github.io/interactive-map/map.html" width="100%" height="500px"></iframe>
    """)

    with gr.Row():
        lat = gr.Textbox(label="Latitude", placeholder="60.39", elem_classes="textbox-custom")
        long = gr.Textbox(label="Longitude", placeholder="5.32", elem_classes="textbox-custom")

    # Button to trigger image generation
    generate_button = gr.Button("Get weather data")

    # Output for the generated image
    image_output = gr.Image(label="Generated Image", width=1792, height=1024, container=True)

    # Textbox for generated text
    text_output = gr.Textbox(label="Recommendations for the weather", placeholder="Text generates here...", lines=10, elem_classes="custom-textbox")

    gr.Markdown("This website has no affiliations with MET Norway or OpenAI. This is a student project for the Western Norway University of Applied Sciences (HVL) ")

    # Set up the button 
    generate_button.click(fn=appfunction, inputs=[lat, long], outputs=[image_output, text_output])

# Launch app
interface.launch(share=True)
