#写一个简单的UI代码，要求运行起来就出现UI，有一个x可以退出UI，中间有个按钮「开始游戏」。
import tkinter as tk
from tkinter import messagebox

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("游戏界面")

        # 创建开始游戏的按钮
        self.start_button = tk.Button(self.root, text="开始游戏", command=self.start_game)
        self.start_button.pack(pady=20)

    def start_game(self):
        messagebox.showinfo("游戏开始", "游戏开始了！")

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

# 写一个冒泡排序算法的代码，要求运行起来就完成排序，排序结果是倒序的.、
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
