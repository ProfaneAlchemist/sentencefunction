import logging

import azure_functions as func
from sentence_transformers import SentenceTransformer

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    sentence = req.params.get('sentence')
    if not sentence:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sentence = req_body.get('sentence')

    if sentence:
        model = SentenceTransformer('paraphrase-MiniLm-l6-v2')
        embedding = model.encode(sentence)
        return func.HttpResponse(str(embedding))
    else:
        return func.HttpResponse(
             "Please pass a sentence on the query string or in the request body",
             status_code=400
        )