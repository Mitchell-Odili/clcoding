from fileinput import filename
import imageio
filenames = ['BAR_5127.jpg', 'BAR_5129.jpg', 'BAR_5131.jpg', 'BAR_5133.jpg']
images = []
for filename in filenames:
     images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images, 'GIF', duration = 1)