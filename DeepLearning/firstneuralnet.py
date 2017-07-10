from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        #Seeds the random number generator, so it genarates the samples
        #every time the program runs.
        random.seed(1)

        #We model a single neuron, with 3 input connections and 1 output connection.
        #We assing random weights to a 3 x 1 matrix, with values in the range -1 to 1
        #and mean 0.
        self.synaptic_weights = 2 * random.random((3,1)) - 1

    #The sigmoid function, witch describes an s shape curve
    #We pass the weighted sum of the inputs through this function
    #to normalize them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp (-x))

    #Gradient of the sigmoid curve.
    def __sigmoid_derivative(self, x):
        return x * (1-x)


    def train (self, training_set_inputs, training_set_outputs, number_of_training_interations):
        for interation in range(number_of_training_interations):
            #Pass the training set through our neural net
            output = self.predict(training_set_inputs)

            #Calculate the error
            error = training_set_outputs - output

            #Multiply the error by the input ad againby the gradient of the sigmoid curve
            adjustments = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            #Adjusts the weights
            self.synaptic_weights += adjustments


    def predict (self, inputs):
        #Pass inputs through our neural network (our single neuron)
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

if __name__ == '__main__':
    #initialize a single neural network
    neural_network = NeuralNetwork()

    print ('randon starting synaptic weights:')
    print (neural_network.synaptic_weights)

    #The training set. We have 4 examples, each consisting of 3 input values
    #and 1 out put value.

    training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    #training the neural network using a training set.
    #Do it 10.000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print ('New synaptics weights after training:')
    print (neural_network.synaptic_weights)

    #test the neural network.
    print ('predicting:')
    print (neural_network.predict(array([1,0,0])))
