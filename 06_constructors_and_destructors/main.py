class Logger:
    def __init__(self):
        print("Object will created") #Constructor
        
    def __del__(self):
        print("Object will destroyed") #Destructor
        
if __name__ == "__main__":
    log = Logger()
    del log 