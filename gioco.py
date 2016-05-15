#!/usr/bin/ python
# -*- coding: utf-8 -*-
import os
import random
puntipolitica = 50
elettori = 5
turno = 0
nomi = ["Mario","Alessio","Patrick","Adelio","Maria Augusta","Rin Michela","Rita","Altiero","Cesara","Giorgia","Francesco Ferdinando","Vittoria","Italia","Francesca Beatrice","Linus","Bartolo","Ariel","Gaetano","Alcide","Salvatore","Fermo","Giuliano","Domenico","Albano","Celere","Giulio Cesare","Valeria","Nicoletta","Ekaternia Giorgia","Jason Ambrogio","Alessia","Emilia","Selena","Alexis","Stefano","Olmo","Ariberto","Dolan","Ermenegilda","Teodolinda","Erminio","Beniamino","Michel","Bambin","Nazario","Paoletto","Glorioso","Gilberto","Helmut","Lotario","Arnaldo","Mauro Lupo","Teodorico","Noemi","Giulia","Adelaide","Roberta","Candace","Pier Giorgio","Andrea","Virgilio","Dante","Nazareno Michele","Ezechele","Lissander","Benìn","Giazint","Adolfino","Domenegh","Gnazzi","Grigoeu","Poldo","Zerill","Polonia","Gigi","Victoria","Agnese","Adelaide","Elvezia","Amanda","Iustizia","Caterina","Martina","Fiorenza","Melissa","Antioco","Barisone","Lucio","Cornelio","Peppone","Gastone","Genoveffo","Giasone","Gavino","Arnold","Cassio","Vercingetorice","Nerone","Anzolo","Tiberio","Mariello","Amerigo","Ernesto","Adamo","Karol","Manfredi","Rotario","Antonello","Alessandro","Michele","Amado","Nikolai","Egidio","Tracaro","Arcangelo","Duomo","Attanasio","Garrumo","Giandomenico","Ciociaro","Giorgio","Licio","Calogero","Mona","Germano","Ugo","Matteo","Attilio","Teodorico","Crescenzo","Arimanno","Floriano","Baldassarre","Berto","Roso","Catalino","Tromlino","Ambroeus","Francesco","Abbondio","Nunzio","Gerardo","Silvio","Alberto","Gianni","Teresio","Ambrogio","Anselmo","Giovese","Amintore","Italo","Arcibaldo","Justinià","Danjuro","Bortolo","Augusto","Piergastone","Diego","Giulio","Giuàn","Azeglio","Adolfo","Benito","Natale","Nazareno","Jorji"]
cognomi = ["Brambilla","Fumagalli","Rossi","dell'Incoronata","Schulzi","Fabero","Kofler","Coffiere","Verdi","Capellaro","da Pirla","Almirante","Casadei","Tettamanzi","Pessotti","Mastranzo","Nasdrovie","Dalle Colonie","Bono","Rovatacchini","Bianchi","Bernasca","Salvino","Porcu","Lefevre","Thompson","Vagneri","Sojuzzi","La Foppa","Dervalaporta","Sforza","Visconti","De Medici","Ottone","Di Calino","Aromano","Megrato","Suscrofa","Lazzaroni","Formaggi","Giamboni","Della Libertà","Di Pioltello","Feltrinelli","Zaccuri","Scoeura","Caselli","Wagner","Bottazzi","Guadone","de Brescello","Prestinée","Caterborino","Mariano","Eleatico","Ploeuv","Taleano","Loserbiddio","Berlinguer","Ol Careàs","Pisaelfoeuc","Puteo","Diletta","Dindina","Prondella","Mangiagalli","Cordileone","De Nicola","Battisti","Terione","Parisi","Contit","Elross","Koener","Wicewski","Milanese","Magutti","Scipoti","Auffo","Caronti","Veneranda Fabbrica","Scapece","Rensi","Bosse","Cetipaga","Dellinfermi","Legnano","Werrant","Scarpa","Soccuso","Varvaro","Moscerini","Mascio","Togliatti","Tramaglino","Ienneri","Kowalsky","Tomat","Muzzo","Putin","Ostuni","Fiorenza","Narodna","Piattirotti","Colleone","Mandi","Fanfani","Corsi","Romano","Perottini","Torvalds","da Giussano","Mantaro","Asburgo","Sala","Passalapalla","Plebfiore","Vaccini","De Stefano","Pizza","Rotino","Spoeusa","Alfulo","Cappi","Di Piero","Altissimo","Maroni","Olsone","Popov","Sensi","Bellotti","Conti","Invernizzi","Nicolello","Legramandi","Olivetti","Vignana","Carminati","Zennaro","Savoia","Figliodigesù","De Hiedler","Ferrero","Colombo","Manzon","Pravesin","Giussan","Lampugnan","Tanzi","Tanz","Galaràa","Bernascon","Hamzar","Rivetti","Lombardi","Basile","Degasperi","Culot","Toccaferro","Hamer","Granlavorador","Fantozzi","Nagotta","Mosconi","Perazzini","Mussolesi","Schavòn"]
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
def invio():
	raw_input("Premi invio per continuare")
