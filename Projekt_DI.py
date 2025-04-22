from hashlib import sha256
import requests
import json


class File:

    name="passwd.txt"

    def __init__(self) -> None:

        self.file_name = File.name
        self.x = None
        self.file_open = None
        self.password_verify = None
        self.password_hash_verify = None
        self.password = None
        self.password_hash = None
        self.password_input = None
        self.row_to_write = None
        self.list = None
        self.file_name_open = None
        self.user_name_input = None
        self.file_write = None
        self.bb = None
        self.aa = None




    def file_op(self):
        try:
            self.file_write = open(self.file_name, "x")
            self.file_write.write(f"UserName,PasswordHash\n")
            self.file_write.close()
        except FileExistsError:
            pass



    def file_ck(self):
        self.user_name_input = input('Enter new username to create: ')
        self.file_name_open = open(self.file_name, "r")

        for row in self.file_name_open:
            self.list = row.split(',')

            if self.user_name_input == (self.list[0].rstrip('\n')):
                print('User already exists: ' + self.list[0])
                exit()



    def hash_pw(self):

        self.password_input = input('Enter password to create: ')
        self.aa=Sha(password_input=self.password_input, password_hash=self.password_hash)
        self.password_hash=self.aa.hash_it()




    def file_wr(self):
        self.row_to_write = (self.user_name_input + ',' + self.password_hash)

        self.file_write = open(self.file_name, "a")
        self.file_write.write(f"{self.row_to_write}\n")
        self.file_write.close()

        print("Username and Hash have been writen. Let's do a test!")
        print()





    def hash_ck(self):
        self.password_verify = input('Login simulation - enter password for "' + self.user_name_input + '": ')

        self.bb = Sha(password_input=self.password_verify, password_hash=self.password_hash_verify)
        self.password_hash_verify = self.bb.hash_it()

        print(f"Hash check: {self.password_hash_verify}")

        self.file_open = open(self.file_name, "r")
        for row in self.file_open:
            self.list=row.split(',')
            if self.password_hash_verify==(self.list[1].rstrip('\n')) and self.user_name_input==(self.list[0].rstrip('\n')):
                self.x=1

        if self.x==1:
            print()
            print("Access granted for username/hash:")
            print(self.list[0], self.list[1])
            api_endpoint = "https://pastebin.com/api/api_post.php"
            api_key = "x5fQasiQOuKkcp2FTaFgghmRuqqUW2t1"
            source_code =("username:" + self.list[0] + "   " +"hash: "+ self.list[1])
            data = {'api_dev_key': api_key,
                    'api_option': 'paste',
                    'api_paste_code': source_code,
                    }
            r = requests.post(url=api_endpoint, data=data)
            pastebin_url = r.text
            print("Your login data have been stored safely.")
            print("The pastebin URL is:%s" % pastebin_url)

        else:
            print()
            print("Login failed - incorrect password")
            print(self.list[0], self.list[1])
            api_url = "https://run.mocky.io/v3/1aed60ec-40a9-4e10-b77e-225c07a9be2d"
            response = requests.get(api_url)
            data=response.json()
            print(data)



class Sha(File):

    def __init__(self, password_input: str, password_hash: str) -> None:
        super().__init__()

        self.password_hash = password_hash
        self.password_input= password_input

    def hash_it(self):

        self.password_hash = (sha256(self.password_input.encode('utf-8')).hexdigest())
        return self.password_hash



class Lister:
    def __init__(self):

        self.file_name = File.name
        self.i = 0
        self.row = None
        self.list = [None]*5
        self.file_open = None


    def read(self):

        self.file_open = open(self.file_name, "r")

        for self.row in self.file_open:
            self.list[self.i] = self.row
            self.i=self.i+1
        return self.list



class UserList(Lister):

    def __init__(self, y):
        super().__init__()
        self.y = y

    def usr (self):

        print('_____________________________________')
        print('List of already created usernames:')
        i=0
        for x in self.y:
            if x is not None:
                z=(self.y[i])
                v=z.split(',')
                print(v[0])
            i=i+1
        print('_____________________________________')
#########################################################################

f=File()
f.file_op()

r=Lister()
y=r.read()
d=UserList(y)
d.usr()

f.file_ck()
f.hash_pw()
f.file_wr()
f.hash_ck()

#########################################################################











