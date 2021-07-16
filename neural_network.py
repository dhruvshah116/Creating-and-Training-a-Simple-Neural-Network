import numpy as np


class NeuralNetwork():

    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        # Forward and Backward Propagation for the training phase
        for iteration in range(training_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments

    def think(self, inputs):  # What goes on in the neuron
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == '__main__':      #the main utility code
    neural_network = NeuralNetwork()
    print("Random Synaptic Weights : ")
    print(neural_network.synaptic_weights)

    training_inputs = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])

    training_outputs = np.array([[0, 1, 1, 0]]).T

    neural_network.train(training_inputs, training_outputs, 20000)

    print("Synaptic Weights after training : ")  #Adjusted Synaptic Weights , that self-learned from the errors (Back Propagation)
    print(neural_network.synaptic_weights)

    #Now to test our model through custom inputs
    A = str(input("Input 1: "))
    B = str(input("Input 2: "))
    C = str(input("Input 3: "))

    print('Custom Inputs : ', A, B, C)
    print("Output Data : ")
    print(neural_network.think(np.array([A, B, C])))


