import numpy as np

def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(x)
    """
    s = 1/(1+np.exp(-x))
    return s

def relu(x):
    """
    Compute the relu of x

    Arguments:
    x -- A scalar or numpy array of any size.

    Return:
    s -- relu(x)
    """
    s = np.maximum(0,x)
    
    return s

def dictionary_to_vector(parameters):
    """
    Roll all our parameters dictionary into a single vector satisfying our specific required shape.
    """
    keys = []
    count = 0
    for key in ["W1", "b1", "W2", "b2", "W3", "b3"]:
        
        print(parameters[key].shape)
        print(parameters[key])
        # flatten parameter
        new_vector = np.reshape(parameters[key], (-1,1))
        print(new_vector.shape)
        # print(new_vector)
        keys = keys + [key]*new_vector.shape[0]
        print(keys)
        
        print(count)
        if count == 0:
            theta = new_vector
            print(theta)
        else:
            theta = np.concatenate((theta, new_vector), axis=0)
            print(theta) 
        count = count + 1

    return theta, keys

def vector_to_dictionary(theta):
    """
    Unroll all our parameters dictionary from a single vector satisfying our specific required shape.
    """
    parameters = {}
    parameters["W1"] = theta[:20].reshape((5,4))
    parameters["b1"] = theta[20:25].reshape((5,1))
    parameters["W2"] = theta[25:40].reshape((3,5))
    parameters["b2"] = theta[40:43].reshape((3,1))
    parameters["W3"] = theta[43:46].reshape((1,3))
    parameters["b3"] = theta[46:47].reshape((1,1))

    return parameters

def gradients_to_vector(gradients):
    """
    Roll all our gradients dictionary into a single vector satisfying our specific required shape.
    """
    
    count = 0
    for key in ["dW1", "db1", "dW2", "db2", "dW3", "db3"]:
        # flatten parameter
        new_vector = np.reshape(gradients[key], (-1,1))
        
        if count == 0:
            theta = new_vector
        else:
            theta = np.concatenate((theta, new_vector), axis=0)
        count = count + 1

    return theta

parameters = {'W1': np.array([[-0.3224172 , -0.38405435,  1.13376944, -1.09989127],
       [-0.17242821, -0.87785842,  0.04221375,  0.58281521],
       [-1.10061918,  1.14472371,  0.90159072,  0.50249434],
       [ 0.90085595, -0.68372786, -0.12289023, -0.93576943],
       [-0.26788808,  0.53035547, -0.69166075, -0.39675353]]), 'b1': np.array([[-0.6871727 ],
       [-0.84520564],
       [-0.67124613],
       [-0.0126646 ],
       [-1.11731035]]), 'W2': np.array([[ 0.2344157 ,  1.65980218,  0.74204416, -0.19183555, -0.88762896],
       [-0.74715829,  1.6924546 ,  0.05080775, -0.63699565,  0.19091548],
       [ 2.10025514,  0.12015895,  0.61720311,  0.30017032, -0.35224985]]), 'b2': np.array([[-1.1425182 ],
       [-0.34934272],
       [-0.20889423]]), 'W3': np.array([[0.58662319, 0.83898341, 0.93110208]]), 'b3': np.array([[0.28558733]])}

parameters_values, _ = dictionary_to_vector(parameters)
thetaplus =  np.copy(parameters_values)
print(thetaplus)
