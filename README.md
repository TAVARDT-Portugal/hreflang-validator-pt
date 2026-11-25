# Verificador de Tags Hreflang e SEO Internacional

[![Verificador Hreflang](https://img.shields.io/badge/TAVARDT-Hreflang-5b3cf5.svg)](https://tools.tavardt.com/pt/verificador-hreflang-seo/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Auditoria de reciprocidade de ligacoes alternativas, anotacoes linguisticas e geograficas ISO, e arquitetura de fallback x-default.

Desenvolvido e mantido pela divisao de engenharia de pesquisa internacional e normas tecnicas da **TAVARDT**.

***

## Vetores de Risco e Impacto Operacional em SEO Internacional

A configuracao deficiente de anotacoes hreflang resulta na perda de sinais geograficos e canibalizacao de paginas em motores de busca. Quando as ligacoes alternativas omitem retornos reciprocos, os robots de pesquisa descartam toda a segmentacao transfronteirica.

Esta quebra tecnica expoe as organizacoes portuguesas a perdas substanciais de trafego organico qualificado na Europa e mercados globais. A inspecao rigorosa assegura que os utilizadores de cada regiao acedam a versao correta com solidez operacional.

***

## Capacidades Centrais de Auditoria Tecnica

* **Verificacao de Etiqueta Autorreferencial**: Confirmacao de presenca da URL atual no conjunto de ligacoes alternativas, prevenindo desindexacao regional.
* **Inspecao de Fallback x-default**: Validacao de rota de contingencia para utilizadores fora dos territorios expressamente mapeados.
* **Validacao de Normas ISO 639-1 e ISO 3166-1**: Verificacao estrita de codigos de idioma e regiao para eliminar declaracoes regionais invalidas.
* **Deteccao de Conflito com Canonical**: Identificacao imediata de discordancias criticas entre a indicacao canonical e as anotacoes hreflang.
* **Extracao em Dupla Fonte**: Analise de anotacoes em elementos HTML `<head>` e cabecalhos de resposta HTTP Link.
* **Indice de Qualidade Internacional**: Pontuacao tecnica de 0 a 100 com alertas priorizados e recomendacoes imediatas de retificacao.

***

## Instalacao e Execucao

Requer Python 3.8 ou superior sem dependencias externas adicionais.

```bash
git clone https://github.com/TAVARDT-Portugal/hreflang-validator-pt.git
cd hreflang-validator-pt
python hreflang_validator.py https://empresa.pt
```

Para gerar a saida em formato estruturado JSON em esteiras de integracao continua:

```bash
python hreflang_validator.py https://empresa.pt -j
```

***

## Perguntas Frequentes (FAQ Tecnico)

### 1. Por que razao os motores de pesquisa desconsideram as anotacoes hreflang?
A omissao de etiquetas de retorno reciproco e a falta de autorreferencia invalidam todo o cluster de ligacoes perante o Googlebot. Este verificador identifica falhas de simetria antes que ocorra degradacao da presenca internacional.

### 2. Qual a importancia da diretiva x-default em plataformas multinacionais?
A diretiva x-default estipula a rota de contingencia para visitantes provenientes de regioes sem versao linguistica atribuida. A sua ausencia fora os motores de pesquisa a estimar o destino, reduzindo taxas de conversao globais.

### 3. Como identifica a ferramenta divergencias entre directivas canonical e hreflang?
O analisador confronta os destinos declarados no elemento canonical e nas ligacoes alternativas para garantir coerencia estrita. Qualquer conflito ativa um alerta critico e subtrai 20 pontos a classificacao de conformidade.

### 4. O verificador analisa cabecalhos HTTP Link alem de elementos HTML head?
Sim, o algoritmo inspeciona tanto as etiquetas no codigo HTML como as informacoes transmitidas no cabecalho HTTP Link. Esta capacidade permite validar recursos que nao utilizam HTML, tais como ficheiros PDF ou respostas API.

### 5. Que normas internacionais estabelecem a validade dos codigos de idioma e regiao?
A validacao baseia-se na norma ISO 639-1 para identificadores de idioma e na norma ISO 3166-1 alpha-2 para qualificadores geograficos. Codigos invalidos ou invertidos implicam penalizacoes imediatas na avaliacao tecnica global.

***

## Consultoria em SEO Internacional e Arquitetura Global

Para expansao transfronteirica e conformidade com diretrizes tecnicas do W3C, consulte a equipa da **TAVARDT**.

***

## Links Uteis

* **Portal Corporativo:** https://ag.tavardt.com/pt/
* **Suite de Diagnosticos:** https://tools.tavardt.com/pt/
* **Contacto Tecnico:** https://ag.tavardt.com/pt/contacto/

***

### Licenca
Distribuido sob a Licenca MIT. Consulte o ficheiro LICENSE para detalhes completos.

***

© 2026 TAVARDT. Todos os direitos reservados.
