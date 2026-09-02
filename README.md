# Entrevistas: kit público de preparação

Material reutilizável para preparar candidaturas, organizar histórias profissionais e
praticar entrevistas técnicas. Esta é uma edição selecionada e adaptada do acervo
privado, com histórico independente. Não é uma cópia integral nem um aplicativo hospedado.

## Comece aqui

Leia o [roteiro de preparação](guias/preparacao.md) e copie os modelos para uma pasta
**fora deste repositório**. Use apenas sua experiência verdadeira nas respostas.
Não precisa instalar nada para ler os arquivos pelo GitHub.

Para baixar tudo, use **Code > Download ZIP** e extraia o arquivo. Com Git instalado:

```sh
git clone https://github.com/rafaelnovaes22/entrevistas-publico.git
cd entrevistas-publico
```

## Laboratório SQL

Requisito: Python 3.11 ou superior com SQLite, disponível na instalação padrão.
Não precisa de `pip install`, chave de API, conta em nuvem ou banco externo.
Abra o terminal na pasta extraída ou clonada e rode:

```sh
python -m unittest discover -s tests -v
python exercicios/sql/praticar.py exercicios/sql/resposta.sql
```

Se seu sistema usa `python3`, substitua `python` por `python3` nos comandos.
Leia os [cinco desafios SQL](exercicios/sql/README.md), edite `resposta.sql` no seu
editor e execute novamente. As soluções de referência estão na mesma pasta.
Os resultados são JSON: `columns` informa as colunas e `rows` contém as linhas.

O banco é criado novamente **em memória** a cada execução. Nada é enviado à internet.
O executor aceita uma consulta por vez e bloqueia escrita e `ATTACH`. Ele não é um
serviço de execução pública: rode somente exercícios locais que você revisou.

## Conteúdo

- [Preparação e simulado](guias/preparacao.md): ciclo de prática e critérios de revisão.
- [Inglês técnico](guias/ingles-tecnico.md): vocabulário e frases para explicar decisões.
- [Modelos reutilizáveis](modelos/README.md): candidatura, histórias e acompanhamento.
- [SQL com dados fictícios](exercicios/sql/README.md): cinco desafios e soluções testadas.
- [Escopo e privacidade](PRIVACIDADE.md): o que foi excluído e como contribuir sem expor pessoas.

## Limites

O material não garante contratação e não substitui as regras de cada entrevista.
Confirme com o entrevistador quais consultas, anotações e ferramentas são permitidas.
As estimativas de tempo são sugestões de treino, não promessas de resultado.

Currículos, contatos, mensagens, candidaturas reais, documentos de terceiros e outros
projetos não fazem parte desta edição. Ao abrir uma issue, use apenas exemplos fictícios.
