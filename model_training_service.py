from prompts.twitter import twitterPrompt
from prompts.facebook import facebookPrompt
from prompts.linkedin import linkedinPrompt
from prompts.instagram import instagramPrompt
from prompts.hashtags import hashtagsPrompt
from prompts.title import titlePrompt
from prompts.engagingQuestion import engagingPrompt
import openai


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key


#Python 3.10
# def platform_prompt(platform):
#     match platform:
#         case "facebook":
#             return facebookPrompt
#         case "twitter":
#             return twitterPrompt
#         case "linkedin":
#             return linkedinPrompt
#         case "instagram":
#             return instagramPrompt
#         case "hashtags":
#             return hashtagsPrompt
#         case "title":
#             return titlePrompt
#         case _:
#             return "Something's wrong with the internet"

def platform_prompt(platform):
    if "facebook" in platform:
        return facebookPrompt
    elif "twitter" in platform:
        return twitterPrompt
    elif "linkedin" in platform:
        return linkedinPrompt
    elif "instagram" in platform:
        return instagramPrompt
    else:
        return "Something's wrong with the internet"

class GeneralModel:
    def __init__(self):
        print("Model Intilization--->")
        # set_openai_key(API_KEY)

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        kwargs = {
            "engine": "text-davinci-002",
            "temperature": 0.70,
            "max_tokens": 2500,
            "best_of": 1,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": ["###"],
        }

        #print out target length

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        


        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0][
            "text"
        ].strip()
        return r

    def model_prediction_subprocess(self, input, social_media_platform, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        promptText = platform_prompt(social_media_platform)
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = self.query(promptText.format(input = input), social_media_platform)
        return output

    def model_prediction(self, input, social_media_platform, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        promptText = platform_prompt(social_media_platform)
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = dict()
        output['outputMain'] = self.query(promptText.format(input = input))
        output['outputEngaging'] = self.query(engagingPrompt.format(input = input))
        output['outputHashtags'] = self.query(hashtagsPrompt.format(input = input))
        output['outputTitle'] = self.query(titlePrompt.format(input = input))
        return output


## Generate Twitter posts
