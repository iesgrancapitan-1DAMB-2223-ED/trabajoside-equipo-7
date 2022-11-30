import module as m

def main():
  try:
    hello = m.hello_world()
    

  except KeyboardInterrupt:
    print("Exiting...")
    exit(1)

if __name__ == '__main__':
  main()