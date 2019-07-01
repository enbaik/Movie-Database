import sys
import rds_config
import pymysql
import ast
import add_Client
import add_Movie
from datetime import datetime
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QPlainTextEdit
from PyQt5.uic import loadUi

class newClient(QDialog):
    def __init__(self,parent = None):
        super(newClient,self).__init__(parent)
        loadUi('add_Client.ui',self)

        ############# connect to rds
        rds_host  = rds_config.db_endpoint
        name = rds_config.db_username
        password = rds_config.db_password
        db_name = rds_config.db_name
        port = 3306
        self.conn = pymysql.connect(rds_host, user=name, 
                                    passwd=password, db=db_name, connect_timeout=5)
        ###################### 

        self.Confirm.clicked.connect(self.addClient)
        # add new client from input info
    def addClient(self):
        first = self.FirstName.toPlainText()
        last = self.LastName.toPlainText()
        phone = self.PhoneNumber.toPlainText()
            
        # input missing
        if first == "" or last == "" or phone == "":
            return None

        # check if exist with phone number
        query = "select * from Clients where PrimaryPhone = " + phone
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            result = list(cur)
            cur.close()
        if len(result) != 0:
            self.FirstName.setPlainText("Client")
            self.LastName.setPlainText("Already")
            self.PhoneNumber.setPlainText("Exists")
            return

        insert = "insert into Clients (ClientId, FirstName, LastName, PrimaryPhone)"
        insert = insert + " values ("
        query = "select max(ClientId) from Clients "
        # first query used to get max id
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            result = list(cur)
            cur.close()
            # increment by 1 for new client id
            nextId = result[0]
            nextId = int(nextId[0]) + 1
            insert = insert + str(nextId) + ", '" + first + "', '" + last + "', " + phone + ")"
            # complete insert and execute
        with self.conn.cursor() as cur:
            cur.execute(insert)
            self.conn.commit()
        self.LastName.setPlainText("New")
        self.LastName.setPlainText("Client")
        self.LastName.setPlainText("Created")

