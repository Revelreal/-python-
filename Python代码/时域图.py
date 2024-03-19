import numpy as np
import matplotlib.pyplot as plt  # 导包numpy和pyplot

t = np.linspace(-4 * np.pi, 4 * np.pi, 1000)  # 设置时间域为( -2*pi 到 2*pi )，取1000步以防图像过于尖锐
signal = np.cos(2 * t) + np.cos(4 * t) + np.sin(2 * t)  # 设置我们想要显示的信号函数

plt.plot(t, signal)  # 设置显示信号函数，将参数传入

plt.grid(axis="x")  # 添加x轴网格
plt.grid(axis="y")  # 添加y轴网格

if __name__ == "__main__":

    choice = input("是否需要自定义图片保存路径？(Y/N):")

    if choice == "Y":

        while 1:
            try:
                path = input("请输入您的路径:")
                path = path.replace("\\", "/")
                plt.savefig(path)
                break
            except Exception as e:
                print("路径错误，请重新输入")
    else:
        path = r"..\图片资源\时域图2.png"  # 保存图片到指定path(这里没写try和expect逻辑，所以需要自己手动建一个名字叫做图片资源的文件夹)
        path = path.replace("\\", "/")
        plt.savefig(path)
    plt.show()
