# 📦 Script de Backup Mikrotik via SSH

Este script realiza o **backup da configuração de dispositivos Mikrotik** conectando-se via **SSH** e exportando o conteúdo para arquivos `.backup`.  
Ele permite entrada manual ou leitura automatizada a partir dos arquivos `hosts.txt` e `usuario_senha.txt`.

---

## ✅ Requisitos

Este script requer Python 3.x e utiliza as seguintes bibliotecas:

- `paramiko` (precisa ser instalada)
- `random` e `time` (inclusas na biblioteca padrão do Python)

Instale a dependência externa com:

```bash
pip install paramiko
```
📁 Estrutura Esperada
    hosts.txt: lista de dispositivos no formato nome_host,ip
    Exemplo:
    
```
mikrotik1,192.168.88.1
mikrotik2,192.168.88.2
```

usuario_senha.txt: credenciais no formato usuario,senha

Exemplo:

    admin,senha123

 O script cria automaticamente a pasta exports/ onde os arquivos de backup serão salvos.
🚀 Como Executar
    Certifique-se de que as dependências estão instaladas.
    Execute o script Python:
```
python script_backup_mikrotik.py
```

   Escolha entre:

 1: Utilizar os arquivos hosts.txt e usuario_senha.txt

 2: Inserir os dados manualmente via terminal

✨ Extras

Ao iniciar, o script exibe aleatoriamente uma mensagem bíblica motivacional.

Feito por Cleiton Santos

# 🔄 Bônus: Automatizando com Service no Linux

Você pode configurar este script para ser executado automaticamente a cada 24 horas usando o systemd no Linux. Siga os passos:

1. Crie o arquivo .service

Crie um novo serviço em:

```
sudo nano /etc/systemd/system/backupmikrotik.service
```

Exemplo de conteúdo (considerando que o script está em /home/seu_usuario/):

```
[Unit]
Description=Backup Mikrotik via SSH
After=network.target

[Service]
# Altere o caminho abaixo caso seu script esteja em outro local
ExecStart=/usr/bin/python3 /home/seu_usuario/script_backup_mikrotik.py
WorkingDirectory=/home/seu_usuario/
Restart=on-failure
```

> Dica: Substitua seu_usuario pelo seu nome de usuário no Linux ou ajuste o caminho conforme necessário.



2. Crie o arquivo .timer para agendamento

```
sudo nano /etc/systemd/system/backupmikrotik.timer
```
Conteúdo:

```
[Unit]
Description=Executa o script de backup Mikrotik a cada 24 horas

[Timer]
OnBootSec=5min
OnUnitActiveSec=24h
Persistent=true

[Install]
WantedBy=timers.target
```

3. Ative o serviço e o agendador

```
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable --now backupmikrotik.timer
```

✅ Verifique se está funcionando

```
sudo systemctl list-timers | grep backupmikrotik
```
Agora seu script de backup será executado automaticamente todos os dias!

Feito por Cleiton Santos

