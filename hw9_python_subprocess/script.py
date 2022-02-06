import subprocess

from time import gmtime, strftime

output = subprocess.run(['ps', 'aux'],
                        stdout=subprocess.PIPE,
                        text=True
                        ).stdout.splitlines()

data = {'USERS': {},
        '%MEM': 0,
        '%CPU': 0,
        'MAX%_MEM': [],
        'MAX%_CPU': [],
        'PROCESS_CNT': len(output) - 1}

for line in output[1:]:
    user = line.split()[0]
    memory = float(line.split()[3])
    cpu = float(line.split()[2])
    process = line.split()[10]

    if user not in data['USERS']:
        data['USERS'][user] = 0

    data['USERS'][user] += 1
    data['%MEM'] += memory
    data['%CPU'] += cpu

    if not data['MAX%_MEM']:
        data['MAX%_MEM'] = (memory, process)
    if memory > data['MAX%_MEM'][0]:
        data['MAX%_MEM'] = (memory, process)

    if not data['MAX%_CPU']:
        data['MAX%_CPU'] = (cpu, process)
    if cpu > data['MAX%_CPU'][0]:
        data['MAX%_CPU'] = (cpu, process)

users_list = list(data['USERS'].items())
users_list.sort(key=lambda i: i[1], reverse=True)
newline = '\n'
tab = '\t'

result = (f'Отчёт о состоянии системы:'
          f'\nПользователи системы: {", ".join(data["USERS"])}'
          f'\nПроцессов запущено: {data["PROCESS_CNT"]}'
          f'\nПользовательских процессов:\n'
          f'{newline.join(f"{tab}{key}: {value}" for key, value in users_list)}'
          f'\nВсего памяти используется: {data["%MEM"]:.1f}%'
          f'\nВсего CPU используется: {data["%CPU"]:.1f}%'
          f'\nБольше всего памяти использует: {data["MAX%_MEM"][1][:20]} ({data["MAX%_MEM"][0]:.1f}%)'
          f'\nБольше всего CPU использует: {data["MAX%_CPU"][1][:20]} ({data["MAX%_CPU"][0]:.1f}%)')

print(result)

datatime = strftime('%d-%m-%Y-%H:%M:%S', gmtime())
with open(f'{datatime}-scan.txt', 'w', encoding='utf-8') as file:
    file.write(result)
