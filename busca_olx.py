import requests
from bs4 import BeautifulSoup
from time import sleep
from random import uniform

def buscar_carros_olx():
    session = requests.Session()
    # Coleta dados do usuário
    modelo = input("Digite o modelo do carro que deseja buscar: ")
    preco_max = input("Digite o preço máximo (opcional, pressione Enter para pular): ")
    ano_min = input("Digite o ano mínimo (opcional, pressione Enter para pular): ")
    
    # Formata a URL de busca
    url_base = "https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios"
    busca = modelo.replace(" ", "-").lower()
    url = f"{url_base}/{busca}?q={modelo}"
    
    if preco_max:
        url += f"&pe={preco_max}"
    if ano_min:
        url += f"&sf=1&rs=29&re={ano_min}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="119"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1'
    }
    sleep(uniform(1, 3))  # Random delay between requests
    sleep(uniform(1, 3))  # Random delay between requests
    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        anuncios = soup.find_all('div', {'data-testid': 'ad-list-item'})
        
        print("\nResultados encontrados:\n")
        # Mostra os 10 primeiros resultados
        for i, anuncio in enumerate(anuncios[:10], 1):
            try:
                titulo = anuncio.find('h2').text.strip()
                preco = anuncio.find('span', {'data-testid': 'ad-price'}).text.strip()
                local = anuncio.find('span', {'data-testid': 'ad-location'}).text.strip()
                
                print(f"{i}. {titulo}")
                print(f"   Preço: {preco}")
                print(f"   Local: {local}")
                print("-" * 50)
            except AttributeError:
                continue
    except requests.RequestException as e:
        print(f"Erro ao buscar dados: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
if __name__ == "__main__":
    print("=== Buscador de Carros OLX ===")
    buscar_carros_olx()