# Escopo da edição pública

Esta edição foi construída com histórico Git novo e uma seleção explícita de arquivos.
Ela preserva a ideia de preparação progressiva, modelos de candidatura e os cinco
exercícios SQL do acervo de entrevistas. Os textos foram generalizados e os nomes do
laboratório foram substituídos por nomes fictícios. Os números são fixtures de treino.

Não foram incluídos currículos, dados de identificação e contato, mensagens com
recrutadores, verificações pessoais, processos seletivos em andamento, gravações,
capturas de tela, documentos de terceiros, propostas comerciais ou projetos independentes.
Nenhum histórico do repositório privado foi importado.

## Antes de contribuir

Revise todos os arquivos e o histórico que pretende enviar. Não basta apagar um segredo
em um commit posterior. Use dados fictícios e não publique modelos preenchidos.
Logs e relatórios de erro também podem conter informações pessoais.

O `.gitignore` reduz inclusões acidentais, mas não remove arquivos já rastreados e não
identifica todos os dados sensíveis. A revisão humana continua necessária.

## Uso local

O laboratório não coleta telemetria e não faz chamadas de rede. O Python lê o schema
local e a consulta escolhida, executa no SQLite em memória e imprime o resultado.
Ele não recebe documentos nem configura acesso a sistemas reais.

Mantenha currículos e candidaturas em uma pasta privada fora do clone. Compartilhe
somente exemplos que você tem autorização para divulgar.
