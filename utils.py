def get_input(day:int=1, splitlines=True):
    

    try:
      with open(f"input{str(day).zfill(2)}.txt") as fin:
          data = fin.read().strip()
          if splitlines: data = data.splitlines()
          return data 

    except:
        print(f"Failed to load input{day}.txt from disk")