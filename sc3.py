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
        
verifica_e_insersci_dati_iniziali()
effettua_oridne()