import sqlite3
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE exercicio1_karime(
                id integer,
                nome text not null,
                email text,
                primary key (id) )'''
                )

c.execute("INSERT INTO exercicio1_karime VALUES (1,'KARIME MARTINEZ','karime@1234.com')")

c.execute('''SELECT * 
                FROM sqlite_master AS m, pragma_table_info(m.name)
                WHERE tbl_name = 'exercicio1_karime'
            ''')
      
for row in c.fetchall():
    print('--------------- Tabelas  --------------- ')
    print('Nomes dos campos: ', row[6])
    print('É PK?: ', row[10])
    print('Permite nulo? ', row[8])

conn.commit()
conn.close()