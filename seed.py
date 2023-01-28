from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)
c3 = Cupcake(
    flavor="strawberry",
    size="small",
    rating=9,
    image="https://www.lifeloveandsugar.com/wp-content/uploads/2021/03/Fresh-Strawberry-Cupcakes3.jpg"
)
c4 = Cupcake(
    flavor="vanilla",
    size="small",
    rating=9,
    image="https://www.cookingclassy.com/wp-content/uploads/2021/09/vanilla-cupcakes-3.jpg"
)
c5 = Cupcake(
    flavor="raspberry",
    size="small",
    rating=9,
    image="https://bonnibakery.com/wp-content/uploads/2022/04/Raspberry-Cupcakes2954-4.jpg"
)
c6 = Cupcake(
    flavor="blueberry",
    size="small",
    rating=9,
    image="https://i2.wp.com/lifemadesimplebakes.com/wp-content/uploads/2022/07/Blueberry-Cupcakes-Recipe-11-2.jpg"
)

db.session.add_all([c1, c2, c3, c4, c5, c6])
db.session.commit()