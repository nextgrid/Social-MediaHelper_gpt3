import streamlit as st
from model_training_service import GeneralModel
from PIL import Image
import pyperclip

image = Image.open('New_Native.png')

def copy (input):
    pyperclip.copy(input)

if 'summary' not in st.session_state:
    st.session_state['summary'] = ""
if 'question' not in st.session_state:
    st.session_state['question'] = ""
if 'hashtags' not in st.session_state:
    st.session_state['hashtags'] = ""
if 'title' not in st.session_state:
    st.session_state['title'] = ""
if 'APIkey' not in st.session_state:
    st.session_state['APIkey'] = ""
    
def app():

    # Creating an object of prediction service
    pred = GeneralModel()
    if st.session_state['APIkey'] == "":
        api_key = st.sidebar.text_input("APIkey", type="password")
        st.session_state['APIkey'] = api_key
    else:
        api_key = st.session_state['APIkey']
    social_media_platform = st.sidebar.selectbox("Select a social media platform/type", ["facebook", "twitter", "instagram", "linkedin"])
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip(),social_media_platform=social_media_platform , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.image(image)
        st.title("Create a social media post-{social_media_platform} from below text".format(social_media_platform=social_media_platform))

        # st.write("---")

        s_example = "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by humans or animals. Leading AI textbooks define the field as the study of 'intelligent agents': any system that perceives its environment and takes actions that maximize its chance of achieving its goals. Some popular accounts use the term 'artificial intelligence' to describe machines that mimic cognitive functions that humans associate with the human mind, such as learning and problem solving, however this definition is rejected by major AI researchers. AI applications include advanced web search engines, recommendation systems (used by YouTube, Amazon and Netflix), understanding human speech (such as Siri or Alexa), self-driving cars (such as Tesla), and competing at the highest level in strategic game systems (such as chess and Go). As machines become increasingly capable, tasks considered to require intelligence are often removed from the definition of AI, a phenomenon known as the AI effect. For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology."
        input = st.text_area(
            "Use the example below or input your own text in English (between 1,000 and 10,000 characters)",
            value=s_example,
            max_chars=10000,
            height=250,
        )


        

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.session_state['summary'] = report_text['outputMain']
                st.session_state['question'] = report_text['outputEngaging']
                st.session_state['hashtags'] = report_text['outputHashtags']
                st.session_state['title'] = report_text['outputTitle']

        if st.session_state['summary']:
            st.subheader("Summary")
            st.write(st.session_state['summary'])
        if st.session_state['question']:
            st.subheader("Engaging question")
            st.write(st.session_state['question'])
        if st.session_state['hashtags']:
            st.subheader("Hashtags")
            st.write(st.session_state['hashtags'])
        if st.session_state['title']:
            st.subheader("Title")
            st.write(st.session_state['title'])
            

        st.session_state
    else:
        st.error("???? Please enter API Key")
