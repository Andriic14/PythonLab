import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,7,100)
y = 5 * np.sin(10*x) *np.sin(3*x)/np.sqrt(x)# Обчислюємо значення функції
plt.plot(x,y,label='Y(x) = 5·sin(10x)·sin(3x)/(x^(1/2)))',color='red', linewidth=2,)# графік
plt.title('Графік функції Y(x) = 5·sin(10x)·sin(3x)/(x^(1/2))',fontsize=15) # назва графіка
plt.xlabel('x', fontsize=15,color='blue')
plt.ylabel('y', fontsize=15,color='blue')
plt.legend(fontsize=12)
plt.grid(True)
plt.show()