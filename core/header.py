import random
import mycolor

def main_header():

    header_1 = mycolor.color.cyan + """
                             _________-----_____ 
              _____------                __        ------_ 
   ___----                 ___------                       \ 
       ----________          ----                           \ 
                        -----__    |                     _____ ) 
                               __-                        /#####\ 
              _______-----    ___--                 \####/)\ 
      ------_______      ---____                     \##/  / 
                        -----__    \ --      _             --   /\   
                                 --__--__     \_____/        \_/\ 
                                          ----|       /              | 
                                                |     |___________| 
                                                 |  |   |  | ((_(_)| )_) 
                                                 |     |  \_((_(_)|/(_) 
                                                   \                   ( 
                                                     \___________) 
                                                          /
   | Version                : 0.5                        /
   | Auth                   : kkk                     /
   | Codename              : X-Frame                /
   | Follow me on Github  : @j3ers3              /
   ------------------------------------------------""" + mycolor.color.end

    header_2 = mycolor.color.green + r"""
                        |\                    
                        | \      
      ()######## |   ========================================================> 
                        | /       
                        |/        
      M		    X Framework   	                 M
      M						                        M
      M						                        M
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      MMMMMMMMMMMMMM			 MMMMMMMMMMMMMM
      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""" + mycolor.color.end

    header_3 = mycolor.color.purple + r"""
      ooooooooooooooooooooooooooooooooooooooooooooooooo
      VVVV##					 ##VVVV
       V	|\\\\"		        |\\\\'       V
                |___|                   |____|
	
			____________
			    |  |
			    |  |
			    UUUU
          ;					  ;  
	   ' \_________________________________'//
	     ; 0000000000000000000000000000000;
	       . \\000000000000000000000000//
	         ------------------------""" + mycolor.color.end
    


    header_4 = mycolor.color.darkcyan + """
                               ,;        ,;                            
         .               f#i       f#i .    .      t                  
        Ef.           .E#t      .E#t  Di   Dt     Ej              
        E#Wi         i#W,      i#W,   E#i  E#i    E#, t      .DD. 
        E#K#D:      L#D.      L#D.    E#t  E#t    E#t EK:   ,WK. L
        E#t,E#f.  :K#Wfff;  :K#Wfff;  E#t  E#t    E#t E#t  i#D :K
        E#WEE##Wt i##WLLLLt i##WLLLLt E########f. E#t E#t j#f  
        E##Ei;;;;. .E#L      .E#L     E#j..K#j... E#t E#tL#i    
        E#DWWt       f#E:      f#E:   E#t  E#t    E#t E#WW,       
        E#t f#K;      ,WW;      ,WW;  E#t  E#t    E#t E#K:    ee;.     
        E#Dfff##E,     .D#;      .D#; f#t  f#t    E#t ED.           
        jLLLLLLLLL;      tt        tt  ii   ii    E#t t               
	
    	""" + mycolor.color.end	

    header_5 = mycolor.color.blue + r"""
	 __________________________
        < whoami >
         --------------------------
                \   ^__^			---
                 \  (00)\_______		 |  \
                    (__)\       )\/\/		| o \
                        ||----w |		 |    \
                        ||        ||		 |-----\
						--      --      --        --
	---------E@###------------%%%###--------|

	E%###$%%%%%%$$##$%%^^^$$$$$$%#$ETTTE##33
	---------------------------------------||||
     """ + mycolor.color.end


    logo = [header_1,header_2,header_3,header_4,header_5]
    banner = random.choice(logo)
    print banner

