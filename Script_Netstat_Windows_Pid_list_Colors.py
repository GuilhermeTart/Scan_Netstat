import subprocess
from colors import colors

def show_name_of_program():
    

    print(f"""{colors.red}
          
    ____ _   _ ___ _     _   _ _____ ____  __  __ _____       _   _   _  ____ _   _ ____ _____ ___  
    / ___| | | |_ _| |   | | | | ____|  _ \|  \/  | ____|    / \ | | | |/ ___| | | / ___|_   _/ _ \ 
    | |  _| | | || || |   | |_| |  _| | |_) | |\/| |  _|    / _ \| | | | |  _| | | \___ \ | || | | |
    | |_| | |_| || || |___|  _  | |___|  _ <| |  | | |___  / ___ \ |_| | |_| | |_| |___) || || |_| |
    \____|\___/|___|_____|_| |_|_____|_| \_\_|  |_|_____| /_/   \_\___/ \____|\___/|____/ |_| \___/ 

                __  __  ___  _   _ ___ _____ ___  ____        _   _ _____ _______        _____  ____  _  __
                |  \/  |/ _ \| \ | |_ _|_   _/ _ \|  _ \      | \ | | ____|_   _\ \      / / _ \|  _ \| |/ /
                | |\/| | | | |  \| || |  | || | | | |_) |     |  \| |  _|   | |  \ \ /\ / / | | | |_) | ' / 
                | |  | | |_| | |\  || |  | || |_| |  _ <      | |\  | |___  | |   \ V  V /| |_| |  _ <| . \
                |_|  |_|\___/|_| \_|___| |_| \___/|_| \_\ ____|_| \_|_____| |_|    \_/\_/  \___/|_| \_\_|\_\
                                                                                                        

   {colors.reset} """)

show_name_of_program()


#Função chamada 'execute_netstat():' dentro dessa função, o script executa o comando netstat /ano, que exibe estatísticas numéricas de todas as conexões de redes ativas, incluindo os endereços IP, portas e identificadores de processos (PID),Através  do 'subprocess.check_output(), que retorna a saída do comando, em seguida imprime a saída descodificada, usando 'latin-1'. Caso ocorra um erro  irá exibir uma mensagem de erro, usando o 'subprocess.CalledProcessError'
def execute_netstat():
    try:
        output = subprocess.check_output(['netstat', '/ano'])
        print(colors.green + output.decode('latin-1') + colors.reset)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando netstat: {e}")

#Este comando chama a função 'execute_netstat(), para executar o comando'netstat /ano'e imprimir sua saída.
execute_netstat()


    

#Colocamos as variáveis como globais, para podermos usá-las dentro e fora das funções.global pid 
global oi
global oi1
pid = input(colors.blue + "Informe o PID:  " + colors.reset) #Variável que  recebe os pids
oi = str(pid.strip()) #Variável que   tira o espaço os pids
oi1 = oi.split() #Variável que   transforma os pids em lista


#Estrutura de repetição que faz a filtragem da lista de pids

for pid in pid.split():
    try:
        command = f'tasklist | findstr "{pid}"'
        output = subprocess.check_output(command, shell=True)
        print(colors.blue + output.decode('latin-1') + colors.reset)
    except subprocess.CalledProcessError as e:
        
       print("Error:", e)


#Input que armazena se o usuário deseja fechar o processo ou não
fechar_processo = input(colors.red + "Deseja fechar os processos? (y/n): " + colors.reset)
if fechar_processo.lower() == 'y':


#Estrutura de repetição que fecha a lista de pids
    for i in oi1:
        try:
            subprocess.check_call([f'taskkill', '/F', '/PID', i])
            print(f"Processo com PID {pid} foi fechado com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao fechar o processo: {e}")


