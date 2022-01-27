from flask_mongoengine import MongoEngine
from model.properties import Properties
from model.weapon import Weapon
from flask import Flask

# Create Flask's `app` object
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
   'db': 'test',
   'host': 'db',
   'port':27017,
   'username':'admin',
   'password':'admin',
   'authentication_source':'admin'
}
db = MongoEngine(app)

@app.route('/')
def selectAll():
    str = ''
    for item in Weapon.objects():
        str += 'ID: {}, name: {}, description: {}, position: {}, level: {}\n'.format(item.id, item.name, item.description, item.position, item.level)
        str += '\t\tPROPERIES: damage: {}, health: {}, weight: {}, value: {}\n'.format(item.properties.damage, item.properties.health, item.properties.weight, item.properties.value)
    return str

@app.route('/json')
def selectJSON():
    q_set = Weapon.objects()
    json_data = q_set.to_json()
    return json_data

@app.route('/create/<name>')
def create(name):
    item=Weapon(name=name, properties=Properties()).save()
    return "success"

@app.route('/delete/<name>')
def delete(name):
    Weapon.objects(name__contains=name).delete()
    return "success"

@app.route('/update/<old_name>/<new_name>')
def update(old_name, new_name):
    Weapon.objects(name__=old_name).update_one(set__name=new_name)
    return "success"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
