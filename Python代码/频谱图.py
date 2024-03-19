import numpy as np
import matplotlib.pyplot as plt                     # 导包
from scipy import fft

# 设置原始信号
t = np.linspace(-4*np.pi, 4*np.pi, 1000)      # 仍然保留相同的时域
signal = np.sin(2*t) + np.cos(2*t) + np.cos(4*t)   # 信号仍然使用与上个代码相同的信号

# 对信号进行FFT变换（进行傅里叶变换）
fft_signal = fft.fft(signal)

# 获取信号的频率值
frequency = (np.fft.fftfreq(len(signal))*2*np.pi/min(t))[:len(t)]

# 计算每个频率下的信号幅值
magnitude = 20*np.log(np.abs(fft_signal[:len(t)]))

# 绘制时域图
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.plot(t, signal, label='Original signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Magnitude of the Time Spectrum')
plt.legend(loc='best')

plt.subplot(1, 2, 2)
plt.plot(frequency, magnitude, label='Frequency Spectrum')
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude')
plt.legend(loc='best')

plt.title('Magnitude of the Frequency Spectrum')
plt.savefig('../图片资源/时域图&频谱图.png')
plt.show()
