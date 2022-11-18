
ordens = ['20010102', '3030304050', '40005004305', '20067802', '3030356750',
          '400050056775', '3030304050', '24505004305', '30067802', '4030356750']

for ordem in ordens:
    if ordem[0] == '2':
        print(f'Ordem {ordem} - Manutenção Preventiva')
    elif ordem[0] == '3':
        print(f'Ordem {ordem} - Manutenção Corretiva')
    else:
        print(f'Ordem {ordem} - Manutenção Preditiva')
