# Laboratório SQL: cinco desafios

Reserve 35 minutos como referência de treino. Explique, antes de escrever, o que
representa uma linha, como as tabelas se relacionam e como você trata ausência e empate.
Todos os nomes e registros deste laboratório são fictícios. Os valores servem apenas
para testar consultas, sem vínculo com empresas, pessoas ou contratos reais.

Na raiz do repositório:

```sh
python exercicios/sql/praticar.py exercicios/sql/resposta.sql
```

Edite [resposta.sql](resposta.sql) para resolver uma questão de cada vez. O
[schema.sql](schema.sql) documenta tabelas e registros: `clients`, `carriers`,
`submissions`, `quotes`, `policies` e `claims`.

## Q1: conversão por seguradora, 7 minutos

Considere somente propostas (`submissions`) de 2026. Retorne seguradora, total de
propostas, quantidade com status `bound` e taxa percentual arredondada a uma casa.
Inclua somente seguradoras com pelo menos três propostas. Ordene por taxa decrescente
e nome crescente em caso de empate.

Esperado: Seguradora Alfa, 6 propostas, 4 `bound`, 66,7%; Seguradora Beta, 6, 3, 50%;
Seguradora Gama, 4, 2, 50%. A Seguradora Delta não atinge o volume mínimo.

## Q2: última cotação por cliente, 8 minutos

Retorne uma linha por cliente com nome, prêmio e data da cotação mais recente.
No empate de datas, escolha o maior identificador da cotação. Ordene por nome.

Esperado: seis linhas. Para Cliente Alfa, prêmio 127000 em 2026-05-15.
Explique por que `MAX(quoted_at)` sozinho não identifica o valor associado à cotação.

## Q3: apólices sem sinistros, 5 minutos

Retorne identificador, cliente e prêmio das apólices que nunca tiveram sinistros.
Ordene pelo identificador da apólice.

Esperado: cinco linhas, apólices 3, 5, 6, 8 e 9. Discuta `LEFT JOIN ... IS NULL`
e `NOT EXISTS` como alternativas para a mesma pergunta.

## Q4: os dois maiores sinistros por apólice, 7 minutos

Retorne apólice, identificador e valor dos dois maiores sinistros de cada apólice.
Se houver empate de valor, escolha primeiro o maior identificador do sinistro.
Ordene por apólice crescente, valor decrescente e identificador decrescente.

Esperado: seis linhas. A apólice 1 retorna 35000 e 12000, excluindo 9000.
Explique a diferença entre `ROW_NUMBER`, `RANK` e `DENSE_RANK` diante de empates.

## Q5: prêmio acumulado por cliente, 8 minutos

Retorne cliente, vigência, prêmio e soma acumulada do prêmio até aquela apólice.
Ordene os eventos por data e, no empate, pelo identificador crescente da apólice.
Ordene o resultado por nome do cliente, data e identificador.

Esperado: dez linhas. Cliente Alfa acumula 115000, 235000 e 362000.
Explique por que uma janela mantém cada linha e `GROUP BY` muda a granularidade.

## Confira depois de tentar

As respostas testadas estão em [Q1](referencias/q1.sql), [Q2](referencias/q2.sql),
[Q3](referencias/q3.sql), [Q4](referencias/q4.sql) e [Q5](referencias/q5.sql).

```sh
python exercicios/sql/praticar.py exercicios/sql/referencias/q1.sql
python -m unittest discover -s tests -v
```

Os testes validam as **referências**, não corrigem automaticamente `resposta.sql`.
Compare sua saída com a referência da questão correspondente e explique as diferenças.
Para discutir escala, meça o plano de execução e a distribuição dos registros antes
de propor índices. O laboratório SQLite não representa desempenho de produção.