def nome():
	global presidente
	global nome
	nome = raw_input("Inserisci il tuo nome:")
	if nome == "Mike Sciking":
		presidente = "Ambrogio Conti"
	else:
		presidente = "Mike Sciking"

def introd():
	global puntipolitica
	global elettori
	global nome
	global presidente
	print """
Benvenuto in Pulitica: Nuove leve. Questo gioco è un prequel di "Pulitica". Li inizi come presidente del Partito. Ma qui? Da un comune piccolo piccolo...
Speriamo che tu possa arrivare a nuovi livelli, e dovrai accumulare Punti Politica per poterti candidare e Elettori per essere votato.
Le nostre idee son le solite, ma te le sintetizzo qui:
1) NO all'unità d'Italia.
2) SI ai matrimony gay, ma NO alle adozioni
3) SI all'unità Europea confederale
4) NO all'immigrazione clandestina
5) SI al decentramento dei poteri
T'heet capii? ;)

Buona avventura politica, caro.
Il Presidente del Partito Indipendente Milanese"""
	nome()
	invio()

	clear()
	print "E io, Giorgio Costava, segretario della Sezione del Partito Indipendente di Caravaggio, comune della Città Autonoma di Bergamo, annuncio i risultati elettorali. Risulta eletto come candidato consigliere comunale per i Giovani Indipendenti:", nome

	print "Complimenti caro, speriamo in una tua grande carriera politica! Dovrai ottenere almeno 45 elettori e 85 punti rilevanza per essere eletto. \n Ogni 5 turni ci saranno le elezioni"
	invio()
	clear()
	ccomunale()

