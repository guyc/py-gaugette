# coding=utf-8
# Module stencil_24
# generated from Stencil 18pt

name        = "Stencil 24"
start_char  = '!'
end_char    = chr(127)
char_height = 24
space_width = 12
gap_width   = 3

bitmaps = (
    # @0 '!' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x70, #  OOO 
    0xF8, # OOOOO
    0xF8, # OOOOO
    0xF8, # OOOOO
    0xF8, # OOOOO
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x30, #   OO 
    0x20, #   O  
    0x20, #   O  
    0x70, #  OOO 
    0xF8, # OOOOO
    0xF8, # OOOOO
    0xF8, # OOOOO
    0x70, #  OOO 
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      

    # @24 '"' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0xEF, # OOO OOOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0xE6, # OOO  OO 
    0x66, #  OO  OO 
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         

    # @48 '#' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x06, 0x30, #      OO   OO  
    0x06, 0x30, #      OO   OO  
    0x06, 0x30, #      OO   OO  
    0x0E, 0x70, #     OOO  OOO  
    0x3F, 0x7C, #   OOOOOO OOOOO
    0x7F, 0x7C, #  OOOOOOO OOOOO
    0x0C, 0x60, #     OO   OO   
    0x0C, 0x60, #     OO   OO   
    0x18, 0xC0, #    OO   OO    
    0x18, 0xC0, #    OO   OO    
    0xFE, 0xF8, # OOOOOOO OOOOO 
    0xFE, 0xF0, # OOOOOOO OOOO  
    0x39, 0x80, #   OOO  OO     
    0x31, 0x80, #   OO   OO     
    0x31, 0x80, #   OO   OO     
    0x31, 0x80, #   OO   OO     
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @96 '$' (11 pixels wide)
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x04, 0x00, #      O     
    0x04, 0x00, #      O     
    0x0F, 0x00, #     OOOO   
    0x3D, 0x80, #   OOOO OO  
    0x35, 0xC0, #   OO O OOO 
    0x75, 0xC0, #  OOO O OOO 
    0x79, 0xC0, #  OOOO  OOO 
    0x7E, 0x00, #  OOOOOO    
    0x7F, 0x80, #  OOOOOOOO  
    0x3F, 0xC0, #   OOOOOOOO 
    0x3F, 0xC0, #   OOOOOOOO 
    0x0F, 0xE0, #     OOOOOOO
    0x63, 0xE0, #  OO   OOOOO
    0xF5, 0xE0, # OOOO O OOOO
    0xF4, 0xE0, # OOOO O  OOO
    0xE4, 0xC0, # OOO  O  OO 
    0x75, 0xC0, #  OOO O OOO 
    0x1F, 0x00, #    OOOOO   
    0x04, 0x00, #      O     
    0x04, 0x00, #      O     
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @144 '%' (17 pixels wide)
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x36, 0x08, 0x00, #   OO OO     O    
    0x63, 0x18, 0x00, #  OO   OO   OO    
    0xE3, 0x90, 0x00, # OOO   OOO  O     
    0xE3, 0xB0, 0x00, # OOO   OOO OO     
    0xE3, 0xA0, 0x00, # OOO   OOO O      
    0x63, 0x60, 0x00, #  OO   OO OO      
    0x36, 0x40, 0x00, #   OO OO  O       
    0x00, 0xC0, 0x00, #         OO       
    0x00, 0x80, 0x00, #         O        
    0x01, 0x9E, 0x00, #        OO  OOOO  
    0x01, 0x33, 0x00, #        O  OO  OO 
    0x03, 0x73, 0x80, #       OO OOO  OOO
    0x02, 0x73, 0x80, #       O  OOO  OOO
    0x06, 0x73, 0x80, #      OO  OOO  OOO
    0x04, 0x33, 0x00, #      O    OO  OO 
    0x0C, 0x1E, 0x00, #     OO     OOOO  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  

    # @216 '&' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x07, 0xA0, #      OOOO O    
    0x0F, 0x10, #     OOOO   O   
    0x1F, 0x10, #    OOOOO   O   
    0x1F, 0x10, #    OOOOO   O   
    0x1F, 0xA0, #    OOOOOO O    
    0x1F, 0x80, #    OOOOOO      
    0x0F, 0xCC, #     OOOOOO  OO 
    0x3F, 0xCC, #   OOOOOOOO  OO 
    0x77, 0xEC, #  OOO OOOOOO OO 
    0x77, 0xE8, #  OOO OOOOOO O  
    0xFB, 0xF0, # OOOOO OOOOOO   
    0xF9, 0xF8, # OOOOO  OOOOOO  
    0xFD, 0xF8, # OOOOOO OOOOOO  
    0x7C, 0xFC, #  OOOOO  OOOOOO 
    0x7E, 0xFC, #  OOOOOO OOOOOO 
    0x1F, 0x7E, #    OOOOO OOOOOO
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @264 ''' (3 pixels wide)
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0x60, #  OO
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    

    # @288 '(' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x0C, #     OO
    0x1C, #    OOO
    0x1C, #    OOO
    0x38, #   OOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0xF8, # OOOOO 
    0xF8, # OOOOO 
    0xF8, # OOOOO 
    0xF8, # OOOOO 
    0xF8, # OOOOO 
    0xF8, # OOOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x38, #   OOO 
    0x1C, #    OOO
    0x1C, #    OOO
    0x0C, #     OO

    # @312 ')' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0xC0, # OO    
    0xE0, # OOO   
    0xE0, # OOO   
    0x70, #  OOO  
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x7C, #  OOOOO
    0x7C, #  OOOOO
    0x7C, #  OOOOO
    0x7C, #  OOOOO
    0x7C, #  OOOOO
    0x7C, #  OOOOO
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x70, #  OOO  
    0xE0, # OOO   
    0xE0, # OOO   
    0xC0, # OO    

    # @336 '*' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x1E, 0x00, #    OOOO  
    0x5F, 0x80, #  O OOOOOO
    0xEF, 0x80, # OOO OOOOO
    0xFB, 0x80, # OOOOO OOO
    0x0C, 0x00, #     OO   
    0x37, 0x00, #   OO OOO 
    0x77, 0x00, #  OOO OOO 
    0x36, 0x00, #   OO OO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @384 '+' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x07, 0x00, #      OOO    
    0x07, 0x00, #      OOO    
    0x07, 0x00, #      OOO    
    0x07, 0x00, #      OOO    
    0x07, 0x00, #      OOO    
    0xFF, 0xF0, # OOOOOOOOOOOO
    0xFF, 0xF0, # OOOOOOOOOOOO
    0xFF, 0xF0, # OOOOOOOOOOOO
    0x07, 0x00, #      OOO    
    0x07, 0x00, #      OOO    
    0x07, 0x00, #      OOO    
    0x07, 0x00, #      OOO    
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @432 ',' (4 pixels wide)
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x60, #  OO 
    0xF0, # OOOO
    0xF0, # OOOO
    0xF0, # OOOO
    0x70, #  OOO
    0x20, #   O 
    0x60, #  OO 
    0xC0, # OO  

    # @456 '-' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0xFC, # OOOOOO
    0xFC, # OOOOOO
    0xFC, # OOOOOO
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @480 '.' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x70, #  OOO 
    0xF8, # OOOOO
    0xF8, # OOOOO
    0xF8, # OOOOO
    0x70, #  OOO 
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      

    # @504 '/' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x01, 0xC0, #        OOO
    0x01, 0xC0, #        OOO
    0x03, 0x80, #       OOO 
    0x03, 0x80, #       OOO 
    0x03, 0x80, #       OOO 
    0x07, 0x00, #      OOO  
    0x07, 0x00, #      OOO  
    0x06, 0x00, #      OO   
    0x0E, 0x00, #     OOO   
    0x0E, 0x00, #     OOO   
    0x0C, 0x00, #     OO    
    0x1C, 0x00, #    OOO    
    0x1C, 0x00, #    OOO    
    0x38, 0x00, #   OOO     
    0x38, 0x00, #   OOO     
    0x38, 0x00, #   OOO     
    0x70, 0x00, #  OOO      
    0x70, 0x00, #  OOO      
    0xF0, 0x00, # OOOO      
    0x00, 0x00, #           

    # @552 '0' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x1B, 0x00, #    OO OO    
    0x39, 0xC0, #   OOO  OOO  
    0x79, 0xC0, #  OOOO  OOO  
    0x79, 0xE0, #  OOOO  OOOO 
    0xF9, 0xE0, # OOOOO  OOOO 
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xE0, # OOOOO  OOOO 
    0x79, 0xE0, #  OOOO  OOOO 
    0x79, 0xC0, #  OOOO  OOO  
    0x39, 0xC0, #   OOO  OOO  
    0x1B, 0x00, #    OO OO    
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @600 '1' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0xF8, # OOOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0x78, #  OOOO 
    0xFC, # OOOOOO
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @624 '2' (11 pixels wide)
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x37, 0x00, #   OO OOO   
    0x63, 0xC0, #  OO   OOOO 
    0xF3, 0xE0, # OOOO  OOOOO
    0xFB, 0xE0, # OOOOO OOOOO
    0xFB, 0xE0, # OOOOO OOOOO
    0x73, 0xE0, #  OOO  OOOOO
    0x03, 0xE0, #       OOOOO
    0x07, 0xC0, #      OOOOO 
    0x0F, 0x80, #     OOOOO  
    0x1C, 0x00, #    OOO     
    0x30, 0x00, #   OO       
    0x40, 0x20, #  O        O
    0x3F, 0xE0, #   OOOOOOOOO
    0x7F, 0xE0, #  OOOOOOOOOO
    0xFF, 0xC0, # OOOOOOOOOO 
    0x8F, 0x80, # O   OOOOO  
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @672 '3' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x33, 0x80, #   OO  OOO   
    0x61, 0xC0, #  OO    OOO  
    0xF1, 0xE0, # OOOO   OOOO 
    0xF1, 0xE0, # OOOO   OOOO 
    0xF1, 0xE0, # OOOO   OOOO 
    0x61, 0xE0, #  OO    OOOO 
    0x01, 0xC0, #        OOO  
    0x07, 0x80, #      OOOO   
    0x01, 0xC0, #        OOO  
    0x01, 0xE0, #        OOOO 
    0x61, 0xF0, #  OO    OOOOO
    0xF1, 0xF0, # OOOO   OOOOO
    0xF1, 0xF0, # OOOO   OOOOO
    0xF1, 0xF0, # OOOO   OOOOO
    0x61, 0xE0, #  OO    OOOO 
    0x33, 0x80, #   OO  OOO   
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @720 '4' (11 pixels wide)
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x01, 0x80, #        OO  
    0x03, 0x80, #       OOO  
    0x07, 0x80, #      OOOO  
    0x07, 0x80, #      OOOO  
    0x07, 0x80, #      OOOO  
    0x0F, 0x80, #     OOOOO  
    0x1F, 0x80, #    OOOOOO  
    0x37, 0x80, #   OO OOOO  
    0x27, 0x80, #   O  OOOO  
    0x47, 0x80, #  O   OOOO  
    0xC7, 0x80, # OO   OOOO  
    0xFF, 0xE0, # OOOOOOOOOOO
    0x07, 0x80, #      OOOO  
    0x07, 0x80, #      OOOO  
    0x07, 0x80, #      OOOO  
    0x0F, 0xC0, #     OOOOOO 
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @768 '5' (11 pixels wide)
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x7F, 0xC0, #  OOOOOOOOO 
    0x7F, 0x80, #  OOOOOOOO  
    0xFF, 0x00, # OOOOOOOO   
    0xFE, 0x00, # OOOOOOO    
    0x80, 0x00, # O          
    0xC0, 0x00, # OO         
    0xF7, 0x80, # OOOO OOOO  
    0xF7, 0xC0, # OOOO OOOOO 
    0xC3, 0xE0, # OO    OOOOO
    0x03, 0xE0, #       OOOOO
    0x63, 0xE0, #  OO   OOOOO
    0xF3, 0xE0, # OOOO  OOOOO
    0xF3, 0xE0, # OOOO  OOOOO
    0xF3, 0xC0, # OOOO  OOOO 
    0x63, 0x80, #  OO   OOO  
    0x37, 0x00, #   OO OOO   
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @816 '6' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x0D, 0xC0, #     OO OOO  
    0x38, 0x60, #   OOO    OO 
    0x38, 0xF0, #   OOO   OOOO
    0x79, 0xF0, #  OOOO  OOOOO
    0x78, 0xE0, #  OOOO   OOO 
    0xF8, 0x00, # OOOOO       
    0xF9, 0xC0, # OOOOO  OOO  
    0xFB, 0xE0, # OOOOO OOOOO 
    0xFD, 0xF0, # OOOOOO OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0x79, 0xF0, #  OOOO  OOOOO
    0x79, 0xF0, #  OOOO  OOOOO
    0x79, 0xE0, #  OOOO  OOOO 
    0x39, 0xE0, #   OOO  OOOO 
    0x0D, 0x80, #     OO OO   
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @864 '7' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xBE, 0x40, # O OOOOO  O
    0xFF, 0xC0, # OOOOOOOOOO
    0xFF, 0x80, # OOOOOOOOO 
    0xFF, 0x00, # OOOOOOOO  
    0x80, 0x00, # O         
    0x03, 0x00, #       OO  
    0x03, 0x00, #       OO  
    0x06, 0x00, #      OO   
    0x0E, 0x00, #     OOO   
    0x1E, 0x00, #    OOOO   
    0x1E, 0x00, #    OOOO   
    0x3E, 0x00, #   OOOOO   
    0x3E, 0x00, #   OOOOO   
    0x3E, 0x00, #   OOOOO   
    0x3E, 0x00, #   OOOOO   
    0x1C, 0x00, #    OOO    
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @912 '8' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x3B, 0x80, #   OOO OOO   
    0x79, 0xC0, #  OOOO  OOO  
    0xF9, 0xE0, # OOOOO  OOOO 
    0xF9, 0xE0, # OOOOO  OOOO 
    0xF9, 0xE0, # OOOOO  OOOO 
    0xF9, 0xE0, # OOOOO  OOOO 
    0x79, 0xC0, #  OOOO  OOO  
    0x1B, 0x00, #    OO OO    
    0x3B, 0xC0, #   OOO OOOO  
    0x79, 0xE0, #  OOOO  OOOO 
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0x79, 0xE0, #  OOOO  OOOO 
    0x3F, 0xC0, #   OOOOOOOO  
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @960 '9' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x3B, 0x00, #   OOO OO    
    0x79, 0xC0, #  OOOO  OOO  
    0x79, 0xE0, #  OOOO  OOOO 
    0xF9, 0xE0, # OOOOO  OOOO 
    0xF9, 0xE0, # OOOOO  OOOO 
    0xF9, 0xF0, # OOOOO  OOOOO
    0xF9, 0xF0, # OOOOO  OOOOO
    0x7D, 0xF0, #  OOOOO OOOOO
    0x3D, 0xF0, #   OOOO OOOOO
    0x01, 0xF0, #        OOOOO
    0x71, 0xF0, #  OOO   OOOOO
    0xF9, 0xE0, # OOOOO  OOOO 
    0xF9, 0xE0, # OOOOO  OOOO 
    0xF1, 0xE0, # OOOO   OOOO 
    0x71, 0xC0, #  OOO   OOO  
    0x3B, 0x00, #   OOO OO    
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1008 ':' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x70, #  OOO 
    0xF8, # OOOOO
    0xF8, # OOOOO
    0xF8, # OOOOO
    0x70, #  OOO 
    0x00, #      
    0x00, #      
    0x70, #  OOO 
    0xF8, # OOOOO
    0xF8, # OOOOO
    0xF8, # OOOOO
    0x70, #  OOO 
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      

    # @1032 ';' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x70, #  OOO 
    0xF8, # OOOOO
    0xF8, # OOOOO
    0xF8, # OOOOO
    0x70, #  OOO 
    0x00, #      
    0x00, #      
    0x00, #      
    0x60, #  OO  
    0xF0, # OOOO 
    0xF0, # OOOO 
    0xF0, # OOOO 
    0x70, #  OOO 
    0x20, #   O  
    0x60, #  OO  
    0xC0, # OO   

    # @1056 '<' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x40, #          O
    0x01, 0xC0, #        OOO
    0x07, 0x00, #      OOO  
    0x0C, 0x00, #     OO    
    0x38, 0x00, #   OOO     
    0xF8, 0x00, # OOOOO     
    0xFE, 0x00, # OOOOOOO   
    0x3F, 0x00, #   OOOOOO  
    0x1F, 0xC0, #    OOOOOOO
    0x07, 0xC0, #      OOOOO
    0x03, 0xC0, #       OOOO
    0x00, 0xC0, #         OO
    0x00, 0x40, #          O
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1104 '=' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFF, 0xF0, # OOOOOOOOOOOO
    0xFF, 0xF0, # OOOOOOOOOOOO
    0xFF, 0xF0, # OOOOOOOOOOOO
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFF, 0xF0, # OOOOOOOOOOOO
    0xFF, 0xF0, # OOOOOOOOOOOO
    0xFF, 0xF0, # OOOOOOOOOOOO
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1152 '>' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x80, 0x00, # O         
    0xE0, 0x00, # OOO       
    0xF0, 0x00, # OOOO      
    0xFC, 0x00, # OOOOOO    
    0x7E, 0x00, #  OOOOOO   
    0x3F, 0x80, #   OOOOOOO 
    0x0F, 0xC0, #     OOOOOO
    0x07, 0x80, #      OOOO 
    0x06, 0x00, #      OO   
    0x1C, 0x00, #    OOO    
    0x30, 0x00, #   OO      
    0xE0, 0x00, # OOO       
    0x80, 0x00, # O         
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1200 '?' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x76, 0x00, #  OOO OO  
    0xF7, 0x00, # OOOO OOO 
    0xF7, 0x80, # OOOO OOOO
    0x67, 0x80, #  OO  OOOO
    0x07, 0x80, #      OOOO
    0x1F, 0x80, #    OOOOOO
    0x3F, 0x80, #   OOOOOOO
    0x3F, 0x00, #   OOOOOO 
    0x3E, 0x00, #   OOOOO  
    0x30, 0x00, #   OO     
    0x20, 0x00, #   O      
    0x38, 0x00, #   OOO    
    0x7C, 0x00, #  OOOOO   
    0x7C, 0x00, #  OOOOO   
    0x7C, 0x00, #  OOOOO   
    0x38, 0x00, #   OOO    
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1248 '@' (16 pixels wide)
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x07, 0xE0, #      OOOOOO     
    0x1C, 0x18, #    OOO     OO   
    0x30, 0x04, #   OO         O  
    0x60, 0x02, #  OO           O 
    0x41, 0xB9, #  O     OO OOO  O
    0xC3, 0x31, # OO    OO  OO   O
    0x83, 0x31, # O     OO  OO   O
    0x87, 0x71, # O    OOO OOO   O
    0x87, 0x71, # O    OOO OOO   O
    0x87, 0x72, # O    OOO OOO  O 
    0x87, 0x76, # O    OOO OOO OO 
    0x43, 0x7C, #  O    OO OOOOO  
    0x60, 0x00, #  OO             
    0x30, 0x00, #   OO            
    0x18, 0x08, #    OO       O   
    0x07, 0xFC, #      OOOOOOOOO  
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 

    # @1296 'A' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x03, 0xE0, #       OOOOO    
    0x07, 0xE0, #      OOOOOO    
    0x03, 0xE0, #       OOOOO    
    0x0B, 0xE0, #     O OOOOO    
    0x0B, 0xE0, #     O OOOOO    
    0x0B, 0xF0, #     O OOOOOO   
    0x09, 0xF0, #     O  OOOOO   
    0x09, 0xF0, #     O  OOOOO   
    0x11, 0xF0, #    O   OOOOO   
    0x11, 0xF8, #    O   OOOOOO  
    0x11, 0xF8, #    O   OOOOOO  
    0x17, 0xF8, #    O OOOOOOOO  
    0x20, 0xF8, #   O     OOOOO  
    0x20, 0xFC, #   O     OOOOOO 
    0x70, 0xFC, #  OOO    OOOOOO 
    0xF9, 0xFE, # OOOOO  OOOOOOOO
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @1344 'B' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFD, 0xF0, # OOOOOO OOOOO  
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7D, 0xE0, #  OOOOO OOOO   
    0x7C, 0xF0, #  OOOOO  OOOO  
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0xFD, 0xF0, # OOOOOO OOOOO  
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @1392 'C' (13 pixels wide)
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x06, 0xF8, #      OO OOOOO
    0x1C, 0x78, #    OOO   OOOO
    0x3C, 0x38, #   OOOO    OOO
    0x7C, 0x18, #  OOOOO     OO
    0x7C, 0x18, #  OOOOO     OO
    0xFC, 0x08, # OOOOOO      O
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x08, # OOOOOO      O
    0x7C, 0x18, #  OOOOO     OO
    0x7C, 0x10, #  OOOOO     O 
    0x3C, 0x70, #   OOOO   OOO 
    0x0E, 0xE0, #     OOO OOO  
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @1440 'D' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFC, 0xC0, # OOOOOO  OO    
    0x7C, 0xF0, #  OOOOO  OOOO  
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x70, #  OOOOO   OOO  
    0x7C, 0xF0, #  OOOOO  OOOO  
    0xFC, 0xC0, # OOOOOO  OO    
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @1488 'E' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFD, 0xF0, # OOOOOO OOOOO
    0x7C, 0xF0, #  OOOOO  OOOO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x50, #  OOOOO   O O
    0x7C, 0xC0, #  OOOOO  OO  
    0x7C, 0xC0, #  OOOOO  OO  
    0x7D, 0xC0, #  OOOOO OOO  
    0x7D, 0xC0, #  OOOOO OOO  
    0x7C, 0xC0, #  OOOOO  OO  
    0x7C, 0x40, #  OOOOO   O  
    0x7C, 0x10, #  OOOOO     O
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0xF0, #  OOOOO  OOOO
    0xFD, 0xF0, # OOOOOO OOOOO
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1536 'F' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFD, 0xF0, # OOOOOO OOOOO
    0x7C, 0xF0, #  OOOOO  OOOO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x50, #  OOOOO   O O
    0x7C, 0xC0, #  OOOOO  OO  
    0x7C, 0xC0, #  OOOOO  OO  
    0x7D, 0xC0, #  OOOOO OOO  
    0x7D, 0xC0, #  OOOOO OOO  
    0x7C, 0xC0, #  OOOOO  OO  
    0x7C, 0x40, #  OOOOO   O  
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0xFE, 0x00, # OOOOOOO     
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1584 'G' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x0E, 0xE4, #     OOO OOO  O
    0x1C, 0x3C, #    OOO    OOOO
    0x3C, 0x1C, #   OOOO     OOO
    0x7C, 0x0C, #  OOOOO      OO
    0x7C, 0x0C, #  OOOOO      OO
    0xFC, 0x04, # OOOOOO       O
    0xFC, 0x00, # OOOOOO        
    0xFC, 0x00, # OOOOOO        
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0x78, # OOOOOO   OOOO 
    0xFC, 0x78, # OOOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x3C, 0x78, #   OOOO   OOOO 
    0x1C, 0x78, #    OOO   OOOO 
    0x0E, 0xE0, #     OOO OOO   
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @1632 'H' (16 pixels wide)
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0xFE, 0x7F, # OOOOOOO  OOOOOOO
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0xFE, #  OOOOO  OOOOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0xFE, 0x7F, # OOOOOOO  OOOOOOO
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 

    # @1680 'I' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0xFE, # OOOOOOO
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0xFE, # OOOOOOO
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @1704 'J' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x07, 0xF0, #      OOOOOOO
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x73, 0xE0, #  OOO  OOOOO 
    0xFB, 0xE0, # OOOOO OOOOO 
    0xFB, 0xE0, # OOOOO OOOOO 
    0xFB, 0xE0, # OOOOO OOOOO 
    0x63, 0xC0, #  OO   OOOO  
    0x37, 0x80, #   OO OOOO   
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1752 'K' (16 pixels wide)
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0xFE, 0x7E, # OOOOOOO  OOOOOO 
    0x7C, 0x3C, #  OOOOO    OOOO  
    0x7C, 0x18, #  OOOOO     OO   
    0x7C, 0x10, #  OOOOO     O    
    0x7C, 0x20, #  OOOOO    O     
    0x7C, 0x70, #  OOOOO   OOO    
    0x7C, 0xF0, #  OOOOO  OOOO    
    0x7D, 0xF0, #  OOOOO OOOOO    
    0x7D, 0xF8, #  OOOOO OOOOOO   
    0x7D, 0xF8, #  OOOOO OOOOOO   
    0x7C, 0xFC, #  OOOOO  OOOOOO  
    0x7C, 0xFC, #  OOOOO  OOOOOO  
    0x7C, 0xFC, #  OOOOO  OOOOOO  
    0x7C, 0x7E, #  OOOOO   OOOOOO 
    0x7C, 0x7E, #  OOOOO   OOOOOO 
    0xFE, 0xFF, # OOOOOOO OOOOOOOO
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 

    # @1800 'L' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFE, 0x00, # OOOOOOO     
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x10, #  OOOOO     O
    0x7C, 0x10, #  OOOOO     O
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0xF0, #  OOOOO  OOOO
    0xFC, 0xF0, # OOOOOO  OOOO
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1848 'M' (18 pixels wide)
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0xFE, 0x0F, 0xC0, # OOOOOOO     OOOOOO
    0x7E, 0x0F, 0x80, #  OOOOOO     OOOOO 
    0x3F, 0x0F, 0x80, #   OOOOOO    OOOOO 
    0x3F, 0x4F, 0x80, #   OOOOOO O  OOOOO 
    0x1F, 0x4F, 0x80, #    OOOOO O  OOOOO 
    0x1F, 0xCF, 0x80, #    OOOOOOO  OOOOO 
    0x1F, 0xCF, 0x80, #    OOOOOOO  OOOOO 
    0x1F, 0xCF, 0x80, #    OOOOOOO  OOOOO 
    0x1F, 0x8F, 0x80, #    OOOOOO   OOOOO 
    0x1F, 0x8F, 0x80, #    OOOOOO   OOOOO 
    0x17, 0x8F, 0x80, #    O OOOO   OOOOO 
    0x17, 0x8F, 0x80, #    O OOOO   OOOOO 
    0x17, 0x0F, 0x80, #    O OOO    OOOOO 
    0x13, 0x0F, 0x80, #    O  OO    OOOOO 
    0x3B, 0x0F, 0x80, #   OOO OO    OOOOO 
    0x7E, 0x1F, 0xC0, #  OOOOOO    OOOOOOO
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   

    # @1920 'N' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0xFE, 0x3E, # OOOOOOO   OOOOO
    0x7F, 0x1C, #  OOOOOOO   OOO 
    0x3F, 0x08, #   OOOOOO    O  
    0x3F, 0x88, #   OOOOOOO   O  
    0x5F, 0x88, #  O OOOOOO   O  
    0x2F, 0xC8, #   O OOOOOO  O  
    0x2F, 0xE8, #   O OOOOOOO O  
    0x27, 0xE8, #   O  OOOOOO O  
    0x27, 0xF8, #   O  OOOOOOOO  
    0x23, 0xF0, #   O   OOOOOO   
    0x21, 0xF8, #   O    OOOOOO  
    0x21, 0xF8, #   O    OOOOOO  
    0x20, 0xF8, #   O     OOOOO  
    0x20, 0xF8, #   O     OOOOO  
    0x70, 0x78, #  OOO     OOOO  
    0xF8, 0x38, # OOOOO     OOO  
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @1968 'O' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x0E, 0xE0, #     OOO OOO    
    0x1C, 0x70, #    OOO   OOO   
    0x3C, 0x78, #   OOOO   OOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO 
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO 
    0x3C, 0x78, #   OOOO   OOOO  
    0x1C, 0x70, #    OOO   OOO   
    0x0E, 0xE0, #     OOO OOO    
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @2016 'P' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFC, 0xE0, # OOOOOO  OOO   
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7D, 0xF0, #  OOOOO OOOOO  
    0x7D, 0xC0, #  OOOOO OOO    
    0x7C, 0x00, #  OOOOO        
    0x7C, 0x00, #  OOOOO        
    0x7C, 0x00, #  OOOOO        
    0x7C, 0x00, #  OOOOO        
    0x7C, 0x00, #  OOOOO        
    0xFE, 0x00, # OOOOOOO       
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2064 'Q' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x1D, 0xC0, #    OOO OOO    
    0x3C, 0xE0, #   OOOO  OOO   
    0x7C, 0xF0, #  OOOOO  OOOO  
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0xFC, 0xF8, # OOOOOO  OOOOO 
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xF8, # OOOOOO  OOOOO 
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0x7F, 0xF0, #  OOOOOOOOOOO  
    0x3D, 0xE0, #   OOOO OOOO   
    0x1D, 0xFC, #    OOO OOOOOOO
    0x00, 0x78, #          OOOO 
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2112 'R' (16 pixels wide)
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0xFC, 0xF0, # OOOOOO  OOOO    
    0x7C, 0xF8, #  OOOOO  OOOOO   
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x78, #  OOOOO   OOOO   
    0x7C, 0xF0, #  OOOOO  OOOO    
    0x7D, 0xF0, #  OOOOO OOOOO    
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7F, #  OOOOO   OOOOOOO
    0x7C, 0x7F, #  OOOOO   OOOOOOO
    0xFE, 0x3C, # OOOOOOO   OOOO  
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 

    # @2160 'S' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x3B, 0xE0, #   OOO OOOOO 
    0x71, 0xE0, #  OOO   OOOO 
    0x70, 0x60, #  OOO     OO 
    0xF0, 0x60, # OOOO     OO 
    0xF8, 0x20, # OOOOO     O 
    0xFF, 0x00, # OOOOOOOO    
    0xFF, 0xC0, # OOOOOOOOOO  
    0x7F, 0xE0, #  OOOOOOOOOO 
    0x7F, 0xE0, #  OOOOOOOOOO 
    0x1F, 0xF0, #    OOOOOOOOO
    0x87, 0xF0, # O    OOOOOOO
    0xC1, 0xF0, # OO     OOOOO
    0xC0, 0xF0, # OO      OOOO
    0xE0, 0xE0, # OOO     OOO 
    0xF1, 0xE0, # OOOO   OOOO 
    0x9B, 0x80, # O  OO OOO   
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @2208 'T' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xE7, 0xDC, # OOO  OOOOO OOO
    0xE7, 0xDC, # OOO  OOOOO OOO
    0xC7, 0xCC, # OO   OOOOO  OO
    0xC7, 0xCC, # OO   OOOOO  OO
    0x87, 0xC4, # O    OOOOO   O
    0x87, 0xC4, # O    OOOOO   O
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x0F, 0xE0, #     OOOOOOO   
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2256 'U' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0xFE, 0x3E, # OOOOOOO   OOOOO
    0x7C, 0x1C, #  OOOOO     OOO 
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x18, #  OOOOO     OO  
    0x3E, 0x30, #   OOOOO   OO   
    0x1E, 0x60, #    OOOO  OO    
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @2304 'V' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFF, 0x3C, # OOOOOOOO  OOOO
    0x7E, 0x18, #  OOOOOO    OO 
    0x7E, 0x10, #  OOOOOO    O  
    0x3E, 0x10, #   OOOOO    O  
    0x3F, 0x30, #   OOOOOO  OO  
    0x3F, 0x20, #   OOOOOO  O   
    0x1F, 0x20, #    OOOOO  O   
    0x1F, 0x20, #    OOOOO  O   
    0x1F, 0xA0, #    OOOOOO O   
    0x1F, 0xC0, #    OOOOOOO    
    0x0F, 0x80, #     OOOOO     
    0x0F, 0xC0, #     OOOOOO    
    0x0F, 0xC0, #     OOOOOO    
    0x07, 0x80, #      OOOO     
    0x07, 0x80, #      OOOO     
    0x07, 0x80, #      OOOO     
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2352 'W' (19 pixels wide)
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0xFF, 0x39, 0xE0, # OOOOOOOO  OOO  OOOO
    0x7E, 0x38, 0xC0, #  OOOOOO   OOO   OO 
    0x7E, 0x38, 0x80, #  OOOOOO   OOO   O  
    0x3E, 0x7C, 0x80, #   OOOOO  OOOOO  O  
    0x3F, 0x7C, 0x80, #   OOOOOO OOOOO  O  
    0x3F, 0x7D, 0x80, #   OOOOOO OOOOO OO  
    0x3F, 0x7D, 0x00, #   OOOOOO OOOOO O   
    0x1F, 0x7F, 0x00, #    OOOOO OOOOOOO   
    0x1F, 0xBF, 0x00, #    OOOOOO OOOOOO   
    0x1F, 0xBE, 0x00, #    OOOOOO OOOOO    
    0x0F, 0xBE, 0x00, #     OOOOO OOOOO    
    0x0F, 0xBE, 0x00, #     OOOOO OOOOO    
    0x0F, 0x9E, 0x00, #     OOOOO  OOOO    
    0x0F, 0x1E, 0x00, #     OOOO   OOOO    
    0x07, 0x1E, 0x00, #      OOO   OOOO    
    0x07, 0x1C, 0x00, #      OOO   OOO     
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    

    # @2424 'X' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFF, 0x7C, # OOOOOOOO OOOOO
    0x7E, 0x38, #  OOOOOO   OOO 
    0x7E, 0x30, #  OOOOOO   OO  
    0x3F, 0x60, #   OOOOOO OO   
    0x3F, 0x40, #   OOOOOO O    
    0x1F, 0x80, #    OOOOOO     
    0x1F, 0x80, #    OOOOOO     
    0x0F, 0xC0, #     OOOOOO    
    0x0F, 0xC0, #     OOOOOO    
    0x07, 0xE0, #      OOOOOO   
    0x0F, 0xE0, #     OOOOOOO   
    0x0B, 0xF0, #     O OOOOOO  
    0x1B, 0xF0, #    OO OOOOOO  
    0x31, 0xF8, #   OO   OOOOOO 
    0x71, 0xF8, #  OOO   OOOOOO 
    0xF9, 0xFC, # OOOOO  OOOOOOO
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2472 'Y' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFE, 0x7C, # OOOOOOO  OOOOO
    0x7C, 0x38, #  OOOOO    OOO 
    0x7C, 0x10, #  OOOOO     O  
    0x3E, 0x10, #   OOOOO    O  
    0x3E, 0x20, #   OOOOO   O   
    0x3F, 0x20, #   OOOOOO  O   
    0x1F, 0x40, #    OOOOO O    
    0x1F, 0x80, #    OOOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x1F, 0xC0, #    OOOOOOO    
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2520 'Z' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x7D, 0xF0, #  OOOOO OOOOO
    0x7B, 0xF0, #  OOOO OOOOOO
    0x63, 0xE0, #  OO   OOOOO 
    0x67, 0xE0, #  OO  OOOOOO 
    0x47, 0xE0, #  O   OOOOOO 
    0x0F, 0xC0, #     OOOOOO  
    0x0F, 0xC0, #     OOOOOO  
    0x1F, 0x80, #    OOOOOO   
    0x1F, 0x80, #    OOOOOO   
    0x3F, 0x00, #   OOOOOO    
    0x3F, 0x00, #   OOOOOO    
    0x3E, 0x10, #   OOOOO    O
    0x7E, 0x30, #  OOOOOO   OO
    0x7C, 0x30, #  OOOOO    OO
    0xFC, 0xF0, # OOOOOO  OOOO
    0xFD, 0xF0, # OOOOOO OOOOO
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @2568 '[' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0xFC, # OOOOOO
    0xF8, # OOOOO 
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF0, # OOOO  
    0xF8, # OOOOO 
    0xFC, # OOOOOO
    0x00, #       

    # @2592 '\' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xE0, 0x00, # OOO       
    0xE0, 0x00, # OOO       
    0x70, 0x00, #  OOO      
    0x70, 0x00, #  OOO      
    0x70, 0x00, #  OOO      
    0x38, 0x00, #   OOO     
    0x38, 0x00, #   OOO     
    0x38, 0x00, #   OOO     
    0x1C, 0x00, #    OOO    
    0x1C, 0x00, #    OOO    
    0x0C, 0x00, #     OO    
    0x0E, 0x00, #     OOO   
    0x0E, 0x00, #     OOO   
    0x07, 0x00, #      OOO  
    0x07, 0x00, #      OOO  
    0x07, 0x00, #      OOO  
    0x03, 0x80, #       OOO 
    0x03, 0x80, #       OOO 
    0x03, 0xC0, #       OOOO
    0x00, 0x00, #           

    # @2640 ']' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0xFC, # OOOOOO
    0x7C, #  OOOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x3C, #   OOOO
    0x7C, #  OOOOO
    0xFC, # OOOOOO
    0x00, #       

    # @2664 '^' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x02, 0x00, #       O       
    0x06, 0x00, #      OO       
    0x07, 0x00, #      OOO      
    0x0F, 0x80, #     OOOOO     
    0x0F, 0xC0, #     OOOOOO    
    0x1B, 0xC0, #    OO OOOO    
    0x31, 0xE0, #   OO   OOOO   
    0x21, 0xF0, #   O    OOOOO  
    0x60, 0xF0, #  OO     OOOO  
    0xC0, 0x7C, # OO       OOOOO
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2712 '_' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFF, 0xF0, # OOOOOOOOOOOO
    0xFF, 0xF0, # OOOOOOOOOOOO

    # @2760 '`' (6 pixels wide)
    0xF0, # OOOO  
    0x38, #   OOO 
    0x1C, #    OOO
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @2784 'a' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x03, 0xE0, #       OOOOO    
    0x07, 0xE0, #      OOOOOO    
    0x03, 0xE0, #       OOOOO    
    0x0B, 0xE0, #     O OOOOO    
    0x0B, 0xE0, #     O OOOOO    
    0x0B, 0xF0, #     O OOOOOO   
    0x09, 0xF0, #     O  OOOOO   
    0x09, 0xF0, #     O  OOOOO   
    0x11, 0xF0, #    O   OOOOO   
    0x11, 0xF8, #    O   OOOOOO  
    0x11, 0xF8, #    O   OOOOOO  
    0x17, 0xF8, #    O OOOOOOOO  
    0x20, 0xF8, #   O     OOOOO  
    0x20, 0xFC, #   O     OOOOOO 
    0x70, 0xFC, #  OOO    OOOOOO 
    0xF9, 0xFE, # OOOOO  OOOOOOOO
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @2832 'b' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFD, 0xF0, # OOOOOO OOOOO  
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7D, 0xE0, #  OOOOO OOOO   
    0x7C, 0xF0, #  OOOOO  OOOO  
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0xFD, 0xF0, # OOOOOO OOOOO  
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2880 'c' (13 pixels wide)
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x06, 0xF8, #      OO OOOOO
    0x1C, 0x78, #    OOO   OOOO
    0x3C, 0x38, #   OOOO    OOO
    0x7C, 0x18, #  OOOOO     OO
    0x7C, 0x18, #  OOOOO     OO
    0xFC, 0x08, # OOOOOO      O
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x00, # OOOOOO       
    0xFC, 0x08, # OOOOOO      O
    0x7C, 0x18, #  OOOOO     OO
    0x7C, 0x10, #  OOOOO     O 
    0x3C, 0x70, #   OOOO   OOO 
    0x0E, 0xE0, #     OOO OOO  
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @2928 'd' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFC, 0xC0, # OOOOOO  OO    
    0x7C, 0xF0, #  OOOOO  OOOO  
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x70, #  OOOOO   OOO  
    0x7C, 0xF0, #  OOOOO  OOOO  
    0xFC, 0xC0, # OOOOOO  OO    
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2976 'e' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFD, 0xF0, # OOOOOO OOOOO
    0x7C, 0xF0, #  OOOOO  OOOO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x50, #  OOOOO   O O
    0x7C, 0xC0, #  OOOOO  OO  
    0x7C, 0xC0, #  OOOOO  OO  
    0x7D, 0xC0, #  OOOOO OOO  
    0x7D, 0xC0, #  OOOOO OOO  
    0x7C, 0xC0, #  OOOOO  OO  
    0x7C, 0x40, #  OOOOO   O  
    0x7C, 0x10, #  OOOOO     O
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0xF0, #  OOOOO  OOOO
    0xFD, 0xF0, # OOOOOO OOOOO
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @3024 'f' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFD, 0xF0, # OOOOOO OOOOO
    0x7C, 0xF0, #  OOOOO  OOOO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x50, #  OOOOO   O O
    0x7C, 0xC0, #  OOOOO  OO  
    0x7C, 0xC0, #  OOOOO  OO  
    0x7D, 0xC0, #  OOOOO OOO  
    0x7D, 0xC0, #  OOOOO OOO  
    0x7C, 0xC0, #  OOOOO  OO  
    0x7C, 0x40, #  OOOOO   O  
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0xFE, 0x00, # OOOOOOO     
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @3072 'g' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x0E, 0xE4, #     OOO OOO  O
    0x1C, 0x3C, #    OOO    OOOO
    0x3C, 0x1C, #   OOOO     OOO
    0x7C, 0x0C, #  OOOOO      OO
    0x7C, 0x0C, #  OOOOO      OO
    0xFC, 0x04, # OOOOOO       O
    0xFC, 0x00, # OOOOOO        
    0xFC, 0x00, # OOOOOO        
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0x78, # OOOOOO   OOOO 
    0xFC, 0x78, # OOOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x3C, 0x78, #   OOOO   OOOO 
    0x1C, 0x78, #    OOO   OOOO 
    0x0E, 0xE0, #     OOO OOO   
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @3120 'h' (16 pixels wide)
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0xFE, 0x7F, # OOOOOOO  OOOOOOO
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0xFE, #  OOOOO  OOOOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0x7C, 0x3E, #  OOOOO    OOOOO 
    0xFE, 0x7F, # OOOOOOO  OOOOOOO
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 

    # @3168 'i' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0xFE, # OOOOOOO
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0x7C, #  OOOOO 
    0xFE, # OOOOOOO
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @3192 'j' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x07, 0xF0, #      OOOOOOO
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x03, 0xE0, #       OOOOO 
    0x73, 0xE0, #  OOO  OOOOO 
    0xFB, 0xE0, # OOOOO OOOOO 
    0xFB, 0xE0, # OOOOO OOOOO 
    0xFB, 0xE0, # OOOOO OOOOO 
    0x63, 0xC0, #  OO   OOOO  
    0x37, 0x80, #   OO OOOO   
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @3240 'k' (16 pixels wide)
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0xFE, 0x7E, # OOOOOOO  OOOOOO 
    0x7C, 0x3C, #  OOOOO    OOOO  
    0x7C, 0x18, #  OOOOO     OO   
    0x7C, 0x10, #  OOOOO     O    
    0x7C, 0x20, #  OOOOO    O     
    0x7C, 0x70, #  OOOOO   OOO    
    0x7C, 0xF0, #  OOOOO  OOOO    
    0x7D, 0xF0, #  OOOOO OOOOO    
    0x7D, 0xF8, #  OOOOO OOOOOO   
    0x7D, 0xF8, #  OOOOO OOOOOO   
    0x7C, 0xFC, #  OOOOO  OOOOOO  
    0x7C, 0xFC, #  OOOOO  OOOOOO  
    0x7C, 0xFC, #  OOOOO  OOOOOO  
    0x7C, 0x7E, #  OOOOO   OOOOOO 
    0x7C, 0x7E, #  OOOOO   OOOOOO 
    0xFE, 0xFF, # OOOOOOO OOOOOOOO
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 

    # @3288 'l' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFE, 0x00, # OOOOOOO     
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x00, #  OOOOO      
    0x7C, 0x10, #  OOOOO     O
    0x7C, 0x10, #  OOOOO     O
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0x30, #  OOOOO    OO
    0x7C, 0xF0, #  OOOOO  OOOO
    0xFC, 0xF0, # OOOOOO  OOOO
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @3336 'm' (18 pixels wide)
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0xFE, 0x0F, 0xC0, # OOOOOOO     OOOOOO
    0x7E, 0x0F, 0x80, #  OOOOOO     OOOOO 
    0x3F, 0x0F, 0x80, #   OOOOOO    OOOOO 
    0x3F, 0x4F, 0x80, #   OOOOOO O  OOOOO 
    0x1F, 0x4F, 0x80, #    OOOOO O  OOOOO 
    0x1F, 0xCF, 0x80, #    OOOOOOO  OOOOO 
    0x1F, 0xCF, 0x80, #    OOOOOOO  OOOOO 
    0x1F, 0xCF, 0x80, #    OOOOOOO  OOOOO 
    0x1F, 0x8F, 0x80, #    OOOOOO   OOOOO 
    0x1F, 0x8F, 0x80, #    OOOOOO   OOOOO 
    0x17, 0x8F, 0x80, #    O OOOO   OOOOO 
    0x17, 0x8F, 0x80, #    O OOOO   OOOOO 
    0x17, 0x0F, 0x80, #    O OOO    OOOOO 
    0x13, 0x0F, 0x80, #    O  OO    OOOOO 
    0x3B, 0x0F, 0x80, #   OOO OO    OOOOO 
    0x7E, 0x1F, 0xC0, #  OOOOOO    OOOOOOO
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   
    0x00, 0x00, 0x00, #                   

    # @3408 'n' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0xFE, 0x3E, # OOOOOOO   OOOOO
    0x7F, 0x1C, #  OOOOOOO   OOO 
    0x3F, 0x08, #   OOOOOO    O  
    0x3F, 0x88, #   OOOOOOO   O  
    0x5F, 0x88, #  O OOOOOO   O  
    0x2F, 0xC8, #   O OOOOOO  O  
    0x2F, 0xE8, #   O OOOOOOO O  
    0x27, 0xE8, #   O  OOOOOO O  
    0x27, 0xF8, #   O  OOOOOOOO  
    0x23, 0xF0, #   O   OOOOOO   
    0x21, 0xF8, #   O    OOOOOO  
    0x21, 0xF8, #   O    OOOOOO  
    0x20, 0xF8, #   O     OOOOO  
    0x20, 0xF8, #   O     OOOOO  
    0x70, 0x78, #  OOO     OOOO  
    0xF8, 0x38, # OOOOO     OOO  
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @3456 'o' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x0E, 0xE0, #     OOO OOO    
    0x1C, 0x70, #    OOO   OOO   
    0x3C, 0x78, #   OOOO   OOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO 
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0xFC, 0x7E, # OOOOOO   OOOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO 
    0x3C, 0x78, #   OOOO   OOOO  
    0x1C, 0x70, #    OOO   OOO   
    0x0E, 0xE0, #     OOO OOO    
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @3504 'p' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFC, 0xE0, # OOOOOO  OOO   
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x7C, #  OOOOO   OOOOO
    0x7C, 0x78, #  OOOOO   OOOO 
    0x7D, 0xF0, #  OOOOO OOOOO  
    0x7D, 0xC0, #  OOOOO OOO    
    0x7C, 0x00, #  OOOOO        
    0x7C, 0x00, #  OOOOO        
    0x7C, 0x00, #  OOOOO        
    0x7C, 0x00, #  OOOOO        
    0x7C, 0x00, #  OOOOO        
    0xFE, 0x00, # OOOOOOO       
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @3552 'q' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x1D, 0xC0, #    OOO OOO    
    0x3C, 0xE0, #   OOOO  OOO   
    0x7C, 0xF0, #  OOOOO  OOOO  
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0xFC, 0xF8, # OOOOOO  OOOOO 
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xFC, # OOOOOO  OOOOOO
    0xFC, 0xF8, # OOOOOO  OOOOO 
    0x7C, 0xF8, #  OOOOO  OOOOO 
    0x7F, 0xF0, #  OOOOOOOOOOO  
    0x3D, 0xE0, #   OOOO OOOO   
    0x1D, 0xFC, #    OOO OOOOOOO
    0x00, 0x78, #          OOOO 
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @3600 'r' (16 pixels wide)
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0xFC, 0xF0, # OOOOOO  OOOO    
    0x7C, 0xF8, #  OOOOO  OOOOO   
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x78, #  OOOOO   OOOO   
    0x7C, 0xF0, #  OOOOO  OOOO    
    0x7D, 0xF0, #  OOOOO OOOOO    
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7C, #  OOOOO   OOOOO  
    0x7C, 0x7F, #  OOOOO   OOOOOOO
    0x7C, 0x7F, #  OOOOO   OOOOOOO
    0xFE, 0x3C, # OOOOOOO   OOOO  
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 

    # @3648 's' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x3B, 0xE0, #   OOO OOOOO 
    0x71, 0xE0, #  OOO   OOOO 
    0x70, 0x60, #  OOO     OO 
    0xF0, 0x60, # OOOO     OO 
    0xF8, 0x20, # OOOOO     O 
    0xFF, 0x00, # OOOOOOOO    
    0xFF, 0xC0, # OOOOOOOOOO  
    0x7F, 0xE0, #  OOOOOOOOOO 
    0x7F, 0xE0, #  OOOOOOOOOO 
    0x1F, 0xF0, #    OOOOOOOOO
    0x87, 0xF0, # O    OOOOOOO
    0xC1, 0xF0, # OO     OOOOO
    0xC0, 0xF0, # OO      OOOO
    0xE0, 0xE0, # OOO     OOO 
    0xF1, 0xE0, # OOOO   OOOO 
    0x9B, 0x80, # O  OO OOO   
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @3696 't' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xE7, 0xDC, # OOO  OOOOO OOO
    0xE7, 0xDC, # OOO  OOOOO OOO
    0xC7, 0xCC, # OO   OOOOO  OO
    0xC7, 0xCC, # OO   OOOOO  OO
    0x87, 0xC4, # O    OOOOO   O
    0x87, 0xC4, # O    OOOOO   O
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x07, 0xC0, #      OOOOO    
    0x0F, 0xE0, #     OOOOOOO   
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @3744 'u' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0xFE, 0x3E, # OOOOOOO   OOOOO
    0x7C, 0x1C, #  OOOOO     OOO 
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x08, #  OOOOO      O  
    0x7C, 0x18, #  OOOOO     OO  
    0x3E, 0x30, #   OOOOO   OO   
    0x1E, 0x60, #    OOOO  OO    
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @3792 'v' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFF, 0x3C, # OOOOOOOO  OOOO
    0x7E, 0x18, #  OOOOOO    OO 
    0x7E, 0x10, #  OOOOOO    O  
    0x3E, 0x10, #   OOOOO    O  
    0x3F, 0x30, #   OOOOOO  OO  
    0x3F, 0x20, #   OOOOOO  O   
    0x1F, 0x20, #    OOOOO  O   
    0x1F, 0x20, #    OOOOO  O   
    0x1F, 0xA0, #    OOOOOO O   
    0x1F, 0xC0, #    OOOOOOO    
    0x0F, 0x80, #     OOOOO     
    0x0F, 0xC0, #     OOOOOO    
    0x0F, 0xC0, #     OOOOOO    
    0x07, 0x80, #      OOOO     
    0x07, 0x80, #      OOOO     
    0x07, 0x80, #      OOOO     
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @3840 'w' (19 pixels wide)
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0xFF, 0x39, 0xE0, # OOOOOOOO  OOO  OOOO
    0x7E, 0x38, 0xC0, #  OOOOOO   OOO   OO 
    0x7E, 0x38, 0x80, #  OOOOOO   OOO   O  
    0x3E, 0x7C, 0x80, #   OOOOO  OOOOO  O  
    0x3F, 0x7C, 0x80, #   OOOOOO OOOOO  O  
    0x3F, 0x7D, 0x80, #   OOOOOO OOOOO OO  
    0x3F, 0x7D, 0x00, #   OOOOOO OOOOO O   
    0x1F, 0x7F, 0x00, #    OOOOO OOOOOOO   
    0x1F, 0xBF, 0x00, #    OOOOOO OOOOOO   
    0x1F, 0xBE, 0x00, #    OOOOOO OOOOO    
    0x0F, 0xBE, 0x00, #     OOOOO OOOOO    
    0x0F, 0xBE, 0x00, #     OOOOO OOOOO    
    0x0F, 0x9E, 0x00, #     OOOOO  OOOO    
    0x0F, 0x1E, 0x00, #     OOOO   OOOO    
    0x07, 0x1E, 0x00, #      OOO   OOOO    
    0x07, 0x1C, 0x00, #      OOO   OOO     
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    
    0x00, 0x00, 0x00, #                    

    # @3912 'x' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFF, 0x7C, # OOOOOOOO OOOOO
    0x7E, 0x38, #  OOOOOO   OOO 
    0x7E, 0x30, #  OOOOOO   OO  
    0x3F, 0x60, #   OOOOOO OO   
    0x3F, 0x40, #   OOOOOO O    
    0x1F, 0x80, #    OOOOOO     
    0x1F, 0x80, #    OOOOOO     
    0x0F, 0xC0, #     OOOOOO    
    0x0F, 0xC0, #     OOOOOO    
    0x07, 0xE0, #      OOOOOO   
    0x0F, 0xE0, #     OOOOOOO   
    0x0B, 0xF0, #     O OOOOOO  
    0x1B, 0xF0, #    OO OOOOOO  
    0x31, 0xF8, #   OO   OOOOOO 
    0x71, 0xF8, #  OOO   OOOOOO 
    0xF9, 0xFC, # OOOOO  OOOOOOO
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @3960 'y' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0xFE, 0x7C, # OOOOOOO  OOOOO
    0x7C, 0x38, #  OOOOO    OOO 
    0x7C, 0x10, #  OOOOO     O  
    0x3E, 0x10, #   OOOOO    O  
    0x3E, 0x20, #   OOOOO   O   
    0x3F, 0x20, #   OOOOOO  O   
    0x1F, 0x40, #    OOOOO O    
    0x1F, 0x80, #    OOOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x0F, 0x80, #     OOOOO     
    0x1F, 0xC0, #    OOOOOOO    
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @4008 'z' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x7D, 0xF0, #  OOOOO OOOOO
    0x7B, 0xF0, #  OOOO OOOOOO
    0x63, 0xE0, #  OO   OOOOO 
    0x67, 0xE0, #  OO  OOOOOO 
    0x47, 0xE0, #  O   OOOOOO 
    0x0F, 0xC0, #     OOOOOO  
    0x0F, 0xC0, #     OOOOOO  
    0x1F, 0x80, #    OOOOOO   
    0x1F, 0x80, #    OOOOOO   
    0x3F, 0x00, #   OOOOOO    
    0x3F, 0x00, #   OOOOOO    
    0x3E, 0x10, #   OOOOO    O
    0x7E, 0x30, #  OOOOOO   OO
    0x7C, 0x30, #  OOOOO    OO
    0xFC, 0xF0, # OOOOOO  OOOO
    0xFD, 0xF0, # OOOOOO OOOOO
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @4056 '{' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x1F, #    OOOOO
    0x3E, #   OOOOO 
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0xF0, # OOOO    
    0x7C, #  OOOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3E, #   OOOOO 
    0x1F, #    OOOOO
    0x00, #         

    # @4080 '|' (3 pixels wide)
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO

    # @4104 '}' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0xF8, # OOOOO   
    0x7C, #  OOOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x0F, #     OOOO
    0x1E, #    OOOO 
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x7C, #  OOOOO  
    0xF8, # OOOOO   
    0x00, #         

    # @4128 '~' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x38, 0x80, #   OOO   O
    0x7F, 0x80, #  OOOOOOOO
    0x8F, 0x00, # O   OOOO 
    0x80, 0x00, # O        
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @4176 '°' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x30, #   OO  
    0x78, #  OOOO 
    0xCC, # OO  OO
    0xCC, # OO  OO
    0xCC, # OO  OO
    0xFC, # OOOOOO
    0x78, #  OOOO 
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
)

descriptors = (
    (5,0),# !
    (8,24),# "
    (14,48),# #
    (11,96),# $
    (17,144),# %
    (15,216),# &
    (3,264),# '
    (6,288),# (
    (6,312),# )
    (9,336),# *
    (12,384),# +
    (4,432),# ,
    (6,456),# -
    (5,480),# .
    (10,504),# /
    (12,552),# 0
    (6,600),# 1
    (11,624),# 2
    (12,672),# 3
    (11,720),# 4
    (11,768),# 5
    (12,816),# 6
    (10,864),# 7
    (12,912),# 8
    (12,960),# 9
    (5,1008),# :
    (5,1032),# ;
    (10,1056),# <
    (12,1104),# =
    (10,1152),# >
    (9,1200),# ?
    (16,1248),# @
    (15,1296),# A
    (14,1344),# B
    (13,1392),# C
    (14,1440),# D
    (12,1488),# E
    (12,1536),# F
    (14,1584),# G
    (16,1632),# H
    (7,1680),# I
    (12,1704),# J
    (16,1752),# K
    (12,1800),# L
    (18,1848),# M
    (15,1920),# N
    (15,1968),# O
    (14,2016),# P
    (14,2064),# Q
    (16,2112),# R
    (12,2160),# S
    (14,2208),# T
    (15,2256),# U
    (14,2304),# V
    (19,2352),# W
    (14,2424),# X
    (14,2472),# Y
    (12,2520),# Z
    (6,2568),# [
    (10,2592),# \
    (6,2640),# ]
    (14,2664),# ^
    (12,2712),# _
    (6,2760),# `
    (15,2784),# a
    (14,2832),# b
    (13,2880),# c
    (14,2928),# d
    (12,2976),# e
    (12,3024),# f
    (14,3072),# g
    (16,3120),# h
    (7,3168),# i
    (12,3192),# j
    (16,3240),# k
    (12,3288),# l
    (18,3336),# m
    (15,3408),# n
    (15,3456),# o
    (14,3504),# p
    (14,3552),# q
    (16,3600),# r
    (12,3648),# s
    (14,3696),# t
    (15,3744),# u
    (14,3792),# v
    (19,3840),# w
    (14,3912),# x
    (14,3960),# y
    (12,4008),# z
    (8,4056),# {
    (3,4080),# |
    (8,4104),# }
    (9,4128),# ~
    (6,4176),# °
)

kerning = (
    (5,5,4,5,5,5,5,5,5,5,4,5,4,5,3,5,4,5,5,4,5,4,5,5,5,5,5,4,5,5,5,4,4,4,4,4,4,4,4,4,4,5,4,4,4,4,4,4,5,4,5,5,4,4,4,4,4,5,5,5,4,4,0,0,4,4,4,4,4,4,4,4,4,5,4,4,4,4,4,4,5,4,5,5,4,4,4,4,4,5,3,5,4,5,5,),
    (8,8,6,7,8,5,8,6,8,8,3,4,2,3,2,7,8,8,8,3,8,7,8,8,8,7,7,5,7,8,8,7,4,8,7,8,8,8,7,8,8,3,8,8,8,8,7,8,7,8,8,8,8,8,8,8,8,7,8,8,8,5,0,2,4,8,7,8,8,8,7,8,8,3,8,8,8,8,7,8,7,8,8,8,8,8,8,8,8,7,6,8,8,8,8,),
    (14,14,13,13,14,13,14,13,13,12,11,10,11,11,9,14,13,14,14,13,14,14,14,14,14,14,14,12,14,14,12,14,10,13,14,13,13,13,14,13,13,12,13,13,12,13,14,13,14,13,14,14,13,12,12,12,12,13,14,13,12,12,2,8,10,13,14,13,13,13,14,13,13,12,13,13,12,13,14,13,14,13,14,14,13,12,12,12,12,13,12,14,12,12,14,),
    (11,10,11,11,10,11,10,11,10,10,11,10,11,11,8,11,10,10,11,11,11,11,10,11,11,11,10,10,11,11,10,11,9,10,11,10,10,10,11,10,10,11,10,10,8,9,11,10,11,10,11,10,10,9,9,9,9,10,11,9,9,10,0,5,9,10,11,10,10,10,11,10,10,11,10,10,8,9,11,10,11,10,11,10,10,9,9,9,9,10,11,11,9,9,10,),
    (17,13,17,17,12,17,14,17,16,12,15,17,15,17,15,17,16,16,17,17,17,16,15,17,17,17,17,12,17,17,16,16,15,16,17,16,16,16,16,16,16,17,16,16,14,15,16,16,17,16,17,13,16,13,13,15,13,16,17,13,15,9,5,11,15,16,17,16,16,16,16,16,16,17,16,16,14,15,16,16,17,16,17,13,16,13,13,15,13,16,15,17,15,13,12,),
    (14,12,13,14,12,13,12,14,14,13,14,15,14,14,13,14,15,15,14,13,14,14,12,14,14,14,15,14,14,14,13,14,15,15,14,15,15,15,14,15,15,14,15,15,14,15,14,15,14,15,15,12,13,11,12,15,12,15,15,12,13,14,3,9,15,15,14,15,15,15,14,15,15,14,15,15,14,15,14,15,14,15,15,12,13,11,12,15,12,15,13,15,13,12,13,),
    (3,3,2,2,3,0,3,2,3,3,0,0,0,0,0,3,3,3,3,0,3,3,3,3,3,3,3,1,3,3,3,3,0,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,1,0,0,0,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,1,3,3,3,3,),
    (6,6,5,5,6,5,6,5,6,6,5,6,5,5,6,5,6,6,6,5,6,5,6,6,5,5,6,5,5,6,6,5,5,6,5,6,6,6,5,6,6,5,6,6,6,6,5,6,5,6,5,6,6,6,6,6,6,5,6,6,6,5,6,0,5,6,5,6,6,6,5,6,6,5,6,6,6,6,5,6,5,6,5,6,6,6,6,6,6,5,5,6,6,6,6,),
    (6,5,6,6,5,6,5,6,5,4,6,5,6,6,3,6,5,5,6,6,6,6,5,6,6,6,6,6,6,6,5,6,5,5,6,5,5,5,6,5,5,6,5,5,4,5,6,5,6,5,6,5,5,3,3,5,3,5,6,4,4,6,3,0,5,5,6,5,5,5,6,5,5,6,5,5,4,5,6,5,6,5,6,5,5,3,3,5,3,5,6,6,4,3,5,),
    (9,9,7,8,9,6,9,7,9,9,7,5,7,4,3,8,8,9,9,5,9,8,9,9,9,8,8,8,8,9,9,8,5,8,8,8,8,8,8,8,8,3,8,8,8,8,8,8,8,8,9,9,8,8,8,8,8,8,9,9,8,6,0,3,5,8,8,8,8,8,8,8,8,3,8,8,8,8,8,8,8,8,9,9,8,8,8,8,8,8,7,9,8,9,9,),
    (11,8,9,10,8,11,9,12,11,10,12,8,12,8,8,12,11,9,8,11,12,12,9,11,11,12,12,12,12,8,10,12,9,11,12,11,11,11,12,11,11,8,11,11,9,10,12,11,12,11,11,8,11,9,9,8,9,10,12,10,10,12,0,6,9,11,12,11,11,11,12,11,11,8,11,11,9,10,12,11,12,11,11,8,11,9,9,8,9,10,12,12,10,3,8,),
    (4,0,2,4,0,3,1,3,3,0,0,4,0,4,3,3,4,4,4,0,4,3,2,4,4,4,4,0,0,4,3,2,4,4,3,4,4,4,2,4,4,4,4,4,3,4,2,4,3,4,4,0,3,0,0,4,1,4,4,0,3,0,3,0,4,4,3,4,4,4,2,4,4,4,4,4,3,4,2,4,3,4,4,0,3,0,0,4,1,4,2,4,3,0,0,),
    (5,0,3,4,0,5,3,6,5,4,6,2,6,1,2,6,5,3,1,5,6,6,3,5,5,6,6,6,6,2,4,6,3,5,6,5,5,5,6,5,5,0,5,5,3,4,6,5,6,5,5,1,5,3,3,2,3,4,6,4,4,6,0,0,3,5,6,5,5,5,6,5,5,0,5,5,3,4,6,5,6,5,5,1,5,3,3,2,3,4,6,6,4,0,0,),
    (5,0,4,5,0,5,2,5,4,0,0,5,0,5,3,4,4,5,5,4,5,4,3,5,5,5,5,0,4,5,4,4,4,4,4,4,4,4,4,4,4,5,4,4,3,4,4,4,4,4,5,0,4,1,1,4,1,5,5,1,3,0,0,0,4,4,4,4,4,4,4,4,4,5,4,4,3,4,4,4,4,4,5,0,4,1,1,4,1,5,3,5,3,0,0,),
    (10,10,7,8,9,6,10,8,10,9,7,6,7,6,4,9,10,9,9,6,9,8,10,9,9,8,8,8,9,10,10,8,5,10,8,10,10,10,8,10,10,6,10,10,10,10,8,10,9,10,9,10,10,10,10,10,10,9,10,10,10,7,4,4,5,10,8,10,10,10,8,10,10,6,10,10,10,10,8,10,9,10,9,10,10,10,10,10,10,9,8,10,10,10,9,),
    (11,11,12,11,11,12,11,12,11,11,12,10,12,11,8,12,11,11,11,12,12,12,11,12,12,12,12,12,12,11,10,12,9,11,12,11,11,11,12,11,11,11,11,11,9,10,12,11,12,11,12,12,11,10,10,9,10,10,12,10,10,12,0,6,9,11,12,11,11,11,12,11,11,11,11,11,9,10,12,11,12,11,12,12,11,10,10,9,10,10,12,12,10,10,12,),
    (5,5,5,5,5,5,5,5,5,5,5,6,5,5,4,5,6,6,5,5,5,5,5,5,5,5,6,5,5,5,5,5,6,6,5,6,6,6,5,6,6,5,6,6,5,6,5,6,5,6,6,5,5,5,5,6,5,6,6,5,5,5,0,0,6,6,5,6,6,6,5,6,6,5,6,6,5,6,5,6,5,6,6,5,5,5,5,6,5,6,5,6,5,5,5,),
    (11,11,11,11,11,11,11,11,11,11,10,11,10,11,9,11,10,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,9,10,11,10,10,10,11,10,10,11,10,10,9,10,11,10,11,10,11,11,10,10,10,10,10,10,11,10,9,9,0,5,9,10,11,10,10,10,11,10,10,11,10,10,9,10,11,10,11,10,11,11,10,10,10,10,10,10,9,11,9,10,11,),
    (12,11,12,12,11,12,11,12,11,11,11,12,11,12,10,12,11,11,12,12,12,12,11,12,12,12,12,10,12,12,11,12,10,11,12,11,11,11,12,11,11,12,11,11,9,10,12,11,12,11,12,11,11,10,10,10,10,11,12,10,10,10,0,6,10,11,12,11,11,11,12,11,11,12,11,11,9,10,12,11,12,11,12,11,11,10,10,10,10,11,11,12,10,10,11,),
    (10,9,11,11,9,11,9,11,10,9,9,10,9,10,8,11,10,10,11,11,11,10,9,11,11,10,10,9,11,9,9,10,10,10,11,10,10,10,10,10,10,11,10,10,9,10,10,10,11,10,11,9,10,9,9,10,9,10,11,9,9,9,0,5,10,10,11,10,10,10,10,10,10,11,10,10,9,10,10,10,11,10,11,9,10,9,9,10,9,10,9,11,9,9,9,),
    (11,10,11,11,8,11,10,11,10,8,11,10,11,11,8,11,10,10,11,11,11,11,10,11,11,11,10,10,11,11,10,11,9,10,11,10,10,10,11,10,10,11,10,10,10,10,11,10,11,10,11,10,10,10,10,10,10,10,11,10,10,11,0,5,9,10,11,10,10,10,11,10,10,11,10,10,10,10,11,10,11,10,11,10,10,10,10,10,10,10,11,11,10,10,8,),
    (12,12,12,12,12,12,12,12,12,12,12,11,12,12,9,12,11,12,12,12,12,12,12,12,12,12,11,11,12,12,12,12,10,11,12,11,11,11,12,11,11,12,11,11,10,10,12,11,12,11,12,12,11,11,11,11,11,11,12,11,10,12,0,6,10,11,12,11,11,11,12,11,11,12,11,11,10,10,12,11,12,11,12,12,11,11,11,11,11,11,12,12,10,11,12,),
    (10,10,7,8,9,7,10,7,10,9,7,7,7,7,5,8,10,9,9,7,9,8,10,9,9,8,8,8,8,10,10,8,6,10,8,10,10,10,8,10,10,7,10,10,10,10,8,10,8,10,9,10,10,10,10,10,10,9,10,10,10,7,0,4,6,10,8,10,10,10,8,10,10,7,10,10,10,10,8,10,8,10,9,10,10,10,10,10,10,9,8,10,10,10,9,),
    (12,11,12,12,11,12,11,12,11,11,11,12,11,12,10,12,11,11,12,12,12,12,11,12,12,12,12,10,12,12,11,12,10,11,12,11,11,11,12,11,11,12,11,11,9,10,12,11,12,11,12,11,11,10,10,10,10,11,12,10,10,10,0,6,10,11,12,11,11,11,12,11,11,12,11,11,9,10,12,11,12,11,12,11,11,10,10,10,10,11,11,12,10,10,11,),
    (11,11,12,11,11,12,11,12,11,11,12,11,12,11,9,12,11,11,11,12,12,12,11,12,12,12,12,12,12,11,11,12,9,11,12,11,11,11,12,11,11,11,11,11,9,10,12,11,12,11,12,12,11,10,10,10,10,10,12,10,10,12,0,6,9,11,12,11,11,11,12,11,11,11,11,11,9,10,12,11,12,11,12,12,11,10,10,10,10,10,12,12,10,10,12,),
    (5,4,4,5,4,5,4,5,4,4,5,5,5,5,3,5,4,5,5,4,5,5,4,5,5,5,5,5,5,5,4,5,4,4,5,4,4,4,5,4,4,5,4,4,3,4,5,4,5,4,5,5,4,3,3,4,3,5,5,3,3,4,0,0,4,4,5,4,4,4,5,4,4,5,4,4,3,4,5,4,5,4,5,5,4,3,3,4,3,5,3,5,3,0,5,),
    (4,4,4,4,4,3,4,5,4,4,5,4,5,4,3,5,4,4,4,3,5,5,4,5,5,5,5,5,5,4,3,5,4,4,5,4,4,4,5,4,4,4,4,4,3,4,5,4,5,4,5,5,4,3,3,4,3,4,5,3,3,4,3,0,4,4,5,4,4,4,5,4,4,4,4,4,3,4,5,4,5,4,5,5,4,3,3,4,3,4,3,5,3,0,5,),
    (10,10,10,10,10,10,10,10,10,10,10,10,10,10,8,10,9,10,10,10,10,10,10,10,10,10,10,7,10,10,10,10,8,9,10,9,9,9,10,9,9,10,9,9,9,9,10,9,10,9,10,10,9,9,9,9,9,9,10,10,9,8,0,4,8,9,10,9,9,9,10,9,9,10,9,9,9,9,10,9,10,9,10,10,9,9,9,9,9,9,10,10,9,10,10,),
    (12,12,12,12,12,12,12,12,11,11,12,8,12,11,9,12,11,12,12,12,12,12,12,12,12,12,12,12,12,12,10,12,9,11,12,11,11,11,12,11,11,12,11,11,9,11,12,11,12,11,12,12,11,10,10,10,10,11,12,11,10,10,0,6,9,11,12,11,11,11,12,11,11,12,11,11,9,11,12,11,12,11,12,12,11,10,10,10,10,11,12,12,10,3,12,),
    (9,6,6,8,7,8,7,10,9,8,10,6,10,5,5,10,9,6,6,8,10,10,6,8,9,10,10,10,9,7,8,10,6,9,10,9,9,9,10,9,9,5,9,9,7,8,10,9,10,9,9,7,9,7,7,6,7,7,10,8,8,9,0,4,6,9,10,9,9,9,10,9,9,5,9,9,7,8,10,9,10,9,9,7,9,7,7,6,7,7,8,10,8,1,8,),
    (9,9,8,8,9,6,9,8,9,9,8,6,8,6,4,9,8,9,9,6,9,9,9,9,9,9,9,9,9,9,9,9,5,8,9,8,8,8,9,8,8,6,8,8,7,8,9,8,9,8,9,9,8,8,8,8,8,8,9,8,7,7,0,3,5,8,9,8,8,8,9,8,8,6,8,8,7,8,9,8,9,8,9,9,8,8,8,8,8,8,7,9,7,8,9,),
    (16,16,15,15,16,15,16,16,15,15,16,14,16,13,12,16,15,16,16,15,16,16,16,16,16,16,16,16,16,16,14,16,14,15,16,15,15,15,16,15,15,14,15,15,13,15,16,15,16,15,16,16,15,14,14,14,14,15,16,15,14,16,4,10,14,15,16,15,15,15,16,15,15,14,15,15,13,15,16,15,16,15,16,16,15,14,14,14,14,15,15,16,14,13,16,),
    (14,11,13,14,11,13,12,14,14,11,13,15,13,14,13,13,15,15,14,13,14,13,12,14,14,14,15,12,13,14,13,13,15,15,13,15,15,15,13,15,15,14,15,15,14,15,13,15,13,15,15,12,13,11,11,15,12,15,15,11,13,12,3,9,15,15,13,15,15,15,13,15,15,14,15,15,14,15,13,15,13,15,15,12,13,11,11,15,12,15,13,15,13,11,12,),
    (14,14,14,14,14,14,14,14,14,14,13,14,13,14,12,14,13,14,14,14,14,14,14,14,14,14,14,13,14,14,14,14,12,13,14,13,13,13,14,13,13,14,13,13,12,13,14,13,14,13,14,14,13,13,13,13,13,13,14,13,12,12,2,8,12,13,14,13,13,13,14,13,13,14,13,13,12,13,14,13,14,13,14,14,13,13,13,13,13,13,13,14,12,13,14,),
    (13,13,13,13,13,13,13,13,13,13,8,12,7,13,10,13,13,13,13,13,13,13,13,13,13,13,13,11,13,13,13,13,11,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,12,13,13,13,11,1,7,11,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,12,11,13,13,13,13,),
    (13,13,14,13,13,14,13,14,13,13,14,12,14,13,10,14,13,13,13,14,14,14,13,14,14,14,14,14,14,13,13,14,11,13,14,13,13,13,14,13,13,13,13,13,11,12,14,13,14,13,14,14,13,12,12,12,12,12,14,12,12,14,2,8,11,13,14,13,13,13,14,13,13,13,13,13,11,12,14,13,14,13,14,14,13,12,12,12,12,12,14,14,12,12,14,),
    (12,12,12,12,12,12,12,12,12,12,10,12,10,12,10,12,12,12,12,12,12,11,12,12,12,12,12,10,12,12,12,11,12,12,12,12,12,12,11,12,12,12,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,10,0,6,12,12,12,12,12,12,11,12,12,12,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,12,10,12,12,12,12,),
    (12,12,10,11,12,10,12,11,12,12,10,8,10,7,6,12,12,12,12,10,12,11,12,12,12,11,11,10,12,12,12,11,8,12,11,12,12,12,11,12,12,9,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,11,12,12,12,10,0,6,8,12,11,12,12,12,11,12,12,9,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,11,10,12,12,12,12,),
    (14,14,13,13,14,13,14,14,14,14,14,13,14,13,11,14,14,14,14,13,14,14,14,14,14,14,14,12,14,14,14,14,12,14,14,14,14,14,14,14,14,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,14,14,14,14,2,8,12,14,14,14,14,14,14,14,14,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,13,14,14,14,14,),
    (15,16,15,15,15,15,16,15,16,15,15,16,15,15,14,15,16,16,15,15,15,15,16,15,15,15,16,15,15,15,15,15,16,16,15,16,16,16,15,16,16,15,16,16,16,16,15,16,15,16,16,16,16,16,16,16,16,16,16,16,16,15,4,10,16,16,15,16,16,16,15,16,16,15,16,16,16,16,15,16,15,16,16,16,16,16,16,16,16,16,15,16,16,16,15,),
    (6,7,6,6,6,6,7,6,7,6,6,7,6,6,5,6,7,7,6,6,6,6,7,6,6,6,7,6,6,6,6,6,7,7,6,7,7,7,6,7,7,6,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,6,0,1,7,7,6,7,7,7,6,7,7,6,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,7,7,6,),
    (11,12,11,11,11,11,12,11,12,11,11,11,11,11,9,11,12,11,11,11,11,11,12,11,11,11,11,11,11,11,11,11,9,12,11,12,12,12,11,12,12,11,12,12,12,12,11,12,11,12,11,12,12,12,12,12,12,11,12,12,12,11,0,6,9,12,11,12,12,12,11,12,12,11,12,12,12,12,11,12,11,12,11,12,12,12,12,12,12,11,11,12,12,12,11,),
    (15,15,14,15,13,14,15,15,15,13,13,16,13,15,14,14,16,16,15,14,15,14,15,15,15,15,16,12,14,15,14,14,16,16,14,16,16,16,14,16,16,15,16,16,15,16,14,16,14,16,16,15,15,15,15,16,15,16,16,15,15,13,4,10,16,16,14,16,16,16,14,16,16,15,16,16,15,16,14,16,14,16,16,15,15,15,15,16,15,16,14,16,15,15,13,),
    (12,7,12,12,8,12,9,12,11,6,7,12,6,12,10,12,12,12,12,12,12,12,10,12,12,12,12,7,12,12,11,12,12,12,12,12,12,12,12,12,12,12,12,12,11,12,12,12,12,12,12,8,11,8,8,12,9,12,12,8,10,6,0,6,12,12,12,12,12,12,12,12,12,12,12,12,11,12,12,12,12,12,12,8,11,8,8,12,9,12,11,12,10,7,6,),
    (17,18,17,17,17,17,18,17,18,17,17,18,17,17,16,17,18,18,17,17,17,17,18,17,17,17,18,17,17,17,17,17,18,18,17,18,18,18,17,18,18,17,18,18,18,18,17,18,17,18,18,18,18,18,18,18,18,18,18,18,18,17,6,12,18,18,17,18,18,18,17,18,18,17,18,18,18,18,17,18,17,18,18,18,18,18,18,18,18,18,17,18,18,18,17,),
    (14,15,13,13,13,13,15,13,15,13,13,13,13,13,11,13,15,13,13,13,14,13,15,13,13,13,13,13,13,14,14,13,13,15,13,15,15,15,13,15,15,13,15,15,15,15,13,15,13,15,13,15,15,15,15,15,15,14,15,15,15,13,3,9,13,15,13,15,15,15,13,15,15,13,15,15,15,15,13,15,13,15,13,15,15,15,15,15,15,14,12,15,15,15,13,),
    (14,14,15,14,14,15,14,15,14,14,15,13,15,14,11,15,14,14,14,15,15,15,14,15,15,15,15,15,15,14,13,15,12,14,15,14,14,14,15,14,14,14,14,14,12,13,15,14,15,14,15,15,14,13,13,12,13,13,15,13,13,15,3,9,12,14,15,14,14,14,15,14,14,14,14,14,12,13,15,14,15,14,15,15,14,13,13,12,13,13,15,15,13,12,15,),
    (14,14,13,13,14,11,14,13,13,14,13,10,13,9,9,14,13,14,14,11,14,14,14,14,14,14,14,14,14,14,13,14,10,13,14,13,13,13,14,13,13,8,13,13,12,13,14,13,14,13,14,14,13,12,12,12,12,13,14,13,12,12,2,8,10,13,14,13,13,13,14,13,13,8,13,13,12,13,14,13,14,13,14,14,13,12,12,12,12,13,12,14,12,13,14,),
    (13,13,14,13,13,14,13,14,13,13,14,14,14,13,12,14,14,14,13,14,14,14,13,14,14,14,14,14,14,13,12,14,14,14,14,14,14,14,14,14,14,13,14,14,13,14,14,14,14,14,14,14,13,12,12,14,12,14,14,12,12,14,2,8,14,14,14,14,14,14,14,14,14,13,14,14,13,14,14,14,14,14,14,14,13,12,12,14,12,14,14,14,12,11,14,),
    (16,14,14,16,14,15,14,15,15,14,14,16,14,16,14,15,15,16,16,14,16,15,14,16,16,16,16,13,14,16,15,14,15,15,15,15,15,15,14,15,15,16,15,15,14,15,14,15,15,15,16,14,15,13,13,15,13,16,16,13,14,12,4,10,15,15,15,15,15,15,14,15,15,16,15,15,14,15,14,15,15,15,16,14,15,13,13,15,13,16,14,16,14,13,14,),
    (12,11,12,12,11,12,11,12,11,11,12,11,12,12,9,12,11,11,12,12,12,12,11,12,12,12,11,11,12,12,11,12,10,11,12,11,11,11,12,11,11,12,11,11,11,11,12,11,12,11,12,11,11,11,11,11,11,11,12,11,11,11,0,6,10,11,12,11,11,11,12,11,11,12,11,11,11,11,12,11,12,11,12,11,11,11,11,11,11,11,12,12,11,11,11,),
    (14,14,13,13,14,11,14,13,14,14,10,11,10,10,9,14,14,14,14,10,14,14,14,14,14,14,14,12,14,14,14,14,11,14,14,14,14,14,14,14,14,10,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,14,14,14,12,2,8,11,14,14,14,14,14,14,14,14,10,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,12,14,14,14,14,),
    (14,15,13,13,13,13,15,13,15,13,13,13,13,13,11,13,15,13,13,13,14,13,15,13,13,13,13,13,13,14,14,13,11,15,13,15,15,15,13,15,15,13,15,15,15,15,13,15,13,15,13,15,15,15,15,15,15,14,15,15,15,13,3,9,11,15,13,15,15,15,13,15,15,13,15,15,15,15,13,15,13,15,13,15,15,15,15,15,15,14,13,15,15,15,13,),
    (13,14,10,11,12,10,14,11,14,12,11,10,11,10,7,12,14,12,12,10,13,11,14,12,12,11,11,11,12,13,13,11,9,14,11,14,14,14,11,14,14,10,14,14,14,14,11,14,12,14,12,14,14,14,14,14,14,13,14,14,14,11,2,8,9,14,11,14,14,14,11,14,14,10,14,14,14,14,11,14,12,14,12,14,14,14,14,14,14,13,11,14,14,14,12,),
    (18,19,16,16,17,15,19,16,19,17,16,15,16,15,13,17,19,17,17,15,18,17,19,17,17,17,17,16,17,18,18,17,14,19,17,19,19,19,17,19,19,15,19,19,19,19,17,19,17,19,17,19,19,19,19,19,19,18,19,19,19,16,7,13,14,19,17,19,19,19,17,19,19,15,19,19,19,19,17,19,17,19,17,19,19,19,19,19,19,18,16,19,19,19,17,),
    (13,14,12,13,12,12,14,13,14,12,11,14,11,13,12,12,14,14,13,12,13,12,14,13,13,13,14,10,12,13,13,11,14,14,12,14,14,14,11,14,14,13,14,14,14,14,11,14,12,14,14,14,14,14,14,14,14,14,14,14,14,10,2,8,14,14,12,14,14,14,11,14,14,13,14,14,14,14,11,14,12,14,14,14,14,14,14,14,14,14,12,14,14,14,12,),
    (13,14,10,11,12,9,14,10,14,12,9,10,9,9,8,11,14,12,12,9,13,11,14,12,12,11,11,10,11,13,13,11,10,14,11,14,14,14,11,14,14,9,14,14,14,14,11,14,11,14,12,14,14,14,14,14,14,13,14,14,14,9,2,8,10,14,11,14,14,14,11,14,14,9,14,14,14,14,11,14,11,14,12,14,14,14,14,14,14,13,11,14,14,14,12,),
    (12,12,12,12,11,12,12,12,12,11,9,12,9,12,10,12,12,12,12,12,12,11,12,12,12,12,12,10,12,12,12,11,12,12,12,12,12,12,11,12,12,12,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,9,0,6,12,12,12,12,12,12,11,12,12,12,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,12,10,12,12,12,11,),
    (5,6,4,4,4,4,6,4,6,4,4,5,4,4,6,4,6,4,4,4,5,4,6,4,4,4,5,4,4,5,5,4,4,6,4,6,6,6,4,6,6,4,6,6,6,6,4,6,4,6,4,6,6,6,6,6,6,5,6,6,6,4,6,0,4,6,4,6,6,6,4,6,6,4,6,6,6,6,4,6,4,6,4,6,6,6,6,6,6,5,4,6,6,6,4,),
    (8,4,7,8,4,7,7,7,10,4,6,9,6,8,10,7,8,8,8,7,8,7,6,8,8,8,9,5,7,8,7,6,8,8,7,8,8,8,6,8,8,8,8,8,7,8,6,8,7,8,8,5,7,3,4,8,5,8,10,4,10,6,10,4,8,8,7,8,8,8,6,8,8,8,8,8,7,8,6,8,7,8,8,5,7,3,4,8,5,8,7,10,10,3,5,),
    (6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,),
    (12,10,11,12,10,13,11,14,13,11,14,10,14,9,10,14,13,10,10,12,14,14,10,12,12,13,13,12,12,10,12,14,11,13,14,13,13,13,14,13,13,8,13,13,11,12,14,13,14,13,13,11,13,11,11,10,10,11,14,11,12,14,2,8,11,13,14,13,13,13,14,13,13,8,13,13,11,12,14,13,14,13,13,11,13,11,11,10,10,11,12,14,12,8,11,),
    (7,4,0,1,0,0,9,9,12,3,0,12,6,7,12,0,6,1,0,1,1,0,2,0,0,7,12,2,0,2,3,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,6,12,0,12,6,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,12,12,3,6,),
    (1,0,0,1,0,0,3,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,4,0,),
    (14,11,13,14,11,13,12,14,14,11,13,15,13,14,13,13,15,15,14,13,14,13,12,14,14,14,15,12,13,14,13,13,15,15,13,15,15,15,13,15,15,14,15,15,14,15,13,15,13,15,15,12,13,11,11,15,12,15,15,11,13,12,3,9,15,15,13,15,15,15,13,15,15,14,15,15,14,15,13,15,13,15,15,12,13,11,11,15,12,15,13,15,13,11,12,),
    (14,14,14,14,14,14,14,14,14,14,13,14,13,14,12,14,13,14,14,14,14,14,14,14,14,14,14,13,14,14,14,14,12,13,14,13,13,13,14,13,13,14,13,13,12,13,14,13,14,13,14,14,13,13,13,13,13,13,14,13,12,12,2,8,12,13,14,13,13,13,14,13,13,14,13,13,12,13,14,13,14,13,14,14,13,13,13,13,13,13,13,14,12,13,14,),
    (13,13,13,13,13,13,13,13,13,13,8,12,7,13,10,13,13,13,13,13,13,13,13,13,13,13,13,11,13,13,13,13,11,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,12,13,13,13,11,1,7,11,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,12,11,13,13,13,13,),
    (13,13,14,13,13,14,13,14,13,13,14,12,14,13,10,14,13,13,13,14,14,14,13,14,14,14,14,14,14,13,13,14,11,13,14,13,13,13,14,13,13,13,13,13,11,12,14,13,14,13,14,14,13,12,12,12,12,12,14,12,12,14,2,8,11,13,14,13,13,13,14,13,13,13,13,13,11,12,14,13,14,13,14,14,13,12,12,12,12,12,14,14,12,12,14,),
    (12,12,12,12,12,12,12,12,12,12,10,12,10,12,10,12,12,12,12,12,12,11,12,12,12,12,12,10,12,12,12,11,12,12,12,12,12,12,11,12,12,12,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,10,0,6,12,12,12,12,12,12,11,12,12,12,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,12,10,12,12,12,12,),
    (12,12,10,11,12,10,12,11,12,12,10,8,10,7,6,12,12,12,12,10,12,11,12,12,12,11,11,10,12,12,12,11,8,12,11,12,12,12,11,12,12,9,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,11,12,12,12,10,0,6,8,12,11,12,12,12,11,12,12,9,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,11,10,12,12,12,12,),
    (14,14,13,13,14,13,14,14,14,14,14,13,14,13,11,14,14,14,14,13,14,14,14,14,14,14,14,12,14,14,14,14,12,14,14,14,14,14,14,14,14,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,14,14,14,14,2,8,12,14,14,14,14,14,14,14,14,13,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,13,14,14,14,14,),
    (15,16,15,15,15,15,16,15,16,15,15,16,15,15,14,15,16,16,15,15,15,15,16,15,15,15,16,15,15,15,15,15,16,16,15,16,16,16,15,16,16,15,16,16,16,16,15,16,15,16,16,16,16,16,16,16,16,16,16,16,16,15,4,10,16,16,15,16,16,16,15,16,16,15,16,16,16,16,15,16,15,16,16,16,16,16,16,16,16,16,15,16,16,16,15,),
    (6,7,6,6,6,6,7,6,7,6,6,7,6,6,5,6,7,7,6,6,6,6,7,6,6,6,7,6,6,6,6,6,7,7,6,7,7,7,6,7,7,6,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,7,7,6,0,1,7,7,6,7,7,7,6,7,7,6,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,6,7,7,7,6,),
    (11,12,11,11,11,11,12,11,12,11,11,11,11,11,9,11,12,11,11,11,11,11,12,11,11,11,11,11,11,11,11,11,9,12,11,12,12,12,11,12,12,11,12,12,12,12,11,12,11,12,11,12,12,12,12,12,12,11,12,12,12,11,0,6,9,12,11,12,12,12,11,12,12,11,12,12,12,12,11,12,11,12,11,12,12,12,12,12,12,11,11,12,12,12,11,),
    (15,15,14,15,13,14,15,15,15,13,13,16,13,15,14,14,16,16,15,14,15,14,15,15,15,15,16,12,14,15,14,14,16,16,14,16,16,16,14,16,16,15,16,16,15,16,14,16,14,16,16,15,15,15,15,16,15,16,16,15,15,13,4,10,16,16,14,16,16,16,14,16,16,15,16,16,15,16,14,16,14,16,16,15,15,15,15,16,15,16,14,16,15,15,13,),
    (12,7,12,12,8,12,9,12,11,6,7,12,6,12,10,12,12,12,12,12,12,12,10,12,12,12,12,7,12,12,11,12,12,12,12,12,12,12,12,12,12,12,12,12,11,12,12,12,12,12,12,8,11,8,8,12,9,12,12,8,10,6,0,6,12,12,12,12,12,12,12,12,12,12,12,12,11,12,12,12,12,12,12,8,11,8,8,12,9,12,11,12,10,7,6,),
    (17,18,17,17,17,17,18,17,18,17,17,18,17,17,16,17,18,18,17,17,17,17,18,17,17,17,18,17,17,17,17,17,18,18,17,18,18,18,17,18,18,17,18,18,18,18,17,18,17,18,18,18,18,18,18,18,18,18,18,18,18,17,6,12,18,18,17,18,18,18,17,18,18,17,18,18,18,18,17,18,17,18,18,18,18,18,18,18,18,18,17,18,18,18,17,),
    (14,15,13,13,13,13,15,13,15,13,13,13,13,13,11,13,15,13,13,13,14,13,15,13,13,13,13,13,13,14,14,13,13,15,13,15,15,15,13,15,15,13,15,15,15,15,13,15,13,15,13,15,15,15,15,15,15,14,15,15,15,13,3,9,13,15,13,15,15,15,13,15,15,13,15,15,15,15,13,15,13,15,13,15,15,15,15,15,15,14,12,15,15,15,13,),
    (14,14,15,14,14,15,14,15,14,14,15,13,15,14,11,15,14,14,14,15,15,15,14,15,15,15,15,15,15,14,13,15,12,14,15,14,14,14,15,14,14,14,14,14,12,13,15,14,15,14,15,15,14,13,13,12,13,13,15,13,13,15,3,9,12,14,15,14,14,14,15,14,14,14,14,14,12,13,15,14,15,14,15,15,14,13,13,12,13,13,15,15,13,12,15,),
    (14,14,13,13,14,11,14,13,13,14,13,10,13,9,9,14,13,14,14,11,14,14,14,14,14,14,14,14,14,14,13,14,10,13,14,13,13,13,14,13,13,8,13,13,12,13,14,13,14,13,14,14,13,12,12,12,12,13,14,13,12,12,2,8,10,13,14,13,13,13,14,13,13,8,13,13,12,13,14,13,14,13,14,14,13,12,12,12,12,13,12,14,12,13,14,),
    (13,13,14,13,13,14,13,14,13,13,14,14,14,13,12,14,14,14,13,14,14,14,13,14,14,14,14,14,14,13,12,14,14,14,14,14,14,14,14,14,14,13,14,14,13,14,14,14,14,14,14,14,13,12,12,14,12,14,14,12,12,14,2,8,14,14,14,14,14,14,14,14,14,13,14,14,13,14,14,14,14,14,14,14,13,12,12,14,12,14,14,14,12,11,14,),
    (16,14,14,16,14,15,14,15,15,14,14,16,14,16,14,15,15,16,16,14,16,15,14,16,16,16,16,13,14,16,15,14,15,15,15,15,15,15,14,15,15,16,15,15,14,15,14,15,15,15,16,14,15,13,13,15,13,16,16,13,14,12,4,10,15,15,15,15,15,15,14,15,15,16,15,15,14,15,14,15,15,15,16,14,15,13,13,15,13,16,14,16,14,13,14,),
    (12,11,12,12,11,12,11,12,11,11,12,11,12,12,9,12,11,11,12,12,12,12,11,12,12,12,11,11,12,12,11,12,10,11,12,11,11,11,12,11,11,12,11,11,11,11,12,11,12,11,12,11,11,11,11,11,11,11,12,11,11,11,0,6,10,11,12,11,11,11,12,11,11,12,11,11,11,11,12,11,12,11,12,11,11,11,11,11,11,11,12,12,11,11,11,),
    (14,14,13,13,14,11,14,13,14,14,10,11,10,10,9,14,14,14,14,10,14,14,14,14,14,14,14,12,14,14,14,14,11,14,14,14,14,14,14,14,14,10,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,14,14,14,12,2,8,11,14,14,14,14,14,14,14,14,10,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,12,14,14,14,14,),
    (14,15,13,13,13,13,15,13,15,13,13,13,13,13,11,13,15,13,13,13,14,13,15,13,13,13,13,13,13,14,14,13,11,15,13,15,15,15,13,15,15,13,15,15,15,15,13,15,13,15,13,15,15,15,15,15,15,14,15,15,15,13,3,9,11,15,13,15,15,15,13,15,15,13,15,15,15,15,13,15,13,15,13,15,15,15,15,15,15,14,13,15,15,15,13,),
    (13,14,10,11,12,10,14,11,14,12,11,10,11,10,7,12,14,12,12,10,13,11,14,12,12,11,11,11,12,13,13,11,9,14,11,14,14,14,11,14,14,10,14,14,14,14,11,14,12,14,12,14,14,14,14,14,14,13,14,14,14,11,2,8,9,14,11,14,14,14,11,14,14,10,14,14,14,14,11,14,12,14,12,14,14,14,14,14,14,13,11,14,14,14,12,),
    (18,19,16,16,17,15,19,16,19,17,16,15,16,15,13,17,19,17,17,15,18,17,19,17,17,17,17,16,17,18,18,17,14,19,17,19,19,19,17,19,19,15,19,19,19,19,17,19,17,19,17,19,19,19,19,19,19,18,19,19,19,16,7,13,14,19,17,19,19,19,17,19,19,15,19,19,19,19,17,19,17,19,17,19,19,19,19,19,19,18,16,19,19,19,17,),
    (13,14,12,13,12,12,14,13,14,12,11,14,11,13,12,12,14,14,13,12,13,12,14,13,13,13,14,10,12,13,13,11,14,14,12,14,14,14,11,14,14,13,14,14,14,14,11,14,12,14,14,14,14,14,14,14,14,14,14,14,14,10,2,8,14,14,12,14,14,14,11,14,14,13,14,14,14,14,11,14,12,14,14,14,14,14,14,14,14,14,12,14,14,14,12,),
    (13,14,10,11,12,9,14,10,14,12,9,10,9,9,8,11,14,12,12,9,13,11,14,12,12,11,11,10,11,13,13,11,10,14,11,14,14,14,11,14,14,9,14,14,14,14,11,14,11,14,12,14,14,14,14,14,14,13,14,14,14,9,2,8,10,14,11,14,14,14,11,14,14,9,14,14,14,14,11,14,11,14,12,14,14,14,14,14,14,13,11,14,14,14,12,),
    (12,12,12,12,11,12,12,12,12,11,9,12,9,12,10,12,12,12,12,12,12,11,12,12,12,12,12,10,12,12,12,11,12,12,12,12,12,12,11,12,12,12,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,9,0,6,12,12,12,12,12,12,11,12,12,12,12,12,12,12,11,12,12,12,12,12,12,12,12,12,12,12,10,12,12,12,11,),
    (7,8,6,6,6,6,8,6,8,6,6,7,6,6,8,6,8,6,6,6,7,6,8,6,6,6,7,6,6,7,7,6,6,8,6,8,8,8,6,8,8,6,8,8,8,8,6,8,6,8,6,8,8,8,8,8,8,7,8,8,8,6,8,2,6,8,6,8,8,8,6,8,8,6,8,8,8,8,6,8,6,8,6,8,8,8,8,8,8,7,5,8,8,8,6,),
    (3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,),
    (6,6,7,6,6,7,6,8,7,6,8,6,8,6,5,8,7,6,6,7,6,8,6,7,6,6,6,6,8,6,6,8,6,7,8,7,7,7,8,7,7,6,7,7,5,6,8,7,8,7,7,6,7,5,5,6,5,6,8,6,6,6,5,2,6,7,8,7,7,7,8,7,7,6,7,7,5,6,8,7,8,7,7,6,7,5,5,6,5,6,8,8,5,6,6,),
    (7,8,3,4,6,3,8,4,8,5,0,5,3,4,1,5,8,6,6,1,7,4,8,6,6,4,4,0,0,1,7,3,2,8,3,8,8,8,4,8,8,3,8,8,8,8,4,8,5,8,6,8,8,8,8,8,8,7,8,8,8,3,0,6,2,8,3,8,8,8,4,8,8,3,8,8,8,8,4,8,5,8,6,8,8,8,8,8,8,7,5,8,8,8,6,),
    (6,6,5,5,6,3,6,5,6,6,1,2,0,1,1,6,5,6,6,2,6,6,6,6,6,6,6,5,6,6,6,6,2,5,6,5,5,5,6,5,5,0,5,5,4,5,6,5,6,5,6,6,5,5,5,5,5,5,6,5,4,4,0,0,2,5,6,5,5,5,6,5,5,0,5,5,4,5,6,5,6,5,6,6,5,5,5,5,5,5,4,6,4,5,6,),
)

# End of font

