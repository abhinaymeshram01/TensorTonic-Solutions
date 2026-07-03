import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0:
        return 0.0

    y = np.array(y)

    _, counts = np.unique(y, return_counts=True)

    probabilities = counts/len(y)

    log_probs = np.where(probabilities > 0, np.log2(probabilities), 0.0)

    entropy = -np.sum(probabilities * log_probs)

    return float(np.abs(entropy))