def indmil1():
	print "L'Indipendente delle Orobie"
	global puntipolitica
	global elettori
	global turno
	turno = turno + 1
	z = random.randint(1,10)
	if z == 1:
		print nome, "all'Incontro con il Partii di Europee-Partito degli Europei"
		elettori = elettori + 3
		puntipolitica = puntipolitica + random.randint(1,5)
	elif z == 2:
		if turno%2 == 0:
			print "Incredibile! Candidato della Sinistra ammette di essere del PIM e di rimanere a Sinistra per motivi familiari"
			elettori = elettori + 6
		else:
			print "Nuovo Presidente del Governo della Città Autonoma di Brescia eletto dal PIM!"
			elettori = elettori + 1
	elif z == 3:
		if turno%2 == 0:
			print "Per errori tecnici la lista amica 'Fradej d'Orobia' non potrà candidarsi"
			puntipolitica = puntipolitica + 3
			elettori = elettori - 2
		else:
			print "La lista avversaria 'Manzina Lombardia' non parteciperà per problemi legali del candidato"
			elettori = elettori + 3
	elif z == 4:
		if turno%4 == 0:
			print "Candidato sindaco", nomi[random.randint(0,165)], cognomi[random.randint(0,165)]," del PIM alla processione al Santuario"
			puntipolitica = puntipolitica + random.randint(-3,5)
			elettori = elettori + random.randint(-1,5)
		else:
			print "Il candidato", nome, "al Convegno in Memoria della battaglia di Legnano parla: Ospiti commossi"
			puntipolitica = puntipolitica + random.randint(0,6)
			elettori = elettori + random.randint(-1,7)
	elif z == 5:
		print "Giornalino dei Giovani indipendenti"
		print "Il nostro candidato di Caravaggio incontra il Presidente della Catalogna:"
		print '"Nostre nazioni legate da profondissimo legame, Visca Catalunya i Llombardia lliures"'
		puntipolitica = puntipolitica + random.randint(-1,6)
		elettori = elettori + random.randint(-2,8)
	elif z == 6:
		print "Candidato del PIM Anziani arrestato per truffa"
		puntipolitica = puntipolitica + random.randint(-1,5)
		elettori = elettori + random.randint(-3,2)
	elif z == 7:
		if turno%2 == 0:
			print "Ma che dice il Nostro Segretario? Italia unita? Se la tenga lui!"
			puntipolitica = puntipolitica + random.randint(-4,1)
			elettori = elettori + random.randint(-2,3)		
		else:
			print "Costava: Ma che lombardo parli?"
			print "Figuraccia al Convegno Galloitalico, persi elettori..."
			puntipolitica = puntipolitica + random.randint(-3,5)
			elettori = elettori + random.randint(-4,0)
	elif z == 8:
		if turno%5 == 0:
			print "Candidato della Sinistra dimentica di essere incandidabile, e vinciamo noi di default..."
			elettori = int(elettori*1.4)
			puntipolitica = int(puntipolitica*1.5)
		else:
			print nome, "contro ai candidati neofascisti nelle liste amiche del PIM: Elettori felici"
			puntipolitica = puntipolitica + random.randint(-3,6)
			elettori = elettori + random.randint(1,5)
	elif z == 9:
		print nome, "chiede spazio per la Scienza a Caravaggio!"
		puntipolitica = puntipolitica + random.randint(-1,3)
		elettori = elettori + random.randint(-1,3)
	elif z == 10:
		if turno%3 == 0:
			print "Il Capo dello Stato incontra", nome
			puntipolitica = puntipolitica + random.randint(-1,10)
			elettori = elettori + random.randint(-2,8)
		else:
			print nome, "dice che la soluzione ai problemi è incendiare i campi rom: Partito perplesso"
			puntipolitica = puntipolitica + random.randint(-4,0)
			elettori = elettori + random.randint(-1,6)
