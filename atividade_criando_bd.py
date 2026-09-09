import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

banco= sqlite3.connect('dados.db')
c = banco.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS biblioteca(
          
          id INTEGER PRIMARY KEY,
          titulo  TEXT,
          autor   TEXT,
          ano     INTEGER,
          genero  TEXT,
          paginas INTEGER

          
)''')
banco.commit()

c.execute('INSERT INTO biblioteca(titulo,autor,ano,genero,paginas)VALUES (?,?,?,?,?)',('lemmy the ace','motore',1997,'biografia',332))
banco.commit()
c.execute('INSERT INTO biblioteca(titulo,autor,ano,genero,paginas)VALUES (?,?,?,?,?)',('rancid','tim',2009,'biografia',190))
banco.commit()
c.execute('INSERT INTO biblioteca(titulo,autor,ano,genero,paginas)VALUES (?,?,?,?,?)',('pulga','flea',2019,'biografia',297))
banco.commit()
c.execute('INSERT INTO biblioteca(titulo,autor,ano,genero,paginas)VALUES (?,?,?,?,?)',('rdp','rplife',2015,'biografia',380))
banco.commit()
c.execute('INSERT INTO biblioteca(titulo,autor,ano,genero,paginas)VALUES (?,?,?,?,?)',('planet','marcelo dias',2020,'biografia',410))
banco.commit()
c.execute('INSERT INTO biblioteca(titulo,autor,ano,genero,paginas)VALUES (?,?,?,?,?)',('clube dos cinco','matt luck',1989,'biografia',579))
banco.commit()



pd.r