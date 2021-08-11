import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    ft_1 = json.dumps(french_text, indent=2, ensure_ascii=False)
    ft = json.loads(ft_1)
    teks_french = ft["translations"][0]["translation"]

    return teks_french


def french_to_english(french_text):
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    et_1 = json.dumps(english_text, indent=2, ensure_ascii=False)
    et = json.loads(et_1)
    teks_english = et["translations"][0]["translation"]

    return teks_english
