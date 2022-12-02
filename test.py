import PySimpleGUI as sg

layout = [[sg.Radio('No.1', "RADIO1", key='r1'),
           sg.Radio('No.2', "RADIO1", key='r2'),
           sg.Radio('No.3', "RADIO1", key='r3')],

          [sg.Button('Reset'), sg.Button('List'), sg.Button('Exit')]]

window = sg.Window('Reset Buttons', font=("Helvetica", 12)).Layout(layout)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'List':
        sg.Popup(values)
    if event == 'Reset':
        window.FindElement('r1').Update(False)
        window.FindElement('r2').Update(False)
        window.FindElement('r3').Update(False)