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


# Bounded Contexts do Bazarium

## Introdução
O **Bazarium** é um marketplace digital que adota uma arquitetura baseada em **Bounded Contexts** para organizar e modularizar suas funcionalidades. Essa segmentação permite que diferentes partes do sistema operem de forma independente, facilitando a escalabilidade, manutenção e evolução da plataforma.

## Contextos Delimitados
A plataforma é segmentada em diferentes contextos funcionais, cada um com responsabilidades bem definidas:

### 1️⃣ **Contexto de Usuário**
Responsável pelo gerenciamento de identidade e acesso dos usuários.
- **Principais funcionalidades**:
  - Cadastro e autenticação.
  - Gerenciamento de perfis (comprador/vendedor/admin).
  - Segurança e autenticação multifator (MFA).

### 2️⃣ **Contexto de Catálogo**
Gerencia os produtos disponíveis no **Bazarium**.
- **Principais funcionalidades**:
  - Cadastro, edição e exclusão de produtos.
  - Organização em categorias e gerenciamento de estoque.
  - Regras de visibilidade e precificação dinâmica.

### 3️⃣ **Contexto de Venda**
Abrange todo o fluxo de compra até a geração do pedido.
- **Principais funcionalidades**:
  - Adição de produtos ao carrinho.
  - Processamento de checkout e cálculo de totais.
  - Criação e rastreamento de pedidos.

### 4️⃣ **Contexto de Pagamento**
Responsável pelo processamento financeiro das transações.
- **Principais funcionalidades**:
  - Integração com gateways de pagamento.
  - Processamento de autorizações e recusas.
  - Emissão de notas fiscais e controle de reembolsos.

### 5️⃣ **Contexto de Entrega**
Gerencia a logística e rastreamento dos pedidos.
- **Principais funcionalidades**:
  - Cálculo de frete e estimativa de prazos.
  - Geração de códigos de rastreamento.
  - Atualização automática do status de entrega.

### 6️⃣ **Contexto de Avaliação**
Controla o sistema de reputação dos produtos e vendedores.
- **Principais funcionalidades**:
  - Registro de avaliações e feedbacks.
  - Cálculo da reputação do vendedor.
  - Moderação de avaliações inadequadas.

### 7️⃣ **Contexto de Notificação**
Orquestra a comunicação entre a plataforma e os usuários.
- **Principais funcionalidades**:
  - Envio de notificações transacionais.
  - Comunicação entre compradores e vendedores.
  - Divulgação de promoções e alertas personalizados.

### 8️⃣ **Contexto de Relatórios**
Fornece insights e métricas operacionais para vendedores e administradores.
- **Principais funcionalidades**:
  - Geração de relatórios financeiros.
  - Monitoramento de desempenho de vendas.
  - Indicadores de experiência do usuário.

## Benefícios da Segmentação
A adoção de **Bounded Contexts** no **Bazarium** permite:
- **Modularidade**: Cada contexto pode evoluir independentemente.
- **Escalabilidade**: Possibilidade de distribuir serviços para melhor performance.
- **Manutenção facilitada**: Isolamento de responsabilidades reduzindo impacto de mudanças.
- **Maior segurança**: Controle granular sobre permissões e acesso aos dados.

## Conclusão
A segmentação do **Bazarium** em diferentes contextos delimitados permite uma arquitetura organizada e escalável, garantindo melhor desempenho e facilidade de manutenção. Essa abordagem facilita a evolução contínua da plataforma, garantindo que cada funcionalidade opere de forma independente e otimizada.

# Personas do Bazarium

## Introdução
O **Bazarium** atende a diferentes perfis de usuários, cada um com necessidades específicas dentro do ecossistema do marketplace. A definição das personas auxilia no desenvolvimento de funcionalidades otimizadas para cada tipo de usuário.

## Personas Principais
A seguir, são descritos os principais perfis de usuários do **Bazarium**:

