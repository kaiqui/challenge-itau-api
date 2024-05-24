# Challenge JWT API

Este repositório contém uma API construída com FastAPI que realiza a validação de tokens JWT. Utiliza o GitHub Actions para automação de CI/CD e faz deploy no Amazon ECS (Elastic Container Service).

## Como Executar o Projeto via GitHub Actions

Para executar o projeto via GitHub Actions e realizar o deploy no Amazon ECS, siga os passos abaixo:

1. **Configuração de Variáveis de Ambiente**

   - É necessário configurar duas variáveis de ambiente no GitHub para o repositório:
     - `JWT_SECRET`: Esta variável deve conter a chave secreta utilizada para validar os tokens JWT.
     - Credenciais AWS: Configure as credenciais da AWS para permitir o deploy no Amazon ECS. As credenciais devem ter permissões adequadas para realizar operações no ECS.

2. **Workflow do GitHub Actions**

   - O fluxo de trabalho do GitHub Actions é configurado no arquivo `.github/workflows/action.yml`. Este arquivo especifica as etapas necessárias para buildar o código, gerar a imagem do Docker, fazer o push para o Amazon ECR (Elastic Container Registry) e realizar o deploy no Amazon ECS.

3. **Execução do Workflow**

   - Após configurar as variáveis de ambiente e as credenciais AWS, a execução do workflow será acionada automaticamente a cada push no repositório. O GitHub Actions irá iniciar o processo de build, geração da imagem do Docker, push para o ECR e deploy no ECS.

## Detalhes dos Métodos

A API possui o seguinte método:

1. **GET /validate_input**
   - Endpoint para validar um parâmetro na URL.
   - **Parâmetros**:
     - `input`: Parâmetro na URL que será validado.
   - **Requisitos de Validação**:
     - O parâmetro `input` é recebido na URL.
     - A API devolve apenas um booleano como resposta.
   - **Exemplo de Requisição**:
     ```
     GET /validate_input?input=teste
     ```
   - **Exemplo de Resposta** (Sucesso):
     ```
     true
     ```
   - **Exemplo de Resposta** (Erro):
     ```
     false
     ```

## Premissas e Decisões

Durante o desenvolvimento, algumas premissas foram assumidas para garantir o funcionamento adequado da API:

- Utilização do FastAPI: Optou-se por utilizar o FastAPI devido à sua performance, facilidade de uso e integração com a documentação automática.
- GitHub Actions para CI/CD: Decidiu-se usar o GitHub Actions devido à sua integração direta com o repositório do GitHub e suas capacidades de automação robustas.
- Deploy no Amazon ECS: O Amazon ECS foi escolhido como plataforma de deploy devido à sua escalabilidade, facilidade de uso e integração com outros serviços da AWS.

Essas decisões foram motivadas pela necessidade de construir uma solução segura, escalável e de fácil manutenção.
