import openai
from prompts.twitter import twitter_prompt
from prompts.facebook import facebook_prompt
from prompts.linkedin import linkedin_prompt
from prompts.instagram import instagram_prompt
from prompts.hashtags import hashtags_prompt
from prompts.title import title_prompt
from prompts.engaging_question import engaging_prompt

def set_openai_key(key):
    """
        Sets OpenAI key.
    """
    openai.api_key = key

def platform_prompt(platform):
    platforms = {
        'facebook': facebook_prompt,
        'twitter': twitter_prompt,
        'linkedin': linkedin_prompt,
        'instagram': instagram_prompt
    }

    return platforms[platform]

class GeneralModel:
    def __init__(self):
        pass

    def predict(self, prompt, **kwargs):
        """
            wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        gpt_options = {
            'engine': 'text-davinci-002',
            'temperature': 0.70,
            'max_tokens': 2500,
            'best_of': 1,
            'top_p': 1,
            'frequency_penalty': 0,
            'presence_penalty': 0,
            'stop': ["###"],
        }

        return openai.Completion.create(prompt=prompt, **gpt_options, **kwargs)['choices'][0]['text'].strip()

    def model_prediction(self, inp, social_media_platform, api_key):
        """
            wrapper for the API to save the prompt and the result
        """
        prompt_text = platform_prompt(social_media_platform)
        
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)

        output = {
            'output_main': self.predict(prompt_text.format(input=inp)),
            'output_engaging': self.predict(engaging_prompt.format(input=inp)),
            'output_hashtags': self.predict(hashtags_prompt.format(input=inp)),
            'output_title': self.predict(title_prompt.format(input=inp))
        }
        
        return output