import numpy as np
x=np.linspace(1,100,100)
A=np.square(np.reshape(x,(10,10)))
div3=A[A%3==0]