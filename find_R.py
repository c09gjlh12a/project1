import csv
import matplotlib.pyplot as plt
import glob;
import os;
import numpy as np

path = "try0117"
doc = glob.glob(f'./{path}/*');


os.makedirs(f'{path}_figure', exist_ok = True);

for i in doc:
    V = [];
    I = [];
    Vi = [];
    Ii = [];
    with open(i, mode = "r", encoding='UTF-8') as csvFile : #開啟檔案
        csvReader = csv.reader(csvFile) #將檔案建立成Reader物件
        for row_list in csvReader:
            # print(row_list)
            if (row_list[0] == "DataValue"):
                try:
                    V_data = float(row_list[1]);
                    I_data = float(row_list[2]);
                except:
                    V_data = 0;
                    I_data = 0;
                Vi.append(V_data);
                Ii.append(I_data);
                try:
                    repeat_index = V.index(V_data);
                    I[repeat_index] = (I[repeat_index] + I_data) / 2;
                except:
                    V.append(V_data);
                    I.append(I_data);
    name = (i.split('\\'))[1].split('.')[0];
    coef = np.polyfit(V,I,1);
    poly1d_fn = np.poly1d(coef)
    plt.subplot(1, 2, 1);
    plt.scatter(Vi, Ii, s = 5);
    plt.title(f'{name} Ii-Vi curve')
    plt.xlabel("Vi")
    plt.ylabel("Ii")
    plt.subplot(1, 2, 2);
    plt.scatter(V, I, s = 5);
    plt.title(f'{name} I-V curve \n R = {coef[0]}')
    plt.xlabel("V")
    plt.ylabel("I")
    plt.plot(V, poly1d_fn(V), '--k')
    plt.savefig(os.path.join(f'{path}_figure', f'{name}.png'));
    plt.close()