############################################################
class newMovie(QDialog):
    def __init__(self,parent = None):
        super(newMovie,self).__init__(parent)
        loadUi('add_Movie.ui',self)

        ############# connect to rds
        rds_host  = rds_config.db_endpoint
        name = rds_config.db_username
        password = rds_config.db_password
        db_name = rds_config.db_name
        port = 3306
        self.conn = pymysql.connect(rds_host, user=name, 
                                    passwd=password, db=db_name, connect_timeout=5)
        ###################### 

        self.Confirm.clicked.connect(self.addMovie)

        # add new movie to database
    def addMovie(self):
        title = self.MovieName.toPlainText()
        year = self.MovieYear.toPlainText()
            
        if title == "" or year == "":
            self.MovieName.setText("No Input Detected")
            return None
        # create insert statement
        insert = "insert into Movies (MovieId, Title, Genre, MovieYear, NoGenre, "
        insert = insert + "ActionF, Adventure, Animation, Children, Comedy, "
        insert = insert + "Crime, Document, Drama, Fantasy, FilmNoir, Horror, "
        insert = insert + "IMAX, Musical, Mystery, Romance, SciFi, thriller, "
        insert = insert + "War, Western) values ( "
        # get max id for creating new id
        query = "select max(MovieId) from Movies "
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            result = list(cur)
            cur.close()

            nextId = result[0]
            nextId = int(nextId[0]) + 1
            insert = insert + str(nextId) + ",'" + title + "', '"
            # complete insert by getting and appending genres section
            genreData = self.checkGenres()
            insert = insert + genreData[0] + "', " + year + "," + genreData[1]
        with self.conn.cursor() as cur:
            cur.execute(insert)
            self.conn.commit()
        self.MovieName.setPlainText("Movie Added")


        # returns genres as strings, one for genre column, other for int values
    def checkGenres(self):
        genreChecked = False
        addGenres = [] # input values for ints
        genresList = [] # string column
        if self.Action.isChecked() == True:
            addGenres.append(1)
            genresList.append("Action")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Adventure.isChecked() == True:
            addGenres.append(1)
            genresList.append("Adventure")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Animation.isChecked() == True:
            addGenres.append(1)
            genresList.append("Animation")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Children.isChecked() == True:
            addGenres.append(1)
            genresList.append("Children")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Comedy.isChecked() == True:
            addGenres.append(1)
            genresList.append("Comedy")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Crime.isChecked() == True:
            addGenres.append(1)
            genresList.append("Crime")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Documentary.isChecked() == True:
            addGenres.append(1)
            genresList.append("Documentary")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Drama.isChecked() == True:
            addGenres.append(1)
            genresList.append("Drama")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Fantasy.isChecked() == True:
            addGenres.append(1)
            genresList.append("Fantasy")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.FilmNoir.isChecked() == True:
            addGenres.append(1)
            genresList.append("FilmNoir")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Horror.isChecked() == True:
            addGenres.append(1)
            genresList.append("Horror")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.IMAX.isChecked() == True:
            addGenres.append(1)
            genresList.append("IMAX")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Musical.isChecked() == True:
            addGenres.append(1)
            genresList.append("Musical")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Mystery.isChecked() == True:
            addGenres.append(1)
            genresList.append("Mystery")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Romance.isChecked() == True:
            addGenres.append(1)
            genresList.append("Romance")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.SciFi.isChecked() == True:
            addGenres.append(1)
            genresList.append("SciFi")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Thriller.isChecked() == True:
            addGenres.append(1)
            genresList.append("Thriller")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.War.isChecked() == True:
            addGenres.append(1)
            genresList.append("War")
            genreChecked = True
        else:
            addGenres.append(0)

        if self.Western.isChecked() == True:
            addGenres.append(1)
            genresList.append("Western")
            genreChecked = True
        else:
            addGenres.append(0)

        ret = []
        if genreChecked: # genres selected
            
            genres = '|'.join(genresList) # combines values
            values = " 0, "
            for i in range(len(addGenres)):
                values = values + str(addGenres[i]) + ","
            values = values[0:len(values) - 1] + ")"
            ret.append(genres)
            ret.append(values)
            return ret
        else: # no genres listed
            genres = "(no genres listed)"
            values = " 1,"
            for i in range (0,19):
                values = values + "0,"
            values = values[0:len(values) - 1] + ")"

            ret.append(genres)
            ret.append(values)
            return ret





############################################################
class MainPage(QDialog):

    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('CSS498_Project.ui',self)
        self.isMovie = True
        self.isClient = False
        self.curClientId = None
        self.curClient = None
        self.curMovie = None
        self.isYear = False
        self.isName = False
        self.isPhone = False
        self.dialogs = list()

        ############# connect to rds
        rds_host  = rds_config.db_endpoint
        name = rds_config.db_username
        password = rds_config.db_password
        db_name = rds_config.db_name
        port = 3306
        self.conn = pymysql.connect(rds_host, user=name, 
                                    passwd=password, db=db_name, connect_timeout=5)
        ###################### 
        self.viewMovies()

        self.Display.setReadOnly(True)
        self.tableDisplay.setSizeAdjustPolicy(
        QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.SelectBar.setPlaceholderText("Select with MovieId or ClientId")
        self.SearchBar.setPlaceholderText("Chose Search Option before entry")
        self.MoviesButton.clicked.connect(self.viewMovies)
        self.ClientsButton.clicked.connect(self.viewClients)
        self.ReturnButton.clicked.connect(self.returnMovie)
        self.RentButton.clicked.connect(self.rentMovie)
        self.SelectButton.clicked.connect(self.selectObject)
        self.SearchButton.clicked.connect(self.searchObject)
        self.AddMovie.clicked.connect(self.movieWindow)
        self.AddClient.clicked.connect(self.clientWindow)

        self.year.stateChanged.connect(self.checkYear)
        self.name.stateChanged.connect(self.checkName)
        self.phone.stateChanged.connect(self.checkPhone)

        self.Action.stateChanged.connect(self.viewMovies)
        self.Adventure.stateChanged.connect(self.viewMovies)
        self.Animation.stateChanged.connect(self.viewMovies)
        self.Children.stateChanged.connect(self.viewMovies)
        self.Comedy.stateChanged.connect(self.viewMovies)
        self.Crime.stateChanged.connect(self.viewMovies)
        self.Documentary.stateChanged.connect(self.viewMovies)
        self.Drama.stateChanged.connect(self.viewMovies)
        self.Fantasy.stateChanged.connect(self.viewMovies)
        self.FilmNoir.stateChanged.connect(self.viewMovies)
        self.Horror.stateChanged.connect(self.viewMovies)
        self.IMAX.stateChanged.connect(self.viewMovies)
        self.Musical.stateChanged.connect(self.viewMovies)
        self.Mystery.stateChanged.connect(self.viewMovies)
        self.Romance.stateChanged.connect(self.viewMovies)
        self.SciFi.stateChanged.connect(self.viewMovies)
        self.Thriller.stateChanged.connect(self.viewMovies)
        self.War.stateChanged.connect(self.viewMovies)
        self.Western.stateChanged.connect(self.viewMovies)


############ populate table with movies list
    def viewMovies(self):
        self.isMovie = True
        self.isClient = False
        query = "select MovieId, Title, Genre, MovieYear from Movies"
        query2 =  self.checkGenres()
        
        if query2 != None: # append genres if exists
            query = query + query2
        # execute query to get movies table
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            result = list(cur)
            self.tableDisplay.setRowCount(len(result)) # set row and column
            self.tableDisplay.setColumnCount(4)
            cur.close()
            # column labes
            self.tableDisplay.setHorizontalHeaderLabels(
                ["MovieId","Title","Genre","Year"])
            for row in range(0,len(result)): # fill table with query result
                sqlRow = result[row]
                if sqlRow == None:
                    break
                for col in range(0,4):
                    self.tableDisplay.setItem(
                        row,col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))
                header = self.tableDisplay.horizontalHeader()
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

