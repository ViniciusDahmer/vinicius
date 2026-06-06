import json
import os
from datetime import datetime

# Arquivo para armazenar dados
ARQUIVO_DADOS = "dados_marcenaria.json"

# Cores para terminal
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"

def carregar_dados():
    """Carrega dados do arquivo JSON"""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "produtos": [],
        "clientes": [],
        "orcamentos": [],
        "vendas": []
    }

def salvar_dados(dados):
    """Salva dados no arquivo JSON"""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu_principal():
    """Exibe o menu principal"""
    limpar_tela()
    print(f"{AZUL}=======================")
    print("SISTEMA DA MARCENARIA")
    print("======================={RESET}\n")
    print(f"{VERDE}1. Gerenciar Produtos")
    print("2. Gerenciar Clientes")
    print("3. Criar Orçamento")
    print("4. Consultar Orçamentos")
    print("5. Registrar Venda")
    print("6. Consultar Vendas")
    print("7. Relatórios")
    print(f"0. Sair{RESET}\n")

def menu_produtos(dados):
    """Menu de gerenciamento de produtos"""
    while True:
        limpar_tela()
        print(f"{AZUL}=== PRODUTOS ==={RESET}\n")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Remover Produto")
        print("0. Voltar\n")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            limpar_tela()
            print(f"{VERDE}--- Adicionar Novo Produto ---{RESET}\n")
            nome = input("Nome do produto: ").strip()
            try:
                preco = float(input("Preço unitário (R$): "))
                descricao = input("Descrição: ").strip()
                
                produto = {
                    "id": len(dados["produtos"]) + 1,
                    "nome": nome,
                    "preco": preco,
                    "descricao": descricao
                }
                dados["produtos"].append(produto)
                salvar_dados(dados)
                print(f"{VERDE}✓ Produto adicionado com sucesso!{RESET}")
            except ValueError:
                print(f"{VERMELHO}✗ Preço inválido!{RESET}")
            input("Pressione Enter para continuar...")
        
        elif opcao == "2":
            limpar_tela()
            print(f"{VERDE}--- Lista de Produtos ---{RESET}\n")
            if dados["produtos"]:
                for p in dados["produtos"]:
                    print(f"ID: {p['id']} | {p['nome']} | R$ {p['preco']:.2f}")
                    print(f"   Descrição: {p['descricao']}")
            else:
                print("Nenhum produto cadastrado.")
            input("\nPressione Enter para continuar...")
        
        elif opcao == "3":
            limpar_tela()
            print(f"{VERDE}--- Atualizar Produto ---{RESET}\n")
            try:
                id_produto = int(input("ID do produto: "))
                produto = next((p for p in dados["produtos"] if p["id"] == id_produto), None)
                if produto:
                    print(f"\nProduto atual: {produto['nome']} | R$ {produto['preco']:.2f}")
                    novo_nome = input("Novo nome (deixe em branco para manter): ").strip()
                    if novo_nome:
                        produto["nome"] = novo_nome
                    novo_preco = input("Novo preço (deixe em branco para manter): ").strip()
                    if novo_preco:
                        produto["preco"] = float(novo_preco)
                    salvar_dados(dados)
                    print(f"{VERDE}✓ Produto atualizado!{RESET}")
                else:
                    print(f"{VERMELHO}✗ Produto não encontrado!{RESET}")
            except ValueError:
                print(f"{VERMELHO}✗ Dados inválidos!{RESET}")
            input("Pressione Enter para continuar...")
        
        elif opcao == "4":
            limpar_tela()
            print(f"{VERDE}--- Remover Produto ---{RESET}\n")
            try:
                id_produto = int(input("ID do produto: "))
                produto = next((p for p in dados["produtos"] if p["id"] == id_produto), None)
                if produto:
                    dados["produtos"].remove(produto)
                    salvar_dados(dados)
                    print(f"{VERDE}✓ Produto removido!{RESET}")
                else:
                    print(f"{VERMELHO}✗ Produto não encontrado!{RESET}")
            except ValueError:
                print(f"{VERMELHO}✗ ID inválido!{RESET}")
            input("Pressione Enter para continuar...")
        
        elif opcao == "0":
            break

