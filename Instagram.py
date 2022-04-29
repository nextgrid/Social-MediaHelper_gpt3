from tkinter import Label
import streamlit as st
from model_training_service import Instagram
import pw_api
import countries


def app():

    # Creating an object of prediction service
    pred = Instagram()

    api_key = st.sidebar.text_input("APIkey", type="password")
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip(), api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Create an instagram post")

        # st.write("---")

        s_example = "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by humans or animals. Leading AI textbooks define the field as the study of 'intelligent agents': any system that perceives its environment and takes actions that maximize its chance of achieving its goals. Some popular accounts use the term 'artificial intelligence' to describe machines that mimic cognitive functions that humans associate with the human mind, such as learning and problem solving, however this definition is rejected by major AI researchers. AI applications include advanced web search engines, recommendation systems (used by YouTube, Amazon and Netflix), understanding human speech (such as Siri or Alexa), self-driving cars (such as Tesla), and competing at the highest level in strategic game systems (such as chess and Go). As machines become increasingly capable, tasks considered to require intelligence are often removed from the definition of AI, a phenomenon known as the AI effect. For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology."
        input = st.text_area(
            "Use the example below or input your own text in English (between 1,000 and 10,000 characters)",
            value=s_example,
            max_chars=10000,
            height=330,
        )
        # targetAge = st.number_input(
        #     label = "Target age",
        #     min_value=14,
        #     max_value=100
        # )
        # country = st.selectbox('Target Country',(countries.countries))

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Password not found")