### 1️⃣ **Comprador 🛒**
Usuário interessado em adquirir produtos na plataforma.

🔹 **Objetivos**:
- Encontrar e comprar produtos de forma rápida e segura.
- Comparar preços e avaliações antes da compra.
- Acompanhar pedidos e receber notificações de entrega.
- Solicitar reembolso ou devolução, se necessário.

🔹 **Principais necessidades**:
- Interface intuitiva para busca e filtros avançados.
- Métodos de pagamento variados e seguros.
- Rastreamento detalhado dos pedidos.
- Sistema de avaliação de vendedores e produtos.

### 2️⃣ **Vendedor 🏪**
Usuário que cadastra e gerencia produtos para venda na plataforma.

🔹 **Objetivos**:
- Cadastrar e gerenciar produtos com descrição, imagens e preços.
- Monitorar estoque e definir promoções.
- Processar pedidos e gerenciar envios.
- Receber avaliações e interagir com clientes.

🔹 **Principais necessidades**:
- Dashboard para monitoramento de vendas e métricas.
- Ferramentas para gestão de promoções e cupons.
- Opções de integração com sistemas de logística.
- Relatórios financeiros para acompanhamento de faturamento.

### 3️⃣ **Administrador do Marketplace 🛠️**
Usuário responsável por gerenciar a plataforma e garantir seu funcionamento adequado.

🔹 **Objetivos**:
- Supervisionar transações e operações na plataforma.
- Garantir conformidade com regulamentações e políticas da empresa.
- Monitorar e mitigar possíveis fraudes ou disputas.
- Gerenciar conteúdos e campanhas promocionais.

🔹 **Principais necessidades**:
- Painéis de monitoramento de transações e métricas de desempenho.
- Ferramentas para análise de segurança e detecção de fraudes.
- Interface para moderação de avaliações e interações entre usuários.
- Controle sobre campanhas de marketing e notificações para usuários.

### 4️⃣ **Gateway de Pagamento 💳 (Sistema Externo)**
Serviço responsável por processar pagamentos e transações financeiras.

🔹 **Objetivos**:
- Autorizar e processar pagamentos de forma segura.
- Emitir notas fiscais e gerenciar estornos.
- Garantir a conformidade das transações financeiras.

🔹 **Principais necessidades**:
- Integração com métodos de pagamento (cartão, boleto, PIX, etc.).
- Monitoramento antifraude e validação de identidade.
- Gestão de reembolsos e disputas de pagamento.

### 5️⃣ **Transportadora/Logística 🚚 (Sistema Externo ou Parceiro)**
Responsável por realizar a entrega dos pedidos aos compradores.

🔹 **Objetivos**:
- Definir custos e prazos de envio.
- Gerar código de rastreamento e atualizar status de entrega.
- Garantir a segurança e eficiência no transporte dos produtos.

🔹 **Principais necessidades**:
- Integração via API para atualização de status.
- Automação de cálculo de frete e tempo estimado de entrega.
- Registro de reclamações e suporte para problemas logísticos.

## Conclusão
A definição clara das personas no **Bazarium** permite um desenvolvimento mais focado nas necessidades específicas de cada usuário. Com essa segmentação, a plataforma pode otimizar a experiência e garantir um funcionamento eficiente para compradores, vendedores, administradores e parceiros logísticos.

# Jornadas do Usuário no Bazarium

## Introdução
As jornadas dos usuários no **Bazarium** representam o fluxo de interações dentro da plataforma, garantindo que cada perfil de usuário tenha uma experiência eficiente e intuitiva. A seguir, são detalhadas as principais jornadas para cada persona.

---

## 🛒 **Jornada do Comprador**

### 1️⃣ **Cadastro e Autenticação**
- O usuário acessa a plataforma e inicia o cadastro.
- Informa dados pessoais e cria uma conta.
- Realiza autenticação via e-mail ou autenticação multifator (MFA).

