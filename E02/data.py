from datetime import datetime, timedelta

nd = input('Inserisci la tua data di nascita (nn-mm-yyyy): ')

datenow = datetime.now()
mydate = datetime.strptime(nd, "%d-%m-%Y")

anni = datenow.year - mydate.year
timediff = datenow - mydate
tots = timediff.total_seconds()
print(f"In questo momento hai {anni} anni, {timediff} giorni e {tots} secondi")