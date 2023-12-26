                                                                              
import numpy as np
import struct
import matplotlib.pyplot as plt

#define activation function                                                                            
def tanh(x):
    return np.tanh(x)

def sigmoid(x):
    return 1.0 / (1 + np.exp(-1.0*x))

def RELU(x):
    return np.maximum(0,x)
# def LEAKRELU(x):
#     return x if x.any()>=0 else 0.1*x
def RELU3(x):
    return np.multiply(np.multiply(RELU(x),RELU(x)),RELU(x))

#define the derivation of activation function                                                                                 
def tanh_deriv(x):
    return 1.0 - np.multiply(tanh(x),tanh(x))

def sigmoid_deriv(x):
    return np.multiply(1.0 - sigmoid(x), sigmoid(x))

def RELU_deriv(x):
    return (x>=0)
def LEAKRELU_deriv(x):
    return 1 if x>=0 else 0.1
    # return 0.1*(x>=0)
def RELU3_deriv(x):
    return 3.0 * np.multiply(RELU(x),RELU(x))

#Construct Neural Networks
class NeuralNetwork:
    def __init__(self, layers, activation, opt_alg):
        """
        layers: layers of NNs
        Activation:activation function
        opt_alg:optimization algorithm
        """
        if activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv
        elif activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_deriv = sigmoid_deriv
        elif activation == 'RELU':
            self.activation = RELU
            self.activation_deriv = RELU_deriv
        # elif activation == 'LEAKRELU':
        #     self.activation = LEAKRELU
        #     self.activation_deriv = LEAKRELU_deriv
        elif activation == 'RELU3':
            self.activation_deriv = RELU3_deriv

        if opt_alg == 'GD':
            self.opt = self.GD
        elif opt_alg == 'SGD':
            self.opt = self.SGD
        elif opt_alg == 'ADAM':
            self.opt = self.ADAM
            #initial parameters of ADAM
            self.mw = []
            self.mtheta = []
            self.vw = []
            self.vtheta = []
            for i in range(len(layers)-1):
                self.mw.append(np.zeros((layers[i+1], layers[i])))
                self.mtheta.append(np.zeros(layers[i+1]))
                self.mtheta[i] = np.mat(self.mtheta[i]).T

            for i in range(len(layers)-1):
                self.vw.append(np.zeros((layers[i+1], layers[i])))
                self.vtheta.append(np.zeros(layers[i+1]))
                self.vtheta[i] = np.mat(self.vtheta[i]).T
            

    #initial weights and thetas
        self.weights = []
        self.thetas = []
    #range in -1 to 1
        for i in range(len(layers)-1):
            self.weights.append(2*(np.random.rand(layers[i+1], layers[i]))-1)
            self.thetas.append(2*(np.random.random(layers[i+1]))-1)
            self.thetas[i] = np.mat(self.thetas[i]).T
        self.layers = layers
    
    def propagation(self, x, k):
        """
        Compute the propagation
        x:input
        return: output
        """
        temp = x
        for i in range(len(self.weights)):
            temp =self.activation(np.dot(self.weights[i],temp) + self.thetas[i])
        z = k * temp
        return z

    def backpropagation(self, x, error):
        """
        Compute the back propagation
        x:input
        return: back propagation
        K:output of each layer
        Delta:the propagation of each layer
        """
        n_w = len(self.weights)
        z = []
        K = []
        dweights = []
        dthetas = []
        delta = []

        for i in range(n_w):
            if i == 0:
                z.append(np.dot(self.weights[i], x) + self.thetas[i])
                K.append(x)
                delta.append(x)
            else:
                z.append(np.dot(self.weights[i], self.activation(z[i-1])) + self.thetas[i])
                K.append(self.activation(z[i-1]))
                delta.append(self.activation(z[i-1]))
            # print("-----delta0------")
            # print(delta[i])

        for i in range(n_w-1, -1, -1):
            if i == n_w-1:
                delta[i] = np.multiply(error, self.activation_deriv(z[i]))
            else:
                delta[i] = np.multiply(np.dot(self.weights[i+1].T, delta[i+1]), self.activation_deriv(z[i]))
                
            # print("-----delta1------")
            # print(delta[i])
            # print(self.weights[i+1])
            # print(self.activation_deriv(z[i]))

        for i in range(n_w):
            dweights.append(np.dot(delta[i], K[i].T))
            dthetas.append(delta[i])
        return dweights, dthetas

    def GD(self, X, Y, k, learning_rate, epochs): 
        """
        Gradient Decent method
        X:input
        y:target
        """
        perf = 0
        ddweights = []
        ddthetas = []
        layers = self.layers
        for i in range(len(layers)-1):
            ddweights.append(np.zeros((layers[i+1], layers[i])))
            ddthetas.append(np.zeros(layers[i+1]))
            ddthetas[i] = np.mat(ddthetas[i]).T    

        for j in range(int(X.shape[1])):
            input = np.mat(X[:,j]).T
            output = self.propagation(input, k)
            y = np.mat(Y[:,j]).T
            error = y - output
            perf += 1.0/2 * np.sum(np.multiply(error, error))
            
            dweights, dthetas = self.backpropagation(input, error)
            for i in range(len(self.weights)):
                ddweights[i] += k * 1.0/len(X)*learning_rate * dweights[i]
                ddthetas[i] += k * 1.0/len(X)*learning_rate * dthetas[i]
                self.weights[i] += k * 1.0*learning_rate * dweights[i]
                self.thetas[i] += k * 1.0*learning_rate * dthetas[i]
        
        for i in range(len(self.weights)):
            self.weights[i] += ddweights[i]
            self.thetas[i] += ddthetas[i]
        return perf

    def SGD(self, X, Y, k, learning_rate, epochs):
        perf = 0
        ddweights = []
        ddthetas = []
        layers = self.layers
        for i in range(len(layers)-1):
            ddweights.append(np.zeros((layers[i+1], layers[i])))
            ddthetas.append(np.zeros(layers[i+1]))
            ddthetas[i] = np.mat(ddthetas[i]).T 

        rand_X = np.arange(X.shape[1])
        np.random.shuffle(rand_X)
        n = int(X.shape[1]/100)
        for j in range(n):
            input = np.mat(X[:,rand_X[j]]).T
            output = self.propagation(input, k)
            y = np.mat(Y[:,rand_X[j]]).T
            error = y - output
            perf += 1.0/2 * np.sum(np.multiply(error, error))
            dweights, dthetas = self.backpropagation(input, error)
            for i in range(len(self.weights)):
                ddweights[i] += k * 1.0/n*learning_rate * dweights[i]
                ddthetas[i] += k * 1.0/n*learning_rate * dthetas[i]

        for i in range(len(self.weights)):
            self.weights[i] += ddweights[i]
            self.thetas[i] += ddthetas[i]
        return perf

    def ADAM(self, X, Y, k, learning_rate , epochs):
        perf = 0
        layers = self.layers
        #initial parameters
        beta2 = 0.999                                                                                         
        beta1 = 0.9
        epsilon = 0.00000001    
        ddweights = []
        ddthetas = []
        for i in range(len(layers)-1):
            ddweights.append(np.zeros((layers[i+1], layers[i])))
            ddthetas.append(np.zeros(layers[i+1]))
            ddthetas[i] = np.mat(ddthetas[i]).T                                                                
        rand_X = np.arange(X.shape[1])
        np.random.shuffle(rand_X)
        n = int(X.shape[1]/10)
        for j in range(n):
            input = np.mat(X[:,rand_X[j]]).T
            output = self.propagation(input, k)
            y = np.mat(Y[:,rand_X[j]]).T
            error = y - output
            perf += 1.0/2 * np.sum(np.multiply(error, error))
           
            dweights, dthetas = self.backpropagation(input, error)
            for i in range(len(self.weights)):
                ddweights[i] += k * 1.0/n * dweights[i]
                ddthetas[i] += k * 1.0/n * dthetas[i]

        for j in range(len(self.weights)):
            self.mw[j] = beta1*self.mw[j] + (1-beta1)*ddweights[j]
            self.vw[j] = beta2*self.vw[j] + (1-beta2)*np.multiply(ddweights[j],ddweights[j])
            self.mtheta[j] = beta1*self.mtheta[j] + (1-beta1)*ddthetas[j]
            self.vtheta[j] = beta2*self.vtheta[j] + (1-beta2)*np.multiply(ddthetas[j],ddthetas[j])
            mwHat = self.mw[j]/(1 - beta1**epochs)
            vwHat = self.vw[j]/(1 - beta2**epochs)
            mtHat = self.mtheta[j] / (1-beta1**epochs)
            vtHat = self.vtheta[j] / (1-beta2**epochs)
            self.weights[j] += learning_rate * np.multiply(mwHat, 1.0/(np.sqrt(vwHat) + epsilon))
            self.thetas[j] += learning_rate * np.multiply(mtHat, 1.0/(np.sqrt(vtHat) + epsilon)) 
        return perf


    def fit(self, X, Y, k, learning_rate, epochs,draw_x,draw_y):
        """
        Training NNs
        X:input data
        Y:target data
        learning_rate
        epochs
        """
        for i in range(epochs):
            
            perf = self.opt(X, Y, k, learning_rate, i+1)
            predict = self.propagation(X, 1)
            true = np.sum(np.argmax(Y,0) == np.argmax(predict,0))
            # print(self.weights)
            # print(np.argmax(Y,0) )
            # print(np.argmax(predict,0))
            # print(np.argmax(Y,0) == np.argmax(predict,0))
            print('perf:', perf, 'epochs:', i, "predict_true:", true, "precision:", 1.0*true/Y.shape[1])
            draw_x.append(i)
            draw_y.append(1.0*true/Y.shape[1])
        
