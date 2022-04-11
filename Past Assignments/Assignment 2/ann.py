"""
Author: <Huihong Zheng> (<28747445>)

Inspired from the human brain, artificial neural networks (ANNs) are a 
type of computer vision model to classify images into certain categories.
In particular, in this assignment we will consider ANNs for the taks of
recognising handwritten digits (0 to 9) from black-and-white images with a
resolution of 28x28 pixels. In Part 1 of this assignment you will create
functions that compute an ANN output for a given input, and in Part 2 you
will write functions to "attack" an ANN. That is, to try to generate inputs
that will fool the network to make a wrong classification.

Part 1 is due at the end of Week 6 and Part 2 is due at the end of week 11.

For more information see the function documentation below and the
assignment sheet.
"""


# Part 1 (due Week 6)
def linear(x, w, b): # 1 Mark
    """
    Input: A list of inputs (x), a list of weights (w) and a bias (b).
    Output: A single number corresponding to the value of f(x) in Equation 1.

    >>> x = [1.0, 3.5]
    >>> w = [3.8, 1.5]
    >>> b = -1.7
    >>> linear(x, w, b)
    7.35
    """
    sum = b
    for i in range(len(x)):
        sum += x[i] * w[i]
    return sum


def linear_layer(x, w, b): # 1 Mark
    """
    Input: A list of inputs (x), a table of weights (w) and a list of 
           biases (b).
    Output: A list of numbers corresponding to the values of f(x) in
            Equation 2.
    
    >>> x = [1.0, 3.5]
    >>> w = [[3.8, 1.5], [-1.2, 1.1]]
    >>> b = [-1.7, 2.5]
    >>> linear_layer(x, w, b)
    [7.35, 5.15]
    """
    output = [[0] for _ in range(len(w))]
    for i in range(len(w)):
        output[i] = linear(x, w[i], b[i])
    return output


def inner_layer(x, w, b): # 1 Mark
    """
    Input: A list of inputs (x), a table of weights (w) and a 
           list of biases (b).
    Output: A list of numbers corresponding to the values of f(x) in 
            Equation 4.

    >>> x = [1, 0]
    >>> w = [[2.1, -3.1], [-0.7, 4.1]]
    >>> b = [-1.1, 4.2]
    >>> inner_layer(x, w, b)
    [1.0, 3.5]
    >>> x = [0, 1]
    >>> inner_layer(x, w, b)
    [0.0, 8.3]
    """
    output = [[0] for _ in range(len(w))]
    for i in range(len(w)):
        output[i] = max(linear_layer(x, w, b)[i], 0.0)
    return output


def inference(x, w, b): # 2 Marks
    """
    Input: A list of inputs (x), a list of tables of weights (w) and a table
           of biases (b).
    Output: A list of numbers corresponding to output of the ANN.
    
    >>> x = [1, 0]
    >>> w = [[[2.1, -3.1], [-0.7, 4.1]], [[3.8, 1.5], [-1.2, 1.1]]]
    >>> b = [[-1.1, 4.2], [-1.7, 2.5]]
    >>> inference(x, w, b)
    [7.35, 5.15]
    """
    for i in range(len(b)):
        x = inner_layer(x, w[i], b[i])
    return x
    

    



def read_weights(file_name): # 1 Mark
    """
    Input: A string (file_name) that corresponds to the name of the file
           that contains the weights of the ANN.
    Output: A list of tables of numbers corresponding to the weights of
            the ANN.
    
    >>> w_example = read_weights('example_weights.txt')
    >>> w_example
    [[[2.1, -3.1], [-0.7, 4.1]], [[3.8, 1.5], [-1.2, 1.1]]]
    >>> w = read_weights('weights.txt')
    >>> len(w)
    3
    >>> len(w[2])
    10
    >>> len(w[2][0])
    16
    """
    f = open(file_name)
    content = f.readlines()
    f.close
    n = 0
    for line in content:
        if line.startswith('#'):
            n += 1
    new_lst = [[] for _ in range (n)]
    i = -1
    templst = []
    for line in content:
        if line.startswith('#'):
            i += 1
        else :
            templst = line.split(',')
            templst = list(map(float, templst))
            new_lst[i].append(templst)
    return new_lst

def read_biases(file_name): # 1 Mark
    """
    Input: A string (file_name), that corresponds to the name of the file
           that contains the biases of the ANN.
    Output: A table of numbers corresponding to the biases of the ANN.
    
    >>> b_example = read_biases('example_biases.txt')
    >>> b_example
    [[-1.1, 4.2], [-1.7, 2.5]]
    >>> b = read_biases('biases.txt')
    >>> len(b)
    3
    >>> len(b[0])
    16
    """
    f = open(file_name)
    content = f.readlines()
    f.close
    n = 0
    for line in content:
        if line.startswith('#'):
            n += 1
    newlst = [[] for _ in range(n)]
    templst = []
    i = -1
    for line in content:
        if line.startswith('#'):
            i += 1
            continue
        else :
            templst = line.split(',')
            templst = list(map(float, templst))
            newlst[i] = templst
    return newlst


def read_image(file_name): # 1 Mark
    """
    Input: A string (file_name), that corresponds to the name of the file
           that contains the image.
    Output: A list of numbers corresponding to input of the ANN.
    
    >>> x = read_image('image.txt')
    >>> len(x)
    784
    """
    f = open(file_name)
    content = f.read()
    f.close

    x = []
    content = content.split('\n')
    for line in content:
        x += line
    x = list(map(int, x))
    return x


def argmax(x): # 1 Mark
    """
    Input: A list of numbers (i.e., x) that can represent the scores 
           computed by the ANN.
    Output: A number representing the index of an element with the maximum
            value, the function should return the minimum index.
    
    >>> x = [1.3, -1.52, 3.9, 0.1, 3.9]
    >>> argmax(x)
    2
    """
    n = 0
    for i in x:
        if i == max(x):
            return(n)
        else :
            n += 1


def predict_number(image_file_name, weights_file_name, biases_file_name): # 1 Mark
    """
    Input: A string (i.e., image_file_name) that corresponds to the image
           file name, a string (i.e., weights_file_name) that corresponds
           to the weights file name and a string (i.e., biases_file_name)
           that corresponds to the biases file name.
    Output: The number predicted in the image by the ANN.

    >>> i = predict_number('image.txt', 'weights.txt', 'biases.txt')
    >>> print('The image is number ' + str(i))
    The image is number 4
    """
    x = read_image(image_file_name)
    w = read_weights(weights_file_name)
    b = read_biases(biases_file_name)

    inference_output = inference(x, w, b)
    i = argmax(inference_output)
    return i




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
