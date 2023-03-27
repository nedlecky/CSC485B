import torch
import torch.nn as nn
from torch.autograd import Variable
import pdb
import numpy as np
from PreProcessing import PreprocessData

# Set Seeds For Randomness
torch.manual_seed(10)
np.random.seed(10)    
InputSize = 6  # Input Size
batch_size = 1 # Batch Size Of Neural Network (original=1)
NumClasses = 1 # Output Size 

############################################# FOR STUDENTS #####################################

# [Ned Lecky] What's a good number?
NumEpochs = 25 # Original was 25

# [Ned Lecky] Might want to expand this
HiddenSize = 10
# 10: Their original... but when I retrain, goes in circles 
# 20: Loss stays at nan
# 50: Loss stays at nan

# Create The Neural Network Model
class Net(nn.Module):
    def __init__(self, InputSize, NumClasses):
        super(Net, self).__init__()
		###### Define The Feed Forward Layers Here! ######
        # [Ned Lecky] Added network design below
        self.fc1 = nn.Linear(InputSize, HiddenSize)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(HiddenSize, NumClasses)
        
    def forward(self, x):
		###### Write Steps For Forward Pass Here! ######
        # [Ned Lecky] Added design below
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

net = Net(InputSize, NumClasses)     

###### Define The Loss Function Here! ######
criterion = nn.MSELoss() # [Ned Lecky]
###### Define The Optimizer Here! ######
optimizer = torch.optim.SGD(net.parameters(), lr=0.01) # [Ned Lecky]

##################################################################################################

if __name__ == "__main__":
        
    TrainSize,SensorNNData,SensorNNLabels = PreprocessData()   
    for j in range(NumEpochs):
        losses = 0
        for i in range(TrainSize):  
            input_values = Variable(SensorNNData[i])
            labels = Variable(SensorNNLabels[i])
            # Forward + Backward + Optimize
            optimizer.zero_grad()
            outputs = net(input_values)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            losses += loss.item()
            
        print ('Epoch %d, Loss: %.4f' %(j+1, losses/SensorNNData.shape[0]))       
        torch.save(net.state_dict(), './SavedNets/NNBot.pkl')
           
        


