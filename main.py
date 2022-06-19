from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from plotly import plot
import json

from word_processing import word
import plotly.express as px

app = Flask(__name__)


#Hier wird ein Dictonary erstellt, welches für die Buchstabenstatistik zuständig ist.
letterstatistics = {}

#Hier wird die Liste erstellt, welche danach die richtigen Buchstaben anzeigt.
loesungliste = ["_", "_", "_", "_", "_"]

#Ist der allgemine Versuchszähler
counter = 0

@app.route("/", methods=['GET', 'POST'])
def ausfuehren():


    #Hier werden die Farben der Bilder definiert.
    farbe1 = "grey.jpg"
    farbe2 = "grey.jpg"
    farbe3 = "grey.jpg"
    farbe4 = "grey.jpg"
    farbe5 = "grey.jpg"



    if request.method == 'POST':

        #Hier wird das Wort, welches der User eingeben hat, ins Python geholt.
        erratenes_wort = request.form['guessed_word']

        #Hier wird das Wort in einen String umgewandelt und das Random Lösungswort aus einer anderen Funktion eines anderen Files geholt.
        erratenes_wort = str(erratenes_wort)
        randomword = str(word)

        #Die Wörter werden in eine Liste gepackt
        wortliste = list(erratenes_wort)
        wordliste = list(randomword)

        #Jeder einzelne Listeneintrag bekommt eine eigene Variable
        letter1 = wortliste[0]
        letter2 = wortliste[1]
        letter3 = wortliste[2]
        letter4 = wortliste[3]
        letter5 = wortliste[4]

        #Jeder Buchstabe, der im Wort ist wir
        if wortliste[0] in wordliste and not wortliste[0]== wordliste[0]:
            farbe1 = "yellow.jpg"
        if wortliste[1] in wordliste and not wortliste[1]== wordliste[1]:
            farbe2 = "yellow.jpg"
        if wortliste[2] in wordliste and not wortliste[2]== wordliste[2]:
            farbe3 = "yellow.jpg"
        if wortliste[3] in wordliste and not wortliste[3]== wordliste[3]:
            farbe4 = "yellow.jpg"
        if wortliste[4] in wordliste and not wortliste[4]== wordliste[4]:
            farbe5 = "yellow.jpg"

        #Hier werden alle richtigen Positionen gecheckt.
        if wortliste[0] == wordliste[0]:
            farbe1 = "green.jpg"
            loesungliste[0] = wortliste[0].upper()
        if wortliste[1] == wordliste[1]:
            farbe2 = "green.jpg"
            loesungliste[1] = wortliste[1].upper()
        if wortliste[2] == wordliste[2]:
            farbe3 = "green.jpg"
            loesungliste[2] = wortliste[2].upper()
        if wortliste[3] == wordliste[3]:
            farbe4 = "green.jpg"
            loesungliste[3] = wortliste[3].upper()
        if wortliste[4] == wordliste[4]:
            farbe5 = "green.jpg"
            loesungliste[4] = wortliste[4].upper()


        #Hier wird jeder Buchstabe kontrolliert, welche nicht stimmen und die Farbe ausgegeben
        if wortliste[0] not in wordliste:
            farbe1 = "grey.jpg"
        if wortliste[1] not in wordliste:
            farbe2 = "grey.jpg"
        if wortliste[2] not in wordliste:
            farbe3 = "grey.jpg"
        if wortliste[3] not in wordliste:
            farbe4 = "grey.jpg"
        if wortliste[4] not in wordliste:
            farbe5 = "grey.jpg"

        #Hier wird der Counter in global umgewandelt, um sie Funtkionisübergreigend zu machen
        global counter
        counter += 1

        #Hier wird jeder Buchstabe in ein Dictionary übertragen.
        for letter in wortliste:
            if letter in letterstatistics:
                letterstatistics[letter] += 1
            else:
                letterstatistics[letter] = 1

        #Hier wird eine BackUp Datei gespeichert
        with open("statistik.json", "w") as open_file:
            json.dump(letterstatistics, open_file)


        #Wenn die beiden Wörter übereinstimmen, wird man auf die victory.html Seite weitergeleitet
        if wortliste == wordliste:
            return render_template("victory.html", counter=counter, letterstatistics= letterstatistics)



        #Hier werden alle wichtigen Daten ins HTML übertragen
        return render_template("index.html",
                               erratenes_worthtml=erratenes_wort,
                               color_1=farbe1, color_2=farbe2, color_3=farbe3, color_4=farbe4, color_5=farbe5,
                               wortliste=wortliste,
                               letter1=letter1, letter2=letter2, letter3=letter3, letter4=letter4, letter5=letter5,
                               counter=counter,
                               letterstatistics=letterstatistics,
                               loesungliste=loesungliste)



    return render_template("index.html", color_1=farbe1, color_2=farbe2, color_3=farbe3, color_4=farbe4, color_5=farbe5)



@app.route("/stat")
def statistik():
    buchstaben = letterstatistics.keys()
    anzahl = letterstatistics.values()

    fig = px.pie(values=anzahl, names=buchstaben)

    fig.show()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
