import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1-x)


training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

#Initialising our synaptic weights by assigning random values to the weights
# There goes a  lot of science that goes into weight initialisation but its not required here
#We will have three synapses for our three inputs

np.random.seed(1)

#Results are from the “continuous uniform” distribution over the stated interval.
# To sample Unif[a, b), b > a multiply the output of random_sample by (b-a) and add a
#b = 1 , a = -1 ,because weights are in the interval (-1,1)
#(b - a) * random_sample() + a
synaptic_weights = 2 * np.random.random((3, 1)) - 1  #3 x 1 Matrix

print('Random Starting Synaptic Weights :', synaptic_weights, sep='\n')


# Now for the main loop
for iteration in range(100000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    '''(multiplying the input layer by their corresponding synaptic weights and summing them and then 
         passing the sum to our normalizing function)'''

    error = training_outputs - outputs
    adjustments = error * sigmoid_derivative(outputs)
    synaptic_weights += np.dot(input_layer.T, adjustments)

print("Synaptic Weights After Training : ")
print(synaptic_weights)


print('Outputs After Training : ')
print(outputs)


