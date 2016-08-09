#!/usr/bin/ python-
# -*- coding: utf-8 -*-
import os
import random
puntipolitica = 50
elettori = 5
seed = random.randint(1,99999)
turno = 0
boiler = 0
nomi = ["Mario","Alessio","Patrick","Adelio","Maria Augusta","Rin Michela","Rita","Altiero","Cesara","Giorgia","Francesco Ferdinando","Vittoria","Italia","Francesca Beatrice","Linus","Bartolo","Ariel","Gaetano","Alcide","Salvatore","Fermo","Giuliano","Domenico","Albano","Celere","Giulio Cesare","Valeria","Nicoletta","Ekaternia Giorgia","Jason Ambrogio","Alessia","Emilia","Selena","Alexis","Stefano","Olmo","Ariberto","Dolan","Ermenegilda","Teodolinda","Erminio","Beniamino","Michel","Bambin","Nazario","Paoletto","Glorioso","Gilberto","Helmut","Lotario","Arnaldo","Mauro Lupo","Teodorico","Noemi","Giulia","Adelaide","Roberta","Candace","Pier Giorgio","Andrea","Virgilio","Dante","Nazareno Michele","Ezechele","Lissander","Benìn","Giazint","Adolfino","Domenegh","Gnazzi","Grigoeu","Poldo","Zerill","Polonia","Gigi","Victoria","Agnese","Adelaide","Elvezia","Amanda","Iustizia","Caterina","Martina","Fiorenza","Melissa","Antioco","Barisone","Lucio","Cornelio","Peppone","Gastone","Genoveffo","Giasone","Gavino","Arnold","Cassio","Vercingetorice","Nerone","Anzolo","Tiberio","Mariello","Amerigo","Ernesto","Adamo","Karol","Manfredi","Rotario","Antonello","Alessandro","Michele","Amado","Nikolai","Egidio","Tracaro","Arcangelo","Duomo","Attanasio","Garrumo","Giandomenico","Ciociaro","Giorgio","Licio","Calogero","Mona","Germano","Ugo","Matteo","Attilio","Teodorico","Crescenzo","Arimanno","Floriano","Baldassarre","Berto","Roso","Catalino","Tromlino","Ambroeus","Francesco","Abbondio","Nunzio","Gerardo","Silvio","Alberto","Gianni","Teresio","Ambrogio","Anselmo","Giovese","Amintore","Italo","Arcibaldo","Justinià","Danjuro","Bortolo","Augusto","Piergastone","Diego","Giulio","Giuàn","Azeglio","Adolfo","Benito","Natale","Nazareno","Jorji"]
cognomi = ["Brambilla","Fumagalli","Rossi","dell'Incoronata","Schulzi","Fabero","Kofler","Coffiere","Verdi","Capellaro","da Pirla","Almirante","Casadei","Tettamanz/*i","Pessotti","Mastranzo","Nasdrovie","Dalle Colonie","Bono","Rovatacchini","Bianchi","Bernasca","Salvino","Porcu","Lefevre","Thompson","Vagneri","Sojuzzi","La Foppa","Dervalaporta","Sforza","Visconti","De Medici","Ottone","Di Calino","Aromano","Megrato","Suscrofa","Lazzaroni","Formaggi","Giamboni","Della Libertà","Di Pioltello","Feltrinelli","Zaccuri","Scoeura","Caselli","Wagner","Bottazzi","Guadone","de Brescello","Prestinée","Caterborino","Mariano","Eleatico","Ploeuv","Taleano","Loserbiddio","Berlinguer","Ol Careàs","Pisaelfoeuc","Puteo","Diletta","Dindina","Prondella","Mangiagalli","Cordileone","De Nicola","Battisti","Terione","Parisi","Contit","Elross","Koener","Wicewski","Milanese","Magutti","Scipoti","Auffo","Caronti","Veneranda Fabbrica","Scapece","Rensi","Bosse","Cetipaga","Dellinfermi","Legnano","Werrant","Scarpa","Soccuso","Varvaro","Moscerini","Mascio","Togliatti","Tramaglino","Ienneri","Kowalsky","Tomat","Muzzo","Putin","Ostuni","Fiorenza","Narodna","Piattirotti","Colleone","Mandi","Fanfani","Corsi","Romano","Perottini","Torvalds","da Giussano","Mantaro","Asburgo","Sala","Passalapalla","Plebfiore","Vaccini","De Stefano","Pizza","Rotino","Spoeusa","Alfulo","Cappi","Di Piero","Altissimo","Maroni","Olsone","Popov","Sensi","Bellotti","Conti","Invernizzi","Nicolello","Legramandi","Olivetti","Vignana","Carminati","Zennaro","Savoia","Figliodigesù","De Hiedler","Ferrero","Colombo","Manzon","Pravesin","Giussan","Lampugnan","Tanzi","Tanz","Galaràa","Bernascon","Hamzar","Rivetti","Lombardi","Basile","Degasperi","Culot","Toccaferro","Hamer","Granlavorador","Fantozzi","Nagotta","Mosconi","Perazzini","Mussolesi","Schavòn"]
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
def invio():
	raw_input("Premi invio per continuare")
def nome():
	global presidente
	global nome
	global seed
	nome = raw_input("Inserisci il tuo nome:")
	if nome == "Mike Sciking":
		presidente = "Ambrogio Conti"
	else:
		presidente = "Mike Sciking"
	print "Il tuo seed è", seed, ". Vuoi cambiarlo? (1) per cambiarlo"
	kem = raw_input(">")
	if kem == "1":
		print "Inserisci seed:"
		seed = input(">>")
	random.seed(seed)
	
	

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
			print "Candidato sindaco", nomi[random.randint(0,165)], cognomi[random.randint(0,165)],"del PIM alla processione al Santuario"
			puntipolitica = puntipolitica + random.randint(-3,5)
			elettori = elettori + random.randint(-1,5)
		else:
			print "Il candidato", nome, "al Convegno in Memoria della battaglia di Legnano parla: Ospiti commossi"
			puntipolitica = puntipolitica + random.randint(0,6)
			elettori = elettori + random.randint(-1,7)
	elif z == 5:
		if turno%2 == 0:
			print "Giornalino dei Giovani indipendenti"
			print "Il nostro candidato di Caravaggio incontra il Presidente della Catalogna:"
			print '"Nostre nazioni legate da profondissimo legame, Visca Catalunya i Llombardia lliures"'
			puntipolitica = puntipolitica + random.randint(-1,6)
			elettori = elettori + random.randint(-2,8)
		else:
			print nome, "all'aperitivo del fancazzista dichiara visibilmente ciucco: \n 'Non segarsi sulle belle ragazze è retrocedere' e canta Els Segadors"
	elif z == 6:
		if turno%2 == 0:
			print "Candidato del PIM Anziani arrestato per truffa"
			puntipolitica = puntipolitica + random.randint(-1,5)
			elettori = elettori + random.randint(-3,2)
		else:
			print "Sinistra ecologica contro gli inciuci di Sinistra. \nPerché supportano il candiato di Sinistra qui allora?"
			puntipolitica = puntipolitica + random.randint(-2,4)
			elettori = elettori + random.randint(-1,5)
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
		if turno%2 == 0:
			print nome, "chiede spazio per la Scienza a Caravaggio!"
			puntipolitica = puntipolitica + random.randint(-1,3)
			elettori = elettori + random.randint(-1,3)
		else:
			print "Strada della Morte a Treviglio: Governo federale stanzia 200000€ per le riparazioni"
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
8) Voterò contro al Registro Comunale Adozioni Omosessuali
9) Più potere per Insubria ed Orobia: Cantoni troppo potenti"""
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
		if giornale == 9:
			print nome,"vuole più potere per gli Stati e meno per i Cantoni"
			elettori = elettori + random.randint(-2,4)
			puntipolitica = puntipolitica + random.randint(-1,3)
	if turno%4 != 0:
		print "Cosa vuoi fare?"
		print """1) Aperitivo con i candidati
