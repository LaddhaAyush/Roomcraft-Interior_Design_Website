
# import streamlit as st
# from PIL import Image
# from diffusers import StableDiffusionPipeline

# # Function to load the model with caching enabled via Streamlit
# @st.cache_resource
# def load_model():
#     try:
#         # Load the Stable Diffusion model with explicit cache directory
#         pipe = StableDiffusionPipeline.from_pretrained(
#             "CompVis/stable-diffusion-v1-4", 
#             cache_dir="./model_cache",  # Set the cache directory directly in the method
#             low_cpu_mem_usage=True      # Enable memory optimization
#         ).to("cpu")
#         return pipe
#     except Exception as e:
#         st.error(f"Error loading the model: {e}")
#         return None

# # Load the model once and cache it
# pipe = load_model()

# # Set up Streamlit page
# st.title("Generate Interior Design Ideas")

# # User form for design options
# with st.form("design_form"):
#     st.subheader("Select Interior Design Options")

#     space_type = st.selectbox("Space Type", [
#         "", "Living Room", "Kitchen", "Dining Room", "Bedroom", "Bathroom",
#         "Home Office", "Children's Room", "Laundry Room", "Garage", "Basement",
#         "Attic", "Entryway/Foyer", "Hallway", "Closet", "Pantry", "Mudroom",
#         "Balcony/Patio", "Home Gym", "Home Theater"
#     ])

#     style = st.selectbox("Style", [
#         "", "Modern", "Minimalist", "Contemporary", "Mid-Century Modern",
#         "Scandinavian", "Traditional", "French Country", "Bohemian (Boho)",
#         "Rustic", "Shabby Chic", "Coastal (Hamptons)", "Hollywood Regency",
#         "Farmhouse", "Industrial"
#     ])

#     layout = st.selectbox("Layout", [
#         "", "Open Plan", "Closed Plan", "L-shaped Layout", "Parallel Layout",
#         "Island Layout", "U-shaped Layout"
#     ])

#     lighting = st.selectbox("Lighting", [
#         "", "Natural Light", "Ambient Lighting", "Task Lighting", "Accent Lighting",
#         "Dramatic Lighting", "Dimmed Lighting", "Colored Lighting"
#     ])

#     perspective = st.selectbox("Perspective", [
#         "", "Eye-Level View", "Bird's Eye View", "Low Angle View",
#         "High Angle View", "Worm's Eye View"
#     ])

#     color_palette = st.selectbox("Color Palette", ["", "Monochromatic", "Complementary"])

#     furniture = st.selectbox("Furniture", [
#         "", "Sofa", "Coffee Table", "Dining Table", "Bed", "Desk",
#         "Vanity", "Bookshelf", "Bunk Bed", "Exercise Equipment", "Theater Seating"
#     ])

#     material = st.selectbox("Material", ["", "Wood", "Metal"])

#     accessories = st.selectbox("Accessories", ["", "Artwork", "Plants"])

#     # Option to upload an image for redesign
#     uploaded_image = st.file_uploader("Upload an Image to Redesign", type=["jpg", "jpeg", "png"])

#     submit_button = st.form_submit_button(label="Generate Design")

# if submit_button:
#     if all([space_type, style, layout, lighting, perspective, color_palette, furniture, material, accessories]):
#         if pipe:  # Ensure the model is loaded
#             with st.spinner("Generating design..."):
#                 try:
#                     # Construct a prompt with user selections
#                     prompt = f"A {style} {space_type} with {layout}, {lighting}, and {color_palette} color palette. Furniture includes {furniture} made of {material} with {accessories} as accessories, viewed from a {perspective} perspective."
                    
#                     # Check if an image has been uploaded
#                     if uploaded_image is not None:
#                         input_image = Image.open(uploaded_image)
#                         # Include the image in the generation pipeline if supported by the model
#                         image = pipe(prompt, init_image=input_image).images[0]
#                     else:
#                         # Generate a new image without using an uploaded image
#                         image = pipe(prompt).images[0]

#                     # Display the generated image
#                     st.image(image, caption="Generated Interior Design", use_column_width=True)
#                 except Exception as e:
#                     st.error(f"Error generating design: {e}")
#         else:
#             st.error("Model failed to load. Please try again later.")
#     else:
#         st.error("Please fill out all fields to generate a design.")

import streamlit as st
from PIL import Image
from PIL import ImageEnhance
from diffusers import StableDiffusionPipeline

