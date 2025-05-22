import json

def format_response_as_json(answer, metadata=None):
    response = {
        "reponse": answer
    }
    if metadata:
        response["metadata"] = metadata
    return json.dumps(response, ensure_ascii=False, indent=2)