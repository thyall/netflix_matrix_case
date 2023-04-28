# Confitech

### Este é um projeto que procura solucionar as demandas solocitadas para o case da Confitech

Há duas pastas uma para o desafio em [Pyspark](https://spark.apache.org/docs/latest/api/python/) e outra para o desafio de Algoritimos.

## Pyspark

### Environment
- Google Colaboratory
- Visual Studio

### Requeriments
- python3.9 (ou superior)
- venv
- [aws cli](https://aws.amazon.com/pt/cli/)

### Getting Start
#### Para executar o notebook basta subir no seu Google Colaboratory e executar as células

#### Para o arquivo upload_csv.py há algumas etapas:
- python3.9 -m venv venv
- source venv/bin/activate (linux) ou .\venv\script\activate (windows)
- pip install boto3

Após realizar o download da sua secret key e da sua access key
é neessário configurar ambas keys pelo comando 
```aws configure```
passar as keys e location (o restante pode ser default)

Após configurar seu ambiente de trabalho o código ja estará pronto para ser executado e enviar o arquivo para o Bucket.

## Matriz

### Environment
- Visual Studio

### Requeriments
- python3.9 (ou superior)
- venv

### Getting Start
- python3.9 -m venv venv
- source venv/bin/activate (linux) ou .\venv\script\activate (windows)
- pip install numpy

Após isso o código já estará pronto para ser executado