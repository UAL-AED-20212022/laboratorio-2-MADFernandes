from re import X
from models.LinkedList import LinkedList
from models.Node import Node


def main():

    lista_ligada = LinkedList()
    while True:

        comandos = input().split(" ")

        if comandos[0] == "RPI":
            lista_ligada.insert_at_start(comandos[1]) 
        
        elif comandos[0] == "RPF":
            lista_ligada.insert_at_end(comandos[1])

        elif comandos[0] == "RPDE":
            lista_ligada.insert_after_item(comandos[2], comandos[1])

        elif comandos[0] == "RPAE":
            lista_ligada.insert_before_item(comandos[2], comandos[1])

        elif comandos[0] == "RPII":
            lista_ligada.insert_at_index(int(comandos[2]), comandos[1])
#Verificar Nr de elementos na Lista
        elif comandos[0] == "VNE":
            print(f"O número de elementos são {lista_ligada.get_count()}.")

#Verificar pais na lista
        elif comandos[0] == "VP":
            if lista_ligada.search_item(comandos[1]) is False:  # Atenção saída com insucesso.
                print(f"O país {comandos[1]} não se encontra na lista.")
            else:
                print(f"O país {comandos[1]} encontra-se na lista.")

#Eliminar Primeiro elemento da lista
        elif comandos[0] == "EPE":
            lista_ligada.delete_at_start(lista_ligada)
            print(f"O país {lista_ligada} foi eliminado da lista.")

#Eliminar ultimo elemento da lista
        elif comandos[0] == "EUE":
            x = lista_ligada.get_last_node()
            lista_ligada.delete_at_end()
            print(f"O país {X} foi eliminado da lista.")

#Eliminar elemento da lista (Escolhido)
        elif comandos[0] == "EP":
            lista_ligada.delete_element_by_value(comandos[1])
            print(f"O país {lista_ligada} foi eliminado da lista.")

        else:
            if comandos[0] == "":
                break
        
        lista_ligada.traverse_list()
        
