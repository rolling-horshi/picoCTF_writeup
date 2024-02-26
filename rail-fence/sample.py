import pandas as pd
import numpy as np



txt = "Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6"
N = 4

txt_len = len(txt)

df = pd.DataFrame(np.zeros((N,txt_len)))
df[:] = np.nan

txt_l = txt.split(" ")

for i in range(txt_len):
    a1 = i % (2*(N-1))

    a2 =  -(N - 1) + (a1)
    if(a2 < 0):
        a2 = -a2
    a3 = (N-1) -a2
    df.iat[a3,i] = 0



t = 0
for i in range(N):
    for j in range(txt_len):
        if(df.iat[i,j] == 0):
            df.iat[i,j] = txt[t]
            t += 1

        if(t>=txt_len):
            break
            

flag = ""

for i in range(txt_len):
    a1 = i % (2*(N-1))

    a2 =  -(N - 1) + (a1)
    if(a2 < 0):
        a2 = -a2
    a3 = (N-1) -a2
    flag += df.iat[a3,i]

print(flag)
