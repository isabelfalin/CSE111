def water_column_height(tower_height, tank_height):
    h = tower_height + 3 * tank_height / 4
    return h

def pressure_gain_from_water_height(height):
    density = 998.2
    g = 9.80665
    pressure = density * g * height / 1000
    return pressure

#PEMDAS

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density = 998.2
    pressure = -friction_factor * pipe_length * density * fluid_velocity ** 2 / (2000 * pipe_diameter)
    return pressure



    

