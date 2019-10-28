import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import sys
import logging

logging.basicConfig(filename='error.log',level=logging.DEBUG)

def get_nlp_entities(text):
    try:
        # Instantiates a client
        client = language.LanguageServiceClient.from_service_account_json("/Users/liuqiaoyu/PycharmProjects/ABTasty/assets/auth.json")
        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        document = types.Document(
            content=text.encode('utf-8'),
            type=enums.Document.Type.PLAIN_TEXT)

        # Detect and send native Python encoding to receive correct word offsets.
        encoding = enums.EncodingType.UTF32
        if sys.maxunicode == 65535:
            encoding = enums.EncodingType.UTF16

        result = client.analyze_entity_sentiment(document, encoding)
        return result.entities
    except Exception as e:
        logging.error(str(e))
