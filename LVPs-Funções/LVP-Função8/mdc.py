def f_mdc(a, b):
    while(b):
        a, b = b, a % b
    return a

def f_mdc_tres(num1, num2, num3):
    #declaração de variáveis
    mdc1 = int(0)
    mdc_final = int(0)
    
    #processamento
    mdc1 = f_mdc(num1, num2)
    mdc_final = f_mdc(mdc1, num3)
    return mdc_final