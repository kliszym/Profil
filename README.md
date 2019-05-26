1. JAK POSTAWIÆ PROJEKT
nale¿y zainstalowaæ modu³ sqlite3 oraz modu³ requests
aby to zrobiæ we wierszu poleceñ nale¿y u¿yæ komend odpowiednio:
> pip install pysqlite3
> pip install requests

2. DOSTÊPNE KOMENDY
najpierw nale¿y wykonaæ skrypt matura.py
poleceniem matura.py
tworzy on bazê danych na podstawie pobranego z Internetu pliku

skrypt który rozwi¹zuje zadania ma nazwê cmd.py
ka¿da komenda rozwi¹zuj¹ca zadanie zaczyna siê od myœlinika oraz numeru zadania
przyk³adowo komenda rozwi¹zuj¹ca zadanie pierwsze zaczyna siê od: cmd.py -1
nastêpnie nale¿y podaæ argumenty odpowiednie dla zadania w dowolnej kolejnoœci
przyk³adowo w zadaniu pierwszym, potrzebujemy podaæ województwo dla którego chcemy otrzymaæ wyniki
oraz rok do którego œrednia ma byæ liczona
przyk³adowe polecenie do zadania 1:
cmd.py -1 rok 2015 region Mazowieckie
co jest równoznaczne
cmd.py -1 region Mazowieckie rok 2015
gdy chcemy sprecyzowaæ p³eæ wystarczy, ¿e dodamy dopisek -k dla kobiet b¹dŸ -m dla mê¿czyzn
mo¿emy go dodaæ po nazwie skrypu b¹dŸ na koñcu komendy, przyk³adowo:
cmd.py -k -1 region Dolnoœl¹skie rok 2012
cmd.py -1 region Polska rok 2013 -m

pozosta³e komendy mo¿na wykonywaæ analogicznie:
cmd.py -2 region Pomorskie
cmd.py -k -3 rok 2010
cmd.py -4 -m
cmd.py -5 region Kujawsko-pomorskie region Lubuskie

W przypadku braku ograniczeñ do interfejsu linii poleceñ u¿y³bym równie¿ paczki tkinter
w celu dorobienia interfejsu graficznego