# Function to load the model with caching enabled via Streamlit
@st.cache_resource
def load_model():
    try:
        # Load the Stable Diffusion model with explicit cache directory
        pipe = StableDiffusionPipeline.from_pretrained(
            "CompVis/stable-diffusion-v1-4", 
            cache_dir="./model_cache",  # Set the cache directory directly in the method
            low_cpu_mem_usage=True      # Enable memory optimization
        ).to("cpu")
        return pipe
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Load the model once and cache it
pipe = load_model()

# Set up Streamlit page
st.title("Generate Interior Design Ideas")

# User form for design options
with st.form("design_form"):
    st.subheader("Select Interior Design Options")

    # Option to upload an image for redesign
    uploaded_image = st.file_uploader("Upload an Image to Redesign", type=["jpg", "jpeg", "png"])

    # If an image is uploaded, show only the additional text prompt
    if uploaded_image is not None:
        additional_prompt = st.text_area("Provide a description to modify the uploaded image")
    else:
        # If no image is uploaded, prompt the user to fill out the form fields
        space_type = st.selectbox("Space Type", [
            "", "Living Room", "Kitchen", "Dining Room", "Bedroom", "Bathroom",
            "Home Office", "Children's Room", "Laundry Room", "Garage", "Basement",
            "Attic", "Entryway/Foyer", "Hallway", "Closet", "Pantry", "Mudroom",
            "Balcony/Patio", "Home Gym", "Home Theater"
        ])

        style = st.selectbox("Style", [
            "", "Modern", "Minimalist", "Contemporary", "Mid-Century Modern",
            "Scandinavian", "Traditional", "French Country", "Bohemian (Boho)",
            "Rustic", "Shabby Chic", "Coastal (Hamptons)", "Hollywood Regency",
            "Farmhouse", "Industrial"
        ])

        layout = st.selectbox("Layout", [
            "", "Open Plan", "Closed Plan", "L-shaped Layout", "Parallel Layout",
            "Island Layout", "U-shaped Layout"
        ])

        lighting = st.selectbox("Lighting", [
            "", "Natural Light", "Ambient Lighting", "Task Lighting", "Accent Lighting",
            "Dramatic Lighting", "Dimmed Lighting", "Colored Lighting"
        ])

        perspective = st.selectbox("Perspective", [
            "", "Eye-Level View", "Bird's Eye View", "Low Angle View",
            "High Angle View", "Worm's Eye View"
        ])

        color_palette = st.selectbox("Color Palette", ["", "Monochromatic", "Complementary"])

        furniture = st.selectbox("Furniture", [
            "", "Sofa", "Coffee Table", "Dining Table", "Bed", "Desk",
            "Vanity", "Bookshelf", "Bunk Bed", "Exercise Equipment", "Theater Seating"
        ])

        material = st.selectbox("Material", ["", "Wood", "Metal"])

        accessories = st.selectbox("Accessories", ["", "Artwork", "Plants"])

    submit_button = st.form_submit_button(label="Generate Design")

if submit_button:
    # If an image is uploaded, require the additional prompt to be filled
    if uploaded_image is not None:
        if additional_prompt:
            # Process with image and prompt
            if pipe:
                with st.spinner("Generating design..."):
                    try:
                        input_image = Image.open(uploaded_image)
                        prompt = additional_prompt  # Use the description as the prompt
                        image = pipe(prompt, init_image=input_image).images[0]
                        enhancer = ImageEnhance.Sharpness(image)
                        mg_sharpened = enhancer.enhance(2.0) 
                        st.image(mg_sharpened, caption="Redesigned Interior", use_column_width=True)
                    except Exception as e:
                        st.error(f"Error generating design: {e}")
            else:
                st.error("Model failed to load. Please try again later.")
        else:
            st.error("Please provide a description to redesign the uploaded image.")
    else:
        # If no image is uploaded, ensure all form fields are filled
        if all([space_type, style, layout, lighting, perspective, color_palette, furniture, material, accessories]):
            if pipe:
                with st.spinner("Generating design..."):
                    try:
                        # Construct a prompt with user selections
                        prompt = f"A {style} {space_type} with {layout}, {lighting}, and {color_palette} color palette. Furniture includes {furniture} made of {material} with {accessories} as accessories, viewed from a {perspective} perspective."
                        image = pipe(prompt).images[0]
                        st.image(image, caption="Generated Interior Design", use_column_width=True)
                    except Exception as e:
                        st.error(f"Error generating design: {e}")
            else:
                st.error("Model failed to load. Please try again later.")
        else:
            st.error("Please fill out all fields to generate a design.")
