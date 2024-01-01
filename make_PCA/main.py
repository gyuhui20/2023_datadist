import sys
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.init as init
import torch.optim as optim
import torch.utils.data as utils
import time
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
path = '/Users/gyuhuikwon/Desktop/KHUphy/github/2023_datadist/dataset_2018/data_2018.xlsx'

class ExcelDataset(utils.Dataset):
    def __init__(self, path, variables):
        df = pd.read_excel(path) #(2208,8)
        self.Y = df.values[:,-1] #(2208,1)
        self.Y = LabelEncoder().fit_transform(self.Y) 
        self.X = df[variables].values #(2208,len(variables))
        self.X = self.X.astype('float32')
        
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return (self.X[idx], self.Y[idx])
    
    def prepare_data(self, n_train=0.8, batch_size=10):
        train_size = round(n_train * len(self.X))
        test_size = len(self.X) - train_size
        train_data, test_data = utils.random_split(self, [train_size, test_size])
        train_ld = utils.DataLoader(dataset=train_data, batch_size=batch_size, shuffle=False)
        test_ld = utils.DataLoader(dataset=test_data, batch_size=batch_size, shuffle=False)
        return train_ld, test_ld

class MLR(nn.Module):
    def __init__(self, n_input=6, n_hidden=6, n_output=1):
        super(MLR, self).__init__()
        self.l1 = nn.Linear(n_input, n_hidden)
        init.kaiming_uniform_(self.l1.weight, nonlinearity='relu')
        self.relu1 =  nn.ReLU(inplace=True)
        
        self.l2 = nn.Linear(n_hidden, n_hidden)
        init.kaiming_uniform_(self.l2.weight, nonlinearity='relu')
        self.relu2 =  nn.ReLU(inplace=True)
        
        self.l3 = nn.Linear(n_hidden, n_output)
        init.xavier_uniform_(self.l3.weight)
        self.softmax = nn.Softmax(dim=1)
        
    def forward(self, X):
        X1 = self.l1(X)
        X2 = self.relu1(X1)
        X3 = self.l2(X2)
        X4 = self.relu2(X3)
        X5 = self.l3(X4)
        X6 = self.softmax(X5)
        return X6    

def train_model(train_ld, model):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.0001)
    
    for epoch in range(500):
        for i, (inputs, outputs) in enumerate(train_ld):
            optimizer.zero_grad()
            y_train_pred = model(inputs)
            outputs = outputs.reshape(len(outputs),-1).type(torch.float64)
            loss = criterion(y_train_pred, outputs)
            loss.backward()
            optimizer.step() 

def test_model(test_ld, model): 
    pred_list, act_list = [], []
    for inputs, outputs in test_ld:
        y_test = model(inputs)
        #.detach() : 역전파를 막기 위함
        y_test = y_test.detach().numpy() 
        y_test_pred = np.argmax(y_test, axis=1) 
        y_actual = outputs.numpy()
        
        test = y_test_pred.reshape((len(y_test),1))
        actual = y_actual.reshape((len(y_actual),1))
        
        pred_list.append(test)
        act_list.append(actual)
        
    predictions, actuals = np.vstack(pred_list), np.vstack(act_list)

    acc = accuracy_score(actuals, predictions)
    return f'{acc:.4f}'

def main():
    print("-"*100)
    #print(f"sys.argv[0]: {sys.argv[0]}")
    variables = [sys.argv[1], sys.argv[2]]
    start_time= time.time()
    dataset=ExcelDataset(path, variables)
    train_ld, test_ld = dataset.prepare_data()
    model = MLR(len(variables),6,1)
    train_model(train_ld, model)
    accuracy = test_model(test_ld, model)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"variables: {sys.argv[1]}, {sys.argv[2]}")
    print(f"accuracy: {accuracy}, time: {total_time}")

if __name__ == "__main__":
    main()