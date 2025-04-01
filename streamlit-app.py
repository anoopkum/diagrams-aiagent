import streamlit as st
import os
from diagrams.diagram_generator import generate_architecture_description, create_diagram

st.title("Diagram Generator Tool")
st.write("Generate AWS Architecture Diagrams from a simple description!")

user_prompt = st.text_input("Enter a description for the diagram:")

if st.button("Generate Diagram"):
    if user_prompt:
        # Generate architecture description based on the user input
        description = generate_architecture_description(user_prompt)
        st.write("Generated Description:")
        st.write(description)
        
        # Create the diagram with a specified output filename
        output_file = "generated_diagram"
        create_diagram(description, output_file=output_file)
        
        # Diagrams saves the file as output_file+".png"
        diagram_path = output_file + ".png"
        if os.path.exists(diagram_path):
            st.image(diagram_path, caption="Generated Diagram", use_column_width=True)
        else:
            st.error("Error: Diagram image not found.")
    else:
        st.warning("Please enter a description.")