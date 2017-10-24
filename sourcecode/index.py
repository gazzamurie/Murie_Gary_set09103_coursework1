from flask import Flask, url_for, render_template, request, redirect
import os, json #Manipulates files
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("base.html")

@app.route("/earth")
def earth():
    name = "Earth"
    category = "Planet"
    description = "Earth is the third planet from the sun and the fifth largest in the solar system. Just slightly larger than nearby Venus, Earth is the biggest of the terrestrial planets. Our home planet is the only planet in our solar system known to harbor living things. The name Earth is at least 1,000 years old. All of the planets, except for Earth, were named after Greek and Roman gods and goddesses. However, the name Earth is an English/German word, which simply means the ground."

    return render_template('earth.html', name=name, category=category, description=description)

@app.route("/jupiter")
def jupiter():
    name = "Jupiter"
    category = "Planet"
    description = "Jupiter is the fifth planet from our sun and the largest planet in the solar system. Jupiter's stripes and swirls are cold, windy clouds of ammonia and water. The atmosphere is mostly hydrogen and helium, and its iconic Great Red Spot is a giant storm bigger than Earth that has raged for hundreds of years. Jupiter is surrounded by more than 50 moons (with more a dozen more awaiting confirmation)."
    return render_template('jupiter.html', name=name, category=category, description=description)

@app.route("/mars")
def mars():
    name = "Mars"
    category = "Planet"
    description = "Mars is a cold desert world. It is half the diameter of Earth and has the same amount of dry land. Like Earth, Mars has seasons, polar ice caps, volcanoes, canyons and weather, but its atmosphere is too thin for liquid water to exist for long on the surface. There are signs of ancient floods on Mars, but evidence for water now exists mainly in icy soil and thin clouds."
    return render_template('mars.html', name=name, category=category, description=description)

@app.route("/mercury")
def mercury():
    name = "Mercury"
    category = "Planet"
    description = "Mercury's eccentric orbit takes the small planet as close as 47 million km (29 million miles) and as far as 70 million km (43 million miles) from the sun. If one could stand on the scorching surface of Mercury when it is at its closest point to the sun, the sun would appear more than three times as large as it does when viewed from Earth."
    return render_template('mercury.html', name=name, category=category, description=description)

@app.route("/uranus")
def uranus():
    name = "Uranus"
    category = "Planet"
    description = "The seventh planet from the sun with the third largest diameter in our solar system, Uranus is very cold and windy. The ice giant is surrounded by 13 faint rings and 27 small moons as it rotates at a nearly 90-degree angle from the plane of its orbit. This unique tilt makes Uranus appear to spin on its side, orbiting the sun like a rolling ball. The first planet found with the aid of a telescope, Uranus was discovered in 1781 by astronomer William Herschel, although he originally thought it was either a comet or a star. It was two years later that the object was universally accepted as a new planet, in part because of observations by astronomer Johann Elert Bode. William Herschel tried unsuccessfully to name his discovery Georgium Sidus after King George III. Instead the planet was named for Uranus, the Greek god of the sky, as suggested by Johann Bode."
    return render_template('uranus.html', name=name, category=category, description=description)

@app.route("/neptune")
def neptune():
    name = "Neptune"
    category = "Planet"
    description = "Dark, cold and whipped by supersonic winds, Neptune is the last of the hydrogen and helium gas giants in our solar system. More than 30 times as far from the sun as Earth, the planet takes almost 165 Earth years to orbit our sun. In 2011 Neptune completed its first orbit since its discovery in 1846."
    return render_template('neptune.html', name=name, category=category, description=description)

@app.route("/saturn")
def saturn():
    name = "Saturn"
    category = "Planet"
    description = "The second largest planet in our solar system, adorned with thousands of beautiful ringlets, Saturn is unique among the planets. It is not the only planet to have rings -- made of chunks of ice and rock -- but none are as spectacular or as complicated as Saturn's. Like fellow gas giant Jupiter, Saturn is a massive ball of mostly hydrogen and helium. Surrounding by 53 confirmed and nine provisional moons, Saturn is home to some of the most fascinating landscapes in our solar system. From the jets of Enceladus to the methane lakes on smoggy Titan, the Saturn system is a rich source of scientific discovery and still holds many mysteries. The farthest planet from Earth observable by the unaided human eye, Saturn has been known since ancient times and is named for the Roman god of agriculture and wealth. The Greek equivalent was Cronos, the father of Zeus/Jupiter."
    return render_template('saturn.html', name=name, category=category, description=description)

