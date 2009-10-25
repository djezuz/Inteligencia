class Perceptron:
    def __init__(self, inputs, learning_rate):
        self.inputs = inputs + 1
        self.weights = [0] * self.inputs # The first one is the bias
        self.learning_rate = learning_rate

    def __repr__(self):
        return '<Weights: %s with learning_rate %s>' % \
               (self.weights, self.learning_rate)

    def train(self, training_set):
        """
        Execute the training with all the examples in the training set
        """
        error = 0
        for inputs, target_result in training_set:
            delta = target_result - self.evaluate(inputs)
            self.weights = [weight + self.learning_rate * delta * inp
                            for weight, inp in zip(self.weights, [1] + inputs)]
            error += delta**2
        return error / 2.

    def evaluate(self, inputs):
        """
        Evaluates the output of the perceptron for the given input
        """
        if len(inputs) != (self.inputs - 1):
            raise ValueError("evaluate needs exactly %s inputs" % \
                             (self.inputs - 1))
        inp = [1] + map(int, inputs)
        #return 1 if sum([w * x for w in self.weights for x in inp]) > 0 else -1
        return int(sum([w * x for w, x in zip(self.weights, inp)]) > 0)

def training(perceptron, training_set):
    """
    Trains the perceptron with the given training set over and over until
    the error converge to 0
    """
    it = 0; log = []
    while True:
        log.append(perceptron.train(training_set))
        print 'Iteration %s - Error: %s' % (it, log[it])
        if not log[it]:
            return log
        it += 1

def plot(log):
    """
    A matplotlib way to plot the training log
    """

and_training_set = [
    ([1,1], 1),
    ([1,0], 0),
    ([0,1], 0),
    ([0,0], 0),
]
or_training_set = [
    ([1,1], 1),
    ([1,0], 1),
    ([0,1], 1),
    ([0,0], 0),
]
xor_training_set = [
    ([1,1], 0),
    ([1,0], 1),
    ([0,1], 1),
    ([0,0], 0),
]
if __name__ == '__main__':
    plot(training(Perceptron(2, 0.5), or_training_set))
