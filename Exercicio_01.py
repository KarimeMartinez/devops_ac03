#conectando a bibiloteca do python, exercicio1 é o nome do arquivo ddl
import sqlite3
conn = sqlite3.connect('exercicio1.db')

c = conn.cursor()

#criando a tabela
c.execute('''CREATE TABLE exercicio1_karime(
                id integer,
                nome text not null,
                email text,
                primary key (id))'''
                )

# Inserindo dados na tabela
c.execute("INSERT INTO exercicio1_brenda VALUES (1,'KARIME MARTINEZ','karime@1234.com')")

# Salvar as alterações
conn.commit()

# Encerrar.
conn.close()