@app.route("/venus")
def venus():
    name = "Venus"
    category = "Planet"
    description = "Venus is the second planet from the sun and our closest planetary neighbor. Similar in structure and size to Earth, Venus spins slowly in the opposite direction most planets do. Its thick atmosphere traps heat in a runaway greenhouse effect, making it the hottest planet in our solar system with surface temperatures hot enough to melt lead. Glimpses below the clouds reveal volcanoes and deformed mountains. Venus is named for the ancient Roman goddess of love and beauty, the counterpart to the Greek goddess Aphrodite."
    return render_template('venus.html', name=name, category=category, description=description)

@app.route("/sun")
def sun():
    name = "Sun"
    category = "Sun"
    description = "The sun at the heart of our solar system is a yellow dwarf star, a hot ball of glowing gases. Its gravity holds the solar system together, keeping everything from the biggest planets to the smallest particles of debris in its orbit. Electric currents in the sun generate a magnetic field that is carried out through the solar system by the solar wind a stream of electrically charged gas blowing outward from the sun in all directions."
    return render_template('sun.html', name=name, category=category, description=description)

@app.route("/dwarfplanet")
def dwarf():
    name = "Dwarf Planets"
    category = "Small Bodies"
    description = "While similar to planets in many ways, dwarf planets share their orbits around the sun with other objects such as asteroids or comets. The first five recognized dwarf planets are:"
    return render_template('dwarf.html', name=name, category=category, description=description)

@app.route("/pluto")
def pluto():
    name = "Pluto"
    category = "Dwarf Planet"
    description = "Discovered in 1930, Pluto was long considered our solar system's ninth planet. But after the discovery of similar intriguing worlds deeper in the distant Kuiper Belt, icy Pluto was reclassified as a dwarf planet. Findings by NASA's New Horizons in 2015 revealed for the first time how that Pluto is a complex and mysterious world. Information about Pluto and its largest moon, Charon, provide insight into the collision believed to have formed the dwarf planet and moons we see today. Dwarf planets may provide the best evidence about the origins of our solar system."
    return render_template('pluto.html', name=name, category=category, description=description)

@app.route("/ceres")
def ceres():
    name = "Ceres"
    category = "Dwarf Planet"
    description = "Dwarf planet Ceres is the largest object in the asteroid belt between Mars and Jupiter and the only dwarf planet located in the inner solar system. It was the first member of the asteroid belt to be discovered when Giuseppe Piazzi spotted it in 1801. And when Dawn arrived in 2015, Ceres became the first dwarf planet to receive a visit from a spacecraft. Called an asteroid for many years, Ceres is so much bigger and so different from its rocky neighbors that scientists classified it as a dwarf planet in 2006. Even though Ceres comprises 25 percent of the asteroid belt's total mass, tiny Pluto is still 14 times more massive. Ceres is named for the Roman goddess of harvests. The word cereal comes from the same name."
    return render_template('ceres.html', name=name, category=category, description=description)

@app.route("/asteroids")
def asteroids():
    name = "Asteroids"
    category = "Small Bodies"
    description = "Asteroids are rocky, airless worlds that orbit our sun, but are too small to be called planets. Tens of thousands of these minor planets are gathered in the main asteroid belt, a vast doughnut-shaped ring between the orbits of Mars and Jupiter. Asteroids that pass close to Earth are called near-earth objects."
    return render_template('asteroids.html', name=name, category=category, description=description)

@app.route("/comets")
def comets():
    name = "Comets"
    category = "Small Bodies"
    description = "Comets are cosmic snowballs of frozen gases, rock and dust roughly the size of a small town. When a comet's orbit brings it close to the sun, it heats up and spews dust and gases into a giant glowing head larger than most planets. The dust and gases form a tail that stretches away from the sun for millions of kilometers."
    return render_template('comets.html', name=name, category=category, description=description)

@app.route("/meteors")
def meteors():
    name = "Meteors & Meteorites"
    category = "Small Bodies"
    description = "Little chunks of rock and debris in space are called meteoroids. They become meteors -- or shooting stars -- when they fall through a planet's atmosphere; leaving a bright trail as they are heated to incandescence by the friction of the atmosphere. Pieces that survive the journey and hit the ground are called meteorites."
    return render_template('meteors.html', name=name, category=category, description=description)

@app.route("/eris")
def eris():
    name = "Eris"
    category = "Dward Planet"
    description = "It takes icy Eris 557 Earth years to complete a single orbit around our sun. The plane of Eris' orbit is well out of the plane of the solar system's planets and extends far beyond the Kuiper Belt, a zone of icy debris beyond the orbit of Neptune. All the asteroids in the asteroid belt would easily fit inside Eris. However, Eris, like Pluto, is still smaller than the Earth's Moon."
    return render_template('eris.html', name=name, category=category, description=description)
#Handles the error is user goes to link in our domain that doesnt exsist
@app.errorhandler(404)
def page_not_found(error):
    return render_template('fourofour.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
