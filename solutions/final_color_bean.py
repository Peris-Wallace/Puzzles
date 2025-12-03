import random 

def final_color_bean(white, black):  
    jar = ["W"] * white + ["B"] * black 
    
    while len(jar) > 1: 
        
        # pick two random beans 
        a, b = random.sample(jar, 2) 
        
        # remove them 
        jar.remove(a) 
        jar.remove(b) 
        
        # apply the rules 
        if a == b: # same color, add black 
            jar.append("B") 
            print(f"Picked {a} and {b}: same color → added B") 
        else: # different colors, white goes back 
            jar.append("W") 
            print(f"Picked {a} and {b}: different colors → returned W") 

        print(f"Jar now: {jar}") 
            
    final = "white" if jar[0] == "W" else "black" 
    print("Final bean:", final) 
        
    return final


if __name__ == "__main__":
    try:
        white = int(input("Enter number of white beans: "))
        black = int(input("Enter number of black beans: "))
    except ValueError:
        print("Please enter valid integers.")
    else:
        final_color_bean(white, black)
