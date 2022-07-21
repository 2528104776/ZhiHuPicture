import os

''' 
注意运行前使用CTRL+A 重名名一下，然后启动此程序
'''

path = "/storage/emulated/0/知乎图片/"
# 获取该目录下所有文件，存入列表中
file = os.listdir(path)
try:

    for index,i in enumerate(file,start = 0):
        # 设置旧文件名（就是路径+文件名）
        oldname = file[index]
        # 设置新文件名
        newname = str(index) + '.jpg'
        # 用os模块中的rename方法对文件改名
        os.rename(path+oldname, path+newname)
        print(oldname, '======>', newname)
except BaseException as B:
    print(B)

