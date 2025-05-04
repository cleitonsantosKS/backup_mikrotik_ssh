

print("""     
                      ,-'`\                                
                  _,"'    j                                
           __....+       /               .                 
       ,-'"             /               ; `-._.'.          
      /                (              ,'       .'          
     |            _.    \             \   ---._ `-.        
     ,|    ,   _.'  Y    \             `- ,'   \   `.`.    
     l'    \ ,'._,\ `.    .              /       ,--. l    
  .,-        `._  |  |    |              \       _   l .   
 /              `"--'    /              .'       ``. |  )  
.\    ,                 |                .        \ `. '   
`.                .     |                '._  __   ;. \'   
  `-..--------...'       \                  `'  `-"'.  \   
      `......___          `._                        |  \  
               /`            `..                     |   . 
              /|                `-.                  |    L
             / |               \   `._               .    |
           ,'  |,-"-.   .       .     `.            /     |
         ,'    |     '   \      |       `.         /      |
       ,'     /|       \  .     |         .       /       |
     ,'      / |        \  .    +          \    ,'       .'
    .       .  |         \ |     \          \_,'        / j
    |       |  L          `|      .          `        ,' ' 
    |    _. |   \          /      |           .     .' ,'  
    |   /  `|    \        .       |  /        |   ,' .'    
    |   ,-..\     -.     ,        | /         |,.' ,'      
    `. |___,`    /  `.   /`.       '          |  .'        
      '-`-'     j     ` /."7-..../|          ,`-'          
                |        .'  / _/_|          .             
                `,       `"'/"'    \          `.           
                  `,       '.       `.         |           
             __,.-'         `.        \'       |           
            /_,-'\          ,'        |        _.          
             |___.---.   ,-'        .-':,-"`\,' .          
                  L,.--"'           '-' |  ,' `-.\         
                                        `.' mh                          
""")

import random

# Banco de passagens bíblicas
passagens = [
    "O Senhor é meu pastor; nada me faltará. Ele me faz repousar \n em pastos verdejantes, guia-me mansamente a águas tranquilas.\n                                                                1— Salmo 23:1-2",
    "Aquele que tem os meus mandamentos e os guarda, esse é o que me ama; e aquele\n que me ama será amado por meu Pai, e eu o amarei e me manifestarei a ele.\n                                                                — João 14:21",
    "Amarás o Senhor, teu Deus, de todo o teu coração,\n de toda a tua alma e de todo o teu entendimento.\n                                                                — Mateus 22:37",
    "Tudo posso naquele que me fortalece.\n                                                                — Filipenses 4:13",
    "E conhecereis a verdade, e a verdade vos libertará.\n                                                                — João 8:32",
    "O amor é paciente, o amor é bondoso. Não inveja, não se vangloria,\n não se orgulha. Não maltrata, não procura seus próprios interesses,\n não se ira facilmente, não guarda rancor.\n                                                                — 1° Coríntios 13:4-5",
    "Bem-aventurados os pacificadores, porque serão chamados filhos de Deus.\n                                                                — Mateus 5:9"
]


def sorteia_passagem():
    passagem = random.choice(passagens)  
    print("\nPassagem do dia:\n")
    print(passagem)  
    print("\n                                                                Feito por: Cleiton Santos")

sorteia_passagem()


import time
import paramiko
import os
def exportar_ssh(ip, nome_host, usuario, senha):
    try:
        data_atual = time.strftime("%Y-%m-%d_%H-%M-%S")
        data_diretorio = data_atual.split('_')[0]  # Pega só a data (YYYY-MM-DD)
        nome_arquivo = f"{nome_host}_export_{data_atual}"
        pasta_backup = f"./backup_{data_diretorio}"

        if not os.path.exists(pasta_backup):
            os.makedirs(pasta_backup)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=usuario, password=senha)  

        stdin, stdout, stderr = ssh.exec_command(f'/export verbose')

        output = stdout.read().decode()

        output = '\n'.join(line.strip() for line in output.splitlines() if line.strip())

        with open(f'{pasta_backup}/{nome_arquivo}.backup', 'w') as file:
            file.write(output)

        print(f"Exportação via SSH concluída. Arquivo salvo como {nome_arquivo}.backup na pasta {pasta_backup}")

        ssh.close()

    except Exception as e:
        print(f"Erro ao exportar via SSH: {e}")


def obter_hosts_do_arquivo(nome_arquivo):
    hosts = []
    try:
        with open(nome_arquivo, 'r') as file:
            for linha in file:
                nome, ip = linha.strip().split(',')
                hosts.append({"nome": nome, "ip": ip})
    except Exception as e:
        print(f"Erro ao ler o arquivo de hosts: {e}")
    return hosts

def obter_usuario_senha_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            usuario, senha = file.read().strip().split(',')
            return usuario, senha
    except Exception as e:
        print(f"Erro ao ler o arquivo de usuário e senha: {e}")
        return None, None

def obter_dados_usuario():
    print("""\nDeseja utilizar a lista de hosts pré-definidos\n \nhosts.txt \nusuario_senha.txt\n\nou digitar manualmente?""")

    resposta = input("""Digite: \n'1' para usar as listas \n'2' para digitar manualmente:""")

    if resposta == '1':
        hosts = obter_hosts_do_arquivo('hosts.txt')

        usuario, senha = obter_usuario_senha_do_arquivo('usuario_senha.txt')

        if usuario is None or senha is None:
            print("Erro ao carregar usuário e senha do arquivo. Verifique o arquivo usuario_senha.txt.")
            return

        for host in hosts:
            print(f"Iniciando exportação para {host['nome']} ({host['ip']})...")
            exportar_ssh(host['ip'], host['nome'], usuario, senha)
    
    elif resposta == '2':
        while True:
            try:
                n_hosts = int(input("Quantos hosts você deseja fazer backup? "))
                if n_hosts <= 0:
                    print("Número de hosts deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("Por favor, insira um número válido para os hosts.")

        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        for i in range(n_hosts):
            nome_host = input(f"Digite o nome do {i+1}º host: ")
            ip_host = input(f"Digite o IP do {i+1}º host: ")

            exportar_ssh(ip_host, nome_host, usuario, senha)

    else:
        print("Opção inválida. Por favor, tente novamente.")

def iniciar_exportacao():
    obter_dados_usuario()

iniciar_exportacao()
