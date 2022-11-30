class NoHelloWorldException(Exception):
  pass

def hello_world():
  while True:
    try:
      hi = str(input(""))
      if hi == "Hello":
        print("Hello World!")
        break
      else:
        raise NoHelloWorldException("Say Hello!!!!")

    except NoHelloWorldException as nhwe:
      print(nhwe.__str__())