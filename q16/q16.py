import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Weights and biases initialization
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_hidden = np.random.rand(self.hidden_size)
        self.bias_output = np.random.rand(self.output_size)

    def forward(self, X):
        # Input to hidden layer
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        
        # Hidden to output layer
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_input)
        
        return self.output

    def backward(self, X, y, learning_rate):
        # Calculate output layer error and gradient
        output_error = y - self.output
        output_gradient = sigmoid_derivative(self.output)
        output_delta = output_error * output_gradient
        
        # Calculate hidden layer error and gradient
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_gradient = sigmoid_derivative(self.hidden_output)
        hidden_delta = hidden_error * hidden_gradient
        
        # Update weights and biases using gradient descent
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0) * learning_rate
        self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)
            if epoch % 1000 == 0:
                loss = np.mean(np.square(y - self.output))
                print(f"Epoch {epoch}, Loss: {loss}")

# Example usage
if __name__ == "__main__":
    # Input dataset (X) and expected output (y)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # XOR problem
    y = np.array([[0], [1], [1], [0]])  # XOR output

    # Create neural network with 2 input nodes, 3 hidden nodes, and 1 output node
    nn = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)

    # Train the network
    nn.train(X, y, epochs=10000, learning_rate=0.1)

    # Test the trained network
    print("Output after training:")
    print(nn.forward(X))
