1. JAK POSTAWI� PROJEKT
Nale�y zainstalowa� modu� sqlite3 oraz modu� requests, aby to zrobi� we wierszu polece� nale�y u�y� komend odpowiednio:
> pip install pysqlite3

> pip install requests

2. DOST�PNE KOMENDY
Najpierw nale�y wykona� skrypt matura.py poleceniem matura.py, tworzy on baz� danych na podstawie pobranego z Internetu pliku

Skrypt kt�ry rozwi�zuje zadania ma nazw� cmd.py.
Ka�da komenda rozwi�zuj�ca zadanie zaczyna si� od my�linika oraz numeru zadania.
Przyk�adowo komenda rozwi�zuj�ca zadanie pierwsze zaczyna si� od: 
> cmd.py -1
Nast�pnie nale�y poda� argumenty odpowiednie dla zadania w dowolnej kolejno�ci.
Przyk�adowo w zadaniu pierwszym, potrzebujemy poda� wojew�dztwo dla kt�rego chcemy otrzyma� wyniki oraz rok do kt�rego �rednia ma by� liczona.
Przyk�adowe polecenie do zadania 1:
> cmd.py -1 rok 2015 region Mazowieckie

co jest r�wnoznaczne

> cmd.py -1 region Mazowieckie rok 2015

Gdy chcemy sprecyzowa� p�e� wystarczy, �e dodamy dopisek -k dla kobiet b�d� -m dla m�czyzn.
Mo�emy go doda� po nazwie skrypu b�d� na ko�cu komendy, przyk�adowo:

> cmd.py -k -1 region Dolno�l�skie rok 2012

> cmd.py -1 region Polska rok 2013 -m

Pozosta�e komendy mo�na wykonywa� analogicznie:

> cmd.py -2 region Pomorskie

> cmd.py -k -3 rok 2010

> cmd.py -4 -m

> cmd.py -5 region Kujawsko-pomorskie region Lubuskie

W przypadku braku ogranicze� do interfejsu linii polece� u�y�bym r�wnie� paczki tkinter.
W celu dorobienia interfejsu graficznego