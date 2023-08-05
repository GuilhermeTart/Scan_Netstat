# Permite executar comandos do sistema operacional.
import subprocess

print(r"""
  ____ _   _ ___ _     _   _ _____ ____  __  __ _____      _   _   _  ____ _   _ ____ _____ ___  
 / ___| | | |_ _| |   | | | | ____|  _ \|  \/  | ____|    / \ | | | |/ ___| | | / ___|_   _/ _ \ 
| |  _| | | || || |   | |_| |  _| | |_) | |\/| |  _|     / _ \| | | | |  _| | | \___ \ | || | | |
| |_| | |_| || || |___|  _  | |___|  _ <| |  | | |___   / ___ \ |_| | |_| | |_| |___) || || |_| |
 \____|\___/|___|_____|_| |_|_____|_| \_\_|  |_|_____| /_/   \_\___/ \____|\___/|____/ |_| \___/ 

             __  __  ___  _   _ ___ _____ ___  ____        _   _ _____ _______        _____  ____  _  __
            |  \/  |/ _ \| \ | |_ _|_   _/ _ \|  _ \      | \ | | ____|_   _\ \      / / _ \|  _ \| |/ /
            | |\/| | | | |  \| || |  | || | | | |_) |     |  \| |  _|   | |  \ \ /\ / / | | | |_) | ' / 
            | |  | | |_| | |\  || |  | || |_| |  _ <      | |\  | |___  | |   \ V  V /| |_| |  _ <| . \ 
            |_|  |_|\___/|_| \_|___| |_| \___/|_| \_\ ____|_| \_|_____| |_|    \_/\_/  \___/|_| \_\_|\_\


""")

# Essa função executa o comando 'netstat ss -tunap'. O parâmetro 'ss' faz uma análise de sockets no linux, que pode fornecer informações detalhadas sobre a conexão de rede, e a opção '-tunap' t= Exibe conexões TCP, u= Exibe conexões UDP, n= Exibe o número de portas ao invés de nomes de serviço, a= Inclui sockets de escuta e conexões não estabelecidas, p= Mostra informações sobre os processos associados a cada conexão. Após isso irá printar a saída do comando com a formatação 'utf-8', ou caso ocorra algum erro, irá exibir uma mensagem de erro.:
def execute_netstat():
    try:
      output = subprocess.check_output(['netstat', 'ss', '-tunap']) #check_output, é uma função do módulo subprocess que executa um comando especificado e retorna sua saída em sequência de bytes
      print(output.decode('utf-8')) # Esse comando pega o output em bytes e descodifica para um formato legível.
    except subprocess.CalledProcessError as e:
      print(f"Erro ao executar o comando netstat: {e}")

execute_netstat()


#Colocamos as variáveis como globais, para podermos usá-las dentro e fora das funções.global pid 
global oi
global oi1
pid = input("Informe o PID:  ") #Variável que  recebe os pids
oi = str(pid.strip()) #Variável que   tira o espaço os pids
oi1 = oi.split() #Variável que   transforma os pids em lista


# Essa função irá executar o comando 'ps -p +PID' que irá filtrar o pid colocado pelo usuário.
for pid in pid.split():
      try:
        command = f'ps -p {pid}'
        output = subprocess.check_output(command, shell=True) # Define que o comando será executado em um shell do sistema operacional.
        print(output.decode('utf-8'))
      except subprocess.CalledProcessError as e: #except trata exceções, ele captura erros específicos durante a execução do script. 'subprocess.CalledProcessError' é uma exceção relacionada à execução de subprocessos usando o módulo 'subprocess'. Essa exceção é usada quando um subprocesso chamado retorna um código de saída diferente de zero.
        print(f"Erro ao executar o comando ps: {e}")



# Essa função Permite o usuário fechar um processo usando o comando 'kill -9 + pid'
fechar_processo = input("Deseja fechar o processo? (y/n): ")
if fechar_processo.lower() == 'y':
    
    
   for i in oi1:
    try:
        subprocess.check_call(['kill', '-9', pid, i])
        print(f"Processo com PID {pid} foi fechado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao fechar o processo: {e}")
else:
    print("O processo não será fechado.")
