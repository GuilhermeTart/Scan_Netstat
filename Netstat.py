
#E fecha o processo

import subprocess

def execute_netstat():
    try:
        output = subprocess.check_output(['netstat', '/ano'])
        print(output.decode('latin-1'))
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando netstat: {e}")

execute_netstat()



def execute_tasklist(pid):
    try:
        command = f'tasklist | findstr "{pid}"'
        output = subprocess.check_output(command, shell=True)
        print(output.decode('latin-1'))
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando tasklist: {e}")

pid = input("Informe seu PID: ")
execute_tasklist(pid)

#
fechar_processo = input("Deseja fechar o processo? (y/n): ")
if fechar_processo.lower() == 'y':
    try:
        subprocess.check_call(['taskkill', '/F', '/PID', pid])
        print(f"Processo com PID {pid} foi fechado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao fechar o processo: {e}")
else:
    print("O processo não será fechado.")
