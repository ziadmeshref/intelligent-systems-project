import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class DemandPredictor(nn.Module):
    def __init__(self, input_dim=11):
        super(DemandPredictor, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        return out

def evaluate_baselines(y_true, y_last_week, y_moving_avg):
    mae_lw = np.mean(np.abs(y_true - y_last_week))
    mae_ma = np.mean(np.abs(y_true - y_moving_avg))
    return {"last_week_mae": mae_lw, "moving_avg_mae": mae_ma}
