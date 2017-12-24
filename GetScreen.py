'''
Date        :   2017/12/24
Author      :   ChangHe
Describe    :   获取当前屏幕的所有内容
'''

from PIL import ImageGrab

class CGetScreenTools:
    #截屏工具类
    
    #实例变量

    #静态变量

    #实例方法
    def __init__(self):
        #初始化函数
        pass

    #静态方法
    




im = ImageGrab.grab()

im.save("teat.jpg",'jpeg')