import json
import PySimpleGUI as pg
import quiz_backend as qb
import time


def start_quiz():
    global score
    global ans_give
    for ind, quest in enumerate(quiz):

        window['head'].update(f'Question {ind + 1}')
        window['txt'].update(quest['Question'])
        window['1'].update(False, text=quest['Options'][0], visible=True)
        window['2'].update(False, text=quest['Options'][1], visible=True)
        window['3'].update(False, text=quest['Options'][2], visible=True)
        window['4'].update(False, text=quest['Options'][3], visible=True)
        # print(option1)
        window['Sub'].update(visible=False)
        events, values = window.read()
        print(events, values)
        while events != 'Sub':
            window['Sub'].update('Submit', visible=True)
            events, values = window.read()
            print(events, values)

        ans_give = {value: key for (key, value) in values.items() if value}

        if ans_give[True] == quest['Answer']:
            score += 1
        else:
            score += 0


retry = True
while True:
    if retry:

        radio_button_config = {'enable_events': True,
                               'visible': False,
                               'expand_x': True,
                               'expand_y': True,
                               'font': ('Times', 30)}

        title_text = {'justification': 'center',
                      'expand_x': True,
                      'expand_y': True}

        head = pg.Text("Welcome to Quiz contest '22", auto_size_text=True, key='head',
                       font=('Times', 50), **title_text)

        question = pg.Text(" ", auto_size_text=True, key='txt', font=('Times', 30), **title_text)

        button1 = pg.Button('Continue', key='Sub', expand_x=True, font=('Times', 14))

        option1 = pg.Radio(' ', 'group1', key='1', **radio_button_config)
        option2 = pg.Radio(' ', 'group1', key='2', **radio_button_config)
        option3 = pg.Radio(' ', 'group1', key='3', **radio_button_config)
        option4 = pg.Radio(' ', 'group1', key='4', **radio_button_config)

        window = pg.Window(title='Quiz Contest'
                           , layout=[[head],
                                     [question],
                                     [option1], [option2], [option3], [option4],
                                     [button1]],
                           resizable=True, auto_size_text=True)

        window.read()
        quiz = qb.get_all_questions()
        # print(quiz)
        ans_give = {}
        score = 0
        start_quiz()
        pg.popup_notify('Quiz Completed. Wait a while for result')
        time.sleep(2)

        if score / len(quiz) > 0.50:
            pg.popup(f'Congratulation!!! Quiz passed \n'
                     f'SCORE: {score}/{len(quiz)}')
            retry = False
        else:
            response = pg.popup_ok_cancel(f'Sorry!!! Quiz failed. \n'
                                          f'SCORE: {score}/{len(quiz)} \n\n'
                                          f'Press ok for retest?')
            if response == 'Cancel':
                window.close()
                retry = False
            else:
                window.close()
                retry = True

    if not retry:
        break
