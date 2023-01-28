def seririalized(cupcake):
    serialized = {'cupcake' : {"id": cupcake.id,
                      "flavor": cupcake.flavor,
                      "size": cupcake.size,
                      "rating": cupcake.rating, 
                      "image": cupcake.image }}
    return serialized