import nlpcloud

def ner(text):
    client = nlpcloud.Client("finetuned-llama-3-70b", "67ee92a07a11daf205627520df4076cd3a7550ef", gpu=True)
    response = client.entities(
        text,
        searched_entity="entities"
    )
    return response