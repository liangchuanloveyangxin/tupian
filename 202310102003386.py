"""
Author:  余婷
Create Time: 2023/10/10 16:58
软件： PyCharm
你只管努力，时间会给你惊喜！
"""

print(f'test2中的__name__:{__name__}')


def download_movie(name):
    print(f'---------{name}开始下载---------')
    print('对电影的链接发送请求')
    print('接受服务器返回的数据')
    print('将数据保存到本地文件中')
    print(f'----------{name}下载结束--------')


if __name__ == '__main__':
    names = ['肖申克的救赎', '霸王别姬', '阿甘正传', '触不可及', '恐怖游轮', '蝴蝶效应']
    for x in names:
        download_movie(x)

