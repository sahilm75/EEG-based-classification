import matplotlib.pyplot as plt
import numpy as np

t1 = 44.3
x1 = np.linspace(0, 5 , 5)
y1 = np.array([142 , 10, 10, 10 ,10])

# Lambda = 0.5
t2 = 2.67
x2 = np.linspace(0, 5 , 5)
y2 = np.array([142 , 14, 14, 14 ,14])


# Lambda = 2
t3 = 1.8
x3 = np.linspace(0, 5 , 5)
y3 = np.array([142 , 20, 20, 20 ,20])

# Lambda = 10
t4 = 2
x4 = np.linspace(0, 5 , 5)
y4 = np.array([142 , 33, 33, 33 ,33])

# Lambda = 0.05
t5 = 3
x5 = np.linspace(0, 5 , 5)
y5 = np.array([142 , 10, 10, 10 ,10])


plt.plot(x1,y1, marker = 'x', label = 'Laplacian Prior (Time taken = 44.3s)')
plt.plot(x5,y5 ,  marker = 'x', label = 'Gaussian Prior, lambda = 0.05  (Time taken = 3s)')
plt.plot(x2,y2, marker = 'x', label = 'Gaussian Prior, lambda = 0.5 (Time taken = 2s)')
plt.plot(x3,y3 ,  marker = 'x', label = 'Gaussian Prior, lambda = 2(Time taken = 2s)')
plt.plot(x4,y4 ,  marker = 'x', label = 'Gaussian Prior, lambda = 10 (Time taken = 2s)')
plt.xlabel('Iterations')
plt.ylabel('Mean Squared Error')
plt.title('Different prior for unknown inputs')
plt.legend()
plt.savefig('Different_priors.png')
