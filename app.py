import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

st.title("Note summary and quizes")
st.markdown("Input 3 images for summary and quizees")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader("Upload images of your notes", type=["jpg", "jpeg", "png"], accept_multiple_files = True)
    
    pil_images = []
    for img in images:
        pil_images.append(Image.open(img))
        
    if images:
        if len(images) > 3:
            st.error("Please upload at max 3 images")
        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #select box
    selected_option = st.selectbox("Select your difficulty level",("Easy", "Medium", "Hard"), index = None)

    if selected_option:
        st.markdown(f"You selected **{selected_option}** as difficulty level")
    else:
        st.error("Please select a difficulty level")

    pressed = st.button("Clcik to initiate AI", type = "primary")

if pressed:
    if not images:
        st.error("Please upload images")
    if not selected_option:
        st.error("Please select difficulty level")

    if images and selected_option:
        #note
        with st.container(border = True):
            st.subheader("Your note")
            with st.spinner("AI is writting for you..."):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

        #audio
        with st.container(border = True):
            st.subheader("Audio Transcription")
            with st.spinner("AI is making audio for you..."):
                generated_notes = generated_notes.replace("#","")
                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)

        #quiz
        with st.container(border = True):
            st.subheader(f"Quiz ({selected_option}) difficulty")
            with st.spinner("AI is generating quiz for you..."):
                quizzes = quiz_generator(pil_images, selected_option)
                st.markdown(quizzes)