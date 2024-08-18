INITIAL_PLAYBOOK = """
Olá: Execute as etapas abaixo.
1 - Leia a user story ao final deste texto.
2 - Leia e entenda o código Python fornecido.
3 - Determine se o código é novo, modificado ou deletado.
4 - Com base na user story e no código Python, escreva um relatório sobre o código Python.

Instruções:
- Evite usar partes específicas do código no relatório.
- Não é necessário explicar imports, bibliotecas e frameworks utilizados.
- Evite descrições óbvias, como a adição de métodos ou funções.
- Explique detalhadamente como os cálculos, transformações de dados e lógicas de negócios foram implementados.
- Descreva o impacto do código no processo geral e como ele contribui para a user story.
- Detalhe o resultado final esperado ao executar o código, como atualizações em tabelas, retornos de relatórios ou outros outputs.
- Inclua uma lista clara e categorizada de todos os arquivos criados, modificados ou deletados.
- Foco nas intenções de negócios e como o código atende a essas intenções.
"""


FINAL_PLAYBOOK = """
Olá: Execute as etapas abaixo.
1 - Leia a user story ao final deste texto.
2 - Leia e entenda os relatórios fornecidos como input.
3 - Com base na user story e nos relatórios de input, escreva um relatório final consolidado.

Instruções:
- Utilize uma linguagem simples, objetiva e de nível corporativo.
- Escreva para um público que entende do processo de negócios, mas que pode não ter familiaridade com detalhes de programação.
- Não é necessário mencionar bibliotecas, frameworks ou importações técnicas.
- Evite justificativas de porque o relatório é importante; foque em explicar o que foi feito e o impacto nos negócios.
- Estruture o relatório da seguinte maneira:
    - **Regras de Negócio:** Resuma as regras de negócio relevantes diretamente da user story.
    - **O que e como foi feito:** Descreva as principais alterações e adições no código, explicando as motivações e a lógica por trás delas.
    - **Dinâmica dos cálculos e transformações:** Explique como os cálculos e transformações de dados foram realizados e como eles contribuem para o resultado final.
    - **Filtros aplicáveis (se houver):** Identifique quaisquer filtros ou condições usados no código que impactam os dados ou resultados.
    - **Resultado final esperado:** Explique claramente o que o código deve produzir ao ser executado, como atualizações em sistemas, relatórios ou outros outputs.
    - **Arquivos modificados, criados ou excluídos:** Liste os arquivos de forma categorizada, indicando o que foi modificado, criado ou deletado.
"""
