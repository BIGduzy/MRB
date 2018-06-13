# Plan van aanpak voor MRB

## Achtergrond
Dit project is een opdracht die aangeleverd is in het kader van het vak MRB (Meten regelen en besturen).
Deze opdracht zal het eindcijfer voor dit vak voor 50% gaan bepalen.
De opdracht is bedoeld als leer process voor het maken van een PID controller.
Deze controller wordt zeer veel gebruikt voor het maken van een regel systeem wat nauwkeuring en snel moet zijn.

Er kon voor deze opdracht uit twee verschillende projecten worden gekozen.
De eerste bestaat uit 3 servo motoren met een plank, en op deze plak moet een balletje gebalanceerd worden.
De tweede opdracht draait om het hooghouden van een balletje in een plexiglas buis. Hierbij moet het balltje op een 
specifieke hoogte worden gehouden d.m.v een fan die onder de buis geplaatst is.

Voor beide opdrachten is het de bedoeling dat het balletje op een nader te specificeren locatie gehouden wordt.
Dit moet dan gedaan worden d.m.v een PID controller die, of de servo's of de fans aanstuurd.

Wij hebben gekozen voor het maken van de opdracht draait om de buis. 

## Tussenproducten
Het eindresultaat zal in de volgende tussenstappen worden gebouwd.

### 1:
Het eerste tussenproduct zal bestaan uit:

- Een vision onderdeel dat de bal kan lokaliseren.
- De locatie van de bal kan omzetten naar een relatieve hoogte.
- Een mechanisme om de fan aan te sturen d.m.v de Arduino Due.

### 2:
Het tweede tussenproduct zal bestaan uit:

- Een vision onderdeel dat zowel de bal als een hand kan lokaliseren.
- Een P controller die een snelheid kan bepalen voor de fan.
- Communicatie tussen het vision gedeelte en de Arduino Due.
- De Arduino Due kan de fan aansturen met de ontvangen snelheid.

### 3:
Het derde tussenproduct zal bestaan uit:

- Een vision onderdeel dat de fan kan aansturen d.m.v de P controller en de gemeete hoogte van de bal.
- Een viison onderdeel dat de setpoint van de bal kan aanpassen aan de hand van een hand die gelokaliseerd wordt.
- Een P controller die zonder al te veel overshoot de bal op een gegeven locatie kan zetten.

### 4:
Het eindproduct zal bestaan uit:

- Een vision onderdeel dat de fan kan aansturen d.m.v de P controller en de gemeete hoogte van de bal.
- Een vision onderdeel dat de setpoint van de bal kan aanpassen aan de hand van een hand die gelokaliseerd wordt.
- Een P controller die zonder al te veel overshoot de bal op een gegeven locatie kan zetten.
- Een speaker die een toon genereerdt aan de hand van de hoogte van de bal.

### Mogelijke extra onderdelen die niet onderdeel zijn van het eindproduct (Could have)

- Volledige PID controller
- Heldere tonen vanuit de speaker, daadwerkelijke muziek noten o.i.d.
- Machine learning voor het bepalen van de parameters van de PID controller.

## Activiteiten
De volgende individuele onderdelen zullen worden ontwikkeld:

- Basis vision voor het herkennen en lokaliseren van de bal
- Uitgebreider vision onderdeel voor het herkennen en lokaliseren van de bal en een hand
- Controller voor de fan die kan worden aangestuurd vanaf de pc
- Controller voor de speak er die kan worden aangestuurd vanaf de pc

## Agenda
De eerste twee weken zullen bestaan uit het ontwikkelen van de basis versie van het vision onderdeel.
Hierna zullen twee weken worden besteed aan het opzetten van de fan controller die kan worden aangestuurd.
Hierbij zal worden gezorgd dat wij d.m.v PWM de fan kunnen aansturen, ook terwijl de fan 12V nodig 
zal hebben om correct te opereren.
De laatste drie weken zullen worden besteed om het vision onderdeel te koppelen aan de controller voor de fan.
Hiermee zal de bal herkend moeten kunnen worden en op het setpoint hoog gehouden kunnen worden.

## Organisatie van je project
Er zal geen harde onderverdeling zijn van wie aan welk onderdeel gaat werken.
Dit bepalen wij terwijl wij met het project bezig zijn. Wij zullen conflicten proberen te vermijden, al is het slecht 
denkbaar dat deze zullen ontstaan.

De onderlingen communicatie zal via _Telegram_ verlopen. D.m.v deze app zullen wij in contact blijven ookal zijn wij niet altijd
fysiek aanwezig op school. Wanneer wij wel aanwezig zijn hebben wij gewoon contact en directe communicatie.

Het onderhouden van de code en documenten zal via _Git_ verlopen. Hiermee kunnen wij versie's onderhouden van de code 
die wij tijdens het project zullen schrijven.

De deadlines voor ons project zullen het zelfde zijn als die in de planning staan.
Er zal getracht worden deze deadlines aan te houden. 

Voor hardware gebruiken wij:
- Arduino Due
- Een laptop
- Minstens 1 fan
- Een voeding die geschikt is voor het aansturen van 1 of meerdere fans

## Risico's
De risico's van dit project zullen vooral zitten in het vision onderdeel.
Dit onderdeel zal een stuk groter zijn dan de rest van het project.
Dit is omdat computer vision een zeer moeilijk onderdeel is, zeker voor het lokaliseren 
en omzetten naar een bruikbare hoogte.
Hierdoor willen wij ook als eerste werken aan het vision onderdeel, hierdoor hopen wij genoeg 
tijd te hebben om dit voor elkaar te krijgen.

Een ander risico's is dat een van de teamleden wegvalt, dit zou mogelijk door b.v ziekte kunnen komen.
Een risio wat redelijk verbonden is het met uitvallen van een team lid, is het in tijdnood komen.
Dit zou mogelijk kunnen komen door het R2D2 project wat zich afspeeld tijdens dit project.
Het zou kunnen dat een of meerdere teamleden hier meer tijd aan zal willen besteden dan het MRB project.

## Kwaliteit
Voor het eindresultaat zijn een aantal kwaliteits eisen opgesteld.
Deze eisen zijn:
- Zonder veel overshoot (20cm in een van de richtingen) de bal naar het setpoint brengen.
- Het mag niet lang duren voordat de bal zich op een nieuwe positie stabiel bevind (niet langer dan 20 seconden).
- De speaker moet zonder vertraging kunnen veranderen van toonhoogte aan de hand van de positie van de bal.

Wij zullen trachten aan deze eisen te voldoen om te zorgen voor een geslaagd project.