2) Confronto pubblico tra candidati
3) Viaggio a Bergamo per incontrare il Segretario Cittadino
4) Corso di lingua lombarda
5) Manifestazione dei Giovani Europei
6) Gay Pride
7) Intervista in TV
8) Partecipa a "Radio Lombardia Internazional"
9) Manifestazione degli Alpini a Legnano """
		try:
			eventi = int(raw_input(":"))
		except:
			print "ERRORE, inserisci un numero valido"
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
			print "Parli a 'Radio Lombardia Internazional' in lombardo e inglese. \n Ti ascoltano in tutta Europa e ottieni una medaglia del Partito Indipendente d'Europa"	
			elettori = elettori + 1
			puntipolitica = puntipolitica + random.randint(4,12)
		if eventi == 9:
			print "Prendi la ciucca e fai il simpaticone ricordando la tua leva nei vigili. Elettori divertiti, PIM meno. Molto meno"
			elettori = elettori + random.randint(2,8)
			puntipolitica = puntipolitica - random.randint(-6,2)	
		if eventi == 44:
			#variabili di debug
			puntipolitica = input("Puntipolitica:")
			elettori = input("Elettori:")
			turno = input("Turno:")


	if puntipolitica > 85 and elettori > 45 and turno%5 == 0:
		print "Complimenti! Sei stato eletto Consigliere Comunale... Ma adesso dobbiamo arrivare più in altro... Diventare CapoZona della Capitale Bergamo"
		print"""
Il CapoZona viene eletto semplicemente barrando il simbolo del PIM e delle Liste Alleate, dunque non dovrai fare molta propaganda come manifesti e santini.
Le elezioni si tengono ogni 6 turni e dovrai avere almeno 200 punti politica e 250 elettori. Eh si, non sono molto grosse le zone di Bergamo."""
		invio()
		clear()
		czonabg()
	else:
		invio()
		clear()
		ccomunale()


def indmil2():
	print "L'Indipendente di Bergamo"
	global puntipolitica
	global elettori
	global turno
	turno = turno + 1
	z = random.randint(1,12)
	if z == 1:
		if turno%2 == 0:
			print "Bollettino del III Distretto di Bergamo"
			print nome, "incontra gli altri candidati di Zona del PIM"
			elettori = elettori + 5
			puntipolitica = puntipolitica + random.randint(2,8)
		else:
			print nome, "presenta la sua ricetta per la lingua lombarda: 15 anni e tutti lo parleranno!"
			elettori = elettori + 3
			puntipolitica = puntipolitica + 4
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
		if turno%2 == 0:
			print "Il consigliere comunale caravaggese", nome, "parla dell'amicizia con il Veneto: Fratelli!"
			puntipolitica = puntipolitica + random.randint(1,9)
			elettori = elettori + random.randint(-1,8)
		else:
			print '"Più Pompini per tutti": La pubblicità del candidato PIM Piergastone Pompini fa discutere.'
			print nome, 'dichiara "Siamo alla follia"'
			puntipolitica = puntipolitica + random.randint(2,10)
			elettori = elettori + random.randint(-4,2)
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
	elif z == 11:
		ke = random.randint(1,3)
		if ke == 1:
			print nome, "all'attacco del candidato di sinistra: \n'Scelto dalle sinistre romane, non credo che pensa ai bergamaschi manco se lo vedo"
			puntipolitica = puntipolitica + random.randint(-1,8)
			elettori = elettori + random.randint(-2,8)
		if ke == 2:
			print "Ma la sinistra sa solo provocare? \nLoro candidato passa il tempo ad attaccare PIM e Liberali... Mancanza cronica d'argomenti"
			puntipolitica = puntipolitica + random.randint(0,2)
			elettori = elettori + random.randint(1,4)
		if ke == 3:
			print nome, "Al LUG di Caravaggio, elettorato hacker alle stelle"
			elettori = elettori + random.randint(-2,5)
	elif z == 12:
		ke = random.randint(1,3)
		if ke == 1:
			print nome, "incontra la cittadinanza con la sua ragazza, che piace molto al popolo"
			puntipolitica = puntipolitica + random.randint(-2,4)
			elettori = elettori + random.randint(1,6)
		if ke == 2:
			print "Candidato PIM non raccoglie la cacca del cane: Multato dalla Polizia Civile di Bergamo"
			puntipolitica = puntipolitica + random.randint(-2,2)
			elettori = elettori + random.randint(-2,5)
		if ke == 3:
			print nome, "torna alle origini: Discorso in sezione PIM di Caravaggio. Tutto il lombardo"
			elettori = elettori + random.randint(1,7)
			puntipolitica = puntipolitica + random.randint(2,6)
	#czonabg()
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
		print "Intervista! Cosa vuoi dichiarare all'Indipendente di Bergamo?"
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
		print """1) Cena con la cittadinanza
2) Confronto pubblico tra candidati
3) Incontro tra candidati PIM della Lombardia Orientale
4) Pellegrinaggio a Legnano
5) Incontro con gli Europarlamentari PIM
6) Manifestazione con i commercianti
7) Diretta TV
8) Partecipa a "Radio Lombardia Internazional"
9) Incontro con gli scolari della zona """
		try:
			eventi = int(raw_input(":"))
		except:
			print "ERRORE, inserisci un numero valido"
			eventi = int(raw_input(":"))
		if eventi == 1:
			print "Organizzi una cena per ascoltare i bisogni della popolazione"
			elettori = elettori + 8
			puntipolitica = puntipolitica + random.randint(-6,3)
		if eventi == 2:
			je = random.randint(1,3)
			if je == 1:
				print "Il confronto lascia indifferente la popolazione"
				puntipolitica = puntipolitica + 7
			if je == 2:
				print "Colpisci i cuori dei cittadini, ottimo!"
				elettori = elettori + 12
				puntipolitica = puntipolitica + random.randint(1,6)
			if je == 3:
				print "Male male male... Gli avversari ti battono nettamente"
				elettori = elettori + random.randint(-6,3)
				puntipolitica = puntipolitica + random.randint(-6,2)
		if eventi == 3:
			print "Incontri a Bergamo i candidati del resto della Lombardia orientale"
			puntipolitica = puntipolitica + 8
		if eventi == 4:
			print "Lasci per un giorno la politica e accompagni un gruppo della parrocchia a Legnano"
			elettori = elettori + random.randint(3,9)
			puntipolitica = puntipolitica + random.randint(-4,2)	
		if eventi == 5:
			print "Incontri gli europarlamentari del PIM insieme ad altri giovani candidati"
			elettori = elettori + random.randint(-3,8)
			puntipolitica = puntipolitica + random.randint(2,9)
		if eventi == 6:
			print "Manifesti con i commercianti bergamaschi: Elettorato locale alle stelle"
			elettori = elettori + random.randint(-8,12)
			puntipolitica = puntipolitica + random.randint(-2,8)	
		if eventi == 7:
			je = random.randint(1,3)
			if je == 1:
				print "Parli a 'TeleBergamo', diffondi l'idea del partito ma divaghi subito"
				puntipolitica = puntipolitica + 2
				elettori = elettori + random.randint(-4,4)
			if je == 2:
				print "Parli a 'Pomeriggio Milano' e convinci molti indecisi a votare il PIM"
				elettori = elettori + 10
				puntipolitica = puntipolitica + random.randint(1,6)
			if je == 3:
				print "Sindaco liberale riesce a far propaganda ai tuoi danni"
				elettori = elettori + random.randint(-8,3)
				puntipolitica = puntipolitica + random.randint(-6,5)	
		if eventi == 8:
			print "Parli a 'Radio Lombardia Internazional' in lombardo e inglese. \n Ti ascoltano in tutta Europa e ottieni una medaglia del Partito Indipendente d'Europa"	
			elettori = elettori + 4
			puntipolitica = puntipolitica + random.randint(8,14)
		if eventi == 9:
			print "Incontri gli alunni della zona e ascolti i loro problemi"
			elettori = elettori + random.randint(-4,9)
			puntipolitica = puntipolitica - random.randint(-4,10)
		if eventi == 44:
			#variabili di debug
			puntipolitica = input("Puntipolitica:")
			elettori = input("Elettori:")
			turno = input("Turno:")


	if puntipolitica > 200 and elettori > 250 and turno%6 == 0:
		print "Complimenti! Sei stato eletto CapoZona... Ma adesso dobbiamo arrivare più in altro..."
		print"""