def ccomunale():


	indmil1()
	global turno
	global puntipolitica
	global elettori
	global nome
	global presidente
	print "Turno:", turno
	print "Hai", elettori, "elettori"
	print "Hai", puntipolitica, "influenza"
	if turno%4 == 0:
		print "Intervista! Cosa vuoi dichiarare all'Indipendente delle Orobie?"
		print """1) Siamo a favore delle adozioni gay!
2) La federazione di oggi è ottima, stop accentramenti
3) Stop degrado urbano, la precedente amministrazione è indegna
4) Faremo cose particolari per la città
5) Continueremo l'opera di Cattaneo in Europa
6) Espelleremo gli stranieri irregolari
7) Serve più coesione tra gli stati italici
8) Voterò contro al Registro Comunale Adozioni Omosessuali"""
		giornale = int(raw_input(":"))
		print "L'Indipendente delle Orobie"
		if giornale == 1:
			print nome, "a favore delle adozioni gay, partito perplesso"
			elettori = elettori + random.randint(-1,5)
			puntipolitica = puntipolitica - random.randint(1,4)
		if giornale == 2:
			print nome, "contento della federazione odierna."
			elettori = elettori + random.randint(-1,3)
			puntipolitica = puntipolitica + random.randint(1,6)
		if giornale == 3:
			print "Il PIM caravaggese contro il degrado urbano: Forti parole sull'amministrazione precedente."
			elettori = elettori + random.randint(-2,6)
			puntipolitica = puntipolitica + random.randint(-1,5)
		if giornale == 4:
			lm = random.randint(1,3)
			if lm == 1:
				print "Piste per pebiottisti a Caravaggio, strana proposta di", nome, "."
				elettori = elettori + random.randint(-3,5)
				puntipolitica = puntipolitica + random.randint(0,1)
			if lm == 2:
				print "PIM Caravaggese vuole un concorso di bestemmie a Caravaggio. Elettori sbigottiti"
				elettori = elettori + random.randint(-3,1)
				puntipolitica = puntipolitica + random.randint(-1,1)
			if lm == 3:
				print "Lombardo unica lingua ufficiale di Careàs, proposta di", nome, "."
				elettori = elettori + random.randint(-2,6)
				puntipolitica = puntipolitica + random.randint(-2,5)
		if giornale == 6:
			print nome, "chiarissimo: Immigrati foeura da le balle"
			elettori = elettori + random.randint(-1,3)
			puntipolitica = puntipolitica + random.randint(1,3)
		if giornale == 7:
			print "Candidato a Caravaggio dei Giovani Indipendenti vuole l'Italia coesa. Costava sbraita 'sta mia a fà el cojon'"
			elettori = elettori + random.randint(-4,3)
			puntipolitica = puntipolitica + random.randint(-5,3)
		if giornale == 5:
			print nome, "si schiera per l'unità europea: 'Noi come Carlo Cattaneo, sempre europeisti saremo'"
			elettori = elettori + random.randint(-1,5)
			puntipolitica = puntipolitica + random.randint(-2,8)
		if giornale == 8:
			print "Il PIM Caravaggio contro alle adozioni gay nel comune"
			elettori = elettori + random.randint(-3,5)
			puntipolitica = puntipolitica + random.randint(1,6)
	if turno%4 != 0:
		print "Cosa vuoi fare?"
		print """1) Aperitivo con i candidati
2) Confronto pubblico tra candidati
3) Viaggio a Bergamo per incontrare il Segretario Cittadino
4) Corso di lingua lombarda
5) Manifestazione dei Giovani Europei
6) Gay Pride
7) Intervista in TV
8) Partecipa a "Radio Lombardia Internazzional"
9) Manifestazione degli Alpini a Legnano """
		eventi = int(raw_input(":"))
		if eventi == 1:
			print "Fai un aperitivo con i candidati del PIM e incontri i cittadini di Caravaggio e Treviglio"
			elettori = elettori + 3
			puntipolitica = puntipolitica + random.randint(-2,1)
		if eventi == 2:
			je = random.randint(1,3)
			if je == 1:
				print "Il confronto lascia indifferente la popolazione"
				puntipolitica = puntipolitica + 3
			if je == 2:
				print "Colpisci i cuori dei cittadini, ottimo!"
				elettori = elettori + 6
				puntipolitica = puntipolitica + random.randint(0,3)
			if je == 3:
				print "Male male male... Gli avversari ti battono nettamente"
				elettori = elettori + random.randint(-3,2)
				puntipolitica = puntipolitica + random.randint(-3,1)
		if eventi == 3:
			print "Incontri a Bergamo il Segretario della Città Autonoma e ti 'benedice'"
			puntipolitica = puntipolitica + 5
		if eventi == 4:
			print "Prendi parte ad un corso di lingua lombarda: \n Importantissimo tutelare la nostra lingua, dici"
			elettori = elettori + random.randint(1,7)
			puntipolitica = puntipolitica + random.randint(-2,4)	
		if eventi == 5:
			print "Vai a manifestare coi Giovani Europei per l'Europa confederale"
			elettori = elettori + random.randint(-2,6)
			puntipolitica = puntipolitica + random.randint(0,5)
		if eventi == 6:
			print "Partecipi al Gay Pride di Cremona, elettorato gay alle stelle"
			elettori = elettori + random.randint(-6,10)
			puntipolitica = puntipolitica + random.randint(-1,6)	
		if eventi == 7:
			je = random.randint(1,3)
			if je == 1:
				print "Parli a 'Mediolanum TV', diffondi l'idea del partito ma passi subito a parlare di calcio a 5"
				puntipolitica = puntipolitica + 1
				elettori = elettori + random.randint(-2,3)
			if je == 2:
				print "Parli a 'Sodoku' e convinci molti indecisi a votare il PIM"
				elettori = elettori + 5
				puntipolitica = puntipolitica + random.randint(0,5)
			if je == 3:
				print "Sindaco liberale dimostra che sei incompetente in politica federale"
				elettori = elettori + random.randint(-6,3)
				puntipolitica = puntipolitica + random.randint(-4,3)	
		if eventi == 8:
			print "Parli a 'Radio Lombardia Internazzional' in lombardo e inglese. \n Ti ascoltano in tutta Europa e ottieni una medaglia del Partito Indipendente d'Europa"	
			elettori = elettori + 1
			puntipolitica = puntipolitica + random.randint(4,12)
		if eventi == 9:
			print "Prendi la ciucca e fai il simpaticone ricordando la tua leva nei vigili. Elettori divertiti, PIM meno. Molto meno"
			elettori = elettori + random.randint(2,8)
			puntipolitica = puntipolitica - random.randint(-2,5)		


	if puntipolitica > 85 and elettori > 45 and turno%5 == 0:
		print "Complimenti! Sei stato eletto Consigliere Comunale... Ma adesso dobbiamo arrivare più in altro... Diventare CapoZona della Capitale Bergamo"
		invio()
		clear()
		czonabg()
	else:
		invio()
		clear()
		ccomunale()

