from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 8889
app.config['MYSQL_DATABASE_USER'] = 'sql12343256'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'order'
mysql.init_app(app)


@app.route('/')
def index():
    cursor.execute("SELECT * FROM `order` WHERE 1")
    data = cursor.fetchone()
    return str(data)

@app.route('/addone/<string:insert>')
def add(insert):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `order`(`product name`, `the type`, `unit price`, `quantity`) VALUES ([value-1],[value-2],[value-3],[value-4])",insert)
        mysql.connect()
        return "Done"

@app.route('/getall')
def getall():
    cursor = mysql.get_db().cursor()
    cursor.execute('''SELECT * FROM `order`''')
    returnvals = cursor.fetchone()



if __name__ == '__main__':
    app.run(debug=True)

