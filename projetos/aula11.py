# Precedencia - Ordem de Efetivação
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 # Objetivo era 1024 mas por causa da "Ordem de Efetivação" fica 7
conta_certa = (1 + 1) ** (5 + 5)
conta_certa2 = (1 + int(0.5 + 0.5)) ** (5+5)
print(conta_1)
print(conta_certa)
print(conta_certa2)