Caro Candidato, sono il Preisdente del Partito. Nella Bergamasca abbiamo tanti giovani abili, e tu sei il migliore. Ma nell'alta Insubria, zona tradizionalmente
liberale, arranchiamo molto. Pertanto non correrai al Consiglio Autonomo di Bergamo, ma proverai a diventare sindaco della capitale dell'Alta Insubria: Como.
Finalmente potrai anche fare propaganda elettorale spendendo denaro, il Partito di darà 1500Å per turno. Divertiti. Le elezioni saranno ogni 7 turni e dovrai avere almeno 800 punti politica e 600 elettori."""
		invio()
		clear()
		sindaco()
	else:
		invio()
		clear()
		czonabg()

def indmil3():
	global boiler
	global gg
	print "L'Indipendente di Como"
	global puntipolitica
	global elettori
	global turno
	turno = turno + 1
	z = random.randint(1,15)
	if z == 1:
		print nome, "incontra gli altri candidati del PIM altinsbure"
		elettori = elettori + 10
		puntipolitica = puntipolitica + random.randint(6,12)
	elif z == 2:
		if turno%2 == 0:
			print "Incredibile! Rampollo della Sinistra lascia e si unisce al PIM!"
			elettori = elettori + 20
			puntipolitica = puntipolitica + 12
		else:
			print "Senato dell'Insubria: Mozione PIM per aumentare il lombardo passa"
			elettori = elettori + 6
	elif z == 3:
		if turno%2 == 0:
			print "Per errori tecnici la lista amica 'Forza Como' non potrà correre con noi"
			puntipolitica = puntipolitica + 10
			elettori = elettori - 8
		else:
			print "La lista avversaria 'Sinistra Comasca' non parteciperà per problemi legali del candidato"
			elettori = elettori + 8
	elif z == 4:
		if turno%2 == 0:
			print  nome, "contro l'area B di Como: \nEcologia spicciola di sinistra: La aboliremo."
			puntipolitica = puntipolitica + random.randint(2,12)
			elettori = elettori + random.randint(-2,12)
		else:
			print "Presidente PIM: Unica via d'Autonomia per Lombardia Alpina è creare nuovo stato, faremo referendum"
			elettori = elettori + 3
	elif z == 5:
		print nome,"contro la riforma linguistica di sinistra: 'Fascista: Non tutela lombardo ed emiliano'"
		puntipolitica = puntipolitica + random.randint(-2,14)
		elettori = elettori + random.randint(-4,12)
	elif z == 6:
		if turno %2 == 0:
			print "Como: Il Movimento Popolare apre la sua sede e si candida"
			puntipolitica = puntipolitica + random.randint(0,6)
			elettoriinfu = elettori + random.randint(-6,4)
		else:
			print "Lume della Ragione supporta", nome, ". Consideratelo nostro candidato"
			elettori = elettori + 12
	elif z == 7:
		if turno%6 == 0:
			print nome,"fotografato al citofono: Elettorato Testimone di Geova alle stelle"
			puntipolitica = puntipolitica + random.randint(-2,6)
			elettori = elettori + random.randint(-4,2)		
		else:
			print "PIM contro il metetricio in strada: Daremo licenza per due postriboli a Como"
			puntipolitica = puntipolitica + random.randint(-1,8)
			elettori = elettori + random.randint(-4,10)
	elif z == 8:
		if turno%5 == 0:
			print "Candidato della Sinistra dimentica di essere incandidabile, e vinciamo noi di default..."
			elettori = int(elettori*1.4)
			puntipolitica = int(puntipolitica*1.5)
		else:
			print nome, "incontra i dipendenti della fabbrica di pantofole 'Zibrett Srl'" #ciao Dalan <3
			puntipolitica = puntipolitica + random.randint(0,5)
			elettori = elettori + random.randint(3,12)
	elif z == 9:
		print nome, "vuole esportare il modello Bergamo a Como: Analisti perplessi"
		puntipolitica = puntipolitica + random.randint(0,7)
		elettori = elettori + random.randint(-6,14)
	elif z == 10:
		if turno%3 == 0:
			print "Il Presidente del Senato insubre incontra", nome
			puntipolitica = puntipolitica + random.randint(-2,12)
			elettori = elettori + random.randint(-4,12)
		else:
			print nome, "criticissimo sull'unità d'Italia: \nNon siamo italiani geograficamente e mai lo saremo politcamente"
			puntipolitica = puntipolitica + random.randint(1,7)
			elettori = elettori + random.randint(-2,6)
	elif z == 11:
		ke = random.randint(1,3)
		if ke == 1:
			print nome, "incontra il governo tirolese: 'Nazione con 5 lingue, da stimare'"
			puntipolitica = puntipolitica + random.randint(-1,12)
			elettori = elettori + random.randint(-3,10)
		if ke == 2:
			print "Il PIM e i liberali chiedono più controlli alla frontiera: La Sinistra si oppone"
			puntipolitica = puntipolitica + random.randint(0,4)
			elettori = elettori + random.randint(1,6)
		if ke == 3:
			print nome, "rappresenta Bergamo al Parlamento Europeo."
			elettori = elettori + random.randint(-1,8)
	elif z == 12:
		ke = random.randint(1,3)
		if ke == 1:
			print nome, "vuole uno psicologo in ogni scuola comasca"
			puntipolitica = puntipolitica + random.randint(-2,6)
			elettori = elettori + random.randint(2,10)
		if ke == 2:
			print "Candidato PIM vuole rendere illegale il culto in pubblico a Como"
			puntipolitica = puntipolitica + random.randint(0,4)
			elettori = elettori + random.randint(-6,4)
		if ke == 3:
			print nome, "cementifica rapporti tra PIM Insubre e Bergamasco"
			elettori = elettori + random.randint(1,7)
			puntipolitica = puntipolitica + random.randint(4,12)
	elif z == 13:
		print nome, "vuole una carta dei diritti internet 'sviluppata con l'idea hacker'"
		elettori = elettori + random.randint(-2,7)
		puntipolitica = puntipolitica + random.randint(1,8)
	elif z == 14:
		if boiler == 0:
			print nome, "fotografato sotto il cartello 'non si affittano case ai meridionali'"
			elettori = elettori + random.randint(-6,3)
			puntipolitica = puntipolitica + random.randint(-4,4)	
		else:
			print "Liberali rinunciano alla loro campagna in favore del PIM"
			puntipolitica = puntipolitica + 10
			elettori = elettori + 30
	elif z == 15:
		if turno%2 == 0:
			print "Costava, sindaco di Bergamo PIM, attacca la chiesa 'Omofoba e maschilista'"
			elettori = elettori + random.randint(-2,8)
			puntipolitica = puntipolitica + random.randint(-2,6)
		else:
			print "Europei di calcio, la Lombardia batte la Catalogna 3-1 in finale!"
				
	#czonabg()
def sindaco(): #che sarebbe sindaCO, non sindaco :D
	indmil3()
	global turno
	global puntipolitica
	global elettori
	global nome
	global presidente
	print "Turno:", turno
	print "Hai", elettori, "elettori"
	print "Hai", puntipolitica, "influenza"
	if turno%4 == 0:
		print "Intervista! Cosa vuoi dichiarare all'Indipendente di Como?"
		print """1) Miglioreremo il trasporto pubblico a Como!
