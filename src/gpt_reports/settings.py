INITIAL_PLAYBOOK = """
Olá: Exectue as etapas abaixo.
1 - Leia a user story ao final deste texto
2 - Leia e entenda este código python
3 - Com base no input, determine se é um código novo, modificado ou deletado.
4 - Com base na User Story e no código python, escreva um relatório sobre o código python.

Instruções:
Não use partes do código para exemplificar. 
Não é necessário explicar imports, bibliotecas e frameworks utilizados.
Não é necessário informar que foram inserido métodos.
Explique a dinânica dos cálculos e transformações aplicadas nos datasets.
Explique o resultado final esperado ao executar o código, como por exemplo cargas de tabelas ou 
o retorno do relatório a ser consumido.
O relatório deve conter a lista com todos os arquivos criados, modificados ou deletados, categorizados."""

FINAL_PLAYBOOK = """
Olá: Exectue as etapas abaixo.
1 - Leia a user story ao final deste texto.
2 - Leia e entenda os relatórios do input.
3 - Com base no input e na user story, escreva um relatório resumido combinando os relatórios do input

Instruções:
Utilize uma linguagem simplificada, objetiva e de nível coorporativo. 
Escreva o relatório para uma pessoa que entende do processo como um todo, mas que não necessáriamente
entenda de programação.
Não é necessário falar sobre bibliotecas, uso de frameworks ou de importações.
Não é necessário explicar do que se trata o relatório ou o porque o relatório é imporante ou não.
O relatório final deve estar na seguinte estrutura de tópicos: 
    - Regras de Negócio (está na user story)
    - O que e como foi feito
    - Dinâmica dos cálculos e transformações de todos os inputs
    - Quais filtros podem ser utilizados (Se houver, caso não haja não é necessário incluir o tópico)
    - Resultado final esperado
    - Arquivos modificados, criados ou excluídos, categorizados.
"""
