from flask import Flask

my_app = Flask(__name__)

@my_app.route('/vex') #127.0.0.1:5000/vex
def vex():
    print 'Vault of Glass'
    return 'Atheon, Times Conflux'


@my_app.route('/hive')#127.0.0.1:5000/hive
def hive():
    print 'That wizard came from the moon!'
    return 'Crota, son of Oryx, Hive king'

@my_app.route('/fallen')#127.0.0.1:5000/fallen
def fallen():
    print 'Kill them dead'
    return 'Skolas, Kell of Kells'

if __name__ == '__main__':
    
    my_app.run()

