# Assignment

It is assumed that python 2.7 is installed

It is assumed that sqlite is configured, if not follow the below steps (in Windows):
    - Download from https://www.sqlite.org/download.html
    - Add path of sqlite3.exe to “path” environment variable
	  - Ex: “C:\Python27\sqlite-shell-win32-x86-3090200” to “path” environment variable
    - From cmd prompt run “sqlite3” or run “sqlite3.exe”
    
    To open a Database 
      - Ex: .open "C:/Users/mohiudds/PycharmProjects/Scalability/test.db"
            Note: forward slash "/" has to be given in the path
    To Show tables
      - .tables
      
It is assumed that sqlalchemy ORM is configured if not follow the below steps:
    -	Download “ez_setup.py” from “https://bootstrap.pypa.io/ez_setup.py”
    -	Run the script: “python ez_setup.py install”   
    -	Download SQLAlchemy from “from https://pypi.python.org/packages/source/S/SQLAlchemy/SQLAlchemy-1.0.9.tar.gz”
    -	Extract it to some folder, say C:\Python27
    -	Install SQLAlchemy, say "C:\Python27\SQLAlchemy-1.0.9>python setup.py install"
    
If running from cmd, "DEMO.db" and "uuids.txt" gets created in the direcotry, to which cmd is pointing.

If running from eclipse, then "DEMO.db" and "uuids.txt" gets created in the directory in which the scripts are kept.

If "assignment_without_argument.py" script is run then no need to provide the "uuids.txt" as argument, because the script itself adds 100 uuid's to the database and 1000 uuid's will be written into the uuids.txt file.

If "assignment_without_argument.py" script is run then its MANDATORY to provide the uuids text file and few of the uuid's has to be added MANUALLY into the database.

  
