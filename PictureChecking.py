import imghdr
import os
root = '/storage/emulated/0/知乎图片'
path_list = os.listdir(root)

bed_times = 0
def is_verify(path):
    global bed_times
    if imghdr.what(path):
        print('Good img')
    else:
        bed_times += 1
        os.remove(path)
        print('图片已损坏,删除！')

if __name__=='__main__':
    for path in path_list:
        is_verify(root+'/' + path)
    print(f'总计删除损坏文件{bed_times}个.')