2) Vogliamo un posto per Como al Senato Insubre!
3) Daremo più potere alle zone
4) Faremo cose particolari per la Città
5) Miglioreremo i rapporti con Chiasso e il Ticino
6) Meno punizioni per chi entra nelle nostre case
7) Darò il potere a tutti gli assessori di far decreti"
8) Faremo risoluzione contro l'unità italiana
9) Il lombardo sarà unica lingua di Como"""
		giornale = int(raw_input(":"))
		print "L'Indipendente di Como"
		if giornale == 2:
			print nome, "vuole Como al Senato Insubre!"
			elettori = elettori + random.randint(2,14)
			puntipolitica = puntipolitica - random.randint(-2,10)
		if giornale == 1:
			print nome, "vuole il trasporto pubblico migliore della Lombardia!"
			elettori = elettori + random.randint(2,10)
			puntipolitica = puntipolitica + random.randint(-2,8)
		if giornale == 3:
			print "Il CapoZona candidato sindaco PIM vuole il federalismo comunale: Cittadini perplessi"
			elettori = elettori + random.randint(-4,10)
			puntipolitica = puntipolitica + random.randint(-2,10)
		if giornale == 4:
			lm = random.randint(1,3)
			if lm == 1:
				print "Metropolitana sopraelevata a Como, con corse per il Lago e il Ticino, strana proposta di", nome, "."
				elettori = elettori + random.randint(-2,8)
				puntipolitica = puntipolitica + random.randint(-2,6)
			if lm == 2:
				print "Il PIM vuole la moschea a Como. Cittadini imbufaliti"
				elettori = elettori + random.randint(-8,4)
				puntipolitica = puntipolitica + random.randint(-2,2)
			if lm == 3:
				print "Un PC per famiglia, la proposta di", nome, "fa discutere."
				elettori = elettori + random.randint(-4,10)
				puntipolitica = puntipolitica + random.randint(-3,12)
		if giornale == 6:
			print nome, "vuole premiare i criminali con castighi di paglia"
			elettori = elettori + random.randint(-10,4)
			puntipolitica = puntipolitica + random.randint(-5,2)
		if giornale == 7:
			print "Il PIM darà più potere agli assessori"
			elettori = elettori + random.randint(-1,9)
			puntipolitica = puntipolitica + random.randint(-2,8)
		if giornale == 5:
			print "'Siamo tutti lombardi': Ecco la frase del candidato PIM per aumentare i rapporti con Chiasso"
			elettori = elettori + random.randint(2,8)
			puntipolitica = puntipolitica + random.randint(-2,12)
		if giornale == 8:
			print "PIM Comasco vuole andare contro all'Italia con una risoluzione"
			elettori = elettori + random.randint(-2,6)
			puntipolitica = puntipolitica + random.randint(2,6)
		if giornale == 9:
			print "Lombardo unica lingua a Como? Proposta interessante per i Liberali, la Sinistra dice no"
			elettori = elettori + 4
			puntipolitica = puntipolitica + 4
	if turno%4 != 0:
		print "Cosa vuoi fare?"
		print """1) Serata con la cittadinanza
2) Confronto pubblico tra candidati
3) Incontro coi candidati di zona del PIM
4) Stampa santini
5) Incontro con i Senatori PIM
6) Manifestazione con i cittadini di periferia
7) Diretta TV
8) Partecipa a "Radio Lombardia Internazional"
9) Stampa manifesti"""
		try:
			eventi = int(raw_input(":"))
		except:
			print "ERRORE, inserisci un numero valido"
			eventi = int(raw_input(":"))
		if eventi == 1:
			print "Organizzi una serata per ascoltare i bisogni della popolazione"
			elettori = elettori + 12
			puntipolitica = puntipolitica + random.randint(-4,8)
		if eventi == 2:
			je = random.randint(1,3)
			if je == 1:
				print "Il confronto lascia indifferente la popolazione"
				puntipolitica = puntipolitica + 8
			if je == 2:
				print "Colpisci i cuori dei cittadini, ottimo!"
				elettori = elettori + 16
				puntipolitica = puntipolitica + random.randint(1,8)
			if je == 3:
				print "Male male male... Gli avversari ti battono nettamente"
				elettori = elettori + random.randint(-6,4)
				puntipolitica = puntipolitica + random.randint(-8,2)
		if eventi == 3:
			print "Incontri i candidati di zona del PIM e delle liste che ci sostengono"
			puntipolitica = puntipolitica + 10
		if eventi == 4:
			print "Stampi santini elettorali"
			elettori = elettori + random.randint(1,20)
			puntipolitica = puntipolitica + random.randint(1,5)	
		if eventi == 5:
			print "Incontri i Senatori del PIM al Consiglio Federale e al Senato Insubre con dei cittadini"
			elettori = elettori + random.randint(1,12)
			puntipolitica = puntipolitica + random.randint(2,14)
		if eventi == 6:
			print "Manifesti con i cittadini di periferia contro il degrado: Elettorato locale alle stelle"
			elettori = elettori + random.randint(-2,20)
			puntipolitica = puntipolitica + random.randint(-2,10)	
		if eventi == 7:
			je = random.randint(1,3)
			if je == 1:
				print "Parli a 'TeleChasso', diffondi l'idea del partito ma divaghi subito"
				puntipolitica = puntipolitica + 6
				elettori = elettori + random.randint(-6,6)
			if je == 2:
				print "Parli a 'Milan Incoeu' e convinci molti indecisi a votare il PIM"
				elettori = elettori + 20
				puntipolitica = puntipolitica + random.randint(2,12)
			if je == 3:
				print "'Lo Sciacallo' ti intervista e dimostra la tua incompetenza in molte materie"
				elettori = elettori + random.randint(-12,5)
				puntipolitica = puntipolitica + random.randint(-8,4)	
		if eventi == 8:
			print "Parli a 'Radio Lombardia Internazional' in lombardo e inglese. \n Ti ascoltano in tutta Europa e ottieni una medaglia del Partito Indipendente d'Europa"	
			elettori = elettori + 10
			puntipolitica = puntipolitica + random.randint(10,18)
		if eventi == 9:
			print "Stampi manifesti"
			elettori = elettori + random.randint(10,50)
			puntipolitica = puntipolitica - random.randint(-20,5)
		if eventi == 44:
			#variabili di debug
			puntipolitica = input("Puntipolitica:")
			elettori = input("Elettori:")
			turno = input("Turno:")		


	if puntipolitica > 800 and elettori > 600 and turno%7 == 0:
		print "Complimenti! Sei stato eletto Sinaco... Ma adesso dobbiamo arrivare più in altro..."
		print"""
