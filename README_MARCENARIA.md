# 📊 Sistema de Gerenciamento da Marcenaria

Um programa completo para gerenciar vendas, orçamentos, produtos e clientes de uma marcenaria.

## 🎯 Funcionalidades

### 1. **Gerenciar Produtos**
- Adicionar novos produtos (puxadores MDF, ferragens, etc.)
- Definir preços e descrições
- Listar, atualizar e remover produtos
- Manter catálogo atualizado

### 2. **Gerenciar Clientes**
- Cadastrar clientes com nome, telefone e email
- Listar todos os clientes
- Atualizar informações
- Controle de data de cadastro

### 3. **Criar Orçamentos**
- Selecionar cliente
- Adicionar múltiplos produtos com quantidades
- Calcular subtotais automaticamente
- Total do orçamento
- Status de acompanhamento

### 4. **Consultar Orçamentos**
- Visualizar todos os orçamentos
- Detalhar itens e valores
- Acompanhar status (Pendente/Vendido)

### 5. **Registrar Vendas**
- Converter orçamentos em vendas
- Aplicar descontos
- Registrar forma de pagamento (À vista/Parcelado)
- Histórico completo de transações

### 6. **Consultar Vendas**
- Listar todas as vendas realizadas
- Valores finais e descontos aplicados
- Total de vendas

### 7. **Relatórios**
- **Resumo de Vendas**: Total, ticket médio, desconto total
- **Produtos Mais Vendidos**: Quantidade e valor por produto
- **Clientes Mais Ativos**: Histórico de compras por cliente

## 💾 Armazenamento

- Dados salvos em arquivo `dados_marcenaria.json`
- Persiste entre execuções
- Fácil de exportar/backup

## 🚀 Como Usar

1. Execute o programa:
```bash
python sistema_marcenaria.py
```

2. **Primeiro acesso**: Adicione alguns produtos no menu "1. Gerenciar Produtos"

3. **Cadastre clientes** no menu "2. Gerenciar Clientes"

4. **Crie orçamentos** selecionando cliente e adicionando produtos

5. **Registre vendas** quando o cliente aprovar o orçamento

6. **Consulte relatórios** para análise de desempenho

## 📋 Exemplo de Fluxo

```
1. Menu Principal → 1. Gerenciar Produtos → 1. Adicionar Produto
   └─ Adicione: "Puxador MDF Preto" - R$ 15,50
   
2. Menu Principal → 2. Gerenciar Clientes → 1. Adicionar Cliente
   └─ Cadastre: "João Silva" - (11) 98765-4321
   
3. Menu Principal → 3. Criar Orçamento
   └─ Cliente: João Silva
   └─ Adicione 10x Puxador MDF = R$ 155,00
   
4. Menu Principal → 5. Registrar Venda
   └─ Selecione orçamento
   └─ Desconto: R$ 10,00 (opcional)
   └─ Forma de pagamento: À vista
   
5. Menu Principal → 7. Relatórios
   └─ Visualize resumo de vendas
```

## 🎨 Interface

- Cores para melhor visualização (verde para sucesso, vermelho para erro, azul para títulos)
- Menus intuitivos e fáceis de navegar
- Confirmações de ações
- Validação de dados

## 📝 Notas

- Todos os cálculos são feitos automaticamente
- Datas/horas são registradas automaticamente
- Orçamentos não vendidos ficam com status "Pendente"
- Desconto é opcional e em valores absolutos (R$)

---
**Sistema desenvolvido para marcenarias | v1.0**
