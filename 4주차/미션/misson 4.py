import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

#사용 마커는 다음과 같습니다. red dashes, blue squares, green triangles
plt.plot(t, color="r", linestyle="dashed") #선형대수
plt.plot(t**2, "bs") #2차함수
plt.plot(t**3, "g^") #3차함수

plt.show()