#devo tradurre

def indmil2():
	print "L'Indipendente di Bergamo"
	global puntipolitica
	global elettori
	global turno
	turno = turno + 1
	z = random.randint(1,10)
	if z == 1:
		print "Bollettino del III Distretto di Bergamo"
		print nome, "incontra gli altri candidati di Zona del PIM"
		elettori = elettori + 5
		puntipolitica = puntipolitica + random.randint(2,8)
	elif z == 2:
		if turno%2 == 0:
			print "Incredibile! Rampollo della Destra lascia e si unisce al PIM!"
			elettori = elettori + 14
			puntipolitica = puntipolitica + 8
		else:
			print "Il PIM e gli Autonomisti Lombardi Alpini eleggono il Sindaco di Sondrio."
			elettori = elettori + 4
	elif z == 3:
		if turno%2 == 0:
			print "Per errori tecnici la lista amica 'NòterBerghèm' non potrà correre con noi"
			puntipolitica = puntipolitica + 7
			elettori = elettori - 5
		else:
			print "La lista avversaria 'Bergamo Democratica - Italia Centralista' non parteciperà per problemi legali del candidato"
			elettori = elettori + 6
	elif z == 4:
		print "Il consigliere comunale caravaggese", nome, "parla dell'amicizia con il Veneto: Fratelli!"
		puntipolitica = puntipolitica + random.randint(1,9)
		elettori = elettori + random.randint(-1,8)
	elif z == 5:
		print "Giornalino dei Giovani indipendenti"
		print "Il nostro consigliere di Caravaggio all'Incontro Federale del PIM:"
		print '"Lavoreremo per la Gioventù lombarda"'
		puntipolitica = puntipolitica + random.randint(-1,11)
		elettori = elettori + random.randint(-3,10)
	elif z == 6:
		if turno %2 == 0:
			print "Rinasce il Socialismo a Bergamo."
			puntipolitica = puntipolitica + random.randint(-2,5)
			elettori = elettori + random.randint(-5,3)
		else:
			print nome, "ha la vena comica e racconda battute sul candidato dalla memoria corta di Destra"
			print "Volevo raccontarvi una barzelletta su Divani, ma l'ho dimenticata"
			elettori = elettori + 6
	elif z == 7:
		if turno%2 == 0:
			print "Segretario locale di Bergamo a favore di un governo di Roma: Destituito!"
			puntipolitica = puntipolitica + random.randint(-2,6)
			elettori = elettori + random.randint(-4,2)		
		else:
			print "Costava: Riforma della Sinistra è fascista,non vogliamo novelli Mussolini in Lombardia"
			puntipolitica = puntipolitica + random.randint(0,6)
			elettori = elettori + random.randint(-2,6)
	elif z == 8:
		if turno%5 == 0:
			print "Candidato della Sinistra dimentica di essere incandidabile, e vinciamo noi di default..."
			elettori = int(elettori*1.4)
			puntipolitica = int(puntipolitica*1.5)
		else:
			print nome, "contro la lombardofobia: Parlare la nostra lingua diritto fondamentale"
			puntipolitica = puntipolitica + random.randint(0,7)
			elettori = elettori + random.randint(1,5)
	elif z == 9:
		print nome, "a favore dell'obbligo vaccinale: Tutti vaccinati entro 5 anni"
		puntipolitica = puntipolitica + random.randint(1,9)
		elettori = elettori + random.randint(-4,12)
	elif z == 10:
		if turno%3 == 0:
			print "Il Capo dello Governo incontra", nome
			puntipolitica = puntipolitica + random.randint(-2,12)
			elettori = elettori + random.randint(-4,12)
		else:
			print nome, "canta l'Inno d'Italia alla partita: Partito perplesso"
			puntipolitica = puntipolitica + random.randint(-5,0)
			elettori = elettori + random.randint(-4,4)
