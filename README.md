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

Feito com ❤️ por Cleiton Santos
