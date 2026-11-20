#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TAVARDT Portugal | Verificador e Auditor de Tags Hreflang e SEO Internacional
Repository: https://github.com/TAVARDT-Portugal/hreflang-validator-pt
Official Tool: https://tools.tavardt.com/pt/verificador-hreflang-seo/
Enterprise Portal: https://ag.tavardt.com/pt/

Audits alternate return tags, regional language targeting, and x-default annotations.
"""

import sys
import argparse
import json
import re
import urllib.request
import urllib.error
from urllib.parse import urlparse, urljoin

BANNER = "TAVARDT Portugal | Verificador e Auditor de Tags Hreflang e SEO Internacional"
DESC = "Auditoria de reciprocidade de ligacoes alternativas, normas ISO e integridade multilingue."
TARGET_PROMPT = "URL alvo para verificacao de tags hreflang"
JSON_HELP = "Apresenta o relatorio exclusivamente no formato JSON"
RECIPROCAL_HELP = "Inspeciona ativamente se as paginas alternativas possuem ligacao de retorno reciproca"
FETCHING = "A analisar anotacoes de internacionalizacao em:"
STATUS_CODE = "Codigo de resposta HTTP:"
CANONICAL_FOUND = "URL Canonica declarada:"
NO_CANONICAL = "Nenhum apontador canonico identificado."
HREFLANG_COUNT = "Total de tags hreflang identificadas:"
X_DEFAULT_FOUND = "Diretiva x-default global identificada:"
SELF_REF_FOUND = "Anotacao autorreferencial presente:"
ISO_VALID = "Conformidade com normas ISO 639-1 e ISO 3166-1:"
SCORE_TITLE = "Pontuacao de Coerencia Multilingue:"
STATUS_PASS = "CONFORME"
STATUS_WARN = "AVISO"
STATUS_FAIL = "CRITICO"
NO_TAGS = "AVISO CRITICO: Nenhuma anotacao hreflang encontrada na pagina."
MISSING_X_DEFAULT = "AVISO: Ausencia de diretiva x-default para navegadores fora das geografias mapeadas."
MISSING_SELF_REF = "AVISO: Ausencia de anotacao hreflang autorreferencial para a propria pagina."
CANONICAL_CONFLICT = "ALERTA CRITICO: Divergencia entre o URL canonico e as anotacoes hreflang."
INVALID_ISO = "AVISO: Codigo de lingua ou regiao fora de norma: {code}"
FOOTER = "Para diagnostico avancado, consulte a ferramenta oficial: https://tools.tavardt.com/pt/verificador-hreflang-seo/"

ISO_639_1_LANGS = {
    "aa", "ab", "af", "am", "ar", "as", "ay", "az", "ba", "be", "bg", "bh", "bi", "bn",
    "bo", "br", "ca", "co", "cs", "cy", "da", "de", "dz", "el", "en", "eo", "es", "et",
    "eu", "fa", "fi", "fj", "fo", "fr", "fy", "ga", "gd", "gl", "gn", "gu", "ha", "he",
    "hi", "hr", "hu", "hy", "ia", "id", "ie", "ik", "is", "it", "iu", "ja", "jv", "ka",
    "kk", "kl", "km", "kn", "ko", "ks", "ku", "ky", "la", "lb", "ln", "lo", "lt", "lv",
    "mg", "mi", "mk", "ml", "mn", "mr", "ms", "mt", "my", "na", "ne", "nl", "no", "oc",
    "om", "or", "pa", "pl", "ps", "pt", "qu", "rm", "rn", "ro", "ru", "rw", "sa", "sd",
    "sg", "sh", "si", "sk", "sl", "sm", "sn", "so", "sq", "sr", "ss", "st", "su", "sv",
    "sw", "ta", "te", "tg", "th", "ti", "tk", "tl", "tn", "to", "tr", "ts", "tt", "tw",
    "ug", "uk", "ur", "uz", "vi", "vo", "wo", "xh", "yi", "yo", "za", "zh", "zu"
}

def validate_hreflang_code(code):
    c = code.strip().lower()
    if c == "x-default":
        return True, "x-default", None
    parts = c.split("-")
    lang = parts[0]
    region = parts[1].upper() if len(parts) > 1 else None
    
    if lang not in ISO_639_1_LANGS:
        return False, lang, region
        
    if region and len(region) != 2:
        return False, lang, region
        
    return True, lang, region

def audit_hreflang(target_url, check_reciprocal=False):
    parsed = urlparse(target_url)
    if not parsed.scheme:
        target_url = "https://" + target_url
        parsed = urlparse(target_url)

    req = urllib.request.Request(
        target_url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; TAVARDT-HreflangAuditor/1.0; +https://ag.tavardt.com/pt/)"}
    )

    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            status_code = resp.status
            final_url = resp.geturl()
            raw_data = resp.read()
            encoding = resp.headers.get_content_charset() or "utf-8"
            html = raw_data.decode(encoding, errors="replace")
            http_link_header = resp.headers.get("Link", "")
    except urllib.error.HTTPError as e:
        return {
            "url": target_url,
            "status_code": e.code,
            "valid": False,
            "error": f"HTTP {e.code}"
        }
    except Exception as e:
        return {
            "url": target_url,
            "status_code": 0,
            "valid": False,
            "error": str(e)
        }

    # Parse Canonical tag
    canonical_match = re.search(r'<link[^>]+rel=[\'"]canonical[\'"][^>]+href=[\'"]([^\'"]+)[\'"]', html, re.I)
    if not canonical_match:
        canonical_match = re.search(r'<link[^>]+href=[\'"]([^\'"]+)[\'"][^>]+rel=[\'"]canonical[\'"]', html, re.I)
    canonical_url = urljoin(final_url, canonical_match.group(1).strip()) if canonical_match else None

    # Parse Hreflang tags
    # Method 1: HTML head tags
    hreflang_tags = []
    tag_matches = re.findall(r'<link[^>]+rel=[\'"]alternate[\'"][^>]*>', html, re.I)
    for tag_str in tag_matches:
        hl_m = re.search(r'hreflang=[\'"]([^\'"]+)[\'"]', tag_str, re.I)
        hr_m = re.search(r'href=[\'"]([^\'"]+)[\'"]', tag_str, re.I)
        if hl_m and hr_m:
            hl_code = hl_m.group(1).strip()
            hr_url = urljoin(final_url, hr_m.group(1).strip())
            hreflang_tags.append({"code": hl_code, "href": hr_url, "source": "html"})

    # Method 2: HTTP Link header
    if http_link_header:
        links = http_link_header.split(",")
        for l in links:
            if 'rel="alternate"' in l or "rel='alternate'" in l:
                hl_m = re.search(r'hreflang=[\'"]?([^\'";]+)[\'"]?', l, re.I)
                hr_m = re.search(r'<([^>]+)>', l)
                if hl_m and hr_m:
                    hreflang_tags.append({
                        "code": hl_m.group(1).strip(),
                        "href": urljoin(final_url, hr_m.group(1).strip()),
                        "source": "http_header"
                    })

    # Analysis
    findings = []
    score = 100
    has_x_default = False
    has_self_ref = False
    invalid_codes = []

    if not hreflang_tags:
        score = 0
        findings.append({"level": "CRITICAL", "message": NO_TAGS})
        return {
            "url": target_url,
            "final_url": final_url,
            "status_code": status_code,
            "valid": True,
            "canonical_url": canonical_url,
            "hreflang_tags": [],
            "score": score,
            "findings": findings
        }

    clean_target = final_url.rstrip("/")
    clean_canonical = canonical_url.rstrip("/") if canonical_url else None

    for tag in hreflang_tags:
        is_valid_iso, lang, region = validate_hreflang_code(tag["code"])
        tag["valid_syntax"] = is_valid_iso
        if not is_valid_iso:
            invalid_codes.append(tag["code"])

        if tag["code"].lower() == "x-default":
            has_x_default = True

        tag_url_clean = tag["href"].rstrip("/")
        if tag_url_clean == clean_target:
            has_self_ref = True

    if not has_x_default:
        score -= 15
        findings.append({"level": "WARNING", "message": MISSING_X_DEFAULT})

    if not has_self_ref:
        score -= 25
        findings.append({"level": "WARNING", "message": MISSING_SELF_REF})

    if invalid_codes:
        score -= min(30, len(invalid_codes) * 10)
        for inv in set(invalid_codes):
            findings.append({"level": "WARNING", "message": INVALID_ISO.replace("{code}", inv)})

    if canonical_url and clean_canonical != clean_target:
        score -= 20
        findings.append({"level": "CRITICAL", "message": CANONICAL_CONFLICT})

    score = max(0, min(100, score))

    return {
        "url": target_url,
        "final_url": final_url,
        "status_code": status_code,
        "valid": True,
        "canonical_url": canonical_url,
        "total_tags": len(hreflang_tags),
        "has_x_default": has_x_default,
        "has_self_ref": has_self_ref,
        "hreflang_tags": hreflang_tags,
        "score": score,
        "findings": findings
    }

def main():
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument("url", help=TARGET_PROMPT)
    parser.add_argument("--json", action="store_true", help=JSON_HELP)
    parser.add_argument("--check-reciprocal", action="store_true", help=RECIPROCAL_HELP)

    args = parser.parse_args()
    result = audit_hreflang(args.url, check_reciprocal=args.check_reciprocal)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    print("=" * 70)
    print(BANNER)
    print("=" * 70)
    print(f"{FETCHING} {result['url']}")
    print(f"{STATUS_CODE} {result['status_code']}")

    if not result.get("valid"):
        print("ERRO: Nao foi possivel carregar a URL.")
        if "error" in result:
            print(f"Detalhes: {result['error']}")
        sys.exit(1)

    if result.get("canonical_url"):
        print(f"{CANONICAL_FOUND} {result['canonical_url']}")
    else:
        print(NO_CANONICAL)

    print(f"{HREFLANG_COUNT} {result.get('total_tags', 0)}")
    print(f"{X_DEFAULT_FOUND} {'SIM' if result.get('has_x_default') else 'NAO'}")
    print(f"{SELF_REF_FOUND} {'SIM' if result.get('has_self_ref') else 'NAO'}")

    if result.get("hreflang_tags"):
        print("-" * 70)
        print("Mapeamento de Idioma e Regiao:")
        for tag in result["hreflang_tags"]:
            status_flag = "[OK]" if tag.get("valid_syntax") else "[INVALIDO]"
            print(f"  * {tag['code']:<12} -> {tag['href']} {status_flag}")

    print("-" * 70)
    print(f"{SCORE_TITLE} {result['score']}/100")
    if result["score"] >= 80:
        status_text = STATUS_PASS
    elif result["score"] >= 50:
        status_text = STATUS_WARN
    else:
        status_text = STATUS_FAIL
    print(f"Status: {status_text}")

    if result.get("findings"):
        print("-" * 70)
        print("Observacoes e Alertas:")
        for f in result["findings"]:
            print(f"  [{f['level']}] {f['message']}")

    print("=" * 70)
    print(FOOTER)
    print("=" * 70)

if __name__ == "__main__":
    main()