### 2️⃣ **Busca e Seleção de Produtos**
- Utiliza filtros e categorias para encontrar produtos.
- Visualiza detalhes, avaliações e comparações.
- Adiciona itens ao carrinho de compras.

### 3️⃣ **Processo de Compra e Pagamento**
- Revisa os produtos no carrinho.
- Escolhe o método de pagamento e confirma a compra.
- Recebe notificação sobre a aprovação do pagamento.

### 4️⃣ **Acompanhamento de Pedido e Entrega**
- Recebe atualizações sobre status do pedido.
- Consulta código de rastreamento da transportadora.
- Confirma recebimento do produto.

### 5️⃣ **Avaliação do Produto e Vendedor**
- Registra feedback sobre a experiência de compra.
- Atribui nota e comentários ao produto e ao vendedor.

### 6️⃣ **Solicitação de Suporte ou Devolução**
- Acessa a central de ajuda.
- Solicita reembolso ou troca conforme política de devolução.

---

## 🏪 **Jornada do Vendedor**

### 1️⃣ **Cadastro e Configuração da Loja**
- O vendedor cria uma conta e define perfil comercial.
- Configura métodos de pagamento e políticas de envio.

### 2️⃣ **Gestão de Produtos e Estoque**
- Cadastra novos produtos com descrições e imagens.
- Define preços e controle de estoque.
- Publica e gerencia ofertas e promoções.

### 3️⃣ **Recebimento e Processamento de Pedidos**
- Recebe notificações sobre novas vendas.
- Confirma a disponibilidade do produto.
- Organiza e despacha o pedido via transportadora.

### 4️⃣ **Atendimento ao Cliente e Avaliações**
- Responde perguntas de compradores.
- Gerencia avaliações e feedbacks recebidos.

### 5️⃣ **Monitoramento e Relatórios**
- Acompanha métricas de vendas e desempenho.
- Ajusta estratégias de preço e marketing com base nos relatórios.

---

## 🛠 **Jornada do Administrador do Marketplace**

### 1️⃣ **Monitoramento da Plataforma**
- Supervisiona métricas gerais de tráfego e transações.
- Garante conformidade com regulamentações e políticas.

### 2️⃣ **Gerenciamento de Disputas e Moderação**
- Avalia disputas entre compradores e vendedores.
- Modera avaliações e interações na plataforma.

### 3️⃣ **Segurança e Compliance**
- Implementa medidas contra fraudes.
- Analisa transações suspeitas.

### 4️⃣ **Campanhas e Promoções**
- Configura promoções globais da plataforma.
- Dispara notificações e campanhas para usuários.

---

## 💳 **Jornada do Gateway de Pagamento**

### 1️⃣ **Autorização de Pagamento**
- Recebe requisição de pagamento.
- Processa autorização ou recusa.
- Informa a plataforma sobre o status do pagamento.

### 2️⃣ **Emissão de Nota Fiscal e Confirmação**
- Gera nota fiscal eletrônica após pagamento aprovado.
- Envia confirmação para o comprador e vendedor.

### 3️⃣ **Gerenciamento de Reembolsos**
- Recebe solicitações de estorno.
- Processa devoluções de valores conforme política da plataforma.

---

## 🚚 **Jornada da Transportadora**

### 1️⃣ **Cálculo de Frete**
- Recebe requisição de cálculo com base no endereço do comprador.
- Retorna valor e prazo estimado para entrega.

### 2️⃣ **Coleta e Envio do Pedido**
- Recebe notificação de pedido pronto para envio.
- Gera código de rastreamento.
- Transporta o produto até o comprador.

### 3️⃣ **Atualização de Status e Confirmação de Entrega**
- Atualiza status de envio em tempo real.
- Confirma entrega bem-sucedida na plataforma.

---

## Conclusão
A definição das jornadas no **Bazarium** permite uma estruturação clara dos fluxos de interação dos usuários. Isso garante que todas as personas tenham uma experiência otimizada e que os processos sejam organizados para eficiência e escalabilidade da plataforma.

