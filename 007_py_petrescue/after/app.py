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
    pets = ['Adele', 'Bella', 'Boo']
    return render_template('pets.html', 
    title='Kittens', 
    image='images/kitten.jpg',
    subtitle='Bring these kittens to your home!',
    pets=pets)    

@app.route('/birds')
def birds():
    pets = ['Charlie', 'Angel', 'Max']
    return render_template('pets.html', 
    title='birds', 
    image='images/bird.jpg',
    subtitle='Bring these birds to your home!',
    pets=pets)      

@app.route('/puppies')
def puppies():
    pets = ['Rufus', 'Corgies', 'Golden Retrievers', 'Beagle', 'Poodle', 'Pug']
    return render_template('pets.html', 
    title='Puppies', 
    image='images/puppy.jpg',
    subtitle='Bring these puppies to your home!',
    pets=pets)

if __name__ == '__main__':
    app.run(debug=True)