######### populate table with clients list################
    def viewClients(self):
        self.isMovie = False
        self.isClient = True
        query = "select * from Clients"

        # execute query
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            result = list(cur)
            self.tableDisplay.setRowCount(len(result))
            self.tableDisplay.setColumnCount(4)
            cur.close()
            # set up and fill table with query result
            self.tableDisplay.setHorizontalHeaderLabels(
                ["ClientId","First Name","Last Name","Phone Number"])
            for row in range(0,len(result)):
                sqlRow = result[row]
                if sqlRow == None:
                    break
                for col in range(0,4):
                    self.tableDisplay.setItem(
                        row,col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))
                

############## remove selected movie from clients rented list
    def returnMovie(self):
        if self.isClient == False or self.isMovie == False:
            return
        if self.curClientId == None or self.curMovie == None:
            self.Display.setText("No Client or Movie Selected, Please Try Again")
            return
        ## checks whether movie is rented out by current client
        movId = self.curMovie[0]
        movId = str(movId[0])
        query = "select MovieId, Title, Genre, MovieYear from Movies m"
        query = query + " where MovieId = " + movId + " AND EXISTS (select ClientId"
        query = query + " from Rentals where ClientId = " + self.curClientId
        query = query + " and m.MovieId = MovieId)"

        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            self.curMovie = list(cur)
            cur.close()
        if len(self.curMovie) == 0:
            return
        ## client has rented movie, return
        query = "delete from Rentals where MovieId = " + movId

        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            result = list(cur)
            cur.close()
        ## update display
        query =  "SELECT Rentals.MovieId, Title, Genre, Rental_Date from "
        query = query + "Rentals join Movies on Rentals.MovieId = "
        query = query + "Movies.MovieId where ClientId = " + self.curClientId
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            self.curClient = list(cur)
            self.tableDisplay.setRowCount(len(self.curClient))
            self.tableDisplay.setColumnCount(4)
            cur.close()

        self.tableDisplay.setHorizontalHeaderLabels(
            ["MovieId","Title","Genre","Rental Date"])
        for row in range(0,len(self.curClient)):
            sqlRow = self.curClient[row]
            if sqlRow == None:
                break
            for col in range(0,4):
                self.tableDisplay.setItem(
                    row,col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))

