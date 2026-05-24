# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def converter_lista(no_atual):
            lista = []

            while no_atual:
                lista.append(no_atual.val)
                no_atual = no_atual.next

            return lista

        # Converte a lista normal em número inteiro
        def lista_numero(lista):
            lista_invertida = lista[::-1]

            texto = ''.join(str(numero) for numero in lista_invertida)

            return int(texto)

        # Converte o número da soma de volta para lista vinculada
        def numero_para_lista_vinculada(numero):
            texto = str(numero)[::-1]

            no_falso = ListNode(0)
            no_atual = no_falso

            for digito in texto:
                no_atual.next = ListNode(int(digito))
                no_atual = no_atual.next

            return no_falso.next

        lista_l1 = converter_lista(l1)
        lista_l2 = converter_lista(l2)

        numero_l1 = lista_numero(lista_l1)
        numero_l2 = lista_numero(lista_l2)

        soma = numero_l1 + numero_l2

        resultado = numero_para_lista_vinculada(soma)

        return resultado    
        

        