from tensorflow import keras

class Model:
    def __init__(self, input_shape, learning_rate):
        self.input_shape = input_shape
        self.learning_rate = learning_rate
        
    def __call__(self, n_hidden, n_neurons, dropout):
        
        input_shape = self.input_shape
        learning_rate = self.learning_rate
        
        print( "Building model with:" )
        print( "Input shape: {}".format(input_shape) )
        print( "Learning rate: {}".format(learning_rate) )
        print( "Number of hidden layers: {}".format(n_hidden) )
        print( "Number of neurons per layer: {}".format(n_neurons) )
        print( "Dropout rate: {}".format(dropout) )
        
        model = keras.models.Sequential()
        model.add( keras.layers.InputLayer(input_shape=input_shape) )
        for layer in range(n_hidden):
            if dropout > 0.:
                model.add( keras.layers.Dropout(rate=dropout) )
            model.add( keras.layers.Dense(n_neurons, activation="elu", kernel_initializer="he_normal") )
        if dropout > 0.:
            model.add( keras.layers.Dropout(rate=dropout) )    
        model.add( keras.layers.Dense(1, activation="sigmoid") )
        
        #optimizer = keras.optimizers.SGD(lr=learning_rate, momentum=0.9, nesterov=True)
        optimizer = keras.optimizers.Nadam(lr=learning_rate)
        model.compile( loss="binary_crossentropy", optimizer=optimizer, metrics=["accuracy"])
        
        return model

def build_model(input_shape, learning_rate=5e-4, n_hidden=1, n_neurons=50, dropout=0.20 ):
    build_fn_ = Model( input_shape=input_shape, learning_rate=learning_rate )
    return build_fn_( n_hidden, n_neurons, dropout )
    