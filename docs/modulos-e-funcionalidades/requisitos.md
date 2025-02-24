# Requisitos do Bazarium

## Introdução
Os requisitos do **Bazarium** definem as funcionalidades e restrições técnicas que a plataforma deve atender para garantir sua operação eficiente e segura. Eles estão organizados em **requisitos funcionais** (RF) e **requisitos não funcionais** (RNF).

---

## 📌 **Requisitos Funcionais (RF)**
Os requisitos funcionais descrevem as funcionalidades essenciais da plataforma.

### 👤 **Perfis de Usuário**
- **RF01** - O sistema deverá permitir que cada usuário possua um perfil como Comprador ou Vendedor.
- **RF02** - O sistema deverá permitir que os usuários alternem entre os modos Comprador e Vendedor dentro de uma mesma conta.
- **RF03** - O sistema deverá permitir que os usuários adicionem foto de perfil e informações de contato, como telefone e endereço.
- **RF04** - O sistema deverá permitir que os usuários excluam suas contas permanentemente.

### 🔐 **Cadastro e Autenticação**
- **RF05** - O sistema deverá fornecer funcionalidades de cadastro e login para os usuários.
- **RF06** - O sistema deverá permitir que os usuários atualizem suas informações cadastrais.
- **RF07** - O sistema deverá oferecer a opção de login via redes sociais.
- **RF08** - O sistema deverá implementar autenticação multifator (MFA) para aumentar a segurança.

### 🏪 **Funcionalidades para Vendedores**
- **RF09** - O sistema deverá permitir que os vendedores cadastrem produtos no catálogo.
- **RF10** - O sistema deverá disponibilizar uma interface para que os vendedores possam acessar a lista de suas vendas.
- **RF11** - O sistema deverá permitir que os vendedores atualizem o status de suas vendas.
- **RF12** - O sistema deverá permitir que os vendedores criem promoções e cupons de desconto.

### 🛒 **Funcionalidades para Compradores**
- **RF13** - O sistema deverá permitir que os compradores adicionem produtos ao carrinho de compras.
- **RF14** - O sistema deverá permitir que os compradores finalizem a compra por meio de um checkout.
- **RF15** - O sistema deverá gerar um pedido no momento da finalização da compra.
- **RF16** - O sistema deverá permitir que os compradores solicitem reembolso ou devolução.

### ⭐ **Avaliações e Comentários**
- **RF17** - O sistema deverá permitir que os compradores avaliem os produtos após a compra.
- **RF18** - O sistema deverá permitir que os compradores publiquem comentários sobre os produtos adquiridos.
- **RF19** - O sistema deverá exibir as avaliações e comentários de compradores na página do produto.
- **RF20** - O sistema deverá calcular a média das notas recebidas por um vendedor.

### 📑 **Catálogo de Produtos e Pesquisa**
- **RF21** - O sistema deverá disponibilizar um catálogo de produtos.
- **RF22** - O sistema deverá permitir que os usuários filtrem e ordenem os produtos no catálogo.
- **RF23** - O sistema deverá permitir que os compradores utilizem filtros avançados.
- **RF24** - O sistema deverá sugerir produtos com base no histórico de navegação.

### 💳 **Pagamentos e Segurança**
- **RF25** - O sistema deverá permitir que os compradores escolham entre diferentes formas de pagamento.
- **RF26** - O sistema deverá processar transações financeiras utilizando gateways seguros.
- **RF27** - O sistema deverá permitir a emissão automática de notas fiscais eletrônicas.
- **RF28** - O sistema deverá bloquear transações suspeitas e alertar administradores sobre fraudes.

### 🚚 **Sistema de Envio e Logística**
- **RF29** - O sistema deverá permitir que os vendedores definam opções de envio.
- **RF30** - O sistema deverá calcular automaticamente o valor do frete.
- **RF31** - O sistema deverá gerar um número de rastreamento para o comprador.
- **RF32** - O sistema deverá integrar com APIs de envio para atualização do status do envio.

### 🔔 **Notificações e Comunicação**
- **RF33** - O sistema deverá ser capaz de notificar os usuários por diferentes canais.
- **RF34** - O sistema deverá permitir que vendedores e compradores se comuniquem diretamente pelo sistema.
- **RF35** - O sistema deverá enviar alertas automáticos sobre mudanças no status dos pedidos.
- **RF36** - O sistema deverá permitir que os administradores enviem anúncios promocionais.

### 📊 **Relatórios e Análises**
- **RF37** - O sistema deverá fornecer aos vendedores relatórios detalhados sobre suas vendas.
- **RF38** - O sistema deverá fornecer relatórios financeiros para os administradores.

---

## 📌 **Requisitos Não Funcionais (RNF)**
Os requisitos não funcionais definem critérios de desempenho, segurança e usabilidade.

### ⚡ **Desempenho e Escalabilidade**
- **RNF01** - O processamento das vendas deverá ser assíncrono.
- **RNF02** - O tempo de resposta das páginas do sistema não deverá ultrapassar 2 segundos.
- **RNF03** - O sistema deverá suportar pelo menos 10.000 usuários simultâneos.
- **RNF04** - O sistema deverá ser capaz de realizar pelo menos 1.000 transações por minuto.

### 🏗 **Arquitetura e Extensibilidade**
- **RNF05** - A arquitetura do sistema deverá ser extensível para suportar novos gateways de pagamento.
- **RNF06** - A arquitetura do sistema deverá ser extensível para suportar novas APIs de envio.
- **RNF07** - O sistema deverá utilizar arquitetura baseada em microsserviços.
- **RNF08** - O sistema deverá ser compatível com diferentes navegadores modernos.

### 🎨 **Usabilidade e Experiência do Usuário**
- **RNF09** - O sistema deverá fornecer uma interface intuitiva e responsiva.
- **RNF10** - O sistema deverá apresentar feedback visual e notificações claras.
- **RNF11** - O sistema deverá ter um design responsivo.
- **RNF12** - O sistema deverá oferecer autocompletar e sugestões inteligentes na busca de produtos.

### 🔒 **Segurança**
- **RNF13** - O sistema deverá utilizar autenticação segura para login.
- **RNF14** - O sistema deverá armazenar e transmitir dados sensíveis de forma criptografada.
- **RNF15** - O sistema deverá garantir que apenas usuários autenticados possam acessar informações confidenciais.
- **RNF16** - O sistema deverá suportar autenticação multifator (MFA).
- **RNF17** - O sistema não deverá armazenar informações completas de cartões de crédito.
- **RNF18** - O sistema deverá ter proteção contra ataques DDoS.
- **RNF19** - O sistema deverá manter logs de auditoria de todas as ações críticas.
- **RNF20** - O sistema deverá ter proteção contra injeção de SQL, XSS e CSRF.

---

## Conclusão
Os requisitos do **Bazarium** garantem que a plataforma seja segura, escalável e intuitiva. Essa documentação serve como base para o desenvolvimento e evolução contínua do sistema, assegurando sua conformidade com padrões técnicos e regulatórios.
