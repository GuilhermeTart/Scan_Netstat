# Permite executar comandos do sistema operacional.
import subprocess
from colors import colors


print(f"""{colors.red}
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


{colors.reset}""")

# Essa função executa o comando 'netstat ss -tunap'. O parâmetro 'ss' faz uma análise de sockets no linux, que pode fornecer informações detalhadas sobre a conexão de rede, e a opção '-tunap' t= Exibe conexões TCP, u= Exibe conexões UDP, n= Exibe o número de portas ao invés de nomes de serviço, a= Inclui sockets de escuta e conexões não estabelecidas, p= Mostra informações sobre os processos associados a cada conexão. Após isso irá printar a saída do comando com a formatação 'utf-8', ou caso ocorra algum erro, irá exibir uma mensagem de erro.:
def execute_netstat():
    try:
      output = subprocess.check_output(['netstat', 'ss', '-tunap']) #check_output, é uma função do módulo subprocess que executa um comando especificado e retorna sua saída em sequência de bytes
      print(colors.green + output.decode('utf-8') + colors.reset) # Esse comando pega o output em bytes e descodifica para um formato legível.
    except subprocess.CalledProcessError as e:
      print(f"Erro ao executar o comando netstat: {e}")

execute_netstat()


#Colocamos as variáveis como globais, para podermos usá-las dentro e fora das funções.global pid 
global list
global list1
pid = input(colors.blue + "Informe o PID:  " + colors.reset) #Variável que  recebe os pids
list = str(pid.strip()) #Variável que   tira o espaço os pids
list1 = list.split() #Variável que   transforma os pids em lista


# Essa função irá executar o comando 'ps -p +PID' que irá filtrar a lista de  pid colocado pelo usuário.
for pid in pid.split():
      try:
        command = f'ps -p {pid}'
        output = subprocess.check_output(command, shell=True) # Define que o comando será executado em um shell do sistema operacional.
        print(colors.blue + output.decode('utf-8') + colors.blue)
      except subprocess.CalledProcessError as e: #except trata exceções, ele captura erros específicos durante a execução do script. 'subprocess.CalledProcessError' é uma exceção relacionada à execução de subprocessos usando o módulo 'subprocess'. Essa exceção é usada quando um subprocesso chamado retorna um código de saída diferente de zero.
        print( colors.red + f"Erro ao executar o comando ps: {e}" + colors.reset)



#Input que armazena se o usuário deseja fechar o processo ou não
fechar_processo = input(colors.green + "Deseja fechar o processo? (y/n): " + colors.reset)
if fechar_processo.lower() == 'y':
    

#Estrutura de repetição que fecha a lista de pids
   for i in list1:
    try:
        subprocess.check_call(['kill', '-9', pid, i])
        print( colors.red + f"Processo com PID {pid} foi fechado com sucesso." + colors.reset)

    except subprocess.CalledProcessError as e:
        print(colors.red + f"Erro ao fechar o processo: {e}" + colors.reset)
else:
    print(colors.red + "O processo não será fechado." + colors.reset)
