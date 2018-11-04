from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    pets = [{'url':'puppies', 'title':'Puppies'},
            {'url':'kittens', 'title':'Kittens'},
            {'url':'birds', 'title':'Birds'}
           ]
    return render_template('home.html', title='Welcome to Pet Rescue',
        pets=pets
    )

@app.route('/kittens')
def kittens():
    kittens = ['Adele', 'Bella', 'Boo']
    return render_template('kittens.html', 
    title='Kittens', 
    subtitle='Bring these kittens to your home!',
    kittens=kittens)    

@app.route('/birds')
def birds():
    birds = ['Charlie', 'Angel', 'Max']
    return render_template('birds.html', 
    title='birds', 
    subtitle='Bring these birds to your home!',
    birds=birds)      

@app.route('/puppies')
def puppies():
    puppies = ['Rufus', 'Corgies', 'Golden Retrievers', 'Beagle', 'Poodle', 'Pug']
    return render_template('puppies.html', 
    title='Puppies', 
    subtitle='Bring these puppies to your home!',
    puppies=puppies)

if __name__ == '__main__':
    app.run(debug=True)