################ rent selected movie for client
    def rentMovie(self):
        if self.isClient == False or self.isMovie == False:
            return
        if self.curClientId == None or self.curMovie == None:
            self.Display.setText("No Client or Movie Selected, Please Try Again")
            return

        ## add movie to client rental
        movId = self.curMovie[0]
        movId = str(movId[0])
        now = datetime.today().strftime('%Y-%m-%d')
        insert = "insert into Rentals (ClientId, MovieId, Rental_Date) values ("
        insert = insert + self.curClientId + ", " + movId + ", '" + now + "')"

        with self.conn.cursor() as cur:
            cur.execute(insert)
            self.conn.commit()
            self.curClient = list(cur)
            cur.close()

        ## update display
        query =  "SELECT Rentals.MovieId, Title, Genre, Rental_Date from "
        query = query + "Rentals join Movies on Rentals.MovieId = "
        query = query + "Movies.MovieId where ClientId = " + self.curClientId
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            self.curClient = list(cur)
            self.tableDisplay.setRowCount(len(self.curClient))
            self.tableDisplay.setColumnCount(4)
            cur.close()

        self.tableDisplay.setHorizontalHeaderLabels(
            ["MovieId","Title","Genre","Rental Date"])
        for row in range(0,len(self.curClient)):
            sqlRow = self.curClient[row]
            if sqlRow == None:
                break
            for col in range(0,4):
                self.tableDisplay.setItem(
                    row,col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))

############### select object accord to type, client, movie
    def selectObject(self):
        select = self.SelectBar.toPlainText()
        if select == "":
            self.Display.setText("No Input Detected Try Again")
            return

        elif self.isMovie:      # for movies, just ouput to display
            query = "select MovieId, Title, Genre, MovieYear from Movies"
            query = query + " where MovieId = " + select

            with self.conn.cursor() as cur:
                cur.execute(query)
                self.conn.commit()
                self.curMovie = list(cur)
                cur.close()

            self.Display.setText(''.join(str(e) for e in self.curMovie))
        else: # when client is selected, display rented movies in table
            self.isMovie = True
            self.isClient = True
            query =  "SELECT Rentals.MovieId, Title, Genre, Rental_Date from "
            query = query + "Rentals join Movies on Rentals.MovieId = "
            query = query + "Movies.MovieId where ClientId = " + select
            self.curClientId = select
            with self.conn.cursor() as cur:
                cur.execute(query)
                self.conn.commit()
                self.curClient = list(cur)
                self.tableDisplay.setRowCount(len(self.curClient))
                self.tableDisplay.setColumnCount(4)
                cur.close()

            self.tableDisplay.setHorizontalHeaderLabels(
                ["MovieId","Title","Genre","Rental Date"])
            for row in range(0,len(self.curClient)):
                sqlRow = self.curClient[row]
                if sqlRow == None:
                    break
                for col in range(0,4):
                    self.tableDisplay.setItem(
                        row,col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))
                

  ############## open new window to add new movie
    def movieWindow(self):
        addMovieDialog = newMovie(self)
        self.dialogs.append(addMovieDialog)
        addMovieDialog.show()

############# open new window to add new client
    def clientWindow(self):
        addClientDialog = newClient(self)
        self.dialogs.append(addClientDialog)
        addClientDialog.show()

############## search for specific name, year, or phone number
    def searchObject(self):
        search = self.SearchBar.toPlainText()
        if search == "":
            self.Display.setText("No Input Detected Try Again")
            return
################## movie year
        if self.isYear:
            if self.isMovie == True:
                query = "select MovieId, Title, Genre, MovieYear from Movies"
                query2 = self.checkGenres()
                if query2 != None:
                    query = query + query2 + " AND MovieYear = " + search
                else:
                    query = query + " where MovieYear = " + search
            else:
                self.Display.setText("Not Avaliable for Clients Page")
                return
##################### movie or client name
        elif self.isName:
            if self.isMovie == True:
                query = "select MovieId, Title, Genre, MovieYear from Movies"
                query2 =  self.checkGenres()
                if query2 != None:
                    query = query + query2
                    query = query + " AND Title like '%" + search + "%'"
                else:
                    query = query + " where Title like '%" + search + "%'"

            else:
                query = "select * from Clients"
                search = search.split()
                query = query + " where FirstName like '%" + search[0]
                query = query +   "%' AND LastName like '%" + search[1] +"%'"

