# Instruções para manutenção

Escopo: kit público de entrevistas com documentos e laboratório SQL local.
Não importar conteúdo de pastas vizinhas nem históricos de repositórios privados.

## Verificação

Python 3.11 ou superior, somente biblioteca padrão:

```sh
python -m unittest discover -s tests -v
```

Para contribuições em Python, executar também `ruff format .` e `ruff check .`.
O Ruff é uma ferramenta de desenvolvimento, não um requisito para usar o material.
Usar ai-jail quando disponível no ambiente do agente. Não contornar isolamento.

## Convenções

Manter funções pequenas e tipadas, nomes específicos e erros com contexto.
Usar dados fictícios. Não incluir chaves, contatos, currículos, mensagens ou gravações.
Não adicionar serviços pagos ou dependências de nuvem ao laboratório.
Criar testes para cada mudança de comportamento. Manter links locais válidos.
Não fazer commit em branch default. Publicação e push exigem autorização do responsável.
