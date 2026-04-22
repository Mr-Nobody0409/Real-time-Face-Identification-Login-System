def evaluate(predictions, actual):
    correct = sum([1 for p, a in zip(predictions, actual) if p == a])
    return correct / len(actual)
