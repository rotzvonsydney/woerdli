from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import url_for
from word_processing import word

app = Flask(__name__)

counter = 0
counter_richtig = 0
counter_halbrichtig = 0
counter_falsch = 0

@app.route("/", methods=['GET', 'POST'])
def ausfuehren():

    farbe1 = "grey.jpg"
    farbe2 = "grey.jpg"
    farbe3 = "grey.jpg"
    farbe4 = "grey.jpg"
    farbe5 = "grey.jpg"

    i = 0

    if request.method == 'POST':

        i = i + 1
        counter_richtig = 0
        counter_halbrichtig = 0
        counter_falsch = 0

        #Hier wird das Wort, welches der User eingeben hat, ins Python geholt.
        erratenes_wort = request.form['guessed_word']
        """
        if len(erratenes_wort) <= 5:
            flash('Sie mönd es wort mit 5 Buechstabe itöggele, susch funktionierts auä nöd.')
            return render_template('index.html')
        """
        erratenes_wort = str(erratenes_wort)
        randomword = str(word)
        wordx = "ficke"

        wortliste = list(erratenes_wort)
        wordliste = list(randomword)

        letter1 = wortliste[0]
        letter2 = wortliste[1]
        letter3 = wortliste[2]
        letter4 = wortliste[3]
        letter5 = wortliste[4]

        if wortliste[0] in wordliste and not wortliste[0]== wordliste[0]:
            farbe1 = "yellow.jpg"
            colordiv1 = "yellow"
            counter_halbrichtig = counter_halbrichtig + 1
        if wortliste[1] in wordliste and not wortliste[1]== wordliste[1]:
            farbe2 = "yellow.jpg"
            colordiv2 = "yellow"
            counter_halbrichtig = counter_halbrichtig + 1
        if wortliste[2] in wordliste and not wortliste[2]== wordliste[2]:
            farbe3 = "yellow.jpg"
            colordiv3 = "yellow"
            counter_halbrichtig = counter_halbrichtig + 1
        if wortliste[3] in wordliste and not wortliste[3]== wordliste[3]:
            farbe4 = "yellow.jpg"
            colordiv4 = "yellow"
            counter_halbrichtig = counter_halbrichtig + 1
        if wortliste[4] in wordliste and not wortliste[4]== wordliste[4]:
            farbe5 = "yellow.jpg"
            colordiv5 = "yellow"
            counter_halbrichtig = counter_halbrichtig + 1

        if wortliste[0] == wordliste[0]:
            farbe1 = "green.jpg"
            colordiv1 = "green"
            counter_richtig = counter_richtig + 1
        if wortliste[1] == wordliste[1]:
            farbe2 = "green.jpg"
            colordiv2 = "green"
            counter_richtig = counter_richtig + 1
        if wortliste[2] == wordliste[2]:
            farbe3 = "green.jpg"
            colordiv3 = "green"
            counter_richtig = counter_richtig + 1
        if wortliste[3] == wordliste[3]:
            farbe4 = "green.jpg"
            colordiv4 = "green"
            counter_richtig = counter_richtig + 1
        if wortliste[4] == wordliste[4]:
            farbe5 = "green.jpg"
            colordiv5 = "green"
            counter_richtig = counter_richtig + 1

        #Hier wird jeder Buchstabe kontrolliert, welche nicht stimmen und die Farbe ausgegeben
        if wortliste[0] not in wordliste:
            farbe1 = "grey.jpg"
            colordiv1 = "grey"
            counter_falsch = counter_falsch + 1
        if wortliste[1] not in wordliste:
            farbe2 = "grey.jpg"
            colordiv2 = "grey"
            counter_falsch = counter_falsch + 1
        if wortliste[2] not in wordliste:
            farbe3 = "grey.jpg"
            colordiv3 = "grey"
            counter_falsch = counter_falsch + 1
        if wortliste[3] not in wordliste:
            farbe4 = "grey.jpg"
            colordiv4 = "grey"
            counter_falsch = counter_falsch + 1
        if wortliste[4] not in wordliste:
            farbe5 = "grey.jpg"
            colordiv5 = "grey"
            counter_falsch = counter_falsch + 1
        #Hier wird der Counter in global umgewandelt, um sie Funtkionisübergreigend zu machen
        global counter
        counter += 1

        if wortliste[0] == wordliste[0] and wortliste[1] == wordliste[1] and wortliste[2] == wordliste[2] and wortliste[3] == wordliste[3] and wortliste[4] == wordliste[4]:
            return render_template("victory.html", counter=counter)



        return render_template("index.html",
                               erratenes_worthtml=erratenes_wort,
                               color_1=farbe1, color_2=farbe2, color_3=farbe3, color_4=farbe4, color_5=farbe5,
                               wortliste=wortliste,
                               letter1=letter1, letter2=letter2, letter3=letter3, letter4=letter4, letter5=letter5,
                               colordiv1=colordiv1, colordiv2=colordiv2, colordiv3=colordiv3,colordiv4=colordiv4, colordiv5=colordiv5,
                               counter_halbrichtig=counter_halbrichtig, counter_falsch=counter_falsch, counter_richtig=counter_richtig,
                               counter=counter)



    return render_template("index.html", color_1=farbe1, color_2=farbe2, color_3=farbe3, color_4=farbe4, color_5=farbe5)


@app.route("/victory")
def statistik():
    hallo = 5




if __name__ == "__main__":
    app.run(debug=True, port=5000)