def menu_clientes(dados):
    """Menu de gerenciamento de clientes"""
    while True:
        limpar_tela()
        print(f"{AZUL}=== CLIENTES ==={RESET}\n")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Cliente")
        print("4. Remover Cliente")
        print("0. Voltar\n")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            limpar_tela()
            print(f"{VERDE}--- Adicionar Novo Cliente ---{RESET}\n")
            nome = input("Nome do cliente: ").strip()
            telefone = input("Telefone: ").strip()
            email = input("Email: ").strip()
            
            cliente = {
                "id": len(dados["clientes"]) + 1,
                "nome": nome,
                "telefone": telefone,
                "email": email,
                "data_cadastro": datetime.now().strftime("%d/%m/%Y")
            }
            dados["clientes"].append(cliente)
            salvar_dados(dados)
            print(f"{VERDE}✓ Cliente adicionado com sucesso!{RESET}")
            input("Pressione Enter para continuar...")
        
        elif opcao == "2":
            limpar_tela()
            print(f"{VERDE}--- Lista de Clientes ---{RESET}\n")
            if dados["clientes"]:
                for c in dados["clientes"]:
                    print(f"ID: {c['id']} | {c['nome']}")
                    print(f"   Tel: {c['telefone']} | Email: {c['email']}")
            else:
                print("Nenhum cliente cadastrado.")
            input("\nPressione Enter para continuar...")
        
        elif opcao == "3":
            limpar_tela()
            print(f"{VERDE}--- Atualizar Cliente ---{RESET}\n")
            try:
                id_cliente = int(input("ID do cliente: "))
                cliente = next((c for c in dados["clientes"] if c["id"] == id_cliente), None)
                if cliente:
                    print(f"\nCliente: {cliente['nome']}")
                    novo_nome = input("Novo nome (deixe em branco para manter): ").strip()
                    if novo_nome:
                        cliente["nome"] = novo_nome
                    novo_telefone = input("Novo telefone (deixe em branco para manter): ").strip()
                    if novo_telefone:
                        cliente["telefone"] = novo_telefone
                    novo_email = input("Novo email (deixe em branco para manter): ").strip()
                    if novo_email:
                        cliente["email"] = novo_email
                    salvar_dados(dados)
                    print(f"{VERDE}✓ Cliente atualizado!{RESET}")
                else:
                    print(f"{VERMELHO}✗ Cliente não encontrado!{RESET}")
            except ValueError:
                print(f"{VERMELHO}✗ ID inválido!{RESET}")
            input("Pressione Enter para continuar...")
        
        elif opcao == "4":
            limpar_tela()
            print(f"{VERDE}--- Remover Cliente ---{RESET}\n")
            try:
                id_cliente = int(input("ID do cliente: "))
                cliente = next((c for c in dados["clientes"] if c["id"] == id_cliente), None)
                if cliente:
                    dados["clientes"].remove(cliente)
                    salvar_dados(dados)
                    print(f"{VERDE}✓ Cliente removido!{RESET}")
                else:
                    print(f"{VERMELHO}✗ Cliente não encontrado!{RESET}")
            except ValueError:
                print(f"{VERMELHO}✗ ID inválido!{RESET}")
            input("Pressione Enter para continuar...")
        
        elif opcao == "0":
            break

def criar_orcamento(dados):
    """Cria um novo orçamento"""
    limpar_tela()
    print(f"{VERDE}--- Criar Orçamento ---{RESET}\n")
    
    if not dados["clientes"]:
        print(f"{VERMELHO}✗ Nenhum cliente cadastrado!{RESET}")
        input("Pressione Enter para continuar...")
        return
    
    if not dados["produtos"]:
        print(f"{VERMELHO}✗ Nenhum produto cadastrado!{RESET}")
        input("Pressione Enter para continuar...")
        return
    
    try:
        print("Clientes disponíveis:")
        for c in dados["clientes"]:
            print(f"  ID: {c['id']} | {c['nome']}")
        
        id_cliente = int(input("\nID do cliente: "))
        cliente = next((c for c in dados["clientes"] if c["id"] == id_cliente), None)
        
        if not cliente:
            print(f"{VERMELHO}✗ Cliente não encontrado!{RESET}")
            input("Pressione Enter para continuar...")
            return
        
        print(f"\n{VERDE}Produtos disponíveis:{RESET}")
        for p in dados["produtos"]:
            print(f"  ID: {p['id']} | {p['nome']} | R$ {p['preco']:.2f}")
        
        itens = []
        total = 0
        
        while True:
            id_produto = input("\nID do produto (0 para finalizar): ").strip()
            if id_produto == "0":
                break
            
            try:
                id_produto = int(id_produto)
                produto = next((p for p in dados["produtos"] if p["id"] == id_produto), None)
                
                if produto:
                    quantidade = int(input(f"Quantidade de {produto['nome']}: "))
                    subtotal = produto["preco"] * quantidade
                    total += subtotal
                    
                    itens.append({
                        "produto_id": produto["id"],
                        "produto_nome": produto["nome"],
                        "quantidade": quantidade,
                        "preco_unitario": produto["preco"],
                        "subtotal": subtotal
                    })
                    print(f"{VERDE}✓ Adicionado ao orçamento!{RESET}")
                else:
                    print(f"{VERMELHO}✗ Produto não encontrado!{RESET}")
            except ValueError:
                print(f"{VERMELHO}✗ Dados inválidos!{RESET}")
        
        if itens:
            orcamento = {
                "id": len(dados["orcamentos"]) + 1,
                "cliente_id": cliente["id"],
                "cliente_nome": cliente["nome"],
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "itens": itens,
                "total": total,
                "status": "Pendente"
            }
            dados["orcamentos"].append(orcamento)
            salvar_dados(dados)
            
            print(f"\n{VERDE}=== ORÇAMENTO CRIADO ==={RESET}")
            print(f"ID: {orcamento['id']}")
            print(f"Cliente: {cliente['nome']}")
            print(f"Data: {orcamento['data']}")
            print(f"\n--- Itens ---")
            for item in itens:
                print(f"{item['quantidade']}x {item['produto_nome']} | R$ {item['preco_unitario']:.2f} = R$ {item['subtotal']:.2f}")
            print(f"\n{AMARELO}TOTAL: R$ {total:.2f}{RESET}")
        else:
            print(f"{VERMELHO}✗ Nenhum item adicionado!{RESET}")
    
    except ValueError:
        print(f"{VERMELHO}✗ Dados inválidos!{RESET}")
    
    input("\nPressione Enter para continuar...")

