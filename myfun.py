import json
from os import system, name
from datetime import datetime


  
def soma(x,y):
  return x+y

def mult(x,y):
  return x*y


def concatenar(*args):
  resultado=''
  for palavra in args:
    resultado += palavra
  return resultado


def find_index(to_find, item):
  for i, valor in enumerate(to_find):
    if valor == item:
      return i
  return -1 


def cls():
  
    if name == 'nt':         # for windows
        _ = system('cls')
  

    else:                    # for mac and linux(here, os.name is 'posix')
        _ = system('clear')

      
def nl():
  print("\n")


def pause(): input("Press Enter to continue...")
  

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
  

def makej(text):
    # JSON string to python object
    obj=json.loads(text)
    return obj

  
def stat():
  print("Response Status: " + str(response.status_code))


def make_date(text):
  return datetime.strptime(text, '%d/%m/%y %H:%M:%S')



