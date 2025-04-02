# remove in public
from utils.utilities import colourprint, color, wait, clear


art = """                                                                                                    





                                                 ..                                                 
                                                -**:                                                
                                             .-*####+:                                              
                                          .+%@#######%@#.                                           
                                      .+%@@%##########@@@@@*.                                       
                                   -@@@@@@@%##########%@@@@@@@@*                                    
                                 =%#%%@@@@@###########@@@@@@@@@*#+:                                 
                               .+*++#%@@@@###########@@@@@@@@@@*+++:                                
                               ...:+*%@@@@@##########%@@@@@@@@@*+++:.                               
                                -#%+--%@@@@@#*#######*%@@@@@@@%+=-+-                                
                             .*#@%@@@@#+=#@@#*###*#####@@@#++#@@@%@#=+                              
                            .+#%***#@@@@@@@*=#%#*==*#++#@@@@@@@%#*-+@=:.                            
                          ....=+++--*#%@@%%@@@%+*-==%@@%##%@@@%##-:---.:.                           
                        .-*=:.--=----=#####*==*%#=:=*%#*=::---------:..:-+.                         
                           .=- .  .---:::::::::::.:::==:::::--:.     .==-::.                        
                          +-.:.:.           .:::.=-...             -:..:.-                          
                          .:. .+%              :@@@@              **. .:=-                          
                           ...-=+#-            #%%%@:            :*+-=...                           
                             .:+++++##       :*#%%%%#-       =%#+++#*:.                             
                             :-===******###%@%*%%%%%%*%####**+#%#*+=-=.                             
                             -=-==+++%@@%##**%*@%@@@%#%*=*@@@@@+*#+===.                             
                              +====++*#%@@*:=%#@@@@@@*%+:-@@@%%%*====*                              
                                :=====**#@#:=#@@@@@@@@@+:=@@@%+++==:                                
                                   .=**+#@%:=%-*@@@@#-%+:+@@%+-:                                    
                                       +#@%:=@-::::.::@+:*%%#                                       
                                       =##%:=@%**==**#@=:#%#*                                       
                                       -##%:.          .:%%#=                                       
                                       .%%@:.          ::@%%.                                       
                                        %%@:.          :-@%%                                        
                                        %@@-:          :=@%%                                        
                                        %@@=:          :+%@#                                        
                                        #@%+:          :*%@+                                        
                                        +%%+:          :#%@:                                        
                                        -%%*:         .:#%@.                                        
                                        .%%*:         .:%@%                                         
                                         @%#:         :-#@#                                         
                                         .*#.          :*-                                          








                                                                                                    """

def doom():
  clear()
  colourprint(art)
  wait(2)
  clear()
  colourprint(f"{color.RED}{color.BOLD}You have found the secret doom!{color.END}")
  wait(0.5)
  colourprint(f"{color.GREEN}{color.BOLD}You have been granted the power to destroy the world!{color.END}")
  wait(0.5)
  colourprint(f"{color.YELLOW}{color.BOLD}AND LISTEN TO MF DOOM!{color.END}")
  wait(3)
  colourprint(f"{color.DARKBLUE}spotify:playlist:1MTqVV0leA3p7VSNaqrOOg{color.END}")
  wait(3)
  clear()
  return