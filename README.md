# Verificador de Tags Hreflang e SEO Internacional

[![Verificador Hreflang](https://img.shields.io/badge/TAVARDT-Hreflang-5b3cf5.svg)](https://tools.tavardt.com/pt/verificador-hreflang-seo/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Auditoria de reciprocidade de ligacoes alternativas, anotacoes linguisticas e geograficas ISO, e arquitetura de fallback x-default.

Desenvolvido e mantido pela divisao de engenharia de pesquisa internacional e normas tecnicas da **TAVARDT**.

***

## Capacidades de Auditoria de Hreflang e SEO Internacional

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

## Diagnostico Completo na Web

Para auditorias aprofundadas e inspecao visual de etiquetas internacionais:

* [Verificador Hreflang](https://tools.tavardt.com/pt/verificador-hreflang-seo/)
* [Portal Corporativo](https://ag.tavardt.com/pt/)

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
