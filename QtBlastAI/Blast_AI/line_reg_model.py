import numpy as np
import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout

class Reg():
    def __init__(self):
        self.rng = np.random
        self.W = tf.Variable(self.rng.randn(), name='weight')
        self.b = tf.Variable(self.rng.randn(), name='bias')
        self.X = []
        self.Y = []
        self.learning_rate = 0.01
        self.train_step = 20001
        self.disp_step = 5000
        self.optim = tf.optimizers.SGD(self.learning_rate)

    def setXY(self,x,y):
        self.X = x
        self.Y = y
        
        print('W = ',self.W.numpy())
        print('b = ',self.b.numpy())
        # print('X = ',self.X)
        # print('Y = ',self.Y)

    def line_reg(self,x):
        return self.W*x + self.b

    def mse(self, y_pred, y_true):
        return tf.reduce_sum(tf.pow(y_pred-y_true,2))/(2*y_pred.shape[0])

    def run_optim(self):
        with tf.GradientTape() as g:
            pred = self.line_reg(self.X)
            loss = self.mse(pred,self.Y)
            # print(f'pred={pred}, loss={loss}')
            # print(f'loss={loss}')
        grad = g.gradient(loss,[self.W,self.b])
        self.optim.apply_gradients(zip(grad,[self.W,self.b]))

    def train(self):
        for step in range(1,self.train_step+1):
            self.run_optim()
            # if(step>5):
            #     exit()
            if step % self.disp_step == 0:
                pred = self.line_reg(self.X)
                loss = self.mse(pred,self.Y)
                
                print(f'step = {step}, loss =  {loss},W =  {self.W.numpy()}, b =  {self.b.numpy()}')
        return pred
