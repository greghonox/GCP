### Gcp Course
- [Link do curso](https://cursos.alura.com.br/course/google-cloud-functions-codigo-serverless)


## Google Cloud Functions
- Google Cloud Functions é um serviço de computação sem servidor que executa seu código em resposta a eventos.  
- O Cloud Functions permite que você escreva funções simples e únicas que são acionadas por eventos de nuvem.
- Seu código é executado em um ambiente totalmente gerenciado. Não é necessário provisionar nenhum recurso e você paga apenas pelo tempo de computação que usa.
- O Cloud Functions escala automaticamente, permitindo que você execute milhares de funções por segundo sem precisar configurar nada.
- O Cloud Functions suporta funções escritas em Node.js, Python, Go, Java, .NET e Ruby.

---
### Vamos ver o comando para fazer um deploy da cloud function
```bash
gcloud functions deploy hello_word --runtime python312 --trigger-http
```