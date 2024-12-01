# Sistema Integrado de Apoip a Pessoas Desaparecidas - KUMA

Este repositório contém o código-fonte do **Sistema Integrado de Apoip a Pessoas Desaparecidas**, uma solução inovadora desenvolvida para auxiliar na identificação e localização de pessoas desaparecidas ou em situações de emergência, utilizando tecnologias como reconhecimento facial e geolocalização.

## 📋 Funcionalidades Principais

- **Cadastro de Usuários**: Registro seguro de indivíduos no sistema.  
- **Publicações de Emergência**: Criação, visualização, edição e exclusão de publicações.  
- **Cadastro de Famílias**: Registro de informações de grupos familiares.  
- **Identificação de Pessoas**: Reconhecimento facial para identificar e localizar indivíduos.  
- **Geolocalização**: Rastreamento em tempo real e acesso a contatos de emergência.  
- **Gerenciamento de Perfil**: Edição de informações e configuração de conta.  
- **Autenticação Segura**: Login e logout com proteção avançada.  

## 🛠️ Tecnologias Utilizadas

- **Back-End**: Django (Python)  
- **Banco de Dados**: PostgreSQL  
- **Reconhecimento Facial**: OpenCV e TensorFlow  
- **Geolocalização**: APIs do Google Maps  
- **Interface Web**: HTML, CSS, JavaScript  
- **Aplicação Móvel**: Desenvolvida em Kotlin  
- **Infraestrutura**: AWS para hospedagem e Cloudinary para armazenamento de imagens  

## 📊 Resultados de Testes

Testes de usabilidade e desempenho foram realizados com 43 participantes, abrangendo as seguintes funcionalidades:  

| **Funcionalidade**       | **Sucesso (%)** | **Principais Dificuldades**                                  |
|---------------------------|-----------------|-------------------------------------------------------------|
| Criar Conta              | 95%             | Alguns usuários confundiram campos obrigatórios.            |
| Fazer Login              | 100%            | Nenhuma dificuldade relatada.                               |
| Criar Publicação         | 90%             | Problemas com o layout do formulário.                       |
| Identificar Indivíduo    | 85%             | Tempo de resposta maior em áreas de baixa conectividade.    |
| Acessar Contatos         | 98%             | Erros mínimos na navegação.                                 |
| Cadastrar Família        | 88%             | Alguns campos não estavam claros para os usuários.          |

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8 ou superior  
- PostgreSQL configurado  
- Google Maps API Key  
- Ambiente virtual configurado  

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/sistema-emergencias.git
   cd sistema-emergencias
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados em `settings.py` e aplique as migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

6. Acesse no navegador:
   ```
   http://127.0.0.1:8000
   ```

## 📂 Estrutura do Repositório

- `backend/` - Código do servidor Django  
- `mobile/` - Código da aplicação Android  
- `frontend/` - Código da interface web  
- `README.md` - Documentação do projecto  

## 🌟 Contribuições

Contribuições são bem-vindas! Siga estas etapas:

1. Faça um fork do projeto.  
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).  
3. Faça suas alterações e commit (`git commit -m 'Adicionei uma nova funcionalidade'`).  
4. Envie suas alterações (`git push origin feature/nova-funcionalidade`).  
5. Abra um Pull Request.

## 📝 Licença

Este projecto está licenciado sob a licença MIT - consulte o arquivo `LICENSE` para mais detalhes.


