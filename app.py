import PySimpleGUI as sg
from utiliti import resultado_imc

sg.theme('Topanga')

def janela_inicial():
    layout = [
        [sg.Text('Idade'),sg.Input(key='Idade',size=(11,1)),sg.Text('Sexo')
            ,sg.Radio('Masculino',group_id='genero',key='Masculino')
            ,sg.Radio('Feminino',group_id='genero',key='Feminino')],
        [sg.Text('Altura(em Centímentros)'),sg.Input(key='Altura',size=(6,1)),
            sg.Text('Peso(em kilos)'),sg.Input(key='Peso',size=(6,1))],
        [sg.Text(key='Status')],
        [sg.Text(key='IMC'),sg.Text(key='Peso Ideal')],
        [sg.Button('Calcular')]
    ]

    return sg.Window('Canculando IMC',layout,finalize=True)

window = janela_inicial()

def main():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Calcular':
            try:
                sexo = f"{'Masculino' if values['Masculino'] else 'Feminino'}"
                idade = values['Idade']
                altura = values['Altura']
                peso = values['Peso']
                status, imc, color, peso_ideal = resultado_imc(sexo,idade,altura,peso)
                window['Status'].update(status,text_color=color,font=("Arial Black",19))
                window['IMC'].update(f"IMC: {imc}",font=('Eras Bold ITC',13),text_color='white')
                if peso_ideal:
                    window['Peso Ideal'].update(f"Peso Ideal: {peso_ideal} kg",
                        font=('Eras Bold ITC',13),text_color='green')
                else:
                    window['Peso Ideal'].update('')
            except ValueError:
                texto ='Por Favor,\nInserir somente números e não deixar campos sem serem preenchidos!!\nNo caso de crianças com menos de 2 anos, inserir Anos.Mês,ou seja, não usar vírgula, mas sim ponto,\nEx: 1.10 ; 0.4 ; 1.2\nJá crianças com mais 2 anos inserir somente anos\nEx: 2 ; 3 ; 4 ...\nExemplo de como dever ser preenchido os Campos Altura e peso:\nEx Campo Altura(todos os valores dever ser em centímentros):\n50 ; 70 ; 100 ; 170 ; 190\nEx Campo Peso(todos os valores dever ser em kilos):\n54 ; 78.92 ; 90.70 ; 100.34'
                sg.popup_error(texto,title='Valor Errado',font=('Consolas',12))

if __name__ == '__main__':
    main()