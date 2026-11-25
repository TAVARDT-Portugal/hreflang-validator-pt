# Verificador de Tags Hreflang e Internacionalizacao SEO

[![Verificador Hreflang](https://img.shields.io/badge/TAVARDT-Hreflang-5b3cf5.svg)](https://tools.tavardt.com/pt/verificador-hreflang-seo/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)](https://www.python.org/)

Auditoria tecnica de ligações reciprocas, codigos de idioma e regiao ISO e diretivas x-default.

***

## Capacidades de Auditoria de Hreflang e SEO Internacional

* **Inspeção de Reciprocidade de Ligações**: Confirma se cada pagina alternativa possui anotacao de retorno equivalente, assegurando a validacao pelo algoritmo de pesquisa.
* **Verificacao de Normas ISO 639-1 e ISO 3166-1**: Análise de sintaxe de idiomas e regioes (ex: `pt-PT`, `es-ES`, `en-GB`), prevenindo erros de formato.
* **Garantia de Tag x-default**: Validacao de rota de contingencia global para utilizadores fora das geografias segmentadas.
* **Harmonia com Tag Canonica**: Deteccao de divergencias entre o apontador canonico e a anotacao hreflang autorreferencial.
* **Indice de Coerencia Multilingue**: Pontuacao tecnica de 0 a 100 com instrucoes de correcao de sintaxe.

***

## Instalação e Execucao

Requer Python 3.8 ou superior, utilizando a biblioteca padrao.

```bash
git clone https://github.com/TAVARDT-Portugal/hreflang-validator-pt.git
cd hreflang-validator-pt
python hreflang_validator.py https://empresa.pt
```

Para inspeção automatizada com saída em formato JSON:

```bash
python hreflang_validator.py https://empresa.pt -json
```

***

## Consultoria em Internacionalizacao SEO

Para expansao europeia e internacional de plataformas web sob Diretivas Europeias de Interoperabilidade e W3C, consulte a equipa da **TAVARDT Portugal**.

## Links Úteis

* **Portal Corporativo:** https://ag.tavardt.com/pt/
* **Suíte de Diagnósticos:** https://tools.tavardt.com/pt/
* **Contacto Técnico:** https://ag.tavardt.com/pt/contacto/

***

### Licença
Distribuído sob a Licença MIT.

***

© 2026 TAVARDT Portugal. Todos os direitos reservados. Soberania e Defesa de Infraestrutura.
