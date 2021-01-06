from observer.observer import DigitObserver, GraphicObserver
from observer.generator import RandomNumberGenerator

def startMain():
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphicObserver()
    generator.addObserver(observer1)
    generator.addObserver(observer2)
    generator.execute()

if __name__ == '__main__':
    startMain()