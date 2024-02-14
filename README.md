# Desafio Tunts.Rocks 2024

Programa desenvolvido no desafio técnico Tunts.Rocks, como parte do processo seletivo da empresa. O software a seguir é um programa bem simples que lê uma planilha com informações sobre alunos de uma escola, calcula suas notas e suas faltas e escreve na planilha a situação de aprovação de cada um.

## Instalação e uso

Para instalar e usar o software são necessários apenas os seguintes comandos:

```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```

```python ./main.py```

A aplicação não possui nenhum comando a ser dado após ser rodada.

Link para a planilha lida e alterada: https://docs.google.com/spreadsheets/d/1yEzMLGotflN5SiIhPbKo0yrngdiXystICWR2yfc_TQw/edit#gid=0

## Regras de funcionamento do programa

O programa recebe a planilha e lê os dados de cada aluno e guarda. Em seguida ele processa as notas e faltas de cada um respectivamente e classifica da seguinte maneira:
- Caso o número de faltas seja maior que 25% do total de aulas o aluno é reprovado por falta;
- Se ele não foi reprovado por falta, é feita a média das 3 notas dele e ela é classificada em:
    - Aprovado se média >= 70%
    - Exame Final se 70 > média >= 50%
    - Reprovado por nota se média < 50%
- Se o aluno estiver de exame final, então é calculada a nota necessária no exame para que ele seja aprovado, que é dada pela seguinte fórmula 5 <= (média + nota exame final) / 2
- Caso a situação do aluno seja qualquer outra, a nota para aprovação é automaticamente preenchida com um 0 (zero)

## Referências
Planilha original fornecida: https://docs.google.com/spreadsheets/d/1XvWJcRLj2WAeXO3ULQ_GxGm9---3SZkjMbGcXMJtt70/edit#gid=0

Documentação da api do Google Sheets: https://developers.google.com/sheets/api/guides/concepts

## Autor

Desenvolvido e publicado por mim, João Pedro, dono deste perfil do github