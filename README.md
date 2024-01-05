# Fire Sensor API

## Descrição
A Fire Sensor API é uma aplicação em Python utilizando o framework Flask, desenvolvida para registrar incidentes de incêndios. Ela integra-se com um sensor de fogo, temperatura e umidade, coletando dados cruciais para monitorar e analisar potenciais situações de risco.

## Tecnologias Utilizadas
[![My Skills](https://skillicons.dev/icons?i=python,flask)](https://skillicons.dev)

## Instalação
Certifique-se de ter o Python instalado em seu ambiente. Em seguida, siga os passos abaixo:

1. Clone este repositório:
   ```bash
   git clone https://github.com/vsenadev/fire-sensor-api.git
   cd fire-sensor-api
   ```

2. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Windows: `venv\Scripts\activate`
   - No macOS e Linux: `source venv/bin/activate`

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Inicie a aplicação:
   ```bash
   python app.py
   ```

A API estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Uso
- Utilize endpoints da API para registrar e consultar incidentes de incêndios.
- Os dados do sensor de fogo, temperatura e umidade podem ser enviados para a API para monitoramento em tempo real.
- Exemplos de endpoints:
  - `POST /post`: Registra um novo incidente.
  - `GET /ocurrences`: Recupera todos os incidentes registrados retornado true ou false a depender do caso de incêndio ou não.

## Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos. Basta seguir os passos mencionados no README ou abrir issues para discussões.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