def consultar_orcamentos(dados):
    """Consulta orçamentos"""
    limpar_tela()
    print(f"{VERDE}--- Orçamentos ---{RESET}\n")
    
    if not dados["orcamentos"]:
        print("Nenhum orçamento registrado.")
    else:
        for o in dados["orcamentos"]:
            print(f"ID: {o['id']} | Cliente: {o['cliente_nome']}")
            print(f"Data: {o['data']} | Total: R$ {o['total']:.2f} | Status: {o['status']}")
            print("-" * 60)
            
            opcao = input("Visualizar detalhes? (s/n): ").strip().lower()
            if opcao == 's':
                print(f"\n{AMARELO}=== DETALHES DO ORÇAMENTO {o['id']} ==={RESET}")
                for item in o["itens"]:
                    print(f"{item['quantidade']}x {item['produto_nome']} | R$ {item['preco_unitario']:.2f} = R$ {item['subtotal']:.2f}")
                print(f"\n{VERDE}TOTAL: R$ {o['total']:.2f}{RESET}\n")
    
    input("\nPressione Enter para continuar...")

def registrar_venda(dados):
    """Registra uma venda a partir de um orçamento"""
    limpar_tela()
    print(f"{VERDE}--- Registrar Venda ---{RESET}\n")
    
    orcamentos_pendentes = [o for o in dados["orcamentos"] if o["status"] == "Pendente"]
    
    if not orcamentos_pendentes:
        print(f"{VERMELHO}✗ Nenhum orçamento pendente!{RESET}")
        input("Pressione Enter para continuar...")
        return
    
    print("Orçamentos pendentes:")
    for o in orcamentos_pendentes:
        print(f"ID: {o['id']} | Cliente: {o['cliente_nome']} | Total: R$ {o['total']:.2f}")
    
    try:
        id_orcamento = int(input("\nID do orçamento para vender: "))
        orcamento = next((o for o in dados["orcamentos"] if o["id"] == id_orcamento), None)
        
        if orcamento and orcamento["status"] == "Pendente":
            desconto = float(input("Desconto (R$) [0 para nenhum]: ") or 0)
            forma_pagamento = input("Forma de pagamento (À vista/Parcelado): ").strip()
            
            valor_final = orcamento["total"] - desconto
            
            venda = {
                "id": len(dados["vendas"]) + 1,
                "orcamento_id": orcamento["id"],
                "cliente_nome": orcamento["cliente_nome"],
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "itens": orcamento["itens"],
                "valor_original": orcamento["total"],
                "desconto": desconto,
                "valor_final": valor_final,
                "forma_pagamento": forma_pagamento
            }
            
            dados["vendas"].append(venda)
            orcamento["status"] = "Vendido"
            salvar_dados(dados)
            
            print(f"\n{VERDE}=== VENDA REGISTRADA ==={RESET}")
            print(f"ID da Venda: {venda['id']}")
            print(f"Cliente: {venda['cliente_nome']}")
            print(f"Data: {venda['data']}")
            print(f"Valor Original: R$ {venda['valor_original']:.2f}")
            if desconto > 0:
                print(f"Desconto: R$ {desconto:.2f}")
            print(f"{AMARELO}VALOR FINAL: R$ {valor_final:.2f}{RESET}")
            print(f"Forma de Pagamento: {forma_pagamento}")
        else:
            print(f"{VERMELHO}✗ Orçamento não encontrado ou já foi vendido!{RESET}")
    
    except ValueError:
        print(f"{VERMELHO}✗ Dados inválidos!{RESET}")
    
    input("\nPressione Enter para continuar...")

