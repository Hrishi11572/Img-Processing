from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt 

# This algorithm Runs faster, with a tc of O(# of Contour Points)

class ContourGenerator: 
    def __init__ (self, imagePath): 
        self.path = imagePath
        self.img = Image.open(self.path)
        self.arr = np.array(self.img);
        self.chainCode = 0; # initial value of the chain code 
        self.contour = [];
    
    def defineNeighbour(self): 
        self.dx = [-1,-1,0,1,1,1,0,-1];  
        self.dy = [0,1,1,1,0,-1,-1,-1];
        
        # define the chain code mapping 
        self.cmp = {
            0 : 6, 
            1 : 6, 
            2 : 0, 
            3 : 0, 
            4 : 2, 
            5 : 2, 
            6 : 4, 
            7 : 4, 
        }; 
    
    def getStartPoint(self): 
        start = None; 
        self.height, self.width = self.arr.shape
        
        for i in range(self.height): 
            for j in range(self.width): 
                if self.arr[i][j] == 255: 
                    start = (i, j); 
                    break; 
        
        return start; 
        
    def createContour(self): 
        self.defineNeighbour(); 
        start = self.getStartPoint(); 
        
        if start == None: 
            print("The input image has not White Pixel ... Closing..."); 
            return; 
        else : 
            current_point = start; 
            
            while True: 
                x, y = current_point; 
                
                for k in range(self.chainCode, self.chainCode+8):
                    nx = x + self.dx[k%8]; 
                    ny = y + self.dy[k%8]; 
                    
                    if 0<= nx <self.height and 0<= ny <self.width and self.arr[nx][ny] == 255: 
                        self.contour.append((nx, ny)); 
                        current_point = (nx, ny); 
                        self.chainCode = self.cmp[k%8]; 
                        break; 
                        
                if current_point == start: 
                    break; 
    
    def showContour(self): 
        plt.imshow(self.arr, cmap="gray"); 
        row, col = zip(*self.contour); 
        plt.scatter(col, row, s=2, c="red"); 
        plt.show(); 
        
    def saveContour(self, r=0 , g=1 , b=0): 
        contour_image = np.zeros((self.arr.shape[0], self.arr.shape[1], 3), dtype=np.uint8); 
        for (i, j) in self.contour: 
            contour_image[i, j] = [255*r,255*g,255*b]; 
        plt.imshow(contour_image); 
        savePATH = self.path.replace(".png", "_Contour_b_.png");
        plt.savefig(savePATH); 
        

# # # # # # # # # # ---- R U N  A S  S C R I P T ---- # # # # 

if __name__ == '__main__': 
    PATH = "Idol_binary.png"
    model = ContourGenerator(PATH); 
    
    # generate the contour 
    model.createContour(); 
    
    # show the contour
    model.showContour(); 
    
    # save the contour. Provide r,g,b values from [0, 1] as color %
    model.saveContour(1,1,1); 
                        
                    