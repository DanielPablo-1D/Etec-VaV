# DECLARACAO DE USO DE INTELIGENCIA ARTIFICIAL
# Para o desenvolvimento deste projeto, foi utilizada a ferramenta
# de inteligencia artificial ChatGPT, da OpenAI, como auxilio
# na elaboracao e organizacao do codigo.


import json
import os
from datetime import date

DATA_FILE = "controle_gastos.json"
transactions = []


def load_data():
    global transactions

    if not os.path.exists(DATA_FILE):
        transactions = []
        save_data()
        return

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        transactions = data.get("transactions", [])


def save_data():
    data = {
        "transactions": transactions
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def register_income():
    description = input("Descrição da receita: ")

    try:
        amount = float(input("Valor recebido: R$ ").replace(",", "."))
    except ValueError:
        print("Valor inválido.")
        return

    if amount <= 0:
        print("O valor deve ser maior que zero.")
        return

    income = {
        "type": "income",
        "description": description,
        "amount": amount,
        "date": date.today().isoformat()
    }

    transactions.append(income)
    save_data()

    print("Receita cadastrada com sucesso!")


def register_expense():
    description = input("Descrição da despesa: ")

    try:
        amount = float(input("Valor gasto: R$ ").replace(",", "."))
    except ValueError:
        print("Valor inválido.")
        return

    if amount <= 0:
        print("O valor deve ser maior que zero.")
        return

    expense = {
        "type": "expense",
        "description": description,
        "amount": amount,
        "date": date.today().isoformat()
    }

    transactions.append(expense)
    save_data()

    print("Despesa registrada com sucesso!")


def check_balance():
    balance = 0

    for transaction in transactions:
        if transaction["type"] == "income":
            balance += transaction["amount"]

        elif transaction["type"] == "expense":
            balance -= transaction["amount"]

    print(f"\nSaldo atual: R$ {balance:.2f}")

    if balance < 0:
        print("Atenção! Seu saldo está negativo.")


def view_history():
    if len(transactions) == 0:
        print("Nenhuma movimentação registrada.")
        return

    print("\nHISTÓRICO DE MOVIMENTAÇÕES")

    for transaction in transactions:

        if transaction["type"] == "income":
            transaction_type = "Receita"
        else:
            transaction_type = "Despesa"

        print(f"\nTipo: {transaction_type}")
        print(f"Descrição: {transaction['description']}")
        print(f"Valor: R$ {transaction['amount']:.2f}")
        print(f"Data: {transaction['date']}")


def generate_report():
    if len(transactions) == 0:
        print("Nenhuma movimentação registrada.")
        return

    total_income = 0
    total_expense = 0
    income_count = 0
    expense_count = 0

    for transaction in transactions:

        if transaction["type"] == "income":
            total_income += transaction["amount"]
            income_count += 1

        elif transaction["type"] == "expense":
            total_expense += transaction["amount"]
            expense_count += 1

    balance = total_income - total_expense

    print("\nRELATÓRIO FINANCEIRO")
    print(f"Quantidade de receitas: {income_count}")
    print(f"Quantidade de despesas: {expense_count}")
    print(f"Total recebido: R$ {total_income:.2f}")
    print(f"Total gasto: R$ {total_expense:.2f}")
    print(f"Saldo final: R$ {balance:.2f}")

    if balance > 0:
        print("Situação financeira: Saldo positivo.")

    elif balance < 0:
        print("Situação financeira: Saldo negativo.")

    else:
        print("Situação financeira: Saldo zerado.")


def show_menu():
    print("\n===== CONTROLE DE GASTOS =====")
    print("1 - Cadastrar receitas")
    print("2 - Registrar despesas")
    print("3 - Consultar saldo")
    print("4 - Visualizar histórico")
    print("5 - Gerar relatórios")
    print("6 - Sair")


def main():
    load_data()

    while True:
        show_menu()

        option = input("\nEscolha uma opção: ")

        if option == "1":
            register_income()

        elif option == "2":
            register_expense()

        elif option == "3":
            check_balance()

        elif option == "4":
            view_history()

        elif option == "5":
            generate_report()

        elif option == "6":
            save_data()
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


main()