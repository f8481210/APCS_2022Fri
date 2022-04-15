class Node:
    def __init__(self ,data=None, next=None):
        self.data = data
        self.next = next #指向下一個 = 指標 
        
class SingleLinkedList:
    def __init__(self):
        self.head = None #頭 起點 
        self.tail = None #尾巴 終點

        #append 從tail新增資料
        def append(self, data):
            #建立一個新節點 new node
            new_node = Node(data)
            # 如果head == None 代表為第一個Node
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = self.tail.next
        
        #delete 從頭刪除
        #delete 從尾巴刪除
        #delete 找特定刪除
        def delete(self): #從尾巴刪除
            if self.head == None:
                return print("This list is empty")
            else:
                if len(self) == 1: #如果linklist裡只有一筆資料
                    self.head = None #把頭刪除 = 沒東西
                else: #利用current_node來尋找倒數第二筆資料
                    current_node = self.head
                    while current_node.next != None:
                        self.tail = current_node
                        current_node = current_node.next
                    self.tail.next = None