Vogliamo candidarti Presidente della Città Autonoma di Novara. Giorgio Costava è stato eletto Consigliere Autonomo e potrà darti man forte nella tua candidatura.
Il tuo ruolo è importantissimo, visto che farai parte del Senato Insubre. Dovrai avere 1500 elettori e 1750 punti infulenza. Le elezioni sono ogni 6 turni."""
		gg = 0
		invio()
		clear()
		presidentecantonale()
	else:
		invio()
		clear()
		sindaco()

def indmil4():
	print "L'Indipendente di Novara"
	global puntipolitica
	global elettori
	global turno
	turno = turno + 1
	z = random.randint(1,15)
	if z == 1:
		print nome, "incontra il presidente del Partito Indipendente!"
		elettori = elettori + 15
		puntipolitica = puntipolitica + random.randint(10,15)
	elif z == 2:
		if turno%2 == 0:
			print "Incredibile! Rampollo della Sinistra lascia e si unisce al PIM!"
			elettori = elettori + 25
			puntipolitica = puntipolitica + 15
		else:
			print "Il Senato Insubre ha un presidente novarese e indipendente!"
			elettori = elettori + 10
	elif z == 3:
		if turno%2 == 0:
			print "Per errori tecnici la lista amica 'Novara Unica' non potrà correre con noi"
			puntipolitica = puntipolitica + 12
			elettori = elettori - 10
		else:
			print "La lista avversaria 'Novara Sociale' non parteciperà per problemi legali del candidato"
			elettori = elettori + 10
	elif z == 4:
		if turno%2 == 0:
			print  nome, "contro la legge d'autonomia odierna: Daremo autonomia ai comuni"
			puntipolitica = puntipolitica + random.randint(4,12)
			elettori = elettori + random.randint(-3,20)
		else:
			print nome, "simpaticamente contro a chi fa togliere le scarpe agli ospiti:"
			print '"Li rispedirò a casa loro in Austria", dice ridendo'
	elif z == 5:
		if turno%2==0:
			print nome,"dichiara 'Novara è lombarda, sempre lo è stata e sempre lo sarà!"
			puntipolitica = puntipolitica + random.randint(0,16)
			elettori = elettori + random.randint(-4,18)
		else:
			print nome,"al convegno del Movimento Poschiavo Lombarda: Spero presto vi possiate unire con un referendum"
			puntipolitica = puntipolitica + 7
			elettori = elettori + random.randint(1,9)
	elif z == 6:
		if turno %2 == 0:
			print "Novara: Il Movimento Popolare apre la sua sede e si candida"
			puntipolitica = puntipolitica + random.randint(0,6)
			elettori = elettori + random.randint(-6,4)
		else:
			print "Lume della Ragione supporta", nome, ". Consideratelo nostro candidato"
			elettori = elettori + 12
	elif z == 7:
		if turno%6 == 0:
			print nome,"fotografato al citofono: Elettorato Testimone di Geova alle stelle"
			puntipolitica = puntipolitica + random.randint(-2,6)
			elettori = elettori + random.randint(-4,2)		
		else:
			print "PIM contro il metetricio in strada: Daremo licenza per due postriboli a Como"
			puntipolitica = puntipolitica + random.randint(-1,8)
			elettori = elettori + random.randint(-4,10)
	elif z == 8:
		if turno%5 == 0:
			print "Candidato della Sinistra dimentica di essere incandidabile, e vinciamo noi di default..."
			elettori = int(elettori*1.4)
			puntipolitica = int(puntipolitica*1.5)
		else:
			print nome, "incontra i dipendenti della fabbrica di pantofole 'Zibrett Srl'" #ciao Dalan <3
			puntipolitica = puntipolitica + random.randint(0,5)
			elettori = elettori + random.randint(3,12)
	elif z == 9:
		if turno%2 == 0:
			print nome, "parla dell'alleanza coi Radicali: Tutto ok"
			puntipolitica = puntipolitica + random.randint(0,7)
			elettori = elettori + random.randint(-6,14)
		else:
			print nome, "contro alla legge sul pedoporno: 'Una 16enne dev'esse libera di fotografarsi nuda'"
	elif z == 10:
		if turno%3 == 0:
			print "Il Presidente del Senato insubre incontra", nome
			puntipolitica = puntipolitica + random.randint(-2,12)
			elettori = elettori + random.randint(-4,12)
		else:
			print nome, "criticissimo sull'unità d'Italia: \nNon siamo italiani geograficamente e mai lo saremo politcamente"
			puntipolitica = puntipolitica + random.randint(1,7)
			elettori = elettori + random.randint(-2,6)
	elif z == 11:
		ke = random.randint(1,3)
		if ke == 1:
			print nome, "a Malta: Incontro fondamentale per l'accesso dell'Isola all'Unione Europea, si parla delle minoranze"
			puntipolitica = puntipolitica + random.randint(-2,14)
			elettori = elettori + random.randint(-4,12)
		if ke == 2:
			print "Scuola trilingue PIM: Cittadini perplessi, il linguista Baschi tranquillizza 'Ottimo per i bambini'"
			puntipolitica = puntipolitica + random.randint(2,8)
			elettori = elettori + random.randint(-2,4)
		if ke == 3:
			print nome, "parla al Convegno delle Cinque Giornate e commuove tutti"
			elettori = elettori + random.randint(-2,10)
	elif z == 12:
		ke = random.randint(1,3)
		if ke == 1:
			print nome, "chiede tutele per i piemontesofoni"
			puntipolitica = puntipolitica + random.randint(-2,6)
			elettori = elettori + random.randint(2,10)
		if ke == 2:
			print "Candidato PIM vuole rendere legale il nudismo"
			puntipolitica = puntipolitica + random.randint(0,4)
			elettori = elettori + random.randint(-6,4)
		if ke == 3:
			print nome, "cementa rapporti tra PIM Insubre e Bergamasco"
			elettori = elettori + random.randint(1,7)
			puntipolitica = puntipolitica + random.randint(4,12)
	elif z == 13:
		if turno%2 == 0:
			print nome, "vuole una carta dei diritti internet 'sviluppata con l'idea hacker'"
			elettori = elettori + random.randint(-2,7)
			puntipolitica = puntipolitica + random.randint(1,8)
		else:
			print nome, "dichiara: 'Lingua lombarda è lingua giovane'"
			elettori = elettori + random.randint(1,12)
			puntipolitica = puntipolitica + random.randint(1,8)
	elif z == 14:
		if turno%2 == 0:
			print "Liberali rinunciano alla loro campagna in favore del PIM"
			puntipolitica = puntipolitica + 10
			elettori = elettori + 30
		else:
			print "Destra folle: Prima si candida, poi sotitene lista locale, poi si ricandida e poi sostiene imprenditore Flavio Marchelli"
			print "Il Presidente: Sinistra centralista incompetente, Liberali incapaci di tenere una coalizione dopo i voti: Noi unica alternativa"
			puntipolitica = puntipolitica + 15
			elettori = elettori + 15
	elif z == 15:
		if turno%2 == 0:
			print "Costava, sindaco di Bergamo PIM, attacca la chiesa 'Omofoba e maschilista'"
			elettori = elettori + random.randint(-2,8)
			puntipolitica = puntipolitica + random.randint(-2,6)
		else:
			print "Nasce la Lista Civica per", nome, "Presidente!"
			elettori = elettori + 5
			puntipolitica = puntipolitica + 5
				
	#czonabg()
def presidentecantonale():
	indmil4()
	global turno
	global puntipolitica
	global elettori
	global nome
	global presidente
	print "Turno:", turno
	print "Hai", elettori, "elettori"
	print "Hai", puntipolitica, "influenza"
	if turno%4 == 0:
		print "Intervista! Cosa vuoi dichiarare all'Indipendente di Novara?"
		print """1) Più autonomia per la Nostra Città Autonoma!
