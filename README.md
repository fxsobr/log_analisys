# FULLSTACK NANODEGREE - LOG ANALYSIS
## Descrição do Projeto
Você foi contratado(a) para um time que trabalha no site de um jornal. O frontend do site, e o banco de dados por trás dele, já estão feitos e em funcionamento. Pediram a você para construir uma **ferramenta interna de relatórios** (internal reporting tool) que usará informações do banco de dados para descobrir de que tipo de artigos os leitores do site gostam.


# Rodando o Projeto

### Pré-requisitos
- [Python 2.7.2](https://www.python.org/download/releases/2.7.2/)
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)

### Configurando o Projeto
- Instalar o Vagrant e o VirtualBox
- Baixar ou clonar o projeto do repositório [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
- Baixar o arquivo os [dados](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) a serem utilizados no projeto.
- Descompactar o arquivo após o download. O arquivo extraído se chama newsdata.sql
- Copie o arquivo newsdata.sql e os arquivos desse repositório para a pasta vagrant que fica dentro do projeto fullstack-nanodegree-vm

### Iniciando a máquina virtual

- Inicie a máquina virtual, acessando o sub diretório "vagrant" que fica dentro do repositório fullstack-nanodegree-vm, utilizando o seguinte comando:
	> vagrant up
- Para logar na máquina virtual, utilize o seguinte comando:
	> vagrant ssh
- Após efetuar o login mudar para o diretório /vagrant, utilize o seguinte comando:
	> cd /vagrant
- Para visualizar os arquivos dentro do diretório vagrant, utilizar o seguinte comando:
	> ls
### Configurando o banco de dados e criando as views
- Execute o seguinte comando para realizar a criação e inserção de dados do arquivo newsdata.sql
	> psql -d news -f newsdata.sql

A base de dados inclui 3 tabelas:
- articles
- authors
- log


- Utilize o seguinte comando para conectar-se ao banco de dados
	> psql -d news
- Crie a view artigos_populares usando:
	> CREATE OR REPLACE VIEW artigos_populares as
    SELECT art.title, COUNT(lg.path) AS views 
	FROM articles art 
	INNER JOIN log lg ON lg.path like CONCAT('/article/', art.slug)
	GROUP BY art.title 
	ORDER BY views DESC;
- Crie a view autores populares usando:
	> CREATE OR REPLACE VIEW autores_populares as
    SELECT ath.name, COUNT(lg.path) AS views
	FROM authors ath 
	INNER JOIN articles art ON art.author = ath.id 
	INNER JOIN log lg ON lg.path like CONCAT('/article/', art.slug)
	GROUP BY ath.name 
	ORDER BY views DESC;
- Crie a view log_erros usando:
	> CREATE OR REPLACE VIEW log_erros as 
	SELECT TO_CHAR(time, 'DD-MM-YYYY') AS data,
	ROUND(100.0*SUM(CASE log.status WHEN '200 OK' 
	THEN 0 ELSE 1 END)/COUNT(log.status),2) AS percentual_erros 
	FROM log 
	GROUP BY data
	ORDER BY percentual_erros desc;

### Rodando a aplicação
- Entrar no diretório vagrant dentro da máquina virtual e acessar a pasta log_analysis, rodar o arquivo analise_logs.py utilizando o comando:
> python analise_logs.py