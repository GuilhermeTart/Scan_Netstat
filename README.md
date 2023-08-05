# Scan_Netstat
Este repositório contém um script em Python que realiza a execução do comando Netstat nos sistemas Linux e Windows, exibindo todas as conexões de redes ativas TCP/UDP, incluindo endereços IP, portas e identificadores de processos (PID). O comando exibe um input onde o usuário pode colocar um PID para verificar qual é o nome do serviço que está estabelecendo conexão na rede. Após isso, o script exibe outro input perguntando se o usuário deseja finalizar o processo utilizando **y/n**.

No script_Netstat_Windows_Pid_list & script_Netstat_Linux_Pid_list, alterei o código para que possa ser consultado uma lista de Pids separado por espaço, ex: 3864 5717 2894, após a consulta o usuário final pode querer fechar a lista de processos ou não. 

## O que é Netstat?
O Netstat é uma ferramenta que permite aos administradores do sistema visualizarem as conexões de rede ativas e as estatísticas de protocolo. Com o Netstat, é possível identificar quais processos estão se comunicando pela rede, exibindo informações como endereços IP, portas e estados das conexões. Essa ferramenta serve para monitorar e diagnosticar a atividade de rede em um sistema.

### Scan_Netstat_Linux
![image](https://github.com/GuilhermeTart/Scan_Netstat/assets/136984328/062eddfe-f0eb-486d-92b8-766b7b1e37ba)

![image](https://github.com/GuilhermeTart/Scan_Netstat/assets/136984328/c3fbfd47-a4a5-4f77-a5d0-1e3e36ef1bdc)



### Scan_Netstat_Windows
![image](https://github.com/GuilhermeTart/Scan_Netstat/assets/136984328/4ed6f435-86ea-441f-a9b3-7a01aa889b6b)

![image](https://github.com/GuilhermeTart/Scan_Netstat/assets/136984328/2a403b54-602c-409c-94f6-71f970ff4367)