2) Se il Presidente mi chiedesse di dimettermi lo farei senza dubbio
3) Novara vivrebbe meglio in un contesto confederale padano
4) Faremo cose particolari per la Città Autonoma
5) Non sventolerei il tricolore italiano nemmeno sotto remunerazione
6) Prima gli stranieri a Novara!
7) Farò una riforma vaccinale importante
8) Ferrovia veloce Novara-Milano-Bergamo obiettivo primario
9) Programmazione in inglese materia obbligatoria nelle nostre scuole, Insubria volente o nolente"""
		giornale = int(raw_input(":"))
		print "L'Indipendente di Novara"
		if giornale == 2:
			print nome, "schiavo di Milano! Si dimetterebbe su semplice richiesta del governo centrale!"
			elettori = elettori + random.randint(-10,5)
			puntipolitica = puntipolitica + random.randint(-20,15)
		if giornale == 1:
			print nome, "vuole più autonomia per la nostra Città Autonoma!"
			elettori = elettori + random.randint(5,20)
			puntipolitica = puntipolitica + random.randint(-6,12)
		if giornale == 3:
			print "Novara Padana? Idea del PIM fa parlare molto..."
			elettori = elettori + random.randint(-6,15)
			puntipolitica = puntipolitica + random.randint(-4,12)
		if giornale == 4:
			lm = random.randint(1,3)
			if lm == 1:
				print "Nuove strade ciclistiche e automobilistiche tra Novara e Ossola, proposta di", nome, "."
				elettori = elettori + random.randint(-2,10)
				puntipolitica = puntipolitica + random.randint(-2,6)
			if lm == 2:
				print "Utero in affitto in tutti gli ospedali pubblici per il PIM. Cittadini imbufaliti"
				elettori = elettori + random.randint(-12,4)
				puntipolitica = puntipolitica + random.randint(-10,4)
			if lm == 3:
				print "Scuole aperte la domenica, la proposta di", nome, "fa discutere."
				elettori = elettori + random.randint(-6,12)
				puntipolitica = puntipolitica + random.randint(-6,20)
		if giornale == 6:
			print nome, "vuole prima gli stranieri a Novara!"
			elettori = elettori + random.randint(-10,4)
			puntipolitica = puntipolitica + random.randint(-5,2)
		if giornale == 7:
			print "Il PIM vuole i nuovi vaccini: Più sicuri e obbligatorietà decisa ogni 3 mesi dal Presidente"
			elettori = elettori + random.randint(2,12)
			puntipolitica = puntipolitica + random.randint(-4,16)
		if giornale == 5:
			print nome, "contro al tricolore italico: Non lo sventolerebbe nemmeno dietro pagamento"
			elettori = elettori + random.randint(2,12)
			puntipolitica = puntipolitica + random.randint(-2,12)
		if giornale == 8:
			print "PIM vuole ferrovia veloce tra Novara e Milano!"
			elettori = elettori + random.randint(-4,10)
			puntipolitica = puntipolitica + random.randint(5,12)
		if giornale == 9:
			print nome, "vuole la programmazione a scuola, anche se contro al volere dello Stato Insubre"
			elettori = elettori + 12
			puntipolitica = puntipolitica + 6
	if turno%4 != 0:
		print "Cosa vuoi fare?"
		print """1) Incontro con la cittadinanza al Teatro Federale
2) Confronto pubblico tra candidati
3) Incontro coi sindaci del PIM Novara
4) Pubblicità televisiva e radio
5) Incontro con i ragazzi di "Podèmm"
6) Manifestazione con i giovani del PIM
7) Diretta TV
8) Partecipa a "Radio Lombardia Internazional"
9) Stampa manifesti"""
		try:
			eventi = int(raw_input(":"))
		except:
			print "ERRORE, inserisci un numero valido"
			eventi = int(raw_input(":"))
		if eventi == 1:
			print "Organizzi una serata per ascoltare i bisogni della popolazione"
			elettori = elettori + 20
			puntipolitica = puntipolitica + random.randint(-10,8)
		if eventi == 2:
			je = random.randint(1,3)
			if je == 1:
				print "Il confronto lascia indifferente la popolazione"
				puntipolitica = puntipolitica + 12
			if je == 2:
				print "Colpisci i cuori dei cittadini, ottimo!"
				elettori = elettori + 30
				puntipolitica = puntipolitica + random.randint(1,12)
			if je == 3:
				print "Male male male... Gli avversari ti battono nettamente"
				elettori = elettori + random.randint(-10,2)
				puntipolitica = puntipolitica + random.randint(-10,2)
		if eventi == 3:
			print "Incontri i candidati di zona del PIM e delle liste che ci sostengono"
			puntipolitica = puntipolitica + 15
		if eventi == 4:
			print "Fai pubblicità"
			elettori = elettori + random.randint(1,40)
			puntipolitica = puntipolitica + random.randint(5,25)	
		if eventi == 5:
			print "Incontri i ragazzi della piattaforma politica 'Podèmm', subito intesa con l'idea 'Obiettivo Comunità'"
			elettori = elettori + random.randint(-2,20)
			puntipolitica = puntipolitica + random.randint(-7,14)
		if eventi == 6:
			print "Manifesti con i giovani del PIM e broccoli qualche ragazza del luogo"
			elettori = elettori + random.randint(-4,30)
			puntipolitica = puntipolitica + random.randint(-2,20)	
		if eventi == 7:
			je = random.randint(1,3)
			if je == 1:
				print "Parli a 'Novarese TV', diffondi l'idea del partito ma poi parli di tutt'altro"
				puntipolitica = puntipolitica + 10
				elettori = elettori + random.randint(-10,15)
			if je == 2:
				print "Parli a 'Noara Ancheuj', TV della minoranza piemontesofona, e convinci molti indecisi a votare il PIM"
				elettori = elettori + 30
				puntipolitica = puntipolitica + random.randint(-6,12)
			if je == 3:
				print "Perdi palesemente il dibattito con il Movimento Popolare"
				elettori = elettori + random.randint(-12,5)
				puntipolitica = puntipolitica + random.randint(-8,4)	
		if eventi == 8:
			print "Parli a 'Radio Lombardia Internazional' in lombardo e inglese. \n Ti ascoltano in tutta Europa e ottieni una medaglia del Partito Indipendente d'Europa"	
			elettori = elettori + 20
			puntipolitica = puntipolitica + random.randint(10,18)
		if eventi == 9:
			print "Stampi manifesti"
			elettori = elettori + random.randint(30,100)
			puntipolitica = puntipolitica - random.randint(-30,10)	
		if eventi == 44:
			#variabili di debug
			puntipolitica = input("Puntipolitica:")
			elettori = input("Elettori:")
			turno = input("Turno:")	


	if puntipolitica > 1500 and elettori > 1750 and turno%6 == 0:
		print "Complimenti! Sei stato eletto Presidente Cantonale... Ma adesso dobbiamo arrivare più in altro..."
		print"""
