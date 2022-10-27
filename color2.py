import requests 
import cv2 #opencv
URL="https://www.thecolorapi.com/id?" #url of the API


#image to be worked upon
img_path='colorpic.jpg' #path of the image
img=cv2.imread(img_path) #

clicked=False
r=g=b=x_pos=y_pos=0

def get_color_name(R,G,B):
    PARAMS = {'rgb':str(R)+","+str(G)+","+str(B)}  #storing the parameters in the r,g,b format string representation
    r = requests.get(url = URL, params = PARAMS)   #API call 
  
    data = r.json()  # fetching data in json format
    
    return str(data["name"]['value'])  #return the color name,extracted from the json data 


def draw_function(event,x,y,flag,param):
    #check if left button is clicked
    #get x and y and r,g,b
    
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,x_pos,y_pos,clicked
        clicked=True
        x_pos=x
        y_pos=y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)
        

cv2.namedWindow('image')

cv2.setMouseCallback('image',draw_function)

while True:
    cv2.imshow("image",img)
    
    if clicked:
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
    
        text=get_color_name(r,g,b)+' R='+str(r)+' G='+str(g)+' B='+str(b)
       
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        
        #for light colors ie those who's R,G,B values add to a value greater than 400, display the text in black
        if r+g+b>=400:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #PRESS ESCAPE KEY TO TERMINATE
    if cv2.waitKey(20) & 0xFF==27:
        break


    
cv2.destroyAllWindows()