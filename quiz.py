# functie
def stel_vraag(vraag, antwoorden):
    
    # teller om bij te houden hoeveel pogingen je hebt gedaan
    counter = 0
    while True:
        # aantal pogingen wordt met 1 verhoogd
        counter = counter + 1
        answer = input(vraag).strip().lower()
        
        # lambda functie om te checken of het antwoord juist is
        check_antwoord = lambda antwoord: antwoord in antwoorden
        
        if check_antwoord(answer):
            print('Goed gedaan!')
            break 
        else:
            if counter == 3:
                # aantal pogingen is op!
                print("Jammer, we gaan door naar de volgende vraag.")
                break
            else:
                # antwoord was fout, maar je hebt nog pogingen
                print(f"Helaas... Je hebt nog: {3-counter} pogingen")

# hoofdprogramma

# lijst maken. Lijst heet in programmeertalen een 'array'
vragen = [] # lege array

# vragen toevoegen met de 'append' functie
vragen.append(["Hoe heet een hert in het Engels? ", ["deer"]])
vragen.append(["Wat is konijn in het Engels? ", ["rabbit", "bunny"]]
    )  # dat haakje moet er staan!!!!! anders doet hij het niet!
vragen.append(["Wat is eend in het Engels? ", ["duck"]])
vragen.append(["Wat is koe in het Engels? ", ["cow", "bull"]])
vragen.append(["Wat is wasbeer in het Engels? ", ["raccoon"]])
vragen.append(["Wat is stokstaartje in het Engels? ", ["meerkat"]])
vragen.append(["Wat is buffel in het Engels? ", ["bufalo"]])
vragen.append(["Wat is zeehond in het Engels? ", ["seal"]])
vragen.append(["Wat is hond in het Engels? ", ["dog"]])
vragen.append(["Wat is vis in het Engels? ", ["fish"]])
vragen.append(["Wat is kever in het Engels? ", ["beetle"]])
vragen.append(["Wat is egel in het Engels? ", ["hegehog"]])
vragen.append(["Wat is vogelbekdier in het Engels? ", ["platypus"]])
vragen.append(["Wat is spreken in het Engels? ", ["speak"]])
vragen.append(["Wat is luisteren in het Engels? ", ["listen"]])
vragen.append(["Wat is begrijpen in het Engels? ", ["understand"]])
vragen.append(["Wat is gesprek in het Engels? ", ["conversation"]])
vragen.append(["Wat is dialoog in het Engels? ", ["dialogue"]])
vragen.append(["Wat is ruilen in het Engels? ", ["exchange"]])
vragen.append(["Wat is bespreken in het Engels? ", ["discuss"]])
vragen.append(["Wat is uitleggen in het Engels? ", ["explain"]])
vragen.append(["Wat is verhelderen in het Engels? ", ["clarify"]])
vragen.append(["Wat is vraag in het Engels? ", ["question"]])
vragen.append(["Wat is antwoorden in het Engels? ", ["answer"]])
vragen.append(["Wat is gebaren in het Engels? ", ["Gesture"]])
vragen.append(["Wat is toon in het Engels? ", ["tone"]])
vragen.append(["Wat is stem in het Engels? ", ["Voice"]])
vragen.append(["Wat is taal in het Engels? ", ["Language"]])
vragen.append(["Wat is woorden in het Engels? ", ["Words"]])
vragen.append(["Wat is alinia in het Engels? ", [" Paragraph"]]) 
vragen.append(["Wat is verhaal in het Engels? ", [" Story "]])  
vragen.append(["Wat is inlichten in het Engels? ", [" Inform"]]) 
vragen.append(["Wat is delen in het Engels? ", [" Share"]]) 
vragen.append(["Wat is verbinden in het Engels? ", [" Connect"]])
vragen.append(["Wat is deelnemen in het Engels? ", [" Participate"]]) 
vragen.append(["Wat is sigaal in het Engels? ", [" Signal "]]) 
vragen.append(["Wat is schriftelijk in het Engels? ", [" Written"]])
vragen.append(["Wat is lezen in het Engels? ", ["read"]]) 
vragen.append(["Wat is schrijven in het Engels? ", [" Write"]]) 
vragen.append(["Wat is spreken in het Engels? ", [" Talk"]]) 
vragen.append(["Wat is zin in het Engels? ", ["Sentence"]])
vragen.append(["Wat is overdragen in het Engels? ", ["convey"]])
vragen.append(["Wat is uitspreken in het Engels? ", ["enunciate"]])
vragen.append(["Wat is redenaar in het Engels? ", ["oratory"]])
vragen.append(["Wat is overtuigen in het Engels? ", ["persuade"]])
vragen.append(["Wat is retoriek in het Engels? ", ["rhetoric"]])
vragen.append(["Wat is gesprek in het Engels? ", ["discourse"]])
vragen.append(["Wat is oratie in het Engels? ", ["oration"]])
vragen.append(["Wat is reciteren in het Engels? ", ["recite"]])
vragen.append(["Wat is woordenvloed in het Engels? ", ["verbiage"]])

# voor elke vraag in de vragenlijst
for vraag in vragen:
    # roep de functie aan
    stel_vraag(vraag[0], vraag[1])
