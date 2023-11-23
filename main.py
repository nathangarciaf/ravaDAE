import sys
from bot import run_bot_terminal

def main():
    n = len(sys.argv)
    resp=""
    for i in range(1,n):
        resp += sys.argv[i] + " "
    print(resp)
    run_bot_terminal(resp)
    
if __name__ == "__main__":
    main()