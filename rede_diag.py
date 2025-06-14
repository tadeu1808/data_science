import subprocess
import re
import sys

def get_interface():
    # Detecta a interface conectada (Windows)
    try:
        output = subprocess.check_output("wmic nic where (NetEnabled=true) get Name,NetConnectionID", shell=True, text=True)
        interfaces = [line.strip() for line in output.splitlines() if line.strip() and "Name" not in line]
        for idx, iface in enumerate(interfaces):
            print(f"{idx}: {iface}")
        idx = int(input("Escolha o número da interface conectada ao cabo: "))
        # Extrai o nome da interface antes do último espaço (NetConnectionID pode ser vazio)
        iface_info = interfaces[idx]
        # O formato geralmente é: Nome_da_Interface   NetConnectionID
        parts = iface_info.split()
        if len(parts) > 1:
            # NetConnectionID pode estar na última posição, mas pode estar vazio
            net_connection_id = parts[-1]
            if net_connection_id != "":
                return net_connection_id
            else:
                # Se NetConnectionID estiver vazio, retorna o nome da interface (tudo menos o último campo)
                return " ".join(parts[:-1])
        else:
            return iface_info
    except Exception as e:
        print("Erro ao listar interfaces:", e)
        sys.exit(1)

def medir_distancia(interface):
    # Usa o comando 'ethtool' equivalente no Windows (PowerShell)
    # No Windows, não há comando nativo para TDR, mas algumas placas Intel suportam via 'Intel PROSet'
    # Aqui, tentamos usar o 'Get-NetAdapterAdvancedProperty' para buscar informações
    try:
        cmd = f'powershell "Get-NetAdapterAdvancedProperty -Name \'{interface}\' | Select-Object DisplayName,DisplayValue"'
        output = subprocess.check_output(cmd, shell=True, text=True, encoding='utf-8', errors='ignore')
        print("Propriedades avançadas da interface:")
        print(output)
        # Não há TDR nativo, mas pode mostrar propriedades do cabo se suportado
        print("Nota: Medição de distância do cabo só é suportada por algumas placas de rede específicas (Intel, Realtek) e drivers.")
        print("Para medições precisas, use ferramentas do fabricante ou execute em Linux com 'ethtool -T'.")
    except Exception as e:
        print("Erro ao tentar medir distância:", e)

if __name__ == "__main__":
    interface = get_interface()
    medir_distancia(interface)