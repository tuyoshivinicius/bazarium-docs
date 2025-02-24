# Domínio do Bazarium

## Introdução
O **Bazarium** é um marketplace digital estruturado em domínios distintos para garantir modularidade, escalabilidade e manutenibilidade do sistema. Cada domínio representa um conjunto de funcionalidades coesas e bem definidas dentro do ecossistema da plataforma.

## Conceitos Principais
O sistema é segmentado em conceitos fundamentais que organizam sua lógica de negócio:

### 1️⃣ Usuário
Representa qualquer pessoa que interage com o sistema, seja como comprador, vendedor ou administrador.
- **Atributos principais**: ID, nome, e-mail, telefone, tipo de conta (comprador/vendedor/admin), data de cadastro.
- **Regras de negócio**:
  - Um usuário pode ter múltiplos endereços cadastrados.
  - A autenticação é obrigatória para acessar funcionalidades críticas.
  - Usuários podem alternar entre os papéis de comprador e vendedor.

### 2️⃣ Produto
Entidade que representa os itens disponíveis para compra na plataforma.
- **Atributos principais**: ID, nome, descrição, preço, estoque, categoria, imagens.
- **Regras de negócio**:
  - Apenas vendedores podem cadastrar e gerenciar produtos.
  - Cada produto pertence a uma única categoria.
  - O estoque deve ser atualizado após cada venda.

### 3️⃣ Pedido
Refere-se a uma transação iniciada por um comprador ao concluir uma compra.
- **Atributos principais**: ID, comprador, lista de produtos, valor total, status (pendente, pago, enviado, entregue, cancelado).
- **Regras de negócio**:
  - Um pedido só pode ser criado se todos os produtos estiverem disponíveis em estoque.
  - O status do pedido deve ser atualizado conforme o fluxo de processamento.
  - Pedidos podem ser cancelados antes da confirmação de envio.

### 4️⃣ Pagamento
Gerencia o processamento financeiro dentro do **Bazarium**.
- **Atributos principais**: ID da transação, pedido associado, método de pagamento, status da transação (autorizado, recusado, estornado).
- **Regras de negócio**:
  - Somente pedidos com pagamento autorizado são considerados válidos.
  - Pagamentos podem ser reembolsados conforme a política de cancelamento.
  - Integração com gateways de pagamento externos para processamento seguro.

### 5️⃣ Entrega
Controle do fluxo logístico dos pedidos realizados na plataforma.
- **Atributos principais**: ID do envio, pedido associado, código de rastreamento, transportadora, status de entrega (processando, enviado, entregue).
- **Regras de negócio**:
  - Apenas pedidos pagos podem gerar um envio.
  - O código de rastreamento deve ser gerado após a confirmação de envio.
  - O status deve ser atualizado conforme o andamento do transporte.

### 6️⃣ Avaliação
Módulo responsável pelo sistema de reputação dos produtos e vendedores.
- **Atributos principais**: ID, usuário avaliador, produto/vendedor, nota (1-5), comentário, data.
- **Regras de negócio**:
  - Somente compradores que concluíram uma compra podem avaliar um produto.
  - Vendedores podem responder avaliações para fornecer suporte.
  - Avaliações são públicas e influenciam a reputação do vendedor.

## Conclusão
O domínio do **Bazarium** é estruturado para garantir um fluxo eficiente de compra e venda dentro da plataforma. A segmentação em entidades bem definidas permite uma melhor organização do sistema, favorecendo a escalabilidade e a manutenção contínua.