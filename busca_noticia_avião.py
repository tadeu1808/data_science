import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Lista de sites de notícias e suas URLs de busca
news_sites = {
    "G1": "https://g1.globo.com/busca/?q=avi%C3%A3o+787",
    "UOL": "https://busca.uol.com.br/?term=avi%C3%A3o+787",
    "Estadão": "https://busca.estadao.com.br/?q=avi%C3%A3o+787",
    "CNN Brasil": "https://www.cnnbrasil.com.br/busca/?q=avi%C3%A3o+787"
}

def fetch_news(site, url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extração simples de títulos de notícias
        titles = []
        if "g1.globo" in url:
            for item in soup.select('.widget--info__title'):
                titles.append(item.get_text(strip=True))
        elif "uol.com.br" in url:
            for item in soup.select('.results-title'):
                titles.append(item.get_text(strip=True))
        elif "estadao.com.br" in url:
            for item in soup.select('.resultado-busca h3'):
                titles.append(item.get_text(strip=True))
        elif "cnnbrasil" in url:
            for item in soup.select('.home__title'):
                titles.append(item.get_text(strip=True))
        return titles
    except Exception as e:
        return [f"Erro ao buscar notícias em {site}: {e}"]

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    with open(f'noticias_787_{today}.txt', 'w', encoding='utf-8') as f:
        for site, url in news_sites.items():
            f.write(f"--- {site} ---\n")
            news = fetch_news(site, url)
            for title in news:
                f.write(f"{title}\n")
            f.write("\n")
    print("Busca diária concluída.")

if __name__ == "__main__":
    main()

# Mostra as notícias encontradas no prompt, com um resumo
with open(f'noticias_787_{datetime.now().strftime("%Y-%m-%d")}.txt', 'r', encoding='utf-8') as f:
    noticias = f.readlines()
    total_noticias = sum(1 for linha in noticias if linha.strip() and not linha.startswith("---"))
    print(f"Resumo: {total_noticias} notícias encontradas.\n")
    print("Principais notícias:")
    for linha in noticias:
        if linha.strip() and not linha.startswith("---"):
            print("-", linha.strip())
            # Exibe até 4 linhas seguintes (se existirem e não forem separadores)
            idx = noticias.index(linha)
            extra_lines = 0
            while extra_lines < 4 and idx + 1 < len(noticias):
                prox = noticias[idx + 1].strip()
                if prox and not prox.startswith("---"):
                    print("   ", prox)
                    extra_lines += 1
                    idx += 1
                else:
                    break

#exporte o arquivo de notícias para um arquivo de texto
        with open(f'noticias_787_{datetime.now().strftime("%Y-%m-%d")}.txt', 'w', encoding='utf-8') as f:
            f.writelines(noticias)
        print("Arquivo de notícias exportado com sucesso.")     
    