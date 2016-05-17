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

#devo tradurre

def indmil2():
	print "L'Indipendente di Bergamo"
	global puntipolitica
	global elettori
	global turno
	turno = turno + 1
	z = random.randint(1,12)
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
8) Partecipa a "Radio Lombardia Internazzional"
9) Incontro con gli scolari della zona """
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
			print "Parli a 'Radio Lombardia Internazzional' in lombardo e inglese. \n Ti ascoltano in tutta Europa e ottieni una medaglia del Partito Indipendente d'Europa"	
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
		print  nome, "contro l'area B di Como: \nEcologia spicciola di sinistra: La aboliremo."
		puntipolitica = puntipolitica + random.randint(2,12)
		elettori = elettori + random.randint(-2,12)
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
		print "Costava, sindaco di Bergamo PIM, attacca la chiesa 'Omofoba e maschilista'"
		elettori = elettori + random.randint(-2,8)
		puntipolitica = puntipolitica + random.randint(-2,6)
				
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
		print "Intervista! Cosa vuoi dichiarare all'Indipendente di Bergamo?"
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
8) Partecipa a "Radio Lombardia Internazzional"
9) Stampa manifesti"""
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
			print "Parli a 'Radio Lombardia Internazzional' in lombardo e inglese. \n Ti ascoltano in tutta Europa e ottieni una medaglia del Partito Indipendente d'Europa"	
			elettori = elettori + 10
			puntipolitica = puntipolitica + random.randint(10,18)
		if eventi == 9:
			print "Stampi manifesti"
			elettori = elettori + random.randint(10,50)
			puntipolitica = puntipolitica - random.randint(-20,5)		


	if puntipolitica > 800 and elettori > 600 and turno%7 == 0:
		print "Complimenti! Sei stato eletto Sinaco... Ma adesso dobbiamo arrivare più in altro..."
		print"""
Vogliamo candidarti Presidente della Città Autonoma di Bergamo. Giorgio Costava è ancora Sindaco, oltre che Consigliere Autonomo di diritto, grazie alla riforma recente, e potrà darti man forte nella tua candidatura.
Il tuo ruolo è importantissimo, visto che farai parte del Senato Orobico. Dovrai avere 1500 elettori e 1750 punti infulenza."""
		invio()
		clear()
		presidentecantonale()
	else:
		invio()
		clear()
		sindaco()

introd()
