# AI Agent Orchestration — Tool-Using AI Workflows

**Portfolio project · AI Agents · Orchestration · Tool Calling · Evaluation**

## Implementado

- orquestrador determinístico;
- roteamento entre conhecimento e cálculo;
- ferramenta de cálculo limitada por AST;
- somente `+`, `-`, `*` e `/`;
- tratamento de erros e fallback;
- testes automatizados e CI.

> Ainda não há LLM externo. O roteamento determinístico demonstra primeiro a camada de controle e segurança.

## Arquitetura atual

~~~text
User Request → Orchestrator → Router → Bounded Calculator / Knowledge Fallback → Structured Result
~~~

## Segurança da ferramenta

A calculadora não executa Python arbitrário. A expressão é analisada por AST e somente operações aritméticas permitidas são aceitas.

## Testes

~~~bash
pip install -r requirements.txt
pytest -q
~~~

## Roadmap

- [ ] router baseado em LLM com schema controlado;
- [ ] ferramentas adicionais com contratos explícitos;
- [ ] RAG;
- [ ] memória controlada;
- [ ] tracing;
- [ ] avaliação automática;
- [ ] testes de regressão.

## Competências

**AI Agents · Agentic Workflows · Tool Calling · Python · Evaluation · Testing · Orchestration · AI Engineering**

[AI & Data Portfolio](https://tsichero.github.io/tsichero.github.io-portfolio-ai/)