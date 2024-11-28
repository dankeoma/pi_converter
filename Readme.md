# PICONVERTER API
This API as the name emplys converts Pi Coins to dollar and vice verser using the globally accepted GCV value of 
1 pI = 314,159 $
Thanks to the global GCV value ambersador Doris Yin who 
established the value that got accepted globally and 
hopefully will be adobted during open mainet as the
global value of Pi

`1 pi = $314159`
## Prerequisites for using the API
1. First is to Install the API in your system. Make sure
Python is installed and copied to the system's environment
variable. Click [here]() to learn how to install python 
in your system.
1. Create a folder and copy the acompaining files for the package in the folder.
1. Navigate to the folder from the command window and create a virtual environmet in the root folder of the package. Open the virtual environment. You can learn more about crating and using a virtual environment [here]().
1. While in the package folder and making sure the virtual environment is on, install the required packages in the virtual environment by running the code given below
`pip install requirements.txt`
1. Run `python app.py` to activate the server thereby waiting to take requests from the browser.
1. Ensure that [MYSQL](https://www.mysql.com/downloads/ "Click to download MYSQL") is installed in the system. Click The link to download mysql workbench and shell. Open command window and type `mysqlsh` to display the figure below to ensure that Mysql is working correctly
  ![mysqltest](https://github.com/user-attachments/assets/888170bd-cf51-4f31-8e66-240f8cff0851)

1. After installing MYSQL, open the workbench and create a database called pi_converter. You can learn to create database in MySQL workbench [Here](https://stackoverflow.com/questions/5515745/create-a-new-database-with-mysql-workbench "Create database in MySQL Workbench").
Click on Insert from the menu bar and select Data Import, click on the second option
to select pi_converter from the folder and equally select the destination as 
the created database, then select bigin import and start importing. The database with the table contents
will be imported into the created database.
Or open the command window and put the below command to copy the database package provided into the already created database in workbench, where you will be prompted to inpute your password as shown in the figure:
    `C:\Project> mysqldump -u root -p pi_converter < pi_converter.sql` as shown below
![mysqlprompt](https://github.com/user-attachments/assets/332b8cd7-1aec-48eb-8e23-46bf0d988304)

NOTE! Ensure that the path to Python   `C:\Users\hp\AppData\Local\Programs\Python\Python39\`and  MYSQL server bin `(C:\Program Files\MySQL\MySQL Server 8.0\bin)` is copied to the system's environmental variable. You can learn about that [here](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html). 
## Testing The API with Postman
After successful installation of the package following the steps discribed above, open the command 
window and navigate to package folder where accompaining files are saved and run the command
`python app.py` to run the server as shown in the diagram below. Make sure to activate the virtual
environment.

Once the server is up, open postman app from the installation icon on the desktop. Click [here](https://www.postman.com/downloads/) to follow the
steps to install Postman in your system.
Run the localhost or 127.0.0.1:5000 url making sure the request body contains 'payment','director' and 'vendor' keys and their values
in string form. The vendor is the name of the institution or organizatio, the director is the head 
of the organization or institution while payment is either confirm or decline. Run the request by 
clicking on the Send making sure it is at Post postion. The return json data contains the API Key 
the Vendorcode and the expring date of the API key, which are required to acces other componenet routes of the API. The whole process
is shown below
## Using the API with Postman App
1. First run the local host root to ubtain Api key for the API. The painment for the API key is in Pi coin. The request body should comprise of keys vendor, and director which is the name of the institution or organisation and the director respectively, applying to use the API. The request body should equally contain the payment confirmation. 