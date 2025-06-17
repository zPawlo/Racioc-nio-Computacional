import json

# Dados iniciais
estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []

# Funções para manipular arquivos
def salvar_dados_em_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo)

def recuperar_dados_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Funções para cada funcionalidade
def incluir_registro(registros, nome_arquivo, campos):
    novo_registro = {}
    for campo in campos:
        while True:
            valor = input(f"{campo}: ")
            if valor:
                novo_registro[campo] = valor
                break
            else:
                print("Valor inválido. Por favor, entre com um valor válido.")
    registros.append(novo_registro)
    salvar_dados_em_arquivo(nome_arquivo, registros)
    print("Registro incluído com sucesso!")

def listar_registros(registros):
    if registros:
        for registro in registros:
            for campo, valor in registro.items():
                print(f"{campo}: {valor}")
            print()
    else:
        print("Nenhum registro encontrado.")

def excluir_registro(registros, nome_arquivo, campo_chave):
    chave = input(f"Entre com o {campo_chave} do registro que deseja excluir: ")
    for registro in registros:
        if registro[campo_chave] == chave:
            registros.remove(registro)
            salvar_dados_em_arquivo(nome_arquivo, registros)
            print("Registro excluído com sucesso!")
            return
    print("Registro não encontrado.")

def alterar_registro(registros, nome_arquivo, campo_chave):
    chave = input(f"Entre com o {campo_chave} do registro que deseja alterar: ")
    for registro in registros:
        if registro[campo_chave] == chave:
            for campo, valor in registro.items():
                novo_valor = input(f"Novo {campo} ({valor}): ")
                if novo_valor:
                    registro[campo] = novo_valor
            salvar_dados_em_arquivo(nome_arquivo, registros)
            print("Registro alterado com sucesso!")
            return
    print("Registro não encontrado.")

# Carregar dados do arquivo
estudantes = recuperar_dados_do_arquivo("estudantes.json")
disciplinas = recuperar_dados_do_arquivo("disciplinas.json")
professores = recuperar_dados_do_arquivo("professores.json")
turmas = recuperar_dados_do_arquivo("turmas.json")
matriculas = recuperar_dados_do_arquivo("matriculas.json")

# Menu principal
while True:
    print("Menu Principal:")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")
    opcao_principal = input("Opção: ")

    if opcao_principal == "1":
        while True:
            print("Menu de Operações:")
            print("1. Incluir")
            print("2. Listar")
            print("3. Excluir")
            print("4. Alterar")
            print("5. Voltar ao menu principal")
            opcao_operacao = input("Opção: ")

            if opcao_operacao == "1":
                incluir_registro(estudantes, "estudantes.json", ["codigo", "nome", "cpf"])
            elif opcao_operacao == "2":
                listar_registros(estudantes)
            elif opcao_operacao == "3":
                excluir_registro(estudantes, "estudantes.json", "codigo")
            elif opcao_operacao == "4":
                alterar_registro(estudantes, "estudantes.json", "codigo")
            elif opcao_operacao == "5":
                break
            else:
                print("Opção inválida")

    elif opcao_principal == "2":
        while True:
            print("Menu de Operações:")
            print("1. Incluir")
            print("2. Listar")
            print("3. Excluir")
            print("4. Alterar")
            print("5. Voltar ao menu principal")
            opcao_operacao = input("Opção: ")

            if opcao_operacao == "1":
                incluir_registro(disciplinas, "disciplinas.json", ["codigo", "nome"])
            elif opcao_operacao == "2":
                listar_registros(disciplinas)
            elif opcao_operacao == "3":
                excluir_registro(disciplinas, "disciplinas.json", "codigo")
            elif opcao_operacao == "4":
                alterar_registro(disciplinas, "disciplinas.json", "codigo")
            elif opcao_operacao == "5":
                break
            else:
                print("Opção inválida")

    elif opcao_principal == "3":
        while True:
            print("Menu de Operações:")
            print("1. Incluir")
            print("2. Listar")
            print("3. Excluir")
            print("4. Alterar")
            print("5. Voltar ao menu principal")
            opcao_operacao = input("Opção: ")

            if opcao_operacao == "1":
                incluir_registro(professores, "professores.json", ["codigo", "nome", "cpf"])
            elif opcao_operacao == "2":
                listar_registros(professores)
            elif opcao_operacao == "3":
                excluir_registro(professores, "professores.json", "codigo")
            elif opcao_operacao == "4":
                alterar_registro(professores, "professores.json", "codigo")
            elif opcao_operacao == "5":
                break
            else:
                print("Opção inválida")

    elif opcao_principal == "4":
        while True:
            print("Menu de Operações:")
            print("1. Incluir")
            print("2. Listar")
            print("3. Excluir")
            print("4. Alterar")
            print("5. Voltar ao menu principal")
            opcao_operacao = input("Opção: ")

            if opcao_operacao == "1":
                codigo_turma = input("Código da turma: ")
                if any(turma["codigo"] == codigo_turma for turma in turmas):
                    print("Código de turma já existente. Por favor, entre com um código diferente.")
                else:
                    codigo_professor = input("Código do professor: ")
                    if not any(professor["codigo"] == codigo_professor for professor in professores):
                        print("Código de professor não encontrado.")
                    else:
                        codigo_disciplina = input("Código da disciplina: ")
                        if not any(disciplina["codigo"] == codigo_disciplina for disciplina in disciplinas):
                            print("Código de disciplina não encontrado.")
                        else:
                            turma = {
                                "codigo": codigo_turma,
                                "codigo_professor": codigo_professor,
                                "codigo_disciplina": codigo_disciplina
                            }
                            turmas.append(turma)
                            salvar_dados_em_arquivo("turmas.json", turmas)
                            print("Turma incluída com sucesso!")

            elif opcao_operacao == "2":
                listar_registros(turmas)
            elif opcao_operacao == "3":
                excluir_registro(turmas, "turmas.json", "codigo")
            elif opcao_operacao == "4":
                alterar_registro(turmas, "turmas.json", "codigo")
            elif opcao_operacao == "5":
                break
            else:
                print("Opção inválida")

    elif opcao_principal == "5":
        while True:
            print("Menu de Operações:")
            print("1. Incluir")
            print("2. Listar")
            print("3. Excluir")
            print("4. Alterar")
            print("5. Voltar ao menu principal")
            opcao_operacao = input("Opção: ")

            if opcao_operacao == "1":
                codigo_turma = input("Código da turma: ")
                if not any(turma["codigo"] == codigo_turma for turma in turmas):
                    print("Código de turma não encontrado.")
                else:
                    codigo_estudante = input("Código do estudante: ")
                    if not any(estudante["codigo"] == codigo_estudante for estudante in estudantes):
                        print("Código de estudante não encontrado.")
                    else:
                        matricula = {
                            "codigo_turma": codigo_turma,
                            "codigo_estudante": codigo_estudante
                        }
                        matriculas.append(matricula)
                        salvar_dados_em_arquivo("matriculas.json", matriculas)
                        print("Matrícula incluída com sucesso!")

            elif opcao_operacao == "2":
                listar_registros(matriculas)
            elif opcao_operacao == "3":
                excluir_registro(matriculas, "matriculas.json", "codigo_turma")
            elif opcao_operacao == "4":
                alterar_registro(matriculas, "matriculas.json", "codigo_turma")
            elif opcao_operacao == "5":
                break
            else:
                print("Opção inválida")

    elif opcao_principal == "6":
        break
    else:
        print("Opção inválida")
