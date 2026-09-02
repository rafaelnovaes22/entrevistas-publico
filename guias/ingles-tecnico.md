# Inglês técnico para explicar decisões

Pratique em voz alta, sem decorar alegações sobre experiência que você não possui.
As frases abaixo são estruturas para completar com o que você realmente implementou.

## Estrutura curta

1. “The expected input is [INPUT], and the result should contain [OUTPUT].”
2. “Each row represents [GRAIN].”
3. “I chose [APPROACH] because [CONSTRAINT].”
4. “The edge case I want to test first is [CASE].”
5. “I have not measured [UNKNOWN] yet. I would validate it with [CHECK].”

## Vocabulário do laboratório

`join`: combinar registros por uma condição. `column`: coluna.
`conditional aggregation`: agregar apenas registros que atendem a uma condição.
`percentage`: percentual. `ascending` e `descending`: crescente e decrescente.
`reference solution`: solução de referência. `drill`: exercício repetido.
`tie-breaker`: critério de desempate. `running total`: total acumulado.
`to filter out`: excluir registros. `to group by`: agrupar por.
`to partition by`: separar grupos para uma função de janela.

No domínio fictício: `client` é cliente, `carrier` é seguradora, `submission` é
proposta, `quote` é cotação, `policy` é apólice e `claim` é sinistro.
Aqui esses termos servem apenas ao exercício técnico.

## Perguntas e esclarecimentos

“What should happen when two records have the same date?”

“Should clients without quotes appear in the result?”

“May I check the official documentation for this syntax?”

“I know the concept, but I need to confirm the exact API.”

## Números e símbolos

`100.0`: “one hundred point zero”. `>=`: “greater than or equal to”.
`!=`: “not equal to”. `_`: “underscore”. `*`: “star” em `SELECT *`.
Em operações matemáticas, `*` é “times” e `/` é “divided by”.

## Como falar do uso de IA

Explique quais partes você delegou, quais verificou e onde manteve revisão humana.
Uma estrutura possível é: “I used AI for [TASK]. I verified the result with [EVIDENCE].
The limitation I found was [LIMITATION].” Complete somente com práticas verdadeiras.
