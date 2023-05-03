import random

# Dicionário que contém os estados e suas respectivas capitais
estados_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}

# Lista que contém os nomes dos estados
estados = list(estados_capitais.keys())

# Loop infinito que só será encerrado se o usuário digitar "sair"
while True:
    # Gera um número aleatório entre 0 e 26 para escolher um estado aleatório
    indice_estado = random.randint(0, 26)
    estado = estados[indice_estado]
    
    # Pede para o usuário digitar a capital do estado
    resposta_usuario = input(f'Diga a capital do estado {estado}: ').title().strip()
    
    # Verifica se a resposta do usuário está correta
    if resposta_usuario == estados_capitais[estado]:
        print('Você acertou!')
    elif resposta_usuario == 'Sair':
        print('Obrigado por jogar!')
        break
    else:
        print(f'Você errou, a resposta certa é: {estados_capitais[estado]}')
