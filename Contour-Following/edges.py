from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt 

class ContourFollower : 
    def __init__(self, path: str): 
        self.path = path;  
        self.img = np.array(Image.open(self.path)); 
        self.dx = [-1,-1,0,1,1,1,0,-1]; 
        self.dy = [0,-1,-1,-1,0,1,1,1];
        self.contour = [];
        
    def getContour(self):
        height, width = self.img.shape; 
        for i in range(height): 
            for j in range(width):
                if self.img[i][j] == 255: 
                    neigh = [];
                    for k in range(8): 
                        neigh.append(self.img[i + self.dx[k]][j + self.dy[k]]); 
                    
                    if any( n == 0 for n in neigh): 
                        self.contour.append((i, j));
    
    def displayContour(self): 
        # first run the method 
        self.getContour()
        
        plt.imshow(self.img, cmap="gray");
        row, col = zip(*self.contour); 
        plt.scatter(col, row, s=2, c="red"); 
        plt.show(); 
        
    def saveContour(self): 
        contour_img = np.zeros((self.img.shape[0], self.img.shape[1], 3), dtype=np.uint8);
        for (i, j) in self.contour: 
            contour_img[i, j] = [255,0,0];
        plt.imshow(contour_img); 
        plt.savefig(self.path.replace(".png", "_Contour.png")); 
        

if __name__ == '__main__': 
    PATH = "Vase_binary.png";
    img = ContourFollower(PATH);
        
    # to display contour
    img.displayContour();
    
    # save contour
    img.saveContour();

        
                    
                        