#####################phone number
        elif self.isPhone:
            if self.isClient == True:
                query = "select * from Clients"
                query = query + " where PrimaryPhone = " + search

            else:
                self.Display.setText("Not Avaliable for Movies Page")
                return
        else:
            self.Display.setText("No Search Options Selected")
            return

################ execute query and display result
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            result = list(cur)
            self.tableDisplay.setRowCount(len(result))
            self.tableDisplay.setColumnCount(4)
            cur.close()

        if self.isMovie:    # set table labels
            self.tableDisplay.setHorizontalHeaderLabels(
                ["MovieId","Title","Genre","Year"])
        else:
            self.tableDisplay.setHorizontalHeaderLabels(
                ["ClientId","First Name","Last Name","Phone Number"])

        for row in range(0,len(result)):
                sqlRow = result[row]
                if sqlRow == None:
                    break
                for col in range(0,4):
                    self.tableDisplay.setItem(
                        row,col, QtWidgets.QTableWidgetItem(str(sqlRow[col])))
                
#################### searches for specific year
    def checkYear(self):
        if self.year.isChecked() == True:
            self.isYear = True
            self.isPhone = False
            self.isName  = False
            self.name.setChecked(False)
            self.phone.setChecked(False)

#################### searches for specific name
    def checkName(self):
        if self.name.isChecked() == True:
            self.isName = True
            self.isYear = False
            self.isPhone = False
            self.year.setChecked(False)
            self.phone.setChecked(False)

#################### searches for specific phone number
    def checkPhone(self):
        if self.phone.isChecked() == True:
            self.isPhone = True
            self.isYear = False
            self.isName = False
            self.name.setChecked(False)
            self.year.setChecked(False)

############ checks which genres are checked and returns where
############ for sql query
    def checkGenres(self):
        genreChecked = False
        addGenres = []
        if self.Action.isChecked() == True:
            addGenres.append(" ActionF = 1")
            genreChecked = True
        if self.Adventure.isChecked() == True:
            addGenres.append(" Adventure = 1")
            genreChecked = True
        if self.Animation.isChecked() == True:
            addGenres.append(" Animation = 1")
            genreChecked = True
        if self.Children.isChecked() == True:
            addGenres.append(" Children = 1")
            genreChecked = True
        if self.Comedy.isChecked() == True:
            addGenres.append(" Comedy = 1")
            genreChecked = True
        if self.Crime.isChecked() == True:
            addGenres.append(" Crime = 1")
            genreChecked = True
        if self.Documentary.isChecked() == True:
            addGenres.append(" Document = 1")
            genreChecked = True
        if self.Drama.isChecked() == True:
            addGenres.append(" Drama = 1")
            genreChecked = True
        if self.Fantasy.isChecked() == True:
            addGenres.append(" Fantasy = 1")
            genreChecked = True
        if self.FilmNoir.isChecked() == True:
            addGenres.append(" FilmNoir= 1")
            genreChecked = True
        if self.Horror.isChecked() == True:
            addGenres.append(" Horror = 1")
            genreChecked = True
        if self.IMAX.isChecked() == True:
            addGenres.append(" IMAX = 1")
            genreChecked = True
        if self.Musical.isChecked() == True:
            addGenres.append(" Musical = 1")
            genreChecked = True
        if self.Mystery.isChecked() == True:
            addGenres.append(" Mystery = 1")
            genreChecked = True
        if self.Romance.isChecked() == True:
            addGenres.append(" Romance = 1")
            genreChecked = True
        if self.SciFi.isChecked() == True:
            addGenres.append(" SciFi = 1")
            genreChecked = True
        if self.Thriller.isChecked() == True:
            addGenres.append(" Thriller = 1")
            genreChecked = True
        if self.War.isChecked() == True:
            addGenres.append(" War = 1")
            genreChecked = True
        if self.Western.isChecked() == True:
            addGenres.append(" Western = 1")
            genreChecked = True

        if genreChecked:
            where = " where" + " AND ".join(str(x) for x in addGenres)
            return where
        else:
            return None

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())