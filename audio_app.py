import json
from flask import Flask, render_template, request, url_for, redirect, Response
from flask_mysqldb import MySQL
app = Flask(__name__)

# database connection
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'audio'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)
# checking mysql connection
if(mysql):
    print("connection working")

else:
    print("connection not working")


# home page
@app.route("/")
def home():
    return render_template("index.html")

# Handling Addition of audio files


@app.route('/create', methods=['POST'])
def create():
    print("uptill here ")
    cur = mysql.connection.cursor()

    if(request.form['audioFileType'] == 'song'):
        cur.execute("INSERT INTO song(name , duration) VALUES (%s, %s)",
                    (request.form['name'], request.form['duration']))

    if(request.form['audioFileType'] == 'podcast'):
        cur.execute("INSERT INTO podcast(name , duration, host) VALUES (%s, %s, %s)",
                    (request.form['name'], request.form['duration'], request.form['host']))

    if(request.form['audioFileType'] == 'audio_book'):
        cur.execute("INSERT INTO audio_book(title , author, narrator,duration) VALUES (%s, %s, %s,%s)",
                    (request.form['title'], request.form['author'], request.form['narrator'], request.form['duration']))

    mysql.connection.commit()
    cur.close()

    resp = Response("Successfully Inserted Data", status=200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

# Handling fetching of all audio files based on audioFileType from url given


@app.route('/<audioFileType>', methods=['GET'])
def showAll(audioFileType):
    if(audioFileType == 'song' or audioFileType == 'podcast' or audioFileType == 'audio_book'):
        print("showing now")
        cur = mysql.connection.cursor()
        qry = "SELECT * FROM {}".format(audioFileType)
        print(qry)
        try:

            cur.execute(qry)
            data = cur.fetchall()

            ar = []

            if data:
                for res in data:
                    if(audioFileType == 'song'):
                        obj = {}
                        obj['id'] = res[0]
                        obj['name'] = res[1]
                        obj['duration'] = res[2]
                        obj['uploaded_at'] = str(res[3])
                        obj['type'] = audioFileType
                    elif audioFileType == 'podcast':
                        obj = {}
                        obj['id'] = res[0]
                        obj['name'] = res[1]
                        obj['duration'] = res[2]
                        obj['uploaded_at'] = str(res[3])
                        obj['type'] = audioFileType
                        obj['host'] = res[4]
                    elif audioFileType == 'audio_book':
                        obj = {}
                        obj['id'] = res[0]
                        obj['title'] = res[1]
                        obj['author'] = res[2]
                        obj['narrator'] = res[3]
                        obj['duration'] = str(res[4])
                        obj['uploaded_at'] = res[5]
                        obj['type'] = audioFileType

                    ar.append(obj)

                mysql.connection.commit()
                cur.close()
                return render_template("show.html", result=ar)

            else:
                resp = Response("Failure")
                resp.headers['Access-Control-Allow-Origin'] = '*'
                return resp

        except Exception as e:
            resp = Response("some exception occure", status=500)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

    else:
        resp = Response("Wrong Url", status=400)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

# Handling fetching of audio files using ID and audioFileType


@app.route('/<audioFileType>/<id>', methods=['GET'])
def showOne(audioFileType, id):
    if(audioFileType == 'song' or audioFileType == 'podcast' or audioFileType == 'audio_book'):
        print("showing now")
        cur = mysql.connection.cursor()
        qry = "SELECT * FROM {} where id = {}".format(audioFileType, id)
        try:

            cur.execute(qry)
            data = cur.fetchall()
            ar = []

            if data:
                for res in data:
                    if(audioFileType == 'song'):
                        obj = {}
                        obj['id'] = res[0]
                        obj['name'] = res[1]
                        obj['duration'] = res[2]
                        obj['uploaded_at'] = str(res[3])
                        obj['type'] = audioFileType
                    elif audioFileType == 'podcast':
                        obj = {}
                        obj['id'] = res[0]
                        obj['name'] = res[1]
                        obj['duration'] = res[2]
                        obj['uploaded_at'] = str(res[3])
                        obj['type'] = audioFileType
                        obj['host'] = res[4]
                    elif audioFileType == 'audio_book':
                        obj = {}
                        obj['id'] = res[0]
                        obj['title'] = res[1]
                        obj['author'] = res[2]
                        obj['narrator'] = res[3]
                        obj['duration'] = str(res[4])
                        obj['uploaded_at'] = res[5]
                        obj['type'] = audioFileType

                    ar.append(obj)

                mysql.connection.commit()
                cur.close()
                return render_template("show.html", result=ar)
            else:
                resp = Response("does not exist", status=500)
                resp.headers['Access-Control-Allow-Origin'] = '*'
                return resp

        except Exception as e:
            resp = Response("Failure or id does not exit", status=500)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
    else:
        resp = Response("Wrong Url", status=400)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

# Handling delete of audio files


@app.route('/delete/<audioFileType>/<id>', methods=['GET'])
def delete(audioFileType, id):
    if(audioFileType == 'song' or audioFileType == 'podcast' or audioFileType == 'audio_book'):

        try:
            print("deleting now")
            cur = mysql.connection.cursor()
            qry_del = "DELETE FROM {} where id = {}".format(audioFileType, id)

            print(qry_del)
            cur.execute(qry_del)

            mysql.connection.commit()
            cur.close()
            resp = Response("Successfully Deleted", status=200)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

        except Exception as e:
            print(e)
            resp = Response("Failure to delete", status=500)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
    else:
        resp = Response("wrong url", status=400)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


# Handling update of audio files
@app.route('/update/<audioFileType>/<id>', methods=['GET', 'POST'])
def update(audioFileType, id):
    if(audioFileType == 'song' or audioFileType == 'podcast' or audioFileType == 'audio_book'):
        if request.method == 'GET':
            ar = []
            ar.append(audioFileType)
            ar.append(id)
            return render_template("update.html", result=ar)

        elif request.method == 'POST':
            cur = mysql.connection.cursor()

            if(request.form['audioFileType'] == 'song'):

                cur.execute(
                    f"update song set name = '{request.form['name']}' , duration = {request.form['duration']} where id = {id} ;")

            if(request.form['audioFileType'] == 'podcast'):
                print(request.form)
                print(request.form['host'])
                cur.execute(
                    f"update podcast set  name = '{request.form['name']}' , duration = {request.form['duration']} , host = '{request.form['host']}' where id = {id} ;")

            if(request.form['audioFileType'] == 'audio_book'):

                cur.execute(
                    f"update  audio_book set  title = '{request.form['title']}' , author = '{request.form['author']}' , narrator = '{request.form['narrator']}', duration = {request.form['duration']} where id = {id} ;")

            mysql.connection.commit()
            cur.close()

        resp = Response("Successfully Updated Data", status=200)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


if __name__ == '__main__':
    # it allow to run it on default port: 5000 , ip:127.0.0.1  ==> http://127.0.0.1:5000/
    app.run(debug=True)
