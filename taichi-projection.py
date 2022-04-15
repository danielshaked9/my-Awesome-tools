
import numpy as np

import taichi as ti

ti.init(arch=ti.gpu)

PARTICLE_N = 100000
GRID_SIZE = 1024
SENSE_ANGLE = 0.3 * np.pi
SENSE_DIST = 4.0
EVAPORATION = 0.95
MOVE_ANGLE = 0.1 * np.pi
MOVE_STEP = 2.0

grid = ti.field(dtype=ti.f32, shape=[2, GRID_SIZE, GRID_SIZE])
position = ti.Vector.field(2, dtype=ti.f32, shape=[PARTICLE_N])
heading = ti.field(dtype=ti.f32, shape=[PARTICLE_N])


@ti.kernel
def init():
    for p in ti.grouped(grid):
        grid[p] = 0.0
    for i in position:
        if i<30000:
            position[i] = ti.Vector([ti.random()*50+500, (ti.random()*50+500)]) 
            #position[i] = ti.Vector([250, 250])
            heading[i] =ti.random() * np.pi * 2.0
        if i>30000 and i<60000:
            position[i] = ti.Vector([ti.random()*50+500, (ti.random()*50+800)]) 
            #position[i] = ti.Vector([250, 250])
            heading[i] =ti.random() * np.pi * 2.0
        if i>60000 and i<90000:
            position[i] = ti.Vector([ti.random()*50+200, (ti.random()*50+500)]) 
            #position[i] = ti.Vector([250, 250])
            heading[i] =ti.random() * np.pi * 2.0
        if i>90000:
            position[i] = ti.Vector([ti.random()*50+800, (ti.random()*50+200)]) 
            #position[i] = ti.Vector([250, 250])
            heading[i] =ti.random() * np.pi * 2.0
            
            



@ti.func
def sense(phase, pos, ang):
    p = pos + ti.Vector([ti.cos(ang), ti.sin(ang)]) * SENSE_DIST
    #p = pos + ti.Vector([ti.cos(ang), ti.sin(ang)]) * SENSE_DIST*ti.random()
    return grid[phase, p.cast(int) % GRID_SIZE]


@ti.kernel
def step(phase: ti.i32):
    # move
    for i in position:
        pos, ang = position[i], heading[i]
        l = sense(phase, pos, ang - SENSE_ANGLE)
        c = sense(phase, pos, ang)
        r = sense(phase, pos, ang + SENSE_ANGLE)
        if l < c < r:
            ang += MOVE_ANGLE
        elif l > c > r:
            ang -= MOVE_ANGLE
        elif c < l and c < r:
            ang += MOVE_ANGLE * (2 * (ti.random() < 0.5) - 1)
        pos += ti.Vector([ti.cos(ang), ti.sin(ang)]) * MOVE_STEP
        position[i], heading[i] = pos, ang

    # deposit
    for i in position:
        ipos = position[i].cast(int) % GRID_SIZE
        grid[phase, ipos] += 0.01

    # diffuse
    for i, j in ti.ndrange(GRID_SIZE, GRID_SIZE):
        a = 0.0
        for di in ti.static(range(-1, 2)):
            for dj in ti.static(range(-1, 2)):
                a += grid[phase, (i + di) % GRID_SIZE, (j + dj) % GRID_SIZE]
        a *= EVAPORATION / 7.0




print("[Hint] Press A/Z to change the simulation speed.")
gui = ti.GUI('Physarum',res=GRID_SIZE)
init()
i = 0
step_per_frame = gui.slider('step_per_frame', 1, 100, 1)
while gui.running and not gui.get_event(gui.ESCAPE):
    for _ in range(int(step_per_frame.value)):
        step(i%2)
        i += 1
    gui.set_image(grid.to_numpy()[0])
    gui.show()
