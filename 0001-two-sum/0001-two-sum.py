class Solution:
    # Cria a função que o LeetCode vai chamar.
    # nums é a lista de números.
    # target é o número que queremos formar com uma soma.
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Primeiro loop.
        # O i representa o índice do primeiro número.
        for i in range(len(nums)):

            # Segundo loop.
            # O j representa o índice do segundo número.
            # Ele começa em i + 1 para não repetir o mesmo elemento.
            for j in range(i + 1, len(nums)):

                # Verifica se o número da posição i
                # somado com o número da posição j
                # é igual ao target.
                if nums[i] + nums[j] == target:

                    # Se encontrou a soma certa,
                    # retorna os dois índices.
                    return [i, j]