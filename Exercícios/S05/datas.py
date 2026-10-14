from datetime import date, datetime

natal="25/12/2026"
natal=datetime.strptime(natal, "%d/%m/%Y")
texto = input("Digite uma data no formato DD/MM/AAAA: ")
data = datetime.strptime(texto, "%d/%m/%Y")

print("\nVocê tem ",(datetime.today() - data).days//365, "anos.")
print("Nasceu no dia da semana:", data.weekday(),"(0=segunda,1=terça...6=domingo)")
print("E faltam",(natal-datetime.today()).days, "dias para o Natal.\n")
