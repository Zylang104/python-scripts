import random,sys

def carica_parole(percorso="parole.txt"): #cambia in base al file
    try:
        with open(percorso,encoding="utf-8") as f:
            return [p.lower() for r in f for p in r.split() if p.strip()]
    except:
        return []

def genera_frase(parole,n=5):
    if not parole or n<=0:
        return ""
    return (" ".join(random.choices(parole,k=n)).capitalize()+".")

if __name__=="__main__":
    parole=list(dict.fromkeys(carica_parole()))
    if not parole:
        print("Nessun dizionario caricato.")
        sys.exit(0)
    print(f"ci sono {len(parole)} parole. premi invio per sapere cosa Dio ti dice")
    try:
        while True:
            input()
            c=random.choice([31,32,33,34,35,36,37])  #colori
            print(f"\x1b[{c}m{genera_frase(parole, random.randint(4,8))}\x1b[0m")
    except KeyboardInterrupt:
        print("\nciao")