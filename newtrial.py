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
    >>> round(linear(x, w, b),6) #linear(x, w, b)
    7.35
    """

    return sum(w[j]*x[j] for j in range(len(w))) + b


def linear_layer(x, w, b): # 1 Mark
    """
    Input: A list of inputs (x), a table of weights (w) and a list of 
           biases (b).
    Output: A list of numbers corresponding to the values of f(x) in
            Equation 2.
    
    >>> x = [1.0, 3.5]
    >>> w = [[3.8, 1.5], [-1.2, 1.1]]
    >>> b = [-1.7, 2.5]
    >>> y = linear_layer(x, w, b)
    >>> [round(y_i,6) for y_i in y] #linear_layer(x, w, b)
    [7.35, 5.15]
    """

    return [linear(x, w[i], b[i]) for i in range(len(w))]


def inner_layer(x, w, b): # 1 Mark
    """
    Input: A list of inputs (x), a table of weights (w) and a 
           list of biases (b).
    Output: A list of numbers corresponding to the values of f(x) in 
            Equation 4.

    >>> x = [1, 0]
    >>> w = [[2.1, -3.1], [-0.7, 4.1]]
    >>> b = [-1.1, 4.2]
    >>> y = inner_layer(x, w, b)
    >>> [round(y_i,6) for y_i in y] #inner_layer(x, w, b)
    [1.0, 3.5]
    >>> x = [0, 1]
    >>> y = inner_layer(x, w, b)
    >>> [round(y_i,6) for y_i in y] #inner_layer(x, w, b)
    [0.0, 8.3]
    """

    return [max(linear(x, w[i], b[i]), 0.0) for i in range(len(w))]


def inference(x, w, b): # 2 Marks
    """
    Input: A list of inputs (x), a list of tables of weights (w) and a table
           of biases (b).
    Output: A list of numbers corresponding to output of the ANN.
    
    >>> x = [1, 0]
    >>> w = [[[2.1, -3.1], [-0.7, 4.1]], [[3.8, 1.5], [-1.2, 1.1]]]
    >>> b = [[-1.1, 4.2], [-1.7, 2.5]]
    >>> y = inference(x, w, b)
    >>> [round(y_i,6) for y_i in y] #inference(x, w, b)
    [7.35, 5.15]
    """

    num_layers = len(w)
    
    for l in range(num_layers-1):
        x = inner_layer(x, w[l], b[l])
        
    return linear_layer(x, w[num_layers-1], b[num_layers-1])


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

    weights_file = open(file_name,"r")
    w = []
    for line in weights_file:
        if "#" == line[0]:
            w.append([])
        else:
            w[-1].append([float(w_ij) for w_ij in line.strip().split(",")])
    
    return w


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

    biases_file = open(file_name,"r")
    b = []
    for line in biases_file:
        if not "#" == line[0]:
            b.append([float(b_j) for b_j in line.strip().split(",")])
    
    return b


def read_image(file_name): # 1 Mark
    """
    Input: A string (file_name), that corresponds to the name of the file
           that contains the image.
    Output: A list of numbers corresponding to input of the ANN.
    
    >>> x = read_image('image.txt')
    >>> len(x)
    784
    """

    image_file = open(file_name,"r")
    x = []
    for line in image_file:
        for x_i in line.strip():
            x.append(int(x_i))
            
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

    num_inputs = len(x)
    max_index = 0
    
    for i in range(1,num_inputs):
        if x[max_index] < x[i]:
            max_index = i
            
    return  max_index


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
    
    y = inference(x, w, b)
    return argmax(y)
#part 1 code taken from part 1 solution
#Monash Engineering (2022) FIT1045 Assignment part 1 solution [python]
#https://lms.monash.edu/mod/resource/view.php?id=8651722

#part 2
import copy
def flip_pixel(x):
    """
    Input: 
        -x: a single pixel (0 or 1)
    Output: 
        -newx: The flipped pixel (if input = 1, output = 0)

    This function's purpose is to take an input of a pixel and flip it.
    If the input was originally 0, it is now 1
    If the input was originally 1, it is now 0
    """
    newx = 0
    if x == 0:
        newx = 1
    return newx

def modified_list(i,x):
    """
    Input:
        -i: position index of the pixel to flip
        -x: input list of pixels
    Output:
        -u: the modified list of pixels after pixel at i is flipped
    
    The purpose of this function is to take a position index and a pixel 
    modified_list and flipped the indexed pixel. The now modified list is then 
    outputed.
    """
    u = copy.deepcopy(x)
    n = len(u)
    for j in range(n):
        if j == i:
            u[j] = flip_pixel(u[j])
    return u

def compute_difference(x1, x2):
    """
    Input:
        -x1: first list
        -x2: second list
    Output:
        -counter: the number of elements that are different between x1 and x2
    
    The purpose of this function is to compute the number of different elements
    between two equal length lists and to output the difference as a number.
    """
    n = len(x1)
    counter = 0
    for i in range(n):
        if x1[i] != x2[i]:
            counter += 1
    return counter

def impact(x1, x2):
    """
    Input:
        -x1: first list
        -x2: second list
    Output:
        -change/-1
    
    The purpose of this function is to calculate the impact of the overall
    change to the list as defined by how much the value of 4th index decreased
    and how much did the rest of the list increased
    """
    num1_change = x1[4] - x2[4]
    overall = [x2[i] - x1[i] for i in range(len(x1)) if i != 4]
    change = sum(overall) + num1_change
    if change <= 0:
        return -1
    return change

def select_pixel(x, w, b):
    """
    Input:
        -x: a list of integers representing an image
        -w: a list of lists representing the weights of the ANN
        -b: a list of lists represnting the biases of the ANN
    
    Output:
        -ind: representing the index of pixel to be flipped that will create the
        biggest impat as defined by impact() function

    The purpose of this function is to compute the pixel that when flipped will
    have the largest impact on the predicted number of the image. This was
    computed using a greedy method where the impact of the list of possible flips
    were sorted by the impact score from the original input.
    The highest impact score was selected as the list was sorted in reverse with
    highest score first and lowest score last.
    """
    x1 = inference(x, w, b)
    u = copy.deepcopy(x)
    x2 = [inference(modified_list(i, u), w, b) for i in range(len(u))]
    n = len(x2)
    def score(i): return impact(x1, x2[i])
    items = sorted(range(n), key=score, reverse=True)
    ind = items[0]
    if impact(x1, inference(modified_list(ind, u), w, b)) == -1:
        return -1
    return ind

def write_image(x, file_name):
    """
    Input:
        -x: the list of pixels representing the image to be written
        -file_name: the string variable representing the name of the file
    Output:
        -Nothing is output into the console, however the file with name file_name
         will be overwritten with x at a spacing of 28 pixels per line
    """
    f = open(file_name, "w")
    x_string = ""
    n = len(x)
    for i in range(n):
        x_string += str(x[i])
        if (i + 1)%28 == 0:
            x_string += "\n"
    f.write(x_string)
    f.close()

def adversarial_image(image_file_name, weight_file_name, biases_file_name):
    """
    Input:
        -image_file_name: string variable representing the image txt file
        -weight_file_name: string variable representing the weight txt file
        -biases_file_name: string variable representing the biases txt file
    Output:
        -"An adversarial image is found! Total of " + str(n) + " pixels were 
          flipped"
        -OR "The algorithm failed"
        -This is an output statement which either outputs the success statement
         and the number of pixel flips required, or outputs -1 stating the
         algorithm was a failure
        
    The purpose of this function is to generate an adversarial image of the
    original if an adversarial image can be generated. The parameters used are
    the previously written select_pixel() function to select a pixel with the
    largest impacts.

    If the failure statement in impact and select_pixel is triggered a failure
    statement will be printed instead
    """
    number = predict_number(image_file_name, weight_file_name, biases_file_name)
    x = read_image(image_file_name)
    x2 = copy.deepcopy(x)
    w = read_weights(weight_file_name)
    b = read_biases(biases_file_name)
    new_number = copy.deepcopy(number)
    while new_number == number:
        p = select_pixel(x2, w, b)
        if p == -1:
            return "The algorithm failed"
        x2 = modified_list(p, x2)
        new_number = argmax(inference(x2, w, b))
    n = compute_difference(x, x2)
    write_image(x2, "new_image.txt")
    return "An adversarial image is found! Total of " + str(n) + " pixels were flipped"
