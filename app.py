from flask import Flask, request, jsonify, session
import logging
import mysql.connector
import datetime
from dateutil.relativedelta import relativedelta
import decimal
import jwt
from functools import wraps
import json
import bcrypt
import secrets
import string
import requests
import os
from dotenv import load_dotenv, dotenv_values
from flask_bcrypt import Bcrypt
from keycove import generate_token, hash

load_dotenv()
#.......................................................................
#log in information to the error.log
logging.basicConfig(filename='error.log',level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)
#.........................................................................
# Configuration
app.config['SECRET_KEY'] = os.getenv("app_secrete_key")

#.......................................................................
#Generate app secrete key
secrete_key = secrets.token_hex(16)

#.......................................................................
#Connection to Mysql database

mydb = mysql.connector.connect(
  host=os.environ.get("mysqli_host"),
  user=os.environ.get("mysqli_user"),
  password= os.environ.get("mysqli_password"),
  database = os.environ.get("mysqli_database")
)
my_cursor = mydb.cursor()
#.....................................................................
#Generate API Key
def gnrApi():
  apiKey = generate_token()
  return hash(value_to_hash=apiKey)
#.........................................................................
#Generate vendocode
def vendocode():
    characters = string.digits
    code = ''.join(secrets.choice(characters) for _ in range(10))
    sql ='select 1 from params where vendorCode = %s'
    my_cursor.execute(sql,(code,))
    dat = my_cursor.fetchall()
    if dat == []:
      return code
    else:
      return vendocode() 
#......................................................................   
#Check the API Key
def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
      try:
        if request.headers.get('apiKey') and request.headers.get('vendorCode'):
          vendorCode = request.headers.get('vendorCode')
          currentDate = datetime.date.today()
          #Connect the params table
          sql1 = 'select apiKey,expiresAt from params where vendorCode = %s'
          value = (vendorCode,)
          my_cursor.execute(sql1,value)
          dat1 = my_cursor.fetchall()
          if dat1 == []:
            return jsonify({"Error": "vendorCode not in database"}),403
          
          if request.headers.get('apiKey') == dat1[0][0] and currentDate < dat1[0][1]:
            return view_function(*args, **kwargs)
          else:
              return jsonify({'Error': 'Incorrect or expired apiKey'}),403
        else:
          return jsonify({"Error":"apiKey and or vendorCode required or expired"}),403
      except Exception:
        return jsonify({"Error": "Something went wrong, Api key configuration"})
    return decorated_function 
 #............................................................................
#Home
@app.route('/', methods = ["POST"])
def get_api_key():
  try:
    data = request.get_json()
    if 'payment' in data and isinstance(data['payment'],str) and data['payment'].lower()== 'confirm':
      if 'vendor' in data and 'director' in data:
        if isinstance(data["vendor"],str) and isinstance(data["director"],str):
          vendor = data["vendor"]
          director = data["director"]
          
          vendo_code = vendocode()
          
          api_key = gnrApi()
        
          createdDate = datetime.date.today()
          expireDate = createdDate + relativedelta(months=3)
          db = "school"
          print(expireDate)
          #Insert into the param table
          try:
            sql = 'insert into params (apiKey,vendorCode,vendor,createdAt,expiresAt,db,director)\
            values(%s,%s,%s,%s,%s,%s,%s)'
            values = (api_key,vendo_code,vendor,createdDate,expireDate,db,director)
            my_cursor.execute(sql,values)
            mydb.commit()
            app.logger.info("Done: API Key generated successfully")
            return jsonify({"Data":{
            "ApiKey": api_key,
            "vendorCode": vendo_code,
            "Expire Date": expireDate},
                          "Status": "Success",
                          "Code":"00",
                          "Message":"Api Key generated successfully"})
          except Exception:
            app.logger.error("Error: Cant save into params table. Check databse connection")
            return jsonify({"Data":None,
                          "Status": "Failed",
                          "Code":"01",
                          "Message":"Incorrect data type for vendor and or director"})
            
        else:
          app.logger.error("Error: Incorrect data type for vendor and or director")
          return jsonify({"Data":None,
                          "Status": "Failed",
                          "Code":"01",
                          "Message":"Incorrect data type for vendor and or director"})
      else:
        app.logger.error("Error: Request body must contain vendor and director")
        return jsonify({"Data":None,
                          "Status": "Failed",
                          "Code":"01",
                          "Message":"Request body must contain vendor and director"})
    else:
      app.logger.error("Error: payment required in the request body")
      return jsonify({"Data":None,
                          "Status": "Failed",
                          "Code":"01",
                          "Message":"payment required in the request body "})
  except Exception:
    app.logger.error("Error: Something went wrong, missing or wrong request body")
    return jsonify({"Data":None,
                        "Status": "Failed",
                        "Code":"01",
                        "Message":"Something went wrong, missing or wrong request body"})

if __name__ == '__main__':
    app.run(debug=True)