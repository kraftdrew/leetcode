from typing import Optional, List, Dict


class ListNode:
    def __init__(self, value = 0, next: Optional['ListNode'] = None): 
        self.value = value
        self.next = next 



class NodeGenerator: 

    def __init__(self, n : int = 1): 
        self.n = n
        self.node_list = []
        self.generate_node()

    def generate_node(self):

        for i in range(self.n): 

            new_node = ListNode(i + 1) 

            self.node_list.append(new_node)

            if i > 0:
                self.node_list[i-1].next = new_node

        return
    
    def print_nodes(self): 
        current = self.node_list[0] if self.node_list else None 

        while current: 
            print(current.value, end= " -> " if current.next else '\n' )
            current = current.next

      


            

graph5 = NodeGenerator(5)   
graph5.print_nodes()      






# head = ListNode(1)

# second_node = ListNode(2)
# head.next = second_node