def consultar_vendas(dados):
    """Consulta vendas"""
    limpar_tela()
    print(f"{VERDE}--- Vendas Registradas ---{RESET}\n")
    
    if not dados["vendas"]:
        print("Nenhuma venda registrada.")
    else:
        total_geral = 0
        for v in dados["vendas"]:
            total_geral += v["valor_final"]
            print(f"ID: {v['id']} | Cliente: {v['cliente_nome']}")
            print(f"Data: {v['data']} | Valor: R$ {v['valor_final']:.2f} | Pagto: {v['forma_pagamento']}")
            print("-" * 60)
        
        print(f"\n{AMARELO}TOTAL DE VENDAS: R$ {total_geral:.2f}{RESET}")
    
    input("\nPressione Enter para continuar...")

def relatorios(dados):
    """Exibe relatórios"""
    while True:
        limpar_tela()
        print(f"{AZUL}=== RELATÓRIOS ==={RESET}\n")
        print("1. Resumo de Vendas")
        print("2. Produtos Mais Vendidos")
        print("3. Clientes Mais Ativos")
        print("0. Voltar\n")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            limpar_tela()
            print(f"{VERDE}--- Resumo de Vendas ---{RESET}\n")
            
            total_vendas = sum(v["valor_final"] for v in dados["vendas"])
            total_desconto = sum(v["desconto"] for v in dados["vendas"])
            
            print(f"Total de Vendas: {len(dados['vendas'])}")
            print(f"Valor Total: R$ {total_vendas:.2f}")
            print(f"Total em Descontos: R$ {total_desconto:.2f}")
            print(f"Ticket Médio: R$ {total_vendas / len(dados['vendas']):.2f if dados['vendas'] else 0:.2f}")
            
            pagto_vista = len([v for v in dados["vendas"] if "vista" in v["forma_pagamento"].lower()])
            pagto_parcelado = len([v for v in dados["vendas"] if "parcelado" in v["forma_pagamento"].lower()])
            
            print(f"\nPagamentos à Vista: {pagto_vista}")
            print(f"Pagamentos Parcelados: {pagto_parcelado}")
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "2":
            limpar_tela()
            print(f"{VERDE}--- Produtos Mais Vendidos ---{RESET}\n")
            
            vendas_por_produto = {}
            for v in dados["vendas"]:
                for item in v["itens"]:
                    nome = item["produto_nome"]
                    if nome not in vendas_por_produto:
                        vendas_por_produto[nome] = {"qtd": 0, "valor": 0}
                    vendas_por_produto[nome]["qtd"] += item["quantidade"]
                    vendas_por_produto[nome]["valor"] += item["subtotal"]
            
            if vendas_por_produto:
                ordenado = sorted(vendas_por_produto.items(), key=lambda x: x[1]["qtd"], reverse=True)
                for nome, dados_prod in ordenado:
                    print(f"{nome}: {dados_prod['qtd']} unidades | R$ {dados_prod['valor']:.2f}")
            else:
                print("Nenhum produto vendido.")
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "3":
            limpar_tela()
            print(f"{VERDE}--- Clientes Mais Ativos ---{RESET}\n")
            
            vendas_por_cliente = {}
            for v in dados["vendas"]:
                cliente = v["cliente_nome"]
                if cliente not in vendas_por_cliente:
                    vendas_por_cliente[cliente] = {"qtd": 0, "valor": 0}
                vendas_por_cliente[cliente]["qtd"] += 1
                vendas_por_cliente[cliente]["valor"] += v["valor_final"]
            
            if vendas_por_cliente:
                ordenado = sorted(vendas_por_cliente.items(), key=lambda x: x[1]["valor"], reverse=True)
                for cliente, dados_cli in ordenado:
                    print(f"{cliente}: {dados_cli['qtd']} compras | Total: R$ {dados_cli['valor']:.2f}")
            else:
                print("Nenhum cliente com vendas.")
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "0":
            break

def main():
    """Função principal"""
    dados = carregar_dados()
    
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            menu_produtos(dados)
        elif opcao == "2":
            menu_clientes(dados)
        elif opcao == "3":
            criar_orcamento(dados)
        elif opcao == "4":
            consultar_orcamentos(dados)
        elif opcao == "5":
            registrar_venda(dados)
        elif opcao == "6":
            consultar_vendas(dados)
        elif opcao == "7":
            relatorios(dados)
        elif opcao == "0":
            limpar_tela()
            print(f"{VERDE}Obrigado por usar o Sistema da Marcenaria!{RESET}")
            break
        else:
            print(f"{VERMELHO}✗ Opção inválida!{RESET}")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
