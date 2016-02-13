import sys                                          # System bindings
import cv2                                          # OpenCV bindings
import numpy as np
import matplotlib.colors as colors 
import matplotlib.pyplot as plt
import re											# Regular Expressions
import seaborn as sns								# Drawing statistical graphics



def rgb_to_hex(rgb): 										# change rgb string to hex
 rgbstr = re.search(r"(.*)\((.*)\)", rgb).group(2)
 r,g,b = map(int ,rgbstr.split(','))
 return '#{:02x}{:02x}{:02x}'.format(r, g, b)

class ColorAnalyser():
    def __init__(self, imageLoc):
        self.src = cv2.imread(imageLoc, 1)                  # Reads in image source
        self.colors_count = {}                              # Empty dictionary container to hold the colour frequencies
 
    def count_colors(self):
        (channel_b, channel_g, channel_r) = cv2.split(self.src) # Splits image Mat into 3 color channels 
 
        channel_b = channel_b.flatten()                         # Flattens the 2D single channel array so as to make it easier to iterate over it
        channel_g = channel_g.flatten()                         #                   ""
        channel_r = channel_r.flatten()                         #                   ""
 
        for i in xrange(len(channel_b)):
            RGB = "(" + str(channel_r[i]) + "," + str(channel_g[i]) + "," + str(channel_b[i]) + ")"
            if RGB in self.colors_count:
                self.colors_count[RGB] += 1
            else:
                self.colors_count[RGB] = 1
 
        print "Colours counted..."
 
    def show_colors(self):
	print "The top5 colours are:" + '\n' + "hex         rgb       frequency"
        toplist = []
        for keys in sorted(self.colors_count, key=self.colors_count.__getitem__, reverse = True)[:5]:       # Sorts dictionary by value and show the top5
            toplist.append(rgb_to_hex(keys))                        
            print rgb_to_hex(keys), keys, ": ",self.colors_count[keys]     #  print hex, rgb and frequency
	      	
	palettecolours = [toplist[0], toplist[1], toplist[2], toplist[3], toplist[4]]
	sns.palplot(sns.color_palette(palettecolours))                         #  create a palette with the top5 colours
	plt.show()                                                             #  show the palette
    def main(self):
        if (self.src == None):                              # Checks if an image was actually loaded and errors if it wasn't
            print "No image data. Check image location for typos"
        else:
            self.count_colors()                             # Counts the amount of instances of RGB values within the image
            self.show_colors()                              # Sorts and shows  colors ordered from least  most often 
            cv2.waitKey(0)                                  # Waits for keypress before closing
 
if __name__ == "__main__":
    if (len(sys.argv) != 2):                                    # Checks if image given as cli argument/runs with the command _ python askisi13.py example.jpg
        print "error: syntax is 'python example.py /image/location.jpg'"
    else:
        Analyser = ColorAnalyser(sys.argv[1])
        Analyser.main()                                      

	