def czonabg():
	indmil2()
	global turno
	global puntipolitica
	global elettori
	global nome
	global presidente
	print "Turno:", turno
	print "Hai", elettori, "elettori"
	print "Hai", puntipolitica, "influenza"
	if turno%4 == 0:
		print "Intervista! Cosa vuoi dichiarare all'Indipendente delle Orobie?"
		print """1) Creeremo un registro adozioni gay di Zona!
2) Costava miglior candidato della storia lombarda, votatelo!
3) Porteremo il bergamasco nelle scuole parificandolo all'italiano toscano
4) Faremo cose particolari per la Zona
5) La lite Brescia-Bergamo è idiota: Siamo tutti lombardi.
6) Ammetteremo più stranieri e senza richiedere permessi
7) Serve più coesione tra gli stati europei
8) Candidati di certe liste amiche impresentabili, non li sento miei"""
		giornale = int(raw_input(":"))
		print "L'Indipendente di Bergamo"
		if giornale == 1:
			print nome, "a favore delle adozioni gay, partito perplesso"
			elettori = elettori + random.randint(-3,8)
			puntipolitica = puntipolitica - random.randint(2,8)
		if giornale == 2:
			print nome, "si schiera con Costava: 'Votatelo, ottimo candidato'."
			elettori = elettori + random.randint(-1,3)
			puntipolitica = puntipolitica + random.randint(1,6)
		if giornale == 3:
			print "Il caravaggese vuole il bergamasco a scuola come l'italiano"
			elettori = elettori + random.randint(-4,9)
			puntipolitica = puntipolitica + random.randint(-2,11)
		if giornale == 4:
			lm = random.randint(1,3)
			if lm == 1:
				print "Superstrada ciclabile in zona 3, strana proposta di", nome, "."
				elettori = elettori + random.randint(-3,5)
				puntipolitica = puntipolitica + random.randint(0,1)
			if lm == 2:
				print "Parquet in tutti gli edifici pubblici per il PIM Bergamasco: Pagano loro?"
				elettori = elettori + random.randint(-6,4)
				puntipolitica = puntipolitica + random.randint(-5,2)
			if lm == 3:
				print "Metropolitana a Bergamo, la proposta di", nome, "fa discutere."
				elettori = elettori + random.randint(-2,6)
				puntipolitica = puntipolitica + random.randint(-2,5)
		if giornale == 6:
			print nome, "vuole immigrati senza controllo. Ma lui è senza ritegno"
			elettori = elettori + random.randint(-8,3)
			puntipolitica = puntipolitica + random.randint(-5,1)
		if giornale == 7:
			print "Candidato dei Giovani Indipendenti vuole l'Europa coesa. Costava a favore"
			elettori = elettori + random.randint(-1,9)
			puntipolitica = puntipolitica + random.randint(-2,8)
		if giornale == 5:
			print nome, '"Idiozia le liti tra Brescia e Bergamo, siamo tutti lombardi"'
			elettori = elettori + random.randint(-3,6)
			puntipolitica = puntipolitica + random.randint(-3,12)
		if giornale == 8:
			print "PIM Bergamasco contro le liste amiche: Hanno candidati impresentabili"
			elettori = elettori + random.randint(-6,4)
			puntipolitica = puntipolitica + random.randint(2,10)
	if turno%4 != 0:
		print "Cosa vuoi fare?"
		print """1) Aperitivo con i candidati
2) Confronto pubblico tra candidati
3) Viaggio a Bergamo per incontrare il Segretario Cittadino
4) Corso di lingua lombarda
5) Manifestazione dei Giovani Europei
6) Gay Pride
7) Intervista in TV
8) Partecipa a "Radio Lombardia Internazzional"
9) Manifestazione degli Alpini a Legnano """
		eventi = int(raw_input(":"))
		if eventi == 1:
			print "Fai un aperitivo con i candidati del PIM e incontri i cittadini di Caravaggio e Treviglio"
			elettori = elettori + 3
			puntipolitica = puntipolitica + random.randint(-2,1)
		if eventi == 2:
			je = random.randint(1,3)
			if je == 1:
				print "Il confronto lascia indifferente la popolazione"
				puntipolitica = puntipolitica + 3
			if je == 2:
				print "Colpisci i cuori dei cittadini, ottimo!"
				elettori = elettori + 6
				puntipolitica = puntipolitica + random.randint(0,3)
			if je == 3:
				print "Male male male... Gli avversari ti battono nettamente"
				elettori = elettori + random.randint(-3,2)
				puntipolitica = puntipolitica + random.randint(-3,1)
		if eventi == 3:
			print "Incontri a Bergamo il Segretario della Città Autonoma e ti 'benedice'"
			puntipolitica = puntipolitica + 5
		if eventi == 4:
			print "Prendi parte ad un corso di lingua lombarda: \n Importantissimo tutelare la nostra lingua, dici"
			elettori = elettori + random.randint(1,7)
			puntipolitica = puntipolitica + random.randint(-2,4)	
		if eventi == 5:
			print "Vai a manifestare coi Giovani Europei per l'Europa confederale"
			elettori = elettori + random.randint(-2,6)
			puntipolitica = puntipolitica + random.randint(0,5)
		if eventi == 6:
			print "Partecipi al Gay Pride di Cremona, elettorato gay alle stelle"
			elettori = elettori + random.randint(-6,10)
			puntipolitica = puntipolitica + random.randint(-1,6)	
		if eventi == 7:
			je = random.randint(1,3)
			if je == 1:
				print "Parli a 'Mediolanum TV', diffondi l'idea del partito ma passi subito a parlare di calcio a 5"
				puntipolitica = puntipolitica + 1
				elettori = elettori + random.randint(-2,3)
			if je == 2:
				print "Parli a 'Sodoku' e convinci molti indecisi a votare il PIM"
				elettori = elettori + 5
				puntipolitica = puntipolitica + random.randint(0,5)
			if je == 3:
				print "Sindaco liberale dimostra che sei incompetente in politica federale"
				elettori = elettori + random.randint(-6,3)
				puntipolitica = puntipolitica + random.randint(-4,3)	
		if eventi == 8:
			print "Parli a 'Radio Lombardia Internazzional' in lombardo e inglese. \n Ti ascoltano in tutta Europa e ottieni una medaglia del Partito Indipendente d'Europa"	
			elettori = elettori + 1
			puntipolitica = puntipolitica + random.randint(4,12)
		if eventi == 9:
			print "Prendi la ciucca e fai il simpaticone ricordando la tua leva nei vigili. Elettori divertiti, PIM meno. Molto meno"
			elettori = elettori + random.randint(2,8)
			puntipolitica = puntipolitica - random.randint(-2,5)		


	if puntipolitica > 85 and elettori > 45 and turno%5 == 0:
		print "Complimenti! Sei stato eletto Consigliere Comunale... Ma adesso dobbiamo arrivare più in altro... Diventare CapoZona della Capitale Bergamo"
		invio()
		clear()
		czonabg()
	else:
		invio()
		clear()
		ccomunale()

introd()