Sarai candidato Presidente della Città di Milano, e prenderai parte al Direttorio Federale in veste di osservatore. Ti serviranno 2250 punti influenza e 2000 elettori. Le elezioni sono ogni 7 turni. """
		invio()
		clear()
		premil()
	else:
		invio()
		clear()
		presidentecantonale()

def indmil5():
	print "L'Indipendente Meneghino"
	global puntipolitica
	global elettori
	global turno
	turno = turno + 1
	z = random.randint(1,15)
	if z == 1:
		print nome, "incontra il Sindaco di Milano e della Città Autonoma!"
		elettori = elettori + 20
		puntipolitica = puntipolitica + random.randint(15,25)
	elif z == 2:
		if turno%2 == 0:
			print "Incredibile! Rampollo della Destra lascia e si unisce al PIM!"
			elettori = elettori + 30
			puntipolitica = puntipolitica + 20
		else:
			print nome, "contro alla Lega della Famiglia:\n 'Famiglia tradizionale idiozia cambiata ogni anno, unica limitazione da dare ai gay è sulle adozioni"
			elettori = elettori + random.randint(-10,20)
	elif z == 3:
		if turno%2 == 0:
			print "Per errori tecnici la lista amica 'Lega dei Milanesi' non potrà correre con noi"
			puntipolitica = puntipolitica + 20
			elettori = elettori - 15
		else:
			print "La lista avversaria 'Partito Cristiano dei Milanesi' non parteciperà per problemi legali del candidato"
			elettori = elettori + 15
	elif z == 4:
		print  nome, "vuole abolire le polizie comunali a Milano: 'Spreco inutile'"
		puntipolitica = puntipolitica + random.randint(-2,10)
		elettori = elettori + random.randint(-10,30)
	elif z == 5:
		if turno%2==0:
			print nome,"incontra il Presidente dell'Autonomia Galiziana: 'Presto sarete stato alleato della Lombardia'"
			puntipolitica = puntipolitica + random.randint(0,20)
			elettori = elettori + random.randint(-10,28)
		else:
			print nome,"vuole limitare il tabacco e proibirlo ai minori."
			puntipolitica = puntipolitica + 30
			elettori = elettori + random.randint(10,45)
	elif z == 6:
		if turno %2 == 0:
			print "Il Partito dei Lombardi ci prova a Milano!"
			puntipolitica = puntipolitica + random.randint(2,12)
			elettori = elettori + random.randint(-10,2)
		else:
			print "Summit di Podèmm: Ufficiale supporto a:", nome
			elettori = elettori + 20
	elif z == 7:
		if turno%6 == 0:
			print nome,"e la barzelletta sull'11/9 non gradita: Elettorato in calo"
			puntipolitica = puntipolitica + random.randint(-10,3)
			elettori = elettori + random.randint(-10,2)		
		else:
			print "PIM 'pagherà di tasca propria' il Centro Polacco:"
			print nome, 'dice "Nazione polacca e lombarda da sempre unite, dagli eventi di Reggio Lombardia"'
			puntipolitica = puntipolitica + random.randint(-2,12)
			elettori = elettori + random.randint(-6,20)
	elif z == 8:
		if turno%5 == 0:
			print "Candidato della Sinistra dimentica di essere incandidabile, e vinciamo noi di default..."
			elettori = int(elettori*1.4)
			puntipolitica = int(puntipolitica*1.5)
		else:
			print nome, "incontra i dipendenti dell'Azienda Informatica di Stato ELECALCO" 
			puntipolitica = puntipolitica + random.randint(2,10)
			elettori = elettori + random.randint(5,20)
	elif z == 9:
		if turno%2 == 0:
			print nome, "agli immigrati napoletani 'Integratevi o tornatevene a casa vostra'"
			puntipolitica = puntipolitica + random.randint(-15,1)
			elettori = elettori + random.randint(-10,22)
		else:
			print "Incredibile: Candidato di sinistra chiama erroneamente il suo candidato 'Beppe Stalin'"
	elif z == 10:
		if turno%3 == 0:
			print "Liberali truccano sondaggi? Dubbio insinuato da", nome
			puntipolitica = puntipolitica + random.randint(-5,5)
			elettori = elettori + random.randint(-20,20)
		else:
			print "Sinistra nega le origini lombarde di Milano"
			puntipolitica = puntipolitica + random.randint(1,7)
			elettori = elettori + random.randint(0,15)
	elif z == 11:
		ke = random.randint(1,3)
		if ke == 1:
			print nome, "alla Parata Bergamasca per il Giorno della Lombardia"
			puntipolitica = puntipolitica + random.randint(0,15)
			elettori = elettori + random.randint(-2,20)
		if ke == 2:
			print "Scandalo nella Chiesa: 12 arresti e 200 denunzie: Politica anticlericale del PIM vicente"
			puntipolitica = puntipolitica + random.randint(5,15)
			elettori = elettori + random.randint(5,25)
		if ke == 3:
			print nome, "incontra i cittadini di Caravaggio per ricordare le sue origini politiche"
			elettori = elettori + random.randint(-2,10)
	elif z == 12:
		ke = random.randint(1,3)
		if ke == 1:
			print nome, "vuole tutti i cartelli bilingue a Milano!"
			puntipolitica = puntipolitica + random.randint(-4,12)
			elettori = elettori + random.randint(5,20)
		if ke == 2:
			print "Alleanza Municipale: L'Alternativa locale al PIM non convince"
			puntipolitica = puntipolitica + random.randint(-4,4)
			elettori = elettori + random.randint(-10,6)
		if ke == 3:
			print nome, "con la maglia indipendentisca catalana al convegno sull'unità italiana. Forse fuori luogo?"
			elettori = elettori + random.randint(-10,10)
			puntipolitica = puntipolitica + random.randint(4,12)
	elif z == 13:
		if turno%2 == 0:
			print nome, "ha il supporto dell'Arcobaleno Pensionati!"
			elettori = elettori + random.randint(-3,10)
			puntipolitica = puntipolitica + random.randint(1,8)
		else:
			print nome, "all'aperitivo federale PIM ci rappresenta e racconta simpatiche storielle!"
			elettori = elettori + random.randint(1,12)
			puntipolitica = puntipolitica + random.randint(1,8)
	elif z == 14:
		if turno%2 == 0:
			print "Noi Milano, famosa lista civica, correrà con noi!"
			puntipolitica = puntipolitica + 10
			elettori = elettori + 30
		else:
			print "Destra presenta il supercandidato: Imprenditore famoso e ricco"
			puntipolitica = puntipolitica - 15
			elettori = elettori - 20
	elif z == 15:
		if turno%2 == 0:
			print "Parito Panificatori: Idee giuste ma modo sbagliato. Davvero?"
			elettori = elettori + random.randint(-5,12)
			puntipolitica = puntipolitica + random.randint(-10,4)
		else:
			print "Comitato spontaneo di cittadini correrà per", nome, "Presidente!"
			elettori = elettori + 8
			puntipolitica = puntipolitica + 4
				
	#czonabg()
def premil():
	indmil5c()
	global turno
	global puntipolitica
	global elettori
	global nome
	global presidente
	print "Turno:", turno
	print "Hai", elettori, "elettori"
	print "Hai", puntipolitica, "influenza"
	if turno%4 == 0:
		print "Intervista! Cosa vuoi dichiarare all'Indipendente Meneghino?"
		print """1) Porremo la sede della Città Autonoma al Castello Sforzesco!
