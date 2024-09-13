#Imports
import os

#Constructing Path
def GetDirectory():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    DIRECTORY = dir_path + "\\Databases"
    return DIRECTORY


#Create Directory
def init():
    if not os.path.exists(GetDirectory()):
        os.makedirs(GetDirectory())

def GetLastID(DB):
    Database = GetDirectory() + "\\" + DB
    Database = open(Database, "r")
    LastID = ""
    for Record in Database:
        LastID = Record.split(",")
    
    return LastID[0].strip()

#Create Database
def CreateDatabase(Name, Fields):
    Field = Fields
    print("1/2 Fields logged successfully")

    # Create the file in the specified directory
    FilePath = os.path.join(GetDirectory(), Name)
    with open(FilePath, 'w') as file:
        file.write("ID," + Field)
    print("2/2 Database created successfully")

def ReadFields(DB):
    Database = GetDirectory() + "\\" + DB
    Database = open(Database, "r")
    for Record in Database:
        return Record
        break
    
def CreateRecord(DB, Record):
    Database = GetDirectory() + f"\\{DB}"
    Database = open(Database, "a")
    if GetLastID(DB) != "ID":
        Database.write(str(int(GetLastID(DB)) + 1) + "," + Record + "\n")
    else:
        Database.write("1," + Record + "\n")
    Database.close()
    print(Record + " written successfully")

def UpdateRecord(DB, Update, ID):
    Database = GetDirectory() + f"\\{DB}"
    Database = open(Database, "r")
    print("1/4 Reading Database")

    AllEntries = []
    for Record in Database:
        AllEntries.append(Record)
    Database.close()
    print("2/4 Records recorded, file closed, updating record")

    FoundID = False
    Counter = 0
    for i in range(0, len(AllEntries)):
        TemporaryEntry = AllEntries[i].split(",")
        TemporaryEntry[0] = TemporaryEntry[0].strip()
        if TemporaryEntry[0].strip() == ID:
            FoundID = True
            Update = ID + "," + Update + "\n"
            AllEntries[i] = Update
        Counter += 1

    if FoundID == True:
        print("3/4 Finishing writing to file")
        Database = GetDirectory() + f"\\{DB}"
        Database = open(Database, "w")
        Database.close()
        Database = open(GetDirectory() + f"\\{DB}", "a")
        for Records in AllEntries:
            Database.write(Records)
        Database.close()

        print("4/4 Operation finished successfully")
    else:
        print("ID NOT FOUND")

def DeleteRecord(DB, ID):
    Database = GetDirectory() + f"\\{DB}"
    Database = open(Database, "r")
    print("1/4 Reading Database")

    AllEntries = []
    for Entry in Database:
        AllEntries.append(Entry)
    print("2/4 Database in memory, searching for ID")

    FoundID = False
    for i in range(1, len(AllEntries)):
        CurrentEntry = AllEntries[i].split(",")
        if CurrentEntry[0] == ID:
            FoundID = True
            AllEntries[i] = ID + ",DELETED\n"

    if FoundID == True:
        print("3/4 Writing back to Database")
        Database = open(GetDirectory() + f"\\{DB}", "w")
        Database = open(GetDirectory() + f"\\{DB}", "a")
        for Entry in AllEntries:
            Database.write(Entry)
        Database.close()

        print("4/4 Entry deleted successfully")
    else:
        print("ID NOT FOUND")
            
def ReadRecord(DB, ID):
    Database = GetDirectory() + f"\\{DB}"
    Database = open(Database, "r")
    print("1/3 Reading Database")

    AllEntries = []
    for Entry in Database:
        AllEntries.append(Entry)
    print("2/3 Database in memory, searching for ID")

    FoundID = False
    Fields = AllEntries[0]
    SoughtAfterID = ""
    for i in range(1, len(AllEntries)):
        CurrentEntry = AllEntries[i].split(",")
        if CurrentEntry[0] == ID:
            FoundID = True
            SoughtAfterID = AllEntries[i]

    if FoundID == True:
        print("3/3 ID found, returning ENTRY, FIELDS")
        return SoughtAfterID.strip(), Fields.strip()
    else:
        print("ID NOT FOUND")
