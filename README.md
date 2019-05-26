1. JAK POSTAWIÆ PROJEKT
Nale¿y zainstalowaæ modu³ sqlite3 oraz modu³ requests, aby to zrobiæ we wierszu poleceñ nale¿y u¿yæ komend odpowiednio:
> pip install pysqlite3

> pip install requests

2. DOSTÊPNE KOMENDY
Najpierw nale¿y wykonaæ skrypt matura.py poleceniem matura.py, tworzy on bazê danych na podstawie pobranego z Internetu pliku

Skrypt który rozwi¹zuje zadania ma nazwê cmd.py.
Ka¿da komenda rozwi¹zuj¹ca zadanie zaczyna siê od myœlinika oraz numeru zadania.
Przyk³adowo komenda rozwi¹zuj¹ca zadanie pierwsze zaczyna siê od: 
> cmd.py -1
Nastêpnie nale¿y podaæ argumenty odpowiednie dla zadania w dowolnej kolejnoœci.
Przyk³adowo w zadaniu pierwszym, potrzebujemy podaæ województwo dla którego chcemy otrzymaæ wyniki oraz rok do którego œrednia ma byæ liczona.
Przyk³adowe polecenie do zadania 1:
> cmd.py -1 rok 2015 region Mazowieckie

co jest równoznaczne

> cmd.py -1 region Mazowieckie rok 2015

Gdy chcemy sprecyzowaæ p³eæ wystarczy, ¿e dodamy dopisek -k dla kobiet b¹dŸ -m dla mê¿czyzn.
Mo¿emy go dodaæ po nazwie skrypu b¹dŸ na koñcu komendy, przyk³adowo:

> cmd.py -k -1 region Dolnoœl¹skie rok 2012

> cmd.py -1 region Polska rok 2013 -m

Pozosta³e komendy mo¿na wykonywaæ analogicznie:

> cmd.py -2 region Pomorskie

> cmd.py -k -3 rok 2010

> cmd.py -4 -m

> cmd.py -5 region Kujawsko-pomorskie region Lubuskie

W przypadku braku ograniczeñ do interfejsu linii poleceñ u¿y³bym równie¿ paczki tkinter.
W celu dorobienia interfejsu graficznego