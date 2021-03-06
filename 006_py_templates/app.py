from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    pets = [{'url':'puppies', 'title':'Puppies', 'image': 'images/puppy.jpg'},
            {'url':'kittens', 'title':'Kittens', 'image': 'images/kitten.jpg'},
            {'url':'birds', 'title':'Birds', 'image': 'images/bird.jpg'}
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

#TODO: Create a route for cats

#TODO: Create a route for birds

if __name__ == '__main__':
    app.run(debug=True)