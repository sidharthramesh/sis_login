import numpy as np
import pickle
import matplotlib.pyplot as plt
keys=np.array(['0', '2', '3', '4', '6', '7', '8', '9', 'A', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L','N', 'P', 'Q', 'R', 'T', 'U', 'V','X', 'Y', 'Z'])
def one_hot(label):
    """converts label to onehots(integer 0 and 1)"""
    keys=np.array(['0', '2', '3', '4', '6', '7', '8', '9', 'A', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L','N', 'P', 'Q', 'R', 'T', 'U', 'V','X', 'Y', 'Z'])
    return (label==keys).astype(np.int)
def to_char(one_hot):
    """converts one_hot back to characters"""
    keys=np.array(['0', '2', '3', '4', '6', '7', '8', '9', 'A', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L','N', 'P', 'Q', 'R', 'T', 'U', 'V','X', 'Y', 'Z'])
    one_hot=one_hot.astype(np.bool)
    return keys[np.where(one_hot==1)]
def std(array):
    return ((array.astype(np.float32)-128)/255).reshape(-1,38,34,1)
