import argparse
from config import load_config 
from tempo import Tempo

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log time to Tempo 😎")
    args = parser.parse_args()

    CONFIG = load_config()

    tempo = Tempo(CONFIG.get('user', 'token'), CONFIG.get('user', 'url'))

    tempo.test()
