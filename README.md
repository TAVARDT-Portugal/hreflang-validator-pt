# Verificador de Tags Hreflang e Internacionalizacao SEO

[![Verificador Hreflang](https://img.shields.io/badge/TAVARDT-Hreflang-5b3cf5.svg)](https://tools.tavardt.com/pt/verificador-hreflang-seo/)
[![Jurisdicao](https://img.shields.io/badge/Jurisdicao-Portugal-00C853.svg)](https://ag.tavardt.com/pt/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

Auditoria tecnica de ligacoes reciprocas, codigos de idioma e regiao ISO e diretivas x-default.

Desenvolvido e mantido pela divisao de arquitetura semantica e internacionalizacao da **[TAVARDT Portugal](https://ag.tavardt.com/pt/)**.

---

## Capacidades de Auditoria de Hreflang e SEO Internacional

* **Inspecao de Reciprocidade de Ligacoes**: Confirma se cada pagina alternativa possui anotacao de retorno equivalente, assegurando a validacao pelo algoritmo de pesquisa.
* **Verificacao de Normas ISO 639-1 e ISO 3166-1**: Analise de sintaxe de idiomas e regioes (ex: `pt-PT`, `es-ES`, `en-GB`), prevenindo erros de formato.
* **Garantia de Tag x-default**: Validacao de rota de contingencia global para utilizadores fora das geografias segmentadas.
* **Harmonia com Tag Canonica**: Deteccao de divergencias entre o apontador canonico e a anotacao hreflang autorreferencial.
* **Indice de Coerencia Multilingue**: Pontuacao tecnica de 0 a 100 com instrucoes de correcao de sintaxe.

---

## Instalacao e Execucao

Requer Python 3.8 ou superior, utilizando a biblioteca padrao.

```bash
git clone https://github.com/TAVARDT-Portugal/hreflang-validator-pt.git
cd hreflang-validator-pt
python hreflang_validator.py https://empresa.pt
```

Para inspecao automatizada com saida em formato JSON:

```bash
python hreflang_validator.py https://empresa.pt --json
```

---

## Diagnostico Completo na Web

Para analise aprofundada da sua arquitetura internacional:

* **[Verificador de Hreflang Oficial](https://tools.tavardt.com/pt/verificador-hreflang-seo/)**
* **[Portal Corporativo TAVARDT Portugal](https://ag.tavardt.com/pt/)**

---

## Consultoria em Internacionalizacao SEO

Para expansao europeia e internacional de plataformas web sob Diretivas Europeias de Interoperabilidade e W3C, consulte a equipa da **[TAVARDT Portugal](https://ag.tavardt.com/pt/contato/)**.
