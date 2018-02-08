import nengo
import numpy as np

model = nengo.Network()
with model:
    stim_food = nengo.Node([0,0])
    food = nengo.Ensemble(n_neurons=200, dimensions=2)

    motor = nengo.Ensemble(n_neurons=200, dimensions=2)

    nengo.Connection(stim_food, food)
    #nengo.Connection(food, motor)
    
    position = nengo.Ensemble(n_neurons=500, dimensions=2, radius=5)
    
    
    nengo.Connection(position, position, synapse=0.1)
    
    #def scaling(x):
    #    return 0.1*x
    #nengo.Connection(motor, position, synapse=0.1, function=scaling)
    nengo.Connection(motor, position, synapse=0.1, transform=0.1)

    stim_light = nengo.Node(0)
    light = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(stim_light, light)
    
    do_food = nengo.Ensemble(n_neurons=300, dimensions=3, radius=1.7)
    
    #def func(x):
    #    return x[0], x[1], 0
    #nengo.Connection(food, do_food, function=func)
    #nengo.Connection(food, do_food[:2])
    nengo.Connection(food, do_food[[0,1]])
    nengo.Connection(light, do_food[2])
    
    def food_func(x):
        foodx, foody, light = x
        if light<0.5:
            return foodx, foody
        else:
            return 0,0
    nengo.Connection(do_food, motor, function=food_func)
    
    #data_xvals = [[1,1,1], [-1,0.2,1], .....]
    #data_motor = [[0,0], [0,0],. ......]
    #nengo.Connection(do_food, motor, eval_points=data_xvals, function=data_motor)
    
    
    do_home = nengo.Ensemble(n_neurons=300, dimensions=3, radius=1.7)
    nengo.Connection(position, do_home[[0,1]])
    nengo.Connection(light, do_home[2])
    def home_func(x):
        posx, posy, light = x
        if light > 0.5:
            return -posx, -posy
        else:
            return 0, 0
    nengo.Connection(do_home, motor, function=home_func)
        
    
    

    
    