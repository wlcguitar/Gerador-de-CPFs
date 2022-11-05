import PySimpleGUI as sg

#Função criada para gerar um cpf matematicamente válido.
def gerador_cpf():
    from random import randint
    cpf = str(randint(100000000, 999999999))
    cont = 10
    cont1 = 11
    soma = mult = soma1 = mult1 = 0
    for v in cpf:
        mult = int(v) * cont
        mult1 = int(v) * cont1
        soma1 += mult1
        soma += mult
        cont -= 1
        cont1 -= 1
    dig1 = 11 - (soma % 11)
    if dig1 > 9:
        dig1 = 0
    dig2 = 11 - ((soma1 + (dig1 * 2)) % 11)
    if dig2 > 9:
        dig2 = 0
    return "{}-{}{}".format(cpf, dig1, dig2)

    
#layout
sg.theme('BlueMono')
layout = [
    [sg.Image(filename="image\cpf.png")],
    [sg.Text("Cpf matematicamente válidos")],
    [sg.InputText('', key='result', size=(35, 1))],
    [sg.Button('Gerar CPF'), sg.Button('Cancelar')],
]
#Janela
janela = sg.Window('CPF\cpf.png', layout)
#Programa principal / Leitura
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Gerar CPF':
        janela['result'].update(gerador_cpf())