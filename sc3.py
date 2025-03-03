import sqlite3
from datetime import datetime

DB_NAME = "ordini_negozio.db"

def verifica_e_insersci_dati_iniziali():
    with sqlite3.connect(DB_NAME) as conn:
        count = conn.execute("SELECT COUNT(*) FROM prodotti").fetchone()[0] # prendo l'elemnto all'indice 0 così capisco se è vuota
        print(count)
        
        if count == 0:
            prodotti = [
                ("T-shirt Bianca", 19.99),
                ("Jeans Slim Fit", 49.99),
                ("Giacca di Pelle", 89.99),
                ("Sneakers Sportive", 59.99),
                ("Felpa con Cappuccio", 39.99)
            ]
            # metodo classico
            # conn.execute("INSERT INTO prodotti (nome, prezzo) VALUES (?, ?)", ("T-shirt Bianca", 19.99),)
            
            # esegue la query su tutti gli elementi della lista (tupla) "prodotti"
            conn.executemany("INSERT INTO prodotti (nome, prezzo) VALUES (?, ?)", prodotti)


def mostra_catalogo_prodotti():
    with sqlite3.connect(DB_NAME) as conn:
        prodotti = conn.execute("SELECT * FROM prodotti").fetchall()
        
        if not prodotti:
            print("\nNessun prodotto disponibile.")
        else:
            print("\nCatalogo prodotti:")
            for p in prodotti:
                print(f"{p[0]} - {p[1]}, €{p[2]}")
                
def effettua_oridne():
    cliente = input("\nNome cliente: ")
    mostra_catalogo_prodotti()
    prodotto_id = input("\nQuale prodotto vuoi ordinare? (id) ")
    data_ordine = datetime.now()
    
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO ordini (cliente, data, prodotto_id) VALUES (?, ?, ?)", (cliente, data_ordine.timestamp(), prodotto_id))
        
        print(f"Ordine inserito in data: {data_ordine.strftime("%d/%m/%Y %H:%M")}")
        
def mostra_ordini():
    sql = """
            SELECT o.id, o.cliente, o."data", p.nome, p.prezzo FROM ordini o INNER JOIN prodotti p ON o.prodotto_id = p.id
          """
    with sqlite3.connect(DB_NAME) as conn:
        ordini = conn.execute(sql).fetchall
    
        if not ordini:
            print("\nNessun ordine effettuato")
        else:
            print("\nOrdini effettuati:")
            
            for o in ordini:
                print(f"{o[0]} - {o[1]} ha ordinato {0[3]} (€ {o[4]}) il {datetime.fromtimestamp(0[2]).strftime("%d/%m/%Y %H:%M")}")

def menu():
    while True:
        print("\n1. Mostra catalogo prodotti")
        print("\n2. Mostra ordini effettuati")
        print("\n3. Effettua un nuovo ordine")
        print("\n4. Esci")
        scelta = int(input("Scegli un opzione: ")) 
        
        if scelta == 1:
            mostra_catalogo_prodotti()
        elif scelta == 2:
            mostra_ordini()
        elif scelta == 3:
            effettua_oridne()
        elif scelta == 4:
            break
        else:
            print("Scelta non valida")    
      
verifica_e_insersci_dati_iniziali()
menu()

