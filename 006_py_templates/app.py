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

@app.route('/puppies')
def puppies():
    puppies = ['Rufus', 'Corgies', 'Golden Retrievers', 'Beagle', 'Poodle', 'Pug']
    return render_template('puppies.html', 
    title='Puppies', 
    subtitle='Bring these puppies to your home!'
    puppies=puppies)

#TODO: Create a route for cats

#TODO: Create a route for birds

if __name__ == '__main__':
    app.run(debug=True)