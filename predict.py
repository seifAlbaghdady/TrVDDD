import argparse
import pandas as pd
import torch
import numpy as np
from gensim.models.word2vec import Word2Vec
from model import BatchProgramClassifier
from torch.autograd import Variable


def parse_options():
    parser = argparse.ArgumentParser(description="TrVD training.")
    parser.add_argument(
        "-i",
        "--input",
        default="mutrvd",
        choices="mutrvd",
        help="training dataset type",
        type=str,
        required=False,
    )
    args = parser.parse_args()
    return args


def get_batch(dataset, idx, bs):
    tmp = dataset.iloc[idx : idx + bs]
    data, labels = [], []
    for _, item in tmp.iterrows():
        data.append(item["code"])
        labels.append(item["label"])
    return data, torch.LongTensor(labels)


def evaluation():
    args = parse_options()
    embedding_size = 128
    test_data = pd.read_pickle("subtrees/" + args.input + "/test_block.pkl")
    test_data = test_data.drop(test_data[test_data["code"].str.len() == 0].index)

    w2v_path = "subtrees/" + args.input + "/node_w2v_" + str(embedding_size)
    word2vec = Word2Vec.load(w2v_path).wv
    embeddings = np.zeros(
        (word2vec.vectors.shape[0] + 1, word2vec.vectors.shape[1]), dtype="float32"
    )
    embeddings[: word2vec.vectors.shape[0]] = word2vec.vectors

    HIDDEN_DIM = 100
    ENCODE_DIM = 128
    LABELS = 86
    BATCH_SIZE = 100
    USE_GPU = True
    MAX_TOKENS = word2vec.vectors.shape[0]
    EMBEDDING_DIM = word2vec.vectors.shape[1]
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = BatchProgramClassifier(
        EMBEDDING_DIM,
        HIDDEN_DIM,
        MAX_TOKENS + 1,
        ENCODE_DIM,
        LABELS,
        BATCH_SIZE,
        device,
        USE_GPU,
        embeddings,
    )
    model.load_state_dict(
        torch.load(
            "./saved_model/best_" + args.input + ".pt", map_location=torch.device("cpu")
        )
    )
    model.to(device)
    model.eval()

    all_preds = []
    while i < len(test_data):
        batch = get_batch(test_data, i, BATCH_SIZE)
        i += BATCH_SIZE
        test_inputs, test_labels = batch
        if USE_GPU:
            test_inputs = test_inputs.to(device)
        model.batch_size = len(test_labels)
        output = model(test_inputs)
        _, predicted = torch.max(output.data, 1)
        all_preds += predicted.tolist()

    return all_preds


if __name__ == "__main__":
    predictions = evaluation()
    print(predictions)
    print("Predictions:")
    for i in range(len(predictions)):
        if predictions[i] == 0:
            print("Not Vulnerable")
        else:
            print("Vulnerable")
