# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:07:04 2022

@author: N
"""
def preorder(i): #前序 i=index
    global nodes
    if i < len(nodes):
        print(nodes[i], end=' ') # 中間 = you
        preorder(2*i) # 左邊
        preorder(2*i+1) #右邊

def inorder(i): #中序
    global nodes
    if i < len(nodes):
        inorder(2*i) #左
        print(nodes[i], end=' ') #印中間
        inorder(2*i+1) #右

def postorder(i): #後序
    global nodes
    if i < len(nodes):
        postorder(2*i) #左
        postorder(2*i+1) #右
        print(nodes[i], end=' ')

nodes = [0,1,2,3,4,5]
#nodes = nodes + input().split()

preorder(1)
nodes = [0,1,2,3,4,5]
print()
inorder(1)
nodes = [0,1,2,3,4,5]
print()
postorder(1)