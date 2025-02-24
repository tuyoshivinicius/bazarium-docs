# Event Storming: Criar Conta e Definir Perfil de Usuário

## 📌 Contexto
Este documento descreve o **Event Storming** para o processo de criação de conta e definição de perfil de usuário na plataforma. As ações estão organizadas dentro de seus respectivos **Bounded Contexts**.

---

## 🔵 Comandos (Commands)
Os comandos representam ações explícitas no sistema, iniciadas pelo usuário ou processos automatizados.

### **Contexto de Usuário**
- `CriarConta(email, senha, nome)`: Solicita a criação de uma nova conta.
- `DefinirPerfilUsuario(tipoPerfil: Comprador ou Vendedor)`: Define o tipo de perfil do usuário após a ativação da conta.

### **Contexto de Notificação**
- `ConfirmarEmail(token)`: Confirma o endereço de e-mail do usuário.

---

## 🟠 Eventos do Domínio (Domain Events)
Os eventos são gerados como resultado da execução de comandos bem-sucedidos.

### **Contexto de Usuário**
- `ContaCriada(usuarioId, email, status: Pendente)`: Indica que uma nova conta foi registrada, mas ainda não ativada.
- `PerfilDefinido(usuarioId, tipoPerfil)`: O usuário selecionou um tipo de perfil (Comprador ou Vendedor).

### **Contexto de Notificação**
- `EmailConfirmado(usuarioId, status: Ativo)`: O usuário confirmou seu e-mail e a conta foi ativada.

---

## 🟡 Agregados e Entidades
Os agregados e entidades representam os principais modelos de dados envolvidos.

### **Contexto de Usuário**
#### **Usuário**
- **ID**: Identificador único do usuário.
- **Nome**: Nome do usuário.
- **E-mail**: Endereço de e-mail cadastrado.
- **Senha**: Armazenada de forma segura (hash).
- **Status**: Pode ser `Pendente`, `Ativo` ou `Bloqueado`.
- **Tipo de perfil**: `Comprador` ou `Vendedor`.

---

## 🟣 Políticas (Regras de Negócio / Process Managers)
As regras de negócio definem as condições e fluxos obrigatórios dentro do sistema.

### **Contexto de Usuário**
1. O usuário deve definir seu perfil (**Comprador** ou **Vendedor**) antes de continuar na plataforma.

### **Contexto de Notificação**
2. Após a criação da conta, o sistema envia um e-mail de confirmação.
3. A conta só pode ser ativada após a confirmação do e-mail.
4. Se o e-mail não for confirmado em **X dias**, a conta será removida automaticamente.

---

## 🟢 Leitura (Projeções / Queries)
Consultas utilizadas para recuperar informações relevantes sobre a conta do usuário.

### **Contexto de Usuário**
- `ObterStatusConta(usuarioId)`: Retorna o status atual da conta do usuário.
- `ObterPerfilUsuario(usuarioId)`: Retorna o tipo de perfil do usuário.

---

## ⚡ Fluxo Completo

1️⃣ **O usuário acessa a tela de cadastro e preenche nome, e-mail e senha.**  
   - ➡️ **Comando:** `CriarConta(email, senha, nome)`  
   - 🚀 **Evento:** `ContaCriada(usuarioId, email, status: Pendente)`

2️⃣ **O sistema envia um e-mail com um link de ativação.**  
   - ➡️ **Comando:** `ConfirmarEmail(token)`  
   - 🚀 **Evento:** `EmailConfirmado(usuarioId, status: Ativo)`

3️⃣ **O usuário acessa a plataforma e define seu perfil.**  
   - ➡️ **Comando:** `DefinirPerfilUsuario(tipoPerfil)`  
   - 🚀 **Evento:** `PerfilDefinido(usuarioId, tipoPerfil)`

4️⃣ **O usuário pode agora navegar na plataforma com o perfil definido.**

---

Este **Event Storming** documenta os comandos, eventos, agregados e regras de negócio relacionados ao fluxo de criação de conta e definição de perfil do usuário, deixando explícita a separação dos **Bounded Contexts** envolvidos.


## 📊 Diagrama

Abaixo, um diagrama Mermaid para ilustrar a jornada

```mermaid
sequenceDiagram
    participant Usuário
    participant UsuárioContexto as Usuário
    participant Notificação
    participant EmailService

    Usuário->>UsuárioContexto: CriarConta(email, senha, nome)
    UsuárioContexto-->>Usuário: ContaCriada(usuarioId, email, status: Pendente)
    UsuárioContexto->>Notificação: Solicitar envio de e-mail de confirmação
    Notificação->>EmailService: Enviar e-mail de ativação
    EmailService-->>Usuário: Link de confirmação enviado

    Usuário->>Notificação: ConfirmarEmail(token)
    Notificação-->>UsuárioContexto: EmailConfirmado(usuarioId, status: Ativo)

    Usuário->>UsuárioContexto: DefinirPerfilUsuario(tipoPerfil)
    UsuárioContexto-->>Usuário: PerfilDefinido(usuarioId, tipoPerfil)

    Usuário->>UsuárioContexto: Acessar plataforma
    UsuárioContexto-->>Usuário: Acesso permitido com perfil definido

