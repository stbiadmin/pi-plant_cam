import plant
import matplotlib.pyplot as plt
import numpy as np
import time, datetime
from IPython.display import clear_output

def plant_health(interval):
    fig = plt.figure(figsize=(15,15))
    plt.axis('off')
    im = plt.imshow(plt.imread('../Mira_chronicles/color_mapped_image.png'))
    while True:
        #take a picture with the external camera attached to the computer
        exec(open( "camera.py").read())

        #run the captured image through the nvdi analysis
        plant.main()
        ndvi_avg = np.average(plant.calc_ndvi(plt.imread('../Mira_chronicles/contrasted.png')))

        #visualize the result
        ndvi_im = plt.imread('../Mira_chronicles/color_mapped_image.png')
        im.set_data(ndvi_im)
        fig.suptitle('Average NDVI: ' + str(f'{ndvi_avg:.5f}') + ' Image Current as of: ' + str(datetime.datetime.now()))
        fig.canvas.draw_idle()
        plt.pause(interval)

plant_health(5)