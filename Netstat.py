#A biblioteca 'subprocess' é usada para execultar comandos do sistema operacional a  partir do python
import subprocess

#A função 'Obter_ips_e_pids() executa o comando 'netstat -ano e coleta a saida. A saida é decodificada em formato de string ultilizando o 'encoding utf-8'. Em seguida o script repete sobre cada linha da saida para extrair os IPs e PIDs, que são armazenados nas listas  'ips' e 'pids';e retorna a lista
def obter_ips_e_pids():
    netstat_process = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE)
    netstat_output = netstat_process.communicate()[0].decode('utf-8')

    ips = []
    pids = []

    for line in netstat_output.splitlines():
        if "TCP" in line or "UDP" in line:
            parts = line.split()
            ip = parts[1]
            pid = parts[4]
            ips.append(ip)
            pids.append(pid)

    return ips, pids


#A função 'verificar_pid(pid)' executa o comando 'tasklist' e redireciona sua saida para o comando 'findstr' para filtrar as linhas correspondentes ao PID fornecido. A saida filtrada é caurada e decodificada em formato de string utilizando o encoding 'utf-8'.
def verificar_pid(pid):
    tasklist_process = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE)
    findstr_process = subprocess.Popen(['findstr', pid], stdin=tasklist_process.stdout, stdout=subprocess.PIPE)
    tasklist_process.stdout.close()
    output = findstr_process.communicate()[0].decode('utf-8')

    return output.strip()

# Obter os IPs e PIDs
ips, pids = obter_ips_e_pids()

# Exibir a lista de IPs e PIDs
for ip, pid in zip(ips, pids):
    print(f"IP: {ip} | PID: {pid}")

# Solicitar ao usuário que insira o PID a ser verificado
pid_verificar = input("Digite o número do PID para verificar: ")

# Verificar o PID fornecido
resultado = verificar_pid(pid_verificar)
print(resultado)
