from flask import Flask, render_template, redirect
import mysql.connector
import os


app = Flask(__name__,
            static_folder='web/static',
            template_folder='web/templates',)



class DataBace:
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="BeanAndBrew",
      password= os.getenv("sqlPassword"),
      database="beanandbrew"
    )
    self.cursor = self.mydb.cursor()

  def createDB(self,name):
    self.cursor.execute(f"CREATE DATABASE {name}")

  def selectDB(self,name):
    self.cursor.execute(f"USE {name}")

  def createTable(self,name,values):
    self.cursor.execute(f"CREATE TABLE {name}{values} ")

  def tableExists(self,name):
    self.cursor.execute("SHOW TABLES")
    for x in self.cursor:
      if x == name:
        return True
    return False  

  def insert(self,table,values,coloumbs):
    sql = f"INSERT INTO {table} ({coloumbs}) VALUES ("
    for i in range(coloumbs.split(",")):
      if i == len(coloumbs.split(","))-1:
        sql += "%s)"
      else:
        sql += "%s,"
    self.cursor.execute(sql, values)
    self.mydb.commit()

  def insertMultiple(self,table,values,coloumbs):
    coloumbs = str(coloumbs).replace("'",'').replace("[","").replace("]","")
    sql = f"INSERT INTO {table} ({coloumbs}) VALUES ("
    for i in range(len(coloumbs.split(","))):
      if i == len(coloumbs.split(","))-1:
        sql += "%s)"
      else:
        sql += "%s,"
    self.cursor.executemany(sql, values)
    self.mydb.commit()
    

  def update(self,table,value,condition):
    self.cursor.execute(f"UPDATE {table} SET {value} WHERE {condition}")
    self.mydb.commit()



  def insertColoum(self):
    pass


  
# DB = DataBace()





class session:
    def __init__(self):
        pass



class auth:
    def __init__(self):
        pass





def auth():
    pass




@app.before_request
def before_request():#session handeling
    pass


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')   


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    if auth():
        return render_template('dashboard.html')
    else:
        return redirect("/login"), 401 # "You are not authorized to view this page. Please login first.", 401



@app.route('/api/login', methods=['POST'])
def login_auth():
    # ToDo handle it 

    return redirect("/dashboard")

@app.route('/api/register', methods=['POST'])
def register_auth():
    # ToDo handle it  
    # set tokens for login auth

    return redirect("/dashboard")

@app.route('/api/logout', methods=['POST'])
def logout_auth():
    # ToDo handle it 

    return redirect("/login")



if __name__ == '__main__':
    app.run()