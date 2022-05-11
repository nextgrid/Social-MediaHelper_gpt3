## 📱 New Native's Social Media Helper 

> **You need access to the OpenAI API Key to use out app** <br> If you dont have the access to the API, please apply [here](https://beta.openai.com/) ✌️


## 🖥️ How to run app locally?

Firstly you have to create virtual enviroment and download necessary packages. For example, using pip:

```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Now you can run it using following command

```
streamlit run main.py
```

### 🗃️ Files/Directories:

* main.py - main application file
* email_sender.py - code with the possibility of sending an email
* model_training_service.py - access to OpenAI's GPT-3 model
* pdf.py - contains code responsible for writing content to .pdf files
* requirements.txt - required python packages/libraries
* prompts/*.py - contains prompts that are given to the model
* fonts/* - contains the fonts used by our pdf.py module
* public/* - contains logos, photos, etc.