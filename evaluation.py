def evaluate(predictions, actual):
    correct = 0

    for p, a in zip(predictions, actual):
        if p == a:
            correct += 1

    accuracy = correct / len(actual)
    return accuracy
