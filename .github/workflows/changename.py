import glob
import os

path = "try0118"
doc = glob.glob(f'./{path}/*');

for i in doc:
    skip=0;
    try:
        num1 = i.index("[");
        num2 = i.index("(");
    except:
        skip=1;
        pass
    if (skip==0):
        try:
            os.rename(i, f'./{path}/{i[num1+1:num2]}.csv');
        except:
            os.remove(i);
    