if __name__ == "__main__":
    
    #get input data
    num = 5000 
    filename = 'files\\t10k-images-idx3-ubyte'
    binfile = open(filename , 'rb')
    buf = binfile.read()
 
    index = 0
    X = np.zeros((784, num))

    magic, numImages , numRows , numColumns = struct.unpack_from('>IIII' , buf , index)
    index += struct.calcsize('>IIII')
    for i in range(num): 
        X[:,i] = struct.unpack_from('>784B' ,buf, index)
        index += struct.calcsize('>784B')
    X = np.array(X)

    testX = np.zeros((784, 6000-num))
    for i in range(6000-num): 
        testX[:,i] = struct.unpack_from('>784B' ,buf, index)
        index += struct.calcsize('>784B')
    testX = np.array(testX)


    # im = X[:,10].reshape(28,28)
 
    # fig = plt.figure()
    # plotwindow = fig.add_subplot(111)
    # plt.imshow(im,cmap = 'gray')
    # plt.show()

    #get target data
    filename_tar = 'files\\t10k-labels-idx1-ubyte'
    binfile_tar = open(filename_tar, 'rb')
    buf_tar = binfile_tar.read()

    index_tar = 8
    Y = np.zeros((10,num))
    magic, numImages , numRows , numColumns = struct.unpack_from('>IIII' , buf_tar , index_tar)
    # index_tar += struct.calcsize('>IIII')
    # print(struct.calcsize('>IIII'))

    for i in range(num):
        k = struct.unpack_from('>1B' ,buf_tar, index_tar)
        Y[k][i] = 1 
        index_tar += struct.calcsize('>1B')
    Y = np.array(Y)
    # print("------Y--------")
    # print(Y[:,10])


    testY = np.zeros((10,6000-num))
    for i in range(6000-num):
        k = struct.unpack_from('>1B' ,buf_tar, index_tar)
        testY[k][i] = 1 
        index_tar += struct.calcsize('>1B')
    testY = np.array(testY)

    #get layers
    layers = np.array([X.shape[0],128,28, Y.shape[0]])
    # print(X.shape[0],28, Y.shape[0])
    active_func = "sigmoid"
    opt = "ADAM"
    Net = NeuralNetwork(layers,activation=active_func,opt_alg=opt)
    """
    initial NNs
    activation function:sigmoid tanh RELU RELU3
    optalg:ADAM GD SGD
    """
    xx = [] ; yy = []

    epoch = 1000
    lr = 0.005
    Net.fit(X,Y,1,lr,epoch,draw_x=xx,draw_y=yy)
    
    output = Net.propagation(testX,1)
    true = np.sum(np.argmax(testY,0) == np.argmax(output,0))
    print(true)
    print("accuracy:",true/(6000-num))

    plt.plot(xx,yy)
    plt.title("Precision after {} epoch,with {} and {}\n lr = {} and layers={}".format(epoch,active_func,opt,lr,layers))
    plt.xlabel("epoch")
    plt.ylabel("Presision")
    plt.show()