2) Milano diverrà polo sportivo internazionale
3) Serve più potere per l'Insubria a scapito dei Cantoni
4) Faremo cose particolari per la Città Autonoma
5) Sogno una Milano trilingue italiano, lombardo e inglese
6) Daremo villette ai Rom per integrarli
7) Avremo gli ospedali migliori d'Europa
8) Binasco dovrebbe tornare sotto Pavia
9) Nella mia città autonoma vedo le adozioni gay"""
		giornale = int(raw_input(":"))
		print "L'Indipendente Meneghino"
		if giornale == 2:
			print nome, "vuole lo sport a Milano, però costerà molto!"
			elettori = elettori + random.randint(-20,15)
			puntipolitica = puntipolitica + random.randint(-10,5)
		if giornale == 1:
			print nome, "vuole la sede della Città Autonoma al Castello Sforzesco!"
			elettori = elettori + random.randint(-5,15)
			puntipolitica = puntipolitica + random.randint(-6,12)
		if giornale == 3:
			print nome, "vuole esautorare i cantoni? Ok che l'area comasca è meglio, ma qui esagera..."
			elettori = elettori + random.randint(-20,5)
			puntipolitica = puntipolitica + random.randint(-10,2)
		if giornale == 4:
			lm = random.randint(1,4)
			if lm == 1:
				print "Nuove quartiere aziendale a Sesto San Giovanni, proposta di", nome, "."
				elettori = elettori + random.randint(-5,20)
				puntipolitica = puntipolitica + random.randint(-5,20)
			if lm == 2:
				print "Gatto alimentare a Milano? Proposta del PIM non piace alla popolazione ma pienamente legale"
				elettori = elettori + random.randint(-20,5)
				puntipolitica = puntipolitica + random.randint(-2,10)
			if lm == 3:
				print "Statua aurea del Carroccio a Milano? Proposta di", nome, "fa discutere."
				elettori = elettori + random.randint(-6,12)
				puntipolitica = puntipolitica + random.randint(-6,20)
			if lm == 4:
				print "Regolarizzare lo spaccio di hashish? Proposta PIM cassata dal Capo dello Stato"
				elettori = elettori + random.randint(-20,10)
				puntipolitica = puntipolitica + random.randint(-10,8)
		if giornale == 6:
			print nome, "vuole dare case ai rom. Fino a qualche anno fa voleva sgomberarli col fuoco."
			elettori = elettori + random.randint(-20,2)
			puntipolitica = puntipolitica + random.randint(-15,2)
		if giornale == 7:
			print "Il PIM vuole i migliori ospedali d'Europa: Esperienza a Novara ottima."
			elettori = elettori + random.randint(2,15)
			puntipolitica = puntipolitica + random.randint(-10,16)
		if giornale == 5:
			print nome, "vuole Milano trilingue"
			elettori = elettori + random.randint(-5,15)
			puntipolitica = puntipolitica + random.randint(-10,20)
		if giornale == 8:
			print "Binasco Pavese? Il PIM e le Sinistre chiedono il referendum, Liberali scettici"
			elettori = elettori + random.randint(-10,10)
			puntipolitica = puntipolitica + random.randint(-20,20)
		if giornale == 9:
			print nome, "vuole le adozioni gay in Città. Milanesi a favore, partito no"
			elettori = elettori + 20
			puntipolitica = puntipolitica - 20
	if turno%4 != 0:
		print "Cosa vuoi fare?"
		print """1) Incontro con la cittadinanza al Teatro Federale
2) Confronto pubblico tra candidati
3) Incontro coi sindaci del PIM Novara
4) Pubblicità televisiva e radio
5) Incontro con i ragazzi di "Podèmm"
6) Manifestazione con i giovani del PIM
7) Diretta TV
8) Partecipa a "Radio Lombardia Internazional"
9) Stampa manifesti"""
		try:
			eventi = int(raw_input(":"))
		except:
			print "ERRORE, inserisci un numero valido"
			eventi = int(raw_input(":"))
		if eventi == 1:
			print "Organizzi una serata per ascoltare i bisogni della popolazione"
			elettori = elettori + 20
			puntipolitica = puntipolitica + random.randint(-10,8)
		if eventi == 2:
			je = random.randint(1,3)
			if je == 1:
				print "Il confronto lascia indifferente la popolazione"
				puntipolitica = puntipolitica + 12
			if je == 2:
				print "Colpisci i cuori dei cittadini, ottimo!"
				elettori = elettori + 30
				puntipolitica = puntipolitica + random.randint(1,12)
			if je == 3:
				print "Male male male... Gli avversari ti battono nettamente"
				elettori = elettori + random.randint(-10,2)
				puntipolitica = puntipolitica + random.randint(-10,2)
		if eventi == 3:
			print "Incontri i candidati di zona del PIM e delle liste che ci sostengono"
			puntipolitica = puntipolitica + 15
		if eventi == 4:
			print "Fai pubblicità"
			elettori = elettori + random.randint(1,40)
			puntipolitica = puntipolitica + random.randint(5,25)	
		if eventi == 5:
			print "Incontri i ragazzi della piattaforma politica 'Podèmm', subito intesa con l'idea 'Obiettivo Comunità'"
			elettori = elettori + random.randint(-2,20)
			puntipolitica = puntipolitica + random.randint(-7,14)
		if eventi == 6:
			print "Manifesti con i giovani del PIM e broccoli qualche ragazza del luogo"
			elettori = elettori + random.randint(-4,30)
			puntipolitica = puntipolitica + random.randint(-2,20)	
		if eventi == 7:
			je = random.randint(1,3)
			if je == 1:
				print "Parli a 'Novarese TV', diffondi l'idea del partito ma poi parli di tutt'altro"
				puntipolitica = puntipolitica + 10
				elettori = elettori + random.randint(-10,15)
			if je == 2:
				print "Parli a 'Noara Ancheuj', TV della minoranza piemontesofona, e convinci molti indecisi a votare il PIM"
				elettori = elettori + 30
				puntipolitica = puntipolitica + random.randint(-6,12)
			if je == 3:
				print "Perdi palesemente il dibattito con il Movimento Popolare"
				elettori = elettori + random.randint(-12,5)
				puntipolitica = puntipolitica + random.randint(-8,4)	
		if eventi == 8:
			print "Parli a 'Radio Lombardia Internazional' in lombardo e inglese. \n Ti ascoltano in tutta Europa e ottieni una medaglia del Partito Indipendente d'Europa"	
			elettori = elettori + 20
			puntipolitica = puntipolitica + random.randint(10,18)
		if eventi == 9:
			print "Stampi manifesti"
			elettori = elettori + random.randint(30,100)
			puntipolitica = puntipolitica - random.randint(-30,10)	
		if eventi == 44:
			#variabili di debug
			puntipolitica = input("Puntipolitica:")
			elettori = input("Elettori:")
			turno = input("Turno:")	


	if puntipolitica > 2250 and elettori > 2000 and turno%7 == 0:
		print "Complimenti! Sei stato eletto Presidente della Città Autonoma... Ma adesso dobbiamo arrivare più in altro..."
		print"""
Sarai candidato alla Carica di Deputato. Questa è l'ultima in cui ti servirà il supporto popolare diretto, che tuttavia dovrai mantenere per non perdere il posto. """
		invio()
		clear()
		deputatus()
	else:
		invio()
		clear()
		premil()

introd()
