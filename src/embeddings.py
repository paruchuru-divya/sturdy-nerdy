from model_loader import get_embedding_model

model = get_embedding_model()


def generate_embeddings(chunks):

    return model.encode(chunks, convert_to_numpy=True)