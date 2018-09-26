# _*_ coding:utf-8 _*_
import os
print(os.getcwd()) #查看当前所在路径  D:\python\learn_p\python基础\基本模块
print(os.listdir(os.getcwd())) #列举目录下的所有文件。返回的是列表类型  ['os模块.py']
print(os.path.abspath('.'))# 返回path的绝对路径。
print(os.path.split(r'D:\python\learn_p\python基础\基本模块\os模块.py'))
#返回元组类型，将路径和文件分开('D:\\python\\learn_p\\python基础\\基本模块', 'os模块.py')
print(os.path.dirname(r'D:\python\learn_p\python基础\基本模块\os模块.py'))#当前文件的文件夹路径 D:\python\learn_p\python基础\基本模块
print(os.path.basename(r'D:\python\learn_p\python基础\基本模块\os模块.py'))#文件名称   os模块.py
print(os.listdir(r'D:\python\learn_p\python基础\多线程'))