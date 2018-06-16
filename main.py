import os.path
import time

class ProjectData:
    def __init__(self):

        print(time.strftime("%c"))
        self.delimiter = ";"
        self.helplist = ["help","request","exit","input","sfile","delete", "edit"]

        if not os.path.isfile("data.csv"):
            self.file = open("data.csv","w",encoding="utf-8")
            self.file.close()
            print("A new data file has been created. The program is ready.")
        else:
            print("The data file exists. The program is ready.")

        self.check = True
        while self.check:
            self.commandFromUser = input("Input your command, please: ")
            if self.commandFromUser == "exit":
                print("The program is terminated.")
                self.check = False
            elif self.commandFromUser == "request":
                self.requestData()
            elif self.commandFromUser == "input":
                self.inputData()
            elif self.commandFromUser == "help":
                self.helpData()
            elif self.commandFromUser == "sfile":
                self.saveToFile()
            elif self.commandFromUser == "delete":
                self.delData()
            elif self.commandFromUser == "edit":
                self.editData()
            else:
                print("Unknown command.")

    def requestData(self):
        self.file = open("data.csv", "r", encoding="utf-8")
        self.contents = self.file.readlines()
        self.file.close()
        if self.contents == []:
            print("The list is empty.")
        counter = 1
        for line in self.contents:
            line = line.replace(self.delimiter, " # ")
            print(str(counter)+". "+line[:-1])
            counter += 1
            
    def saveToFile(self):
        time1 = time.time()
        self.file = open("data.csv", "r", encoding="utf-8")
        self.lines = self.file.readlines()
        self.file.close()

        self.textHTML = """<!DOCTYPE HTML>
<html> <head><meta charset="utf-8"><title>data base</title>
</head><body>
<h1>Data Base </h1>
<h2>%s</h2>
<table style="width: 500px; border: 1px dashed black;">
<thead style="background: #f87">
<tr><td>№</td><td>Name</td><td>Age</td>
<td>Profession</td><td>Time</td>
</tr></thead><tbody style="background: #a78">""" % time.strftime("%c")

        counter = 0
        for line in self.lines:
            counter +=1
            self.textHTML += "<tr><td>%d.</td>" % counter
            cells = line.split(self.delimiter)
            for cell in cells:
                self.textHTML += "<td>%s</td>" % cell
            self.textHTML += "</tr>"
                                 
        self.textHTML += "</tbody></table></body></html>"

        self.file = open("data.html", "w", encoding="utf-8")
        self.file.write(self.textHTML)
        self.file.close()
        time2 = time.time()
        print("The data have been saved.")
        print("The program has been created within %.4f seconds" % (time2-time1))


    def helpData(self):
        print("List of commands: ")
        for i in self.helplist:
            print("\t"+i)

    def inputData(self):
        self.name = input("Enter a name, please: ")
        self.age = input("Enter the age: ")
        self.profession = input("Enter the profession: ")
##        self.address = input("Enter the address: ")
##        self.birthday = input("Enter the day of birth: ")
##        self.notes = input("You may enter some notes: ")
        self.line = self.name+self.delimiter+self.age+self.delimiter+self.profession
##        self.line += self.delimiter+self.address+self.delimiter+self.birthday+self.delimiter+self.notes
        self.line += self.delimiter+str(time.strftime("%Y-%m-%d // %H:%M:%S"))+ "\n"
        self.file = open("data.csv","a",encoding="utf-8")
        self.file.write(self.line)
        self.file.close()

    def editData(self):
        self.requestData()
        print("What row do you want to edit?")
        rowNumber = int(input("Enter a number: "))
        self.contents[rowNumber-1] = ""
        print("Enter something new.")
        self.name = input("Enter a name, please: ")
        self.age = input("Enter the age: ")
        self.profession = input("Enter the profession: ")
        self.contents[rowNumber-1] =  self.name+self.delimiter+self.age+self.delimiter+self.profession
        self.contents[rowNumber-1] += self.delimiter+str(time.strftime("%Y-%m-%d // %H:%M:%S"))+ "\n"
        self.modified = ""
        for line in self.contents:
            self.modified += line
        self.file = open("data.csv", "w", encoding="utf-8")
        self.file.write(self.modified)
        self.file.close()
        self.requestData()

    def delData(self):
        self.requestData()
        print("What row do you want to delete?")
        rowNumber = int(input("Enter a number: "))
        if rowNumber <= len(self.contents) and rowNumber >0:
            self.delGivenRow(rowNumber)
            print("The row number %d has been deleted." % self.rowNumber)
        else:
            print("Out of range.")
            
    def delGivenRow(self,rowNumber):
        self.rowNumber = rowNumber
        del self.contents[self.rowNumber-1]
        self.modified = ""
        for line in self.contents:
            self.modified += line
        self.file = open("data.csv", "w", encoding="utf-8")
        self.file.write(self.modified)
        self.file.close()
        self.requestData()

a=ProjectData()
