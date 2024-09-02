SentencaDoPalindromo = input("escreva o que você deseja saber se é palindromo ou não: ").lower().strip()

SentençaLimpa = ''.join(caracteres for caracteres in SentencaDoPalindromo if caracteres.isalnum())

InversoSentenca = SentençaLimpa[::-1]


if SentençaLimpa == InversoSentenca:
    print("é palindromo")
elif SentençaLimpa != InversoSentenca:
    print("não é palindromo")