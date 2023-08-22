import PySimpleGUI as sg
from datetime import datetime
import json

base = list()
with open('base.json','r') as openfile:
    base = json.load(openfile)

layout = [  [sg.Text('Digite seu nome completo: '), sg.InputText()],
            [sg.Text('Adicione uma mensagem: '), sg.InputText()],  
            [sg.Button('Ok'), sg.Button('Sair')]    ]

window = sg.Window('Title', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
    if event in ('Ok'):
        name = str(values[0])
        msg = str(values[1])
        
        hj = datetime.now().strftime('%d de %B de %Y - %H:%M')

        sg.popup(name, msg, hj)
        
        base.append(dict(nome = name, info = msg, hj = hj))
        with open('base.json','w') as openfile:
            json.dump(base,openfile, indent=4)

window.close()