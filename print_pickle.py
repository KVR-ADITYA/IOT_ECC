import os
import pickle
from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt

curve_list = ["brainpoolP192r1", "brainpoolP160r1", "brainpoolP224r1",  "brainpoolP256r1", "brainpoolP320r1", "brainpoolP384r1", "brainpoolP512r1", "secp192r1", "secp224r1", "secp256r1", "secp384r1", "secp521r1"]

mean_dict = {}
full_dict = {}

for i in curve_list:
    time_lst = pickle.load(open(f'./{i}.pickle','rb'))
    mean_dict[i] = mean(time_lst)
    full_dict[i] = time_lst

print(mean_dict)

df = pd.DataFrame(full_dict)
df.plot()
plt.show()