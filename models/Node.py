class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
    
    def get_item(self): #item 
        return self.item
    
    def get_ref(self): #referencia do apontador 
        return self.ref