import os
import json
import datetime

class App :

    def __init__ (self,path):
        self.path = path
    
    def utf8len(self,s):
        return len(s.encode('utf-8'))

    def dataentry(self,data,data_ttl,data_arg):
        #print('2')
        #print(data)
        print("Enter file contents:- ")
        continuation = "Y"
        while continuation == "Y":
            key = str()
            value = str()
            key = input("Enter key :- ")

            while len(key) > 32 or key in data.keys():
                print("Key is either too long kindly re-enter key 32 char limit or the key already exists :-  ")
                key = input()
            ttl_validation  = input("Doest it have time to live arg. (Y/N) ")
            if ttl_validation=="Y":
                data_ttl[key] = str(datetime.datetime.now())
                data_arg[key] = input("Enter in seconds")
                
            value = input("Enter Value :- ")
            while self.utf8len(value)>1000:
                print("Value is too long kindly re-enter value 16 KB limit  :-")
                value = input()
            data[key] = value
            print("Want to continue entering (Y/N):-  ")
            continuation = input()


    def create_data(self):

        #print('1')

        if not os.path.isfile(self.path):
            print("File does not exists creating file with the same name :-")
            data = dict()
            data_ttl = dict()
            data_arg = dict()
            self.dataentry(data,data_ttl,data_arg)
            print(data)
            print(data_ttl)
            json_object = json.dumps(data,indent = 1)
            ttl_object = json.dumps(data_ttl,indent = 1)
            arg_object = json.dumps(data_arg,indent = 1)
            file_ttl = self.path.split('.')[0]+"ttl.json"
            file_arg = self.path.split('.')[0]+"arg.json"
            with open (self.path, "w") as file:
                file.write(json_object)
                file.close()
            with open (file_ttl, "w") as file:
                file.write(ttl_object)
                file.close()
            with open (file_arg, "w") as file:
                file.write(arg_object)
                file.close()
            
        else :
            existing_data = dict()
            existing_data_ttl = dict()
            existing_data_arg = dict()
            try:
                print(self.path)
                json_object = str()
                ttl_object = str()
                arg_object = str()
                with open (self.path, "r") as file:
                    json_object = json.loads(file.read())
                with open (self.path.split('.')[0]+"ttl.json", "r") as file:
                    json_ttl_object = json.loads(file.read())
                with open (self.path.split('.')[0]+"arg.json", "r") as file:
                    json_arg_object = json.loads(file.read())
                print("Content of file:-  ",json_object)
                existing_data=json_object
                existing_data_ttl = json_ttl_object
                existing_data_arg = json_arg_object
                print("Want to update existing data or add new data or read the data:- ")
                print("Writing - 1 ")
                print("Reading - 2 ")
                print("Deleting - 3 ")
                choice = input()

                if choice == "1":
                    self.dataentry(existing_data,existing_data_ttl,existing_data_arg)
                    wjson = json.dumps(existing_data,indent= 1)
                    with open(self.path, "r+") as wfile :
                        wfile.truncate()
                        wfile.write(wjson)
                    w_ttl_json = json.dumps(existing_data_ttl,indent= 1)
                    with open(self.path.split('.')[0]+"ttl.json", "r+") as wfile :
                        wfile.truncate()
                        wfile.write(w_ttl_json)
                    w_arg_json = json.dumps(existing_data_arg,indent= 1)
                    with open(self.path.split('.')[0]+"arg.json", "r+") as wfile :
                        wfile.truncate()
                        wfile.write(w_arg_json)
                    

                elif choice == "2" :    
                    read_ch = "Y"
                    while read_ch == "Y":
                        asked_key = input("Enter the Key to be read :-")
                        if asked_key in existing_data.keys() :
                            if asked_key in existing_data_ttl.keys():
                                print((datetime.datetime.strptime(existing_data_ttl[asked_key], '%Y-%m-%d %H:%M:%S.%f')- datetime.datetime.now()).seconds)
                                if (datetime.datetime.strptime(existing_data_ttl[asked_key], '%Y-%m-%d %H:%M:%S.%f')- datetime.datetime.now()).seconds < int(existing_data_arg[asked_key]) :
                                    print(existing_data[asked_key])
                                else:
                                    del existing_data[asked_key]
                                    del existing_data_ttl[asked_key]
                                    del existing_data_arg[asked_key]
                                    del_json_ttl = json.dumps(existing_data_ttl, indent=1)
                                    del_json_arg = json.dumps(existing_data_arg, indent=1 )
                                    del_json = json.dumps(existing_data,indent = 1)
                                    with open(self.path,"r+") as del_file:
                                        del_file.truncate()
                                        del_file.write(del_json)
                                    with open (self.path.split(".")[0]+"ttl.json",'r+') as del_ttl:
                                        del_ttl.truncate()
                                        del_ttl.write(del_json_ttl)
                                    with open (self.path.split(".")[0]+"arg.json",'r+') as del_arg:
                                        del_arg.truncate()
                                        del_arg.write(del_json_arg)
                                    print("Key does not exist")
                            else :
                                print(existing_data[asked_key])
                        else :
                            print("Key does not exist")
                        print("Want to read some data (Y/N) :-")
                        read_ch = input()

                elif choice =="3":
                    
                    read_del = "Y"
                    while read_del == "Y":
                        asked_del = input("Enter the Key to be deleted :-")
                        if asked_del in existing_data.keys():
                            del existing_data[asked_del]
                            if asked_del in existing_data_ttl.keys():
                                del existing_data_ttl[asked_del]
                                del existing_data_arg[asked_del]
                                del_json_ttl = json.dumps(existing_data_ttl, indent=1)
                                del_json_arg = json.dumps(existing_data_arg, indent=1 )
                                with open (self.path.split(".")[0]+"ttl.json",'r+') as del_ttl:
                                    del_ttl.truncate()
                                    del_ttl.write(del_json_ttl)
                                with open (self.path.split(".")[0]+"arg.json",'r+') as del_arg:
                                    del_arg.truncate()
                                    del_arg.write(del_json_arg)                            
                            del_json = json.dumps(existing_data,indent = 1)
                            with open(self.path,"r+") as del_file:
                                del_file.truncate()
                                del_file.write(del_json)
                        else :
                            print("Key does not exist")
                        read_del = input("Would you like to delete more (Y/N)")

            except Exception as e:
                print(e)


def execution ():
    print("================================")
    print("Kindly Enter the path for file to create")
    path = input()
    a = App(path) 
    a.create_data()
    #create_data(path)

#execution()