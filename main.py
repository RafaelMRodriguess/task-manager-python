import json
try:
    with open("dados.json", "r") as arquivo:
        tarefas = json.load(arquivo)

except (FileNotFoundError, json.JSONDecodeError):
    tarefas = []

def add_tarefa(tarefas):
    tarefa = {
        "titulo" : input('\nTitulo da tarefa: '),
        "descricao" : input('Descricao (detalhe o que precisa ser feito): ').strip(),
        "prioridade" : input('Prioridade [baixa/média/alta]: ').strip().lower(),
        "status" : input('Status [pendente/em andamento/concluída]: ').strip().lower()
    }
    tarefas.append(tarefa)

    with open("dados.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=  4)


def listar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas, start = 1):
        print(f'\nTarefa {[i]}')
        print(f'Titulo : {tarefa['titulo']}')
        print(f'Descricao : {tarefa['descricao']}')
        print(f'Prioridade : {tarefa['prioridade']}')
        print(f'Status : {tarefa['status']}')

def marcar_como_concluido(tarefas):
    for i, tarefa in enumerate(tarefas, start = 1):
        print(f'\n{[i]} {tarefa['titulo']} - {tarefa['status']}')
    
    marcar_conc = int(input('Selecione a tarefa para marcar como concluida: '))
    
    tarefas[marcar_conc - 1]['status'] = 'Concluida'

    with open("dados.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)


def remover_tarefa(tarefas):
    for i, tarefa in enumerate(tarefas, start= 1):
        print(f'{[i]} - {tarefa['titulo']}')
    remocao = int(input('Escolha uma tarefa para remover: '))
    tarefas.pop(remocao - 1)

    with open("dados.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent = 4)
    

def filtro(tarefas):
    print('\nFILTRO DE PRIORIDADE: ')
    print('\n[1] Baixa\n[2] Media\n[3] Alta')
    
    escolha_filtro = input('\nEscolha a prioridade: ').capitalize()
    
    for tarefa in tarefas:
        if escolha_filtro.capitalize() in tarefa['prioridade']:
            print(f'\nTitulo : {tarefa['titulo']}')
            print(f'Prioridade : {tarefa['prioridade']}')

while True:
    print('\n[1] Adicionar tarefa\n[2] Listar tarefas\n[3] Marcar como concluida\n[4] Remover tarefa\n[5] Filtrar por prioridade\n[0] Sair\n')
    opcao  = int(input('Escolha uma opcao: '))

    if opcao == 1:
        add_tarefa(tarefas)

    elif opcao == 2:
        listar_tarefas(tarefas)

    elif opcao == 3:
        marcar_como_concluido(tarefas)
    
    elif opcao == 4:
        remover_tarefa(tarefas)
    
    elif opcao == 5:
        filtro(tarefas)
    
    elif opcao == 0:
        break

print('Programa encerrado.')