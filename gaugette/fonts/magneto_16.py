# coding=utf-8
# Module magneto_bold_16
# generated from Magneto 11.25pt

name        = "Magneto 16"
start_char  = '!'
end_char    = chr(127)
char_height = 16
space_width = 8
gap_width   = 2

bitmaps = (
    # @0 '!' (6 pixels wide)
    0x00, #       
    0x1C, #    OOO
    0x38, #   OOO 
    0x38, #   OOO 
    0x30, #   OO  
    0x70, #  OOO  
    0x60, #  OO   
    0x00, #       
    0xE0, # OOO   
    0xE0, # OOO   
    0xE0, # OOO   
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @16 '"' (6 pixels wide)
    0x00, #       
    0x6C, #  OO OO
    0xD8, # OO OO 
    0xD8, # OO OO 
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

    # @32 '#' (11 pixels wide)
    0x00, 0x00, #            
    0x0C, 0xC0, #     OO  OO 
    0x1D, 0xC0, #    OOO OOO 
    0x19, 0x80, #    OO  OO  
    0x7F, 0xE0, #  OOOOOOOOOO
    0x19, 0x80, #    OO  OO  
    0x33, 0x00, #   OO  OO   
    0xFF, 0xC0, # OOOOOOOOOO 
    0x33, 0x00, #   OO  OO   
    0x66, 0x00, #  OO  OO    
    0x66, 0x00, #  OO  OO    
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @64 '$' (12 pixels wide)
    0x01, 0x40, #        O O  
    0x0F, 0xE0, #     OOOOOOO 
    0x18, 0xF0, #    OO   OOOO
    0x18, 0xE0, #    OO   OOO 
    0x1D, 0x00, #    OOO O    
    0x0F, 0x00, #     OOOO    
    0x0F, 0x80, #     OOOOO   
    0x0B, 0x80, #     O OOO   
    0x79, 0x80, #  OOOO  OO   
    0xF1, 0x80, # OOOO   OO   
    0x7F, 0x00, #  OOOOOOO    
    0x24, 0x00, #   O  O      
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @96 '%' (9 pixels wide)
    0x00, 0x00, #          
    0x71, 0x80, #  OOO   OO
    0x73, 0x00, #  OOO  OO 
    0x76, 0x00, #  OOO OO  
    0x06, 0x00, #      OO  
    0x0C, 0x00, #     OO   
    0x18, 0x00, #    OO    
    0x10, 0x00, #    O     
    0x37, 0x00, #   OO OOO 
    0x67, 0x00, #  OO  OOO 
    0xC7, 0x00, # OO   OOO 
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @128 '&' (11 pixels wide)
    0x00, 0x00, #            
    0x0F, 0x80, #     OOOOO  
    0x18, 0xC0, #    OO   OO 
    0x19, 0xC0, #    OO  OOO 
    0x1F, 0x80, #    OOOOOO  
    0x1C, 0x00, #    OOO     
    0x7C, 0x00, #  OOOOO     
    0xEC, 0x00, # OOO OO     
    0xCE, 0x00, # OO  OOO    
    0xC6, 0x00, # OO   OO    
    0x7F, 0xE0, #  OOOOOOOOOO
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @160 ''' (3 pixels wide)
    0x00, #    
    0x60, #  OO
    0xC0, # OO 
    0xC0, # OO 
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

    # @176 '(' (6 pixels wide)
    0x0C, #     OO
    0x18, #    OO 
    0x30, #   OO  
    0x60, #  OO   
    0x60, #  OO   
    0xC0, # OO    
    0xC0, # OO    
    0xC0, # OO    
    0xC0, # OO    
    0xC0, # OO    
    0x40, #  O    
    0x60, #  OO   
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @192 ')' (6 pixels wide)
    0x18, #    OO 
    0x08, #     O 
    0x0C, #     OO
    0x0C, #     OO
    0x0C, #     OO
    0x0C, #     OO
    0x0C, #     OO
    0x18, #    OO 
    0x18, #    OO 
    0x30, #   OO  
    0x60, #  OO   
    0xC0, # OO    
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @208 '*' (5 pixels wide)
    0xA8, # O O O
    0x70, #  OOO 
    0xF8, # OOOOO
    0x70, #  OOO 
    0xA8, # O O O
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

    # @224 '+' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x06, 0x00, #      OO  
    0x0C, 0x00, #     OO   
    0x0C, 0x00, #     OO   
    0xFF, 0x80, # OOOOOOOOO
    0xFF, 0x00, # OOOOOOOO 
    0x18, 0x00, #    OO    
    0x18, 0x00, #    OO    
    0x30, 0x00, #   OO     
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @256 ',' (3 pixels wide)
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
    0x40, #  O 
    0x80, # O  
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    

    # @272 '-' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x7C, #  OOOOO
    0xF8, # OOOOO 
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @288 '.' (3 pixels wide)
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    
    0x00, #    

    # @304 '/' (7 pixels wide)
    0x00, #        
    0x02, #       O
    0x04, #      O 
    0x08, #     O  
    0x08, #     O  
    0x10, #    O   
    0x10, #    O   
    0x20, #   O    
    0x40, #  O     
    0x40, #  O     
    0x80, # O      
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @320 '0' (10 pixels wide)
    0x00, 0x00, #           
    0x1F, 0x00, #    OOOOO  
    0x3F, 0x80, #   OOOOOOO 
    0x70, 0xC0, #  OOO    OO
    0xE0, 0xC0, # OOO     OO
    0xC0, 0xC0, # OO      OO
    0xC0, 0xC0, # OO      OO
    0xC1, 0xC0, # OO     OOO
    0xC3, 0x80, # OO    OOO 
    0x7F, 0x00, #  OOOOOOO  
    0x3E, 0x00, #   OOOOO   
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @352 '1' (5 pixels wide)
    0x00, #      
    0x70, #  OOO 
    0x78, #  OOOO
    0x30, #   OO 
    0x30, #   OO 
    0x30, #   OO 
    0x60, #  OO  
    0x60, #  OO  
    0x60, #  OO  
    0xE0, # OOO  
    0xC0, # OO   
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      

    # @368 '2' (10 pixels wide)
    0x00, 0x00, #           
    0x3F, 0x80, #   OOOOOOO 
    0x7F, 0xC0, #  OOOOOOOOO
    0x71, 0xC0, #  OOO   OOO
    0x00, 0xC0, #         OO
    0x01, 0x80, #        OO 
    0x03, 0x80, #       OOO 
    0x06, 0x00, #      OO   
    0x3C, 0x00, #   OOOO    
    0x7F, 0xC0, #  OOOOOOOOO
    0xFF, 0x80, # OOOOOOOOO 
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @400 '3' (9 pixels wide)
    0x00, 0x00, #          
    0x3F, 0x80, #   OOOOOOO
    0x7F, 0x00, #  OOOOOOO 
    0x06, 0x00, #      OO  
    0x0E, 0x00, #     OOO  
    0x1F, 0x00, #    OOOOO 
    0x03, 0x80, #       OOO
    0x01, 0x80, #        OO
    0xE1, 0x80, # OOO    OO
    0xE7, 0x00, # OOO  OOO 
    0x7C, 0x00, #  OOOOO   
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @432 '4' (10 pixels wide)
    0x00, 0x00, #           
    0x38, 0xC0, #   OOO   OO
    0x39, 0x80, #   OOO  OO 
    0x39, 0x80, #   OOO  OO 
    0x11, 0x80, #    O   OO 
    0x63, 0x00, #  OO   OO  
    0xFF, 0xC0, # OOOOOOOOOO
    0xFF, 0x80, # OOOOOOOOO 
    0x06, 0x00, #      OO   
    0x06, 0x00, #      OO   
    0x0C, 0x00, #     OO    
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @464 '5' (9 pixels wide)
    0x00, 0x00, #          
    0x1F, 0x80, #    OOOOOO
    0x3F, 0x00, #   OOOOOO 
    0x30, 0x00, #   OO     
    0x30, 0x00, #   OO     
    0x7F, 0x00, #  OOOOOOO 
    0x03, 0x80, #       OOO
    0x01, 0x80, #        OO
    0xF1, 0x80, # OOOO   OO
    0xF3, 0x00, # OOOO  OO 
    0x7C, 0x00, #  OOOOO   
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @496 '6' (9 pixels wide)
    0x00, 0x00, #          
    0x0C, 0x00, #     OO   
    0x18, 0x00, #    OO    
    0x30, 0x00, #   OO     
    0x60, 0x00, #  OO      
    0xC7, 0x00, # OO   OOO 
    0xC7, 0x80, # OO   OOOO
    0xC3, 0x80, # OO    OOO
    0xE1, 0x80, # OOO    OO
    0x7F, 0x00, #  OOOOOOO 
    0x3E, 0x00, #   OOOOO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @528 '7' (8 pixels wide)
    0x00, #         
    0x7F, #  OOOOOOO
    0xFE, # OOOOOOO 
    0x86, # O    OO 
    0x0C, #     OO  
    0x0C, #     OO  
    0x7E, #  OOOOOO 
    0x18, #    OO   
    0x30, #   OO    
    0x30, #   OO    
    0x60, #  OO     
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         

    # @544 '8' (9 pixels wide)
    0x00, 0x00, #          
    0x0F, 0x00, #     OOOO 
    0x3F, 0x80, #   OOOOOOO
    0x31, 0x80, #   OO   OO
    0x31, 0x80, #   OO   OO
    0x7E, 0x00, #  OOOOOO  
    0xE3, 0x00, # OOO   OO 
    0xC3, 0x00, # OO    OO 
    0xC7, 0x00, # OO   OOO 
    0xC6, 0x00, # OO   OO  
    0x3C, 0x00, #   OOOO   
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @576 '9' (8 pixels wide)
    0x00, #         
    0x3C, #   OOOO  
    0x62, #  OO   O 
    0xC3, # OO    OO
    0xC3, # OO    OO
    0xC3, # OO    OO
    0x67, #  OO  OOO
    0x3E, #   OOOOO 
    0x0C, #     OO  
    0x18, #    OO   
    0x30, #   OO    
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         

    # @592 ':' (4 pixels wide)
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x70, #  OOO
    0x70, #  OOO
    0x00, #     
    0xE0, # OOO 
    0xE0, # OOO 
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     

    # @608 ';' (4 pixels wide)
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x70, #  OOO
    0x70, #  OOO
    0x00, #     
    0x60, #  OO 
    0x40, #  O  
    0x80, # O   
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     

    # @624 '<' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x03, #       OO
    0x0E, #     OOO 
    0x3C, #   OOOO  
    0xF0, # OOOO    
    0xC0, # OO      
    0xF0, # OOOO    
    0x38, #   OOO   
    0x1C, #    OOO  
    0x04, #      O  
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         

    # @640 '=' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0xFE, # OOOOOOO
    0xFC, # OOOOOO 
    0x00, #        
    0xFC, # OOOOOO 
    0xFC, # OOOOOO 
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @656 '>' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x20, #   O     
    0x38, #   OOO   
    0x1C, #    OOO  
    0x0F, #     OOOO
    0x03, #       OO
    0x0F, #     OOOO
    0x3C, #   OOOO  
    0x70, #  OOO    
    0xC0, # OO      
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         

    # @672 '?' (8 pixels wide)
    0x00, #         
    0xFE, # OOOOOOO 
    0xE3, # OOO   OO
    0xE3, # OOO   OO
    0x07, #      OOO
    0x3C, #   OOOO  
    0x70, #  OOO    
    0x00, #         
    0x70, #  OOO    
    0x70, #  OOO    
    0x70, #  OOO    
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         

    # @688 '@' (11 pixels wide)
    0x00, 0x00, #            
    0x0F, 0x80, #     OOOOO  
    0x30, 0xC0, #   OO    OO 
    0x40, 0x20, #  O        O
    0x5F, 0xA0, #  O OOOOOO O
    0xB9, 0xA0, # O OOO  OO O
    0xB3, 0x20, # O OO  OO  O
    0xBF, 0xC0, # O OOOOOOOO 
    0xC0, 0x00, # OO         
    0x61, 0x80, #  OO    OO  
    0x1E, 0x00, #    OOOO    
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @720 'A' (21 pixels wide)
    0x00, 0x00, 0x00, #                      
    0x00, 0x03, 0x80, #               OOO    
    0x00, 0x07, 0x00, #              OOO     
    0x00, 0x0B, 0x00, #             O OO     
    0x00, 0x17, 0x00, #            O OOO     
    0x00, 0x26, 0x00, #           O  OO      
    0x0F, 0xFF, 0xF8, #     OOOOOOOOOOOOOOOOO
    0x30, 0x8C, 0x00, #   OO    O   OO       
    0x41, 0x8C, 0x00, #  O     OO   OO       
    0xC7, 0x1C, 0x00, # OO   OOO   OOO       
    0xFC, 0x18, 0x00, # OOOOOO     OO        
    0x78, 0x00, 0x00, #  OOOO                
    0x00, 0x00, 0x00, #                      
    0x00, 0x00, 0x00, #                      
    0x00, 0x00, 0x00, #                      
    0x00, 0x00, 0x00, #                      

    # @768 'B' (13 pixels wide)
    0x00, 0x00, #              
    0x7F, 0xF0, #  OOOOOOOOOOO 
    0xFF, 0xF8, # OOOOOOOOOOOOO
    0x00, 0x18, #            OO
    0x0C, 0x10, #     OO     O 
    0x1C, 0x20, #    OOO    O  
    0x19, 0xC0, #    OO  OOO   
    0x38, 0xC0, #   OOO   OO   
    0x30, 0xC0, #   OO    OO   
    0x31, 0x80, #   OO   OO    
    0x7F, 0x00, #  OOOOOOO     
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @800 'C' (10 pixels wide)
    0x00, 0x00, #           
    0x0F, 0xC0, #     OOOOOO
    0x19, 0xC0, #    OO  OOO
    0x31, 0xC0, #   OO   OOO
    0x60, 0x00, #  OO       
    0xC0, 0x00, # OO        
    0xC0, 0x00, # OO        
    0xC0, 0x00, # OO        
    0xC0, 0x00, # OO        
    0x60, 0x00, #  OO       
    0x3F, 0xC0, #   OOOOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @832 'D' (13 pixels wide)
    0x00, 0x00, #              
    0x7F, 0xE0, #  OOOOOOOOOO  
    0xFF, 0xF0, # OOOOOOOOOOOO 
    0x00, 0x38, #           OOO
    0x18, 0x18, #    OO      OO
    0x18, 0x18, #    OO      OO
    0x38, 0x10, #   OOO      O 
    0x30, 0x30, #   OO      OO 
    0x30, 0x60, #   OO     OO  
    0x73, 0x80, #  OOO  OOO    
    0x7E, 0x00, #  OOOOOO      
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @864 'E' (11 pixels wide)
    0x00, 0x00, #            
    0x07, 0xE0, #      OOOOOO
    0x18, 0xE0, #    OO   OOO
    0x18, 0xE0, #    OO   OOO
    0x1C, 0x00, #    OOO     
    0x1C, 0x00, #    OOO     
    0x70, 0x00, #  OOO       
    0xC0, 0x00, # OO         
    0xC0, 0x00, # OO         
    0xC0, 0x00, # OO         
    0x7F, 0xE0, #  OOOOOOOOOO
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @896 'F' (14 pixels wide)
    0x00, 0x00, #               
    0x3F, 0xFC, #   OOOOOOOOOOOO
    0x7F, 0xF8, #  OOOOOOOOOOOO 
    0xC0, 0xC0, # OO      OO    
    0x9C, 0xC0, # O  OOO  OO    
    0xFC, 0xC0, # OOOOOO  OO    
    0x79, 0xF0, #  OOOO  OOOOO  
    0x01, 0x80, #        OO     
    0x01, 0x80, #        OO     
    0x7B, 0x00, #  OOOO OO      
    0xFE, 0x00, # OOOOOOO       
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @928 'G' (11 pixels wide)
    0x00, 0x00, #            
    0x07, 0xE0, #      OOOOOO
    0x18, 0xE0, #    OO   OOO
    0x30, 0xE0, #   OO    OOO
    0x60, 0x00, #  OO        
    0xC0, 0x00, # OO         
    0xC0, 0xC0, # OO      OO 
    0xC0, 0xC0, # OO      OO 
    0xE1, 0xC0, # OOO    OOO 
    0x71, 0x80, #  OOO   OO  
    0x1F, 0x80, #    OOOOOO  
    0x01, 0x80, #        OO  
    0x01, 0x00, #        O   
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @960 'H' (21 pixels wide)
    0x00, 0x60, 0x00, #          OO          
    0x00, 0x61, 0x80, #          OO    OO    
    0x00, 0xE3, 0x00, #         OOO   OO     
    0x00, 0xC3, 0x00, #         OO    OO     
    0x00, 0xC7, 0x00, #         OO   OOO     
    0x00, 0xC6, 0x00, #         OO   OO      
    0x1F, 0xFF, 0xF8, #    OOOOOOOOOOOOOOOOOO
    0x71, 0x8C, 0x00, #  OOO   OO   OO       
    0xE3, 0x8C, 0x00, # OOO   OOO   OO       
    0xC3, 0x1C, 0x00, # OO    OO   OOO       
    0xC6, 0x18, 0x00, # OO   OO    OO        
    0x78, 0x00, 0x00, #  OOOO                
    0x00, 0x00, 0x00, #                      
    0x00, 0x00, 0x00, #                      
    0x00, 0x00, 0x00, #                      
    0x00, 0x00, 0x00, #                      

    # @1008 'I' (11 pixels wide)
    0x00, 0x00, #            
    0x3F, 0xE0, #   OOOOOOOOO
    0x7F, 0xE0, #  OOOOOOOOOO
    0xC0, 0xC0, # OO      OO 
    0x9C, 0xC0, # O  OOO  OO 
    0xFC, 0xC0, # OOOOOO  OO 
    0x79, 0x80, #  OOOO  OO  
    0x01, 0x80, #        OO  
    0x01, 0x80, #        OO  
    0x73, 0x00, #  OOO  OO   
    0xFE, 0x00, # OOOOOOO    
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @1040 'J' (12 pixels wide)
    0x00, 0x00, #             
    0x3F, 0xF0, #   OOOOOOOOOO
    0x7F, 0xE0, #  OOOOOOOOOO 
    0xC0, 0x60, # OO       OO 
    0x9C, 0xC0, # O  OOO  OO  
    0xFC, 0xC0, # OOOOOO  OO  
    0x79, 0x80, #  OOOO  OO   
    0x01, 0x80, #        OO   
    0x03, 0x80, #       OOO   
    0x03, 0x00, #       OO    
    0xE6, 0x00, # OOO  OO     
    0xFC, 0x00, # OOOOOO      
    0x78, 0x00, #  OOOO       
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1072 'K' (13 pixels wide)
    0x00, 0x00, #              
    0x7C, 0x18, #  OOOOO     OO
    0xFC, 0x30, # OOOOOO    OO 
    0x0C, 0x60, #     OO   OO  
    0x1C, 0xC0, #    OOO  OO   
    0x19, 0x80, #    OO  OO    
    0x1B, 0xC0, #    OO OOOO   
    0x36, 0xC0, #   OO OO OO   
    0x3D, 0xC0, #   OOOO OOO   
    0x39, 0x80, #   OOO  OO    
    0x71, 0xF0, #  OOO   OOOOO 
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @1104 'L' (16 pixels wide)
    0x00, 0x00, #                 
    0x00, 0x1E, #            OOOO 
    0x00, 0x7F, #          OOOOOOO
    0x00, 0xE7, #         OOO  OOO
    0x00, 0xC0, #         OO      
    0x00, 0xC0, #         OO      
    0x00, 0xC0, #         OO      
    0x00, 0xC0, #         OO      
    0x01, 0x80, #        OO       
    0x63, 0x00, #  OO   OO        
    0xFF, 0xFE, # OOOOOOOOOOOOOOO 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 

    # @1136 'M' (17 pixels wide)
    0x00, 0x00, 0x00, #                  
    0x7C, 0x00, 0x00, #  OOOOO           
    0xFC, 0x60, 0x00, # OOOOOO   OO      
    0x18, 0xE0, 0x00, #    OO   OOO      
    0x19, 0xCE, 0x00, #    OO  OOO  OOO  
    0x1B, 0xDC, 0x00, #    OO OOOO OOO   
    0x37, 0xBC, 0x00, #   OO OOOO OOOO   
    0x3D, 0xEC, 0x00, #   OOOO OOOO OO   
    0x39, 0xCC, 0x00, #   OOO  OOO  OO   
    0x63, 0x98, 0x00, #  OO   OOO  OO    
    0x63, 0x1F, 0x80, #  OO   OO   OOOOOO
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  

    # @1184 'N' (16 pixels wide)
    0x00, 0x00, #                 
    0x03, 0x87, #       OOO    OOO
    0x03, 0x8F, #       OOO   OOOO
    0x03, 0xCF, #       OOOO  OOOO
    0x06, 0xCC, #      OO OO  OO  
    0x06, 0xD8, #      OO OO OO   
    0x06, 0xF8, #      OO OOOOO   
    0x0C, 0x78, #     OO   OOOO   
    0x0C, 0x70, #     OO   OOO    
    0x7C, 0x30, #  OOOOO    OO    
    0xF8, 0x30, # OOOOO     OO    
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 
    0x00, 0x00, #                 

    # @1216 'O' (13 pixels wide)
    0x00, 0x00, #              
    0x7F, 0xE0, #  OOOOOOOOOO  
    0xFF, 0xF0, # OOOOOOOOOOOO 
    0x00, 0x38, #           OOO
    0x1C, 0x18, #    OOO     OO
    0x38, 0x18, #   OOO      OO
    0x30, 0x18, #   OO       OO
    0x30, 0x30, #   OO      OO 
    0x30, 0x60, #   OO     OO  
    0x18, 0xC0, #    OO   OO   
    0x0F, 0x80, #     OOOOO    
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @1248 'P' (12 pixels wide)
    0x00, 0x00, #             
    0x7F, 0xE0, #  OOOOOOOOOO 
    0xFF, 0xF0, # OOOOOOOOOOOO
    0x00, 0x30, #           OO
    0x18, 0x30, #    OO     OO
    0x18, 0xE0, #    OO   OOO 
    0x37, 0xC0, #   OO OOOOO  
    0x3F, 0x00, #   OOOOOO    
    0x30, 0x00, #   OO        
    0x70, 0x00, #  OOO        
    0x60, 0x00, #  OO         
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1280 'Q' (12 pixels wide)
    0x00, 0x00, #             
    0x0F, 0xC0, #     OOOOOO  
    0x1F, 0xE0, #    OOOOOOOO 
    0x30, 0x70, #   OO     OOO
    0x3C, 0x30, #   OOOO    OO
    0x3C, 0x30, #   OOOO    OO
    0x1C, 0x30, #    OOO    OO
    0x00, 0x60, #          OO 
    0x00, 0xC0, #         OO  
    0x61, 0x00, #  OO    O    
    0xFF, 0xF0, # OOOOOOOOOOOO
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1312 'R' (13 pixels wide)
    0x00, 0x00, #              
    0x7F, 0xF0, #  OOOOOOOOOOO 
    0xFF, 0xF8, # OOOOOOOOOOOOO
    0x00, 0x18, #            OO
    0x0C, 0x18, #     OO     OO
    0x0C, 0x30, #     OO    OO 
    0x1C, 0xE0, #    OOO  OOO  
    0x1B, 0x80, #    OO OOO    
    0x19, 0x80, #    OO  OO    
    0x38, 0xC0, #   OOO   OO   
    0x30, 0xF8, #   OO    OOOOO
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @1344 'S' (15 pixels wide)
    0x00, 0x00, #                
    0x00, 0x3E, #           OOOOO
    0x00, 0x6E, #          OO OOO
    0x00, 0x6E, #          OO OOO
    0x00, 0x60, #          OO    
    0x00, 0x70, #          OOO   
    0x7E, 0x30, #  OOOOOO   OO   
    0xC0, 0x30, # OO        OO   
    0xC0, 0x30, # OO        OO   
    0x60, 0x60, #  OO      OO    
    0x3F, 0x80, #   OOOOOOO      
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @1376 'T' (15 pixels wide)
    0x00, 0x00, #                
    0x3F, 0xFE, #   OOOOOOOOOOOOO
    0x7F, 0xFC, #  OOOOOOOOOOOOO 
    0xC0, 0x60, # OO       OO    
    0x9C, 0xE0, # O  OOO  OOO    
    0xFC, 0xC0, # OOOOOO  OO     
    0x78, 0xC0, #  OOOO   OO     
    0x01, 0xC0, #        OOO     
    0x01, 0x80, #        OO      
    0x71, 0x80, #  OOO   OO      
    0xFF, 0x00, # OOOOOOOO       
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @1408 'U' (12 pixels wide)
    0x00, 0x00, #             
    0x7C, 0x60, #  OOOOO   OO 
    0xFC, 0xF0, # OOOOOO  OOOO
    0x18, 0x70, #    OO    OOO
    0x18, 0x30, #    OO     OO
    0x18, 0x60, #    OO    OO 
    0x30, 0x60, #   OO     OO 
    0x30, 0xC0, #   OO    OO  
    0x31, 0xC0, #   OO   OOO  
    0x3F, 0x80, #   OOOOOOO   
    0x1F, 0x00, #    OOOOO    
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1440 'V' (13 pixels wide)
    0x00, 0x00, #              
    0x7C, 0x38, #  OOOOO    OOO
    0xFC, 0x38, # OOOOOO    OOO
    0x0C, 0x38, #     OO    OOO
    0x1C, 0x30, #    OOO    OO 
    0x1C, 0x60, #    OOO   OO  
    0x18, 0xC0, #    OO   OO   
    0x19, 0x80, #    OO  OO    
    0x1B, 0x00, #    OO OO     
    0x1E, 0x00, #    OOOO      
    0x1C, 0x00, #    OOO       
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @1472 'W' (17 pixels wide)
    0x00, 0x00, 0x00, #                  
    0x7C, 0x61, 0x80, #  OOOOO   OO    OO
    0xFC, 0xE3, 0x00, # OOOOOO  OOO   OO 
    0x0C, 0xE7, 0x00, #     OO  OOO  OOO 
    0x0D, 0xE6, 0x00, #     OO OOOO  OO  
    0x0D, 0xEC, 0x00, #     OO OOOO OO   
    0x0F, 0x6C, 0x00, #     OOOO OO OO   
    0x1A, 0x78, 0x00, #    OO O  OOOO    
    0x1E, 0x70, 0x00, #    OOOO  OOO     
    0x1C, 0x70, 0x00, #    OOO   OOO     
    0x1C, 0x60, 0x00, #    OOO   OO      
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  

    # @1520 'X' (14 pixels wide)
    0x00, 0x00, #               
    0x3E, 0x1C, #   OOOOO    OOO
    0x7F, 0x3C, #  OOOOOOO  OOOO
    0x03, 0x7C, #       OO OOOOO
    0x03, 0xC0, #       OOOO    
    0x03, 0x80, #       OOO     
    0x03, 0x80, #       OOO     
    0x07, 0x80, #      OOOO     
    0xFD, 0x80, # OOOOOO OO     
    0xF1, 0x80, # OOOO   OO     
    0xE0, 0xF8, # OOO     OOOOO 
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @1552 'Y' (14 pixels wide)
    0x00, 0x00, #               
    0xFF, 0x0C, # OOOOOOOO    OO
    0xE3, 0x1C, # OOO   OO   OOO
    0xE6, 0x38, # OOO  OO   OOO 
    0x06, 0x78, #      OO  OOOO 
    0x06, 0xF8, #      OO OOOOO 
    0x0F, 0xB0, #     OOOOO OO  
    0x0F, 0x30, #     OOOO  OO  
    0x00, 0x30, #           OO  
    0x00, 0x60, #          OO   
    0x1F, 0xE0, #    OOOOOOOO   
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @1584 'Z' (15 pixels wide)
    0x00, 0x00, #                
    0x0F, 0xF0, #     OOOOOOOO   
    0x1F, 0xF0, #    OOOOOOOOO   
    0x01, 0xC0, #        OOO     
    0x0E, 0x00, #     OOO        
    0x03, 0x00, #       OO       
    0x0F, 0xFE, #     OOOOOOOOOOO
    0x39, 0x80, #   OOO  OO      
    0x71, 0x80, #  OOO   OO      
    0xE3, 0x00, # OOO   OO       
    0xC3, 0x00, # OO    OO       
    0xCE, 0x00, # OO  OOO        
    0x78, 0x00, #  OOOO          
    0x00, 0x00, #                
    0x00, 0x00, #                
    0x00, 0x00, #                

    # @1616 '[' (7 pixels wide)
    0x0E, #     OOO
    0x18, #    OO  
    0x18, #    OO  
    0x30, #   OO   
    0x30, #   OO   
    0x30, #   OO   
    0x60, #  OO    
    0x60, #  OO    
    0x60, #  OO    
    0xE0, # OOO    
    0xC0, # OO     
    0xE0, # OOO    
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @1632 '\' (6 pixels wide)
    0xC0, # OO    
    0x60, #  OO   
    0x60, #  OO   
    0x60, #  OO   
    0x30, #   OO  
    0x30, #   OO  
    0x30, #   OO  
    0x18, #    OO 
    0x18, #    OO 
    0x18, #    OO 
    0x0C, #     OO
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @1648 ']' (7 pixels wide)
    0x0E, #     OOO
    0x06, #      OO
    0x06, #      OO
    0x0C, #     OO 
    0x0C, #     OO 
    0x0C, #     OO 
    0x18, #    OO  
    0x18, #    OO  
    0x18, #    OO  
    0x38, #   OOO  
    0x30, #   OO   
    0xF0, # OOOO   
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @1664 '^' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x18, #    OO 
    0x38, #   OOO 
    0x68, #  OO O 
    0xCC, # OO  OO
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @1680 '_' (17 pixels wide)
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x00, 0x00, 0x00, #                  
    0x7F, 0xFF, 0x80, #  OOOOOOOOOOOOOOOO
    0xFF, 0xFF, 0x00, # OOOOOOOOOOOOOOOO 

    # @1728 '`' (3 pixels wide)
    0x00, #    
    0x00, #    
    0x00, #    
    0xC0, # OO 
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

    # @1744 'a' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x7C, 0x00, #  OOOOO   
    0xEC, 0x00, # OOO OO   
    0xCC, 0x00, # OO  OO   
    0xDC, 0x00, # OO OOO   
    0x7F, 0x80, #  OOOOOOOO
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1776 'b' (13 pixels wide)
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x18, 0x00, #    OO        
    0x30, 0x00, #   OO         
    0x30, 0x00, #   OO         
    0x30, 0x00, #   OO         
    0x67, 0xF8, #  OO  OOOOOOOO
    0x66, 0x00, #  OO  OO      
    0x66, 0x00, #  OO  OO      
    0xEC, 0x00, # OOO OO       
    0xF8, 0x00, # OOOOO        
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @1808 'c' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x7E, 0x00, #  OOOOOO  
    0xE6, 0x00, # OOO  OO  
    0xC0, 0x00, # OO       
    0xC0, 0x00, # OO       
    0x7F, 0x80, #  OOOOOOOO
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1840 'd' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x03, 0x00, #       OO  
    0x06, 0x00, #      OO   
    0x06, 0x00, #      OO   
    0x06, 0x00, #      OO   
    0x3C, 0x00, #   OOOO    
    0xEC, 0x00, # OOO OO    
    0xCC, 0x00, # OO  OO    
    0xCC, 0x00, # OO  OO    
    0xFF, 0xC0, # OOOOOOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1872 'e' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x7C, 0x00, #  OOOOO   
    0xE6, 0x00, # OOO  OO  
    0xC6, 0x00, # OO   OO  
    0xC0, 0x00, # OO       
    0x7F, 0x80, #  OOOOOOOO
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1904 'f' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x0C, 0x00, #     OO      
    0x18, 0x00, #    OO       
    0x18, 0x00, #    OO       
    0x18, 0x00, #    OO       
    0x7F, 0xF0, #  OOOOOOOOOOO
    0x3C, 0x00, #   OOOO      
    0x6C, 0x00, #  OO OO      
    0x6C, 0x00, #  OO OO      
    0x6C, 0x00, #  OO OO      
    0xD8, 0x00, # OO OO       
    0xD0, 0x00, # OO O        
    0xE0, 0x00, # OOO         
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1936 'g' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x3E, 0x00, #   OOOOO  
    0xE6, 0x00, # OOO  OO  
    0xC6, 0x00, # OO   OO  
    0xCC, 0x00, # OO  OO   
    0x7F, 0x80, #  OOOOOOOO
    0x6C, 0x00, #  OO OO   
    0x6C, 0x00, #  OO OO   
    0x78, 0x00, #  OOOO    
    0x70, 0x00, #  OOO     
    0x00, 0x00, #          

    # @1968 'h' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x18, 0x00, #    OO     
    0x30, 0x00, #   OO      
    0x30, 0x00, #   OO      
    0x30, 0x00, #   OO      
    0x66, 0x00, #  OO  OO   
    0x6E, 0x00, #  OO OOO   
    0x76, 0x00, #  OOO OO   
    0xEE, 0x00, # OOO OOO   
    0xCF, 0xC0, # OO  OOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @2000 'i' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x38, #   OOO 
    0x38, #   OOO 
    0x38, #   OOO 
    0x00, #       
    0x60, #  OO   
    0x60, #  OO   
    0x60, #  OO   
    0xE0, # OOO   
    0xFC, # OOOOOO
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @2016 'j' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x07, #      OOO
    0x07, #      OOO
    0x07, #      OOO
    0x00, #         
    0x0C, #     OO  
    0x0C, #     OO  
    0x0C, #     OO  
    0x1C, #    OOO  
    0x7F, #  OOOOOOO
    0xD8, # OO OO   
    0xD8, # OO OO   
    0xF0, # OOOO    
    0x00, #         
    0x00, #         

    # @2032 'k' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x18, 0x00, #    OO     
    0x30, 0x00, #   OO      
    0x30, 0x00, #   OO      
    0x34, 0x00, #   OO O    
    0x6E, 0x00, #  OO OOO   
    0x6E, 0x00, #  OO OOO   
    0x76, 0x00, #  OOO OO   
    0xEE, 0x00, # OOO OOO   
    0xCF, 0xC0, # OO  OOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @2064 'l' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x18, #    OO 
    0x30, #   OO  
    0x30, #   OO  
    0x30, #   OO  
    0x60, #  OO   
    0x60, #  OO   
    0x60, #  OO   
    0xE0, # OOO   
    0xFC, # OOOOOO
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @2080 'm' (14 pixels wide)
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x67, 0x40, #  OO  OOO O    
    0x6E, 0xC0, #  OO OOO OO    
    0x77, 0xC0, #  OOO OOOOO    
    0xEE, 0xC0, # OOO OOO OO    
    0xCC, 0xFC, # OO  OO  OOOOOO
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               
    0x00, 0x00, #               

    # @2112 'n' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x66, 0x00, #  OO  OO   
    0x6E, 0x00, #  OO OOO   
    0x76, 0x00, #  OOO OO   
    0xEE, 0x00, # OOO OOO   
    0xCF, 0xC0, # OO  OOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @2144 'o' (13 pixels wide)
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x7F, 0xF8, #  OOOOOOOOOOOO
    0xE6, 0x00, # OOO  OO      
    0xCE, 0x00, # OO  OOO      
    0xCE, 0x00, # OO  OOO      
    0x7C, 0x00, #  OOOOO       
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              
    0x00, 0x00, #              

    # @2176 'p' (11 pixels wide)
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x18, 0x00, #    OO      
    0x18, 0x00, #    OO      
    0x3F, 0x00, #   OOOOOO   
    0x33, 0x80, #   OO  OOO  
    0x31, 0x80, #   OO   OO  
    0x73, 0x00, #  OOO  OO   
    0x67, 0xE0, #  OO  OOOOOO
    0x60, 0x00, #  OO        
    0x60, 0x00, #  OO        
    0xC0, 0x00, # OO         
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @2208 'q' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x7C, 0x00, #  OOOOO   
    0xEC, 0x00, # OOO OO   
    0xCC, 0x00, # OO  OO   
    0xDC, 0x00, # OO OOO   
    0xFF, 0x80, # OOOOOOOOO
    0x18, 0x00, #    OO    
    0x18, 0x00, #    OO    
    0x10, 0x00, #    O     
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @2240 'r' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x60, 0x00, #  OO      
    0xC0, 0x00, # OO       
    0xF8, 0x00, # OOOOO    
    0x58, 0x00, #  O OO    
    0x98, 0x00, # O  OO    
    0xB8, 0x00, # O OOO    
    0x3F, 0x80, #   OOOOOOO
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @2272 's' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x08, 0x00, #     O    
    0x18, 0x00, #    OO    
    0x18, 0x00, #    OO    
    0x1C, 0x00, #    OOO   
    0x2C, 0x00, #   O OO   
    0xEC, 0x00, # OOO OO   
    0xFF, 0x80, # OOOOOOOOO
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @2304 't' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x10, #    O   
    0x30, #   OO   
    0x70, #  OOO   
    0xF8, # OOOOO  
    0x60, #  OO    
    0x60, #  OO    
    0xE0, # OOO    
    0xFE, # OOOOOOO
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @2320 'u' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x66, 0x00, #  OO  OO   
    0x66, 0x00, #  OO  OO   
    0x66, 0x00, #  OO  OO   
    0xCC, 0x00, # OO  OO    
    0xFF, 0xC0, # OOOOOOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @2352 'v' (11 pixels wide)
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0xC7, 0xE0, # OO   OOOOOO
    0xC8, 0x00, # OO  O      
    0xD0, 0x00, # OO O       
    0xE0, 0x00, # OOO        
    0xC0, 0x00, # OO         
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @2384 'w' (11 pixels wide)
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x66, 0x60, #  OO  OO  OO
    0x66, 0x60, #  OO  OO  OO
    0x66, 0x60, #  OO  OO  OO
    0xCC, 0xC0, # OO  OO  OO 
    0xFF, 0xC0, # OOOOOOOOOO 
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @2416 'x' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x76, #  OOO OO
    0x3C, #   OOOO 
    0x18, #    OO  
    0x6C, #  OO OO 
    0xCE, # OO  OOO
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @2432 'y' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x66, 0x00, #  OO  OO   
    0x66, 0x00, #  OO  OO   
    0x66, 0x00, #  OO  OO   
    0xCC, 0x00, # OO  OO    
    0xFF, 0xC0, # OOOOOOOOOO
    0x6C, 0x00, #  OO OO    
    0x6C, 0x00, #  OO OO    
    0x78, 0x00, #  OOOO     
    0x70, 0x00, #  OOO      
    0x00, 0x00, #           

    # @2464 'z' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0xFC, # OOOOOO  
    0x18, #    OO   
    0x30, #   OO    
    0xE0, # OOO     
    0xFF, # OOOOOOOO
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         

    # @2480 '{' (7 pixels wide)
    0x0E, #     OOO
    0x18, #    OO  
    0x18, #    OO  
    0x30, #   OO   
    0x30, #   OO   
    0x40, #  O     
    0x60, #  OO    
    0x60, #  OO    
    0x60, #  OO    
    0xC0, # OO     
    0xC0, # OO     
    0xE0, # OOO    
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @2496 '|' (1 pixels wide)
    0x80, # O
    0x80, # O
    0x80, # O
    0x80, # O
    0x80, # O
    0x80, # O
    0x80, # O
    0x80, # O
    0x80, # O
    0x80, # O
    0x80, # O
    0x80, # O
    0x00, #  
    0x00, #  
    0x00, #  
    0x00, #  

    # @2512 '}' (7 pixels wide)
    0x0E, #     OOO
    0x06, #      OO
    0x06, #      OO
    0x0C, #     OO 
    0x0C, #     OO 
    0x0C, #     OO 
    0x0C, #     OO 
    0x18, #    OO  
    0x18, #    OO  
    0x38, #   OOO  
    0x30, #   OO   
    0xE0, # OOO    
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @2528 '~' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x38, 0x80, #   OOO   O
    0x7F, 0x00, #  OOOOOOO 
    0x8E, 0x00, # O   OOO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @2560 '°' (4 pixels wide)
    0x60, #  OO 
    0x90, # O  O
    0x90, # O  O
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
)

descriptors = (
    (6,0),# !
    (6,16),# "
    (11,32),# #
    (12,64),# $
    (9,96),# %
    (11,128),# &
    (3,160),# '
    (6,176),# (
    (6,192),# )
    (5,208),# *
    (9,224),# +
    (3,256),# ,
    (6,272),# -
    (3,288),# .
    (7,304),# /
    (10,320),# 0
    (5,352),# 1
    (10,368),# 2
    (9,400),# 3
    (10,432),# 4
    (9,464),# 5
    (9,496),# 6
    (8,528),# 7
    (9,544),# 8
    (8,576),# 9
    (4,592),# :
    (4,608),# ;
    (8,624),# <
    (7,640),# =
    (8,656),# >
    (8,672),# ?
    (11,688),# @
    (21,720),# A
    (13,768),# B
    (10,800),# C
    (13,832),# D
    (11,864),# E
    (14,896),# F
    (11,928),# G
    (21,960),# H
    (11,1008),# I
    (12,1040),# J
    (13,1072),# K
    (16,1104),# L
    (17,1136),# M
    (16,1184),# N
    (13,1216),# O
    (12,1248),# P
    (12,1280),# Q
    (13,1312),# R
    (15,1344),# S
    (15,1376),# T
    (12,1408),# U
    (13,1440),# V
    (17,1472),# W
    (14,1520),# X
    (14,1552),# Y
    (15,1584),# Z
    (7,1616),# [
    (6,1632),# \
    (7,1648),# ]
    (6,1664),# ^
    (17,1680),# _
    (3,1728),# `
    (9,1744),# a
    (13,1776),# b
    (9,1808),# c
    (10,1840),# d
    (9,1872),# e
    (12,1904),# f
    (9,1936),# g
    (10,1968),# h
    (6,2000),# i
    (8,2016),# j
    (10,2032),# k
    (6,2064),# l
    (14,2080),# m
    (10,2112),# n
    (13,2144),# o
    (11,2176),# p
    (9,2208),# q
    (9,2240),# r
    (9,2272),# s
    (7,2304),# t
    (10,2320),# u
    (11,2352),# v
    (11,2384),# w
    (7,2416),# x
    (10,2432),# y
    (8,2464),# z
    (7,2480),# {
    (1,2496),# |
    (7,2512),# }
    (9,2528),# ~
    (4,2560),# °
)

kerning = (
    (3,5,3,3,5,3,5,4,2,5,4,3,3,3,3,4,5,4,4,4,3,4,5,3,5,3,2,4,4,3,6,4,3,5,4,5,3,5,4,3,5,5,5,3,5,3,5,5,3,5,3,5,5,5,5,4,6,3,3,5,1,2,0,5,3,3,3,3,3,2,3,3,3,2,3,3,3,3,3,2,3,4,3,3,3,3,3,3,3,3,3,6,1,3,6,),
    (3,5,2,2,5,2,5,4,2,5,1,3,0,3,1,4,5,4,4,4,3,3,5,3,5,2,2,1,0,3,6,4,0,5,3,5,2,5,3,0,5,5,5,0,5,0,5,5,3,5,0,5,5,5,5,4,6,2,3,5,1,0,0,5,0,3,0,0,0,2,0,3,3,0,3,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,3,6,1,0,6,),
    (9,10,10,8,9,10,10,10,7,11,9,8,9,8,8,11,9,9,9,10,9,10,10,10,11,9,9,10,9,8,10,10,8,10,10,10,10,11,10,9,11,11,10,7,10,7,10,10,9,10,10,11,10,10,10,9,10,8,9,9,7,10,0,10,10,9,10,10,10,8,10,9,9,6,9,9,9,9,10,8,10,10,7,9,9,10,9,8,9,8,9,11,7,9,10,),
    (10,12,9,9,11,9,12,10,8,12,9,9,9,9,8,10,11,11,11,10,10,9,12,10,11,9,8,9,9,10,12,10,9,12,9,12,9,11,9,9,11,11,12,8,12,8,12,12,9,12,9,11,12,12,12,11,12,9,9,11,7,9,0,11,9,9,9,9,9,8,9,9,10,7,9,9,9,9,9,8,9,9,9,9,9,9,9,8,9,9,9,12,7,9,12,),
    (8,8,7,8,8,8,8,8,7,8,6,7,8,8,8,8,8,8,8,7,8,8,8,8,7,8,7,6,8,8,9,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,8,8,8,6,4,0,7,8,8,8,8,8,7,8,8,8,7,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,9,6,8,9,),
    (11,10,10,10,11,10,10,10,10,10,6,10,7,11,11,9,11,11,10,8,10,9,10,9,10,11,10,7,7,11,10,9,11,10,9,10,10,11,8,11,11,11,10,11,10,11,10,10,11,10,9,11,10,10,10,11,10,11,11,9,9,6,0,10,10,11,10,11,10,10,10,11,11,10,11,11,11,11,10,10,11,9,11,11,11,11,11,11,11,11,11,11,9,7,10,),
    (0,2,0,0,2,0,2,1,0,2,0,0,0,0,0,1,2,1,1,1,0,0,2,0,2,0,0,0,0,0,3,1,0,2,0,2,0,2,0,0,2,2,2,0,2,0,2,2,0,2,0,2,2,2,2,1,3,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,),
    (2,4,2,2,4,2,4,2,3,6,2,3,2,3,2,3,4,3,3,3,2,2,4,2,3,2,3,2,2,2,5,2,2,4,2,4,2,3,2,2,3,3,4,2,4,2,4,4,2,4,2,3,4,4,4,3,5,3,3,6,3,2,0,3,2,2,2,2,2,3,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,6,3,2,5,),
    (5,6,5,4,5,5,6,6,2,6,6,3,5,5,4,6,5,5,5,6,5,6,6,6,6,5,5,6,6,4,6,6,4,6,6,6,5,6,6,5,6,6,6,3,6,3,6,6,4,6,5,6,6,6,6,5,6,4,5,5,3,5,0,6,5,5,5,5,5,5,5,5,5,2,5,5,5,5,5,4,5,6,4,6,5,6,5,5,5,6,5,6,2,5,6,),
    (3,5,4,2,4,2,5,4,2,5,1,2,0,2,1,5,4,4,4,3,3,4,5,3,5,1,1,3,0,3,5,4,0,5,4,5,2,5,4,0,5,5,5,0,5,0,5,5,3,5,0,5,5,5,5,4,5,2,3,5,1,2,0,4,0,3,0,0,0,2,0,3,3,0,3,3,0,0,0,2,0,4,1,3,0,0,0,0,0,0,3,5,1,0,5,),
    (8,7,6,5,6,7,7,9,5,7,9,6,5,6,6,9,7,6,6,8,8,9,7,8,9,7,7,9,9,5,7,9,4,7,9,7,7,9,9,5,9,9,7,3,7,4,7,7,7,7,7,9,7,7,7,6,7,4,7,7,5,7,0,6,7,7,7,6,7,7,6,7,7,4,7,7,7,7,7,6,7,9,6,8,7,8,7,7,7,8,8,9,5,6,7,),
    (3,0,2,3,2,3,0,3,1,0,1,2,0,3,2,2,3,2,3,0,3,2,1,3,0,3,2,0,3,2,2,2,3,1,2,2,3,2,2,3,2,2,1,2,2,2,0,2,2,1,2,2,1,0,0,3,0,3,3,0,1,0,0,0,3,3,3,3,3,2,3,3,3,1,3,3,3,3,3,2,3,3,3,3,3,3,3,2,3,3,3,3,1,0,0,),
    (5,0,6,4,3,6,3,6,3,1,3,3,5,5,4,6,5,3,5,6,5,6,3,6,4,5,5,6,5,3,4,6,4,4,6,4,6,0,6,5,0,0,4,0,4,2,4,4,0,3,6,0,4,3,3,5,2,4,5,3,3,6,0,3,6,5,6,6,6,4,6,5,5,2,5,5,5,5,6,4,6,5,3,5,5,6,5,4,5,3,5,6,3,5,2,),
    (3,0,2,3,3,3,0,3,2,0,1,2,3,3,3,3,3,3,3,0,3,3,2,3,1,3,2,1,3,3,2,3,3,2,3,2,3,3,3,3,3,3,2,3,2,3,1,2,3,1,3,3,1,0,0,3,0,3,3,0,1,0,0,0,3,3,3,3,3,2,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,1,3,0,),
    (4,6,4,3,6,3,6,4,3,6,4,4,2,4,1,5,6,5,5,5,4,4,6,4,5,3,3,4,4,4,7,4,2,6,4,6,3,5,4,2,5,5,6,1,6,1,6,6,3,6,3,5,6,6,6,5,7,3,4,6,2,3,0,5,3,3,3,3,3,3,3,3,4,1,3,3,3,3,3,2,3,4,2,4,3,4,3,3,3,4,4,7,2,2,7,),
    (9,10,10,8,9,10,10,10,7,10,10,7,9,9,8,10,9,9,9,10,9,10,10,10,10,9,9,10,10,8,10,10,8,9,10,9,10,10,10,9,10,10,9,7,9,7,9,9,8,9,10,10,9,9,9,9,10,8,9,9,7,10,0,10,10,9,10,10,10,9,10,9,9,6,9,9,9,9,10,8,10,10,8,10,9,10,9,9,9,10,9,10,7,9,9,),
    (3,5,3,3,4,3,5,4,1,5,4,2,3,3,2,4,4,4,4,3,3,4,5,3,4,3,2,4,4,3,5,4,3,5,4,5,3,4,4,3,4,4,5,2,5,2,5,5,2,5,3,4,5,5,5,4,5,3,3,4,1,3,0,4,3,3,3,3,3,2,3,3,3,1,3,3,3,3,3,2,3,4,3,3,3,3,3,2,3,3,3,5,1,3,5,),
    (10,10,9,10,9,10,10,10,8,10,9,9,6,10,9,10,10,9,10,9,10,9,10,10,10,10,9,9,10,9,10,9,10,10,9,10,10,10,9,10,10,10,10,9,10,9,10,10,9,10,9,10,10,10,10,10,10,10,10,9,8,8,0,10,10,10,10,10,10,9,10,10,10,8,10,10,10,10,10,9,10,10,10,10,10,10,10,9,10,10,10,10,8,7,10,),
    (9,8,9,8,8,9,8,9,6,8,9,7,9,9,8,9,8,7,9,9,9,9,8,9,8,8,8,9,9,7,9,9,8,8,9,8,9,8,9,9,8,8,8,7,8,7,8,8,7,8,9,8,8,8,8,9,9,8,8,8,6,9,0,7,9,8,9,9,9,8,9,8,8,5,8,8,8,8,9,7,9,9,8,9,8,9,8,8,8,9,8,9,6,9,9,),
    (9,9,9,7,9,9,9,10,6,9,10,7,8,7,7,10,9,8,8,10,7,10,9,10,9,9,9,10,10,7,10,10,7,9,10,9,9,9,10,8,9,9,9,6,9,6,9,9,7,9,9,9,9,9,9,8,10,7,9,9,7,9,0,9,9,9,9,9,9,9,9,9,9,6,9,9,9,9,9,8,9,10,7,10,9,10,9,9,9,10,9,10,6,8,10,),
    (9,8,9,8,8,9,8,9,6,8,9,7,9,9,8,9,8,7,9,9,9,9,8,9,8,8,8,9,9,7,9,9,8,8,9,8,9,8,9,9,8,8,8,7,8,7,8,8,7,8,9,8,8,8,8,9,9,8,8,8,6,9,0,6,9,8,9,9,9,8,9,8,8,5,8,8,8,8,9,7,9,9,8,9,8,9,8,8,8,9,8,9,6,9,9,),
    (9,5,9,8,7,9,6,9,6,5,9,7,9,9,8,9,8,7,9,9,9,9,8,9,8,8,8,9,9,7,8,9,8,7,9,7,9,8,9,9,8,8,7,7,7,7,7,7,7,6,9,8,7,6,6,9,6,8,8,7,6,9,0,6,9,8,9,9,9,8,9,8,8,6,8,8,8,8,9,7,9,9,8,9,8,9,8,8,8,9,8,9,6,9,6,),
    (6,7,5,4,7,6,7,7,4,7,7,5,4,5,4,7,7,6,6,7,5,7,7,7,7,6,6,7,7,5,8,7,4,7,7,7,6,7,7,4,7,7,7,3,7,3,7,7,5,7,6,7,7,7,7,6,8,4,6,7,4,6,0,7,6,6,6,5,6,6,5,6,6,3,6,6,6,6,6,5,6,7,4,7,6,7,6,6,6,7,6,8,3,5,8,),
    (8,9,8,7,8,8,9,8,5,9,8,6,8,8,7,9,8,8,8,8,8,8,9,8,9,7,7,8,8,7,9,8,7,9,8,9,8,9,8,8,9,9,9,6,9,6,9,9,7,9,8,9,9,9,9,8,9,7,7,8,5,8,0,9,8,7,8,8,8,7,8,7,7,5,7,7,7,7,8,6,8,8,7,8,7,8,7,7,7,8,7,9,5,8,9,),
    (7,8,7,5,7,7,8,8,4,8,8,5,6,6,5,8,7,7,6,8,7,8,8,8,8,7,7,8,8,6,8,8,5,7,8,7,7,8,8,6,8,8,7,4,7,4,7,7,6,7,7,8,7,7,7,6,8,5,7,7,5,7,0,8,7,7,7,7,7,7,7,7,7,4,7,7,7,7,7,6,7,8,5,8,7,8,7,7,7,8,7,8,4,6,7,),
    (3,0,4,3,3,4,1,4,2,0,4,2,3,3,3,4,3,3,3,4,3,4,3,4,3,3,3,4,4,3,3,4,3,2,4,2,4,3,4,3,3,3,2,3,2,3,2,2,3,1,4,3,2,1,1,3,0,3,3,2,1,4,0,1,4,3,4,4,4,3,4,3,3,2,3,3,3,3,4,2,4,4,3,4,3,4,3,3,3,4,3,4,1,3,0,),
    (3,0,4,3,2,4,1,4,1,0,4,2,3,3,2,4,3,2,3,4,3,4,3,4,3,3,3,4,4,2,3,4,3,2,4,2,4,3,4,3,3,3,2,2,2,2,2,2,2,1,4,3,2,1,1,3,0,3,3,2,1,4,0,1,4,3,4,4,4,3,4,3,3,1,3,3,3,3,4,2,4,4,3,4,3,4,3,3,3,4,3,4,1,3,0,),
    (6,8,5,6,7,6,8,6,5,8,4,5,5,6,6,6,7,7,7,6,6,5,8,6,7,6,5,4,6,6,8,6,6,8,5,8,6,7,5,6,7,7,8,6,8,6,8,8,6,8,5,7,8,8,8,7,8,6,6,7,4,4,0,7,6,6,6,6,6,5,6,6,6,5,6,6,6,6,6,5,6,6,6,6,6,6,6,6,6,6,6,8,4,5,8,),
    (6,1,5,6,5,6,4,7,4,2,7,5,6,6,5,7,6,5,6,6,6,7,5,6,7,6,5,7,7,5,5,7,6,4,7,5,6,7,7,6,7,7,4,5,5,5,5,5,5,4,6,7,4,4,3,6,2,6,6,5,4,5,0,4,6,6,6,6,6,5,6,6,6,3,6,6,6,6,6,5,6,7,6,6,6,6,6,5,6,6,6,7,4,6,3,),
    (7,5,8,5,5,8,5,8,5,6,8,5,7,6,6,8,7,4,6,8,7,8,7,8,8,7,7,8,8,4,7,8,6,6,8,6,8,8,8,7,8,8,6,3,6,4,6,6,6,5,8,8,6,5,5,6,5,6,7,6,5,8,0,5,8,7,8,8,8,7,8,7,7,4,7,7,7,7,8,6,8,8,5,8,7,8,7,7,7,8,7,8,5,7,4,),
    (6,8,7,5,7,5,8,7,4,8,6,5,4,5,4,8,7,7,7,6,6,7,8,6,8,4,4,6,6,6,8,7,4,8,7,8,5,8,7,4,8,8,8,4,8,4,8,8,6,8,4,8,8,8,8,7,8,5,6,7,4,5,0,8,4,6,4,4,4,5,4,6,6,3,6,6,4,4,4,5,4,7,4,6,4,4,4,4,4,4,6,8,4,4,8,),
    (10,11,10,9,10,10,11,11,7,11,11,8,9,9,8,11,10,10,9,11,10,11,11,11,11,10,10,11,11,9,11,11,9,10,11,10,10,11,11,9,11,11,10,8,10,8,10,10,9,10,10,11,10,10,10,9,11,9,10,10,8,10,0,11,10,10,10,10,10,10,10,10,10,7,10,10,10,10,10,9,10,11,9,11,10,11,10,10,10,11,10,11,7,9,10,),
    (20,16,19,17,18,20,18,21,17,16,21,18,15,18,18,21,20,15,15,21,15,21,20,21,20,20,20,21,21,15,20,21,17,18,21,19,20,20,21,18,20,20,18,13,19,16,19,19,18,18,20,20,19,18,17,15,17,17,20,19,18,20,4,18,20,20,20,19,20,20,19,20,20,17,20,20,20,20,20,19,20,21,18,21,20,21,20,20,20,21,20,21,17,19,17,),
    (11,13,11,10,12,10,13,12,9,13,11,10,10,10,9,12,12,12,12,11,11,11,13,11,13,9,9,11,11,11,13,12,9,13,11,13,10,13,11,10,13,13,13,8,13,8,13,13,11,13,10,13,13,13,13,12,13,10,11,12,9,10,0,13,10,11,10,10,10,10,10,11,11,8,11,11,9,9,10,9,10,11,9,10,9,10,9,9,9,10,11,13,9,10,13,),
    (10,10,9,9,10,9,10,9,9,10,6,9,4,10,10,9,10,10,9,8,9,8,10,8,10,10,9,6,3,10,10,9,10,10,8,10,9,10,8,10,10,10,10,10,10,10,10,10,10,10,8,10,10,10,10,10,10,10,10,9,8,4,0,10,9,10,9,10,9,9,9,10,10,9,10,10,10,10,9,9,10,8,10,10,10,10,10,10,10,10,10,10,8,2,10,),
    (12,13,12,10,12,12,13,13,9,13,13,10,11,11,10,13,11,12,11,12,12,13,13,12,13,11,11,13,13,11,13,13,10,12,13,12,12,13,13,11,13,13,12,8,12,8,12,12,11,12,12,13,12,12,12,11,13,10,11,12,9,12,0,13,12,11,12,12,12,11,12,11,11,8,11,11,11,11,12,10,12,13,10,12,11,12,11,11,11,12,12,13,9,11,12,),
    (11,11,10,10,11,10,11,10,10,11,7,10,5,11,11,10,11,11,10,9,10,9,11,9,11,11,10,7,6,11,11,10,11,11,9,11,10,11,9,11,11,11,11,11,11,11,11,11,11,11,9,11,11,11,11,11,11,11,11,10,9,5,0,11,10,11,10,11,10,10,10,11,11,10,11,11,11,11,10,10,11,9,11,11,11,11,11,11,11,11,11,11,9,2,11,),
    (11,13,10,10,13,11,13,12,10,13,12,11,9,11,9,12,13,12,12,12,11,12,13,12,12,11,11,12,12,11,14,12,8,13,12,13,11,12,12,9,12,12,13,7,13,8,13,13,10,13,11,12,13,13,13,12,14,10,11,13,9,11,0,11,11,11,11,10,11,11,10,11,11,8,11,11,11,11,11,10,11,12,9,12,11,12,11,11,11,12,11,14,9,10,14,),
    (10,11,10,9,10,10,11,10,9,11,10,9,10,10,9,10,10,10,10,10,10,10,11,10,11,9,9,10,10,9,11,10,9,11,10,11,10,11,10,10,11,11,11,9,11,9,11,11,9,11,10,11,11,11,11,10,11,9,9,10,9,10,0,11,10,9,10,10,10,9,10,9,9,9,9,9,9,9,10,8,10,10,9,10,9,10,9,9,9,10,9,11,9,10,11,),
    (20,16,19,17,18,20,18,21,17,16,21,18,15,18,18,21,20,15,15,21,15,21,20,21,20,20,20,21,21,15,20,21,17,18,21,19,20,20,21,18,20,20,18,13,19,16,19,19,18,18,20,20,19,18,17,15,17,17,20,19,18,20,4,18,20,20,20,19,20,20,19,20,20,17,20,20,20,20,20,19,20,21,18,21,20,21,20,20,20,21,20,21,17,19,17,),
    (9,11,9,8,10,9,11,10,7,11,10,8,9,9,8,10,10,10,10,9,9,10,11,9,10,8,8,10,10,9,11,10,8,11,10,11,9,10,10,9,10,10,11,7,11,7,11,11,8,11,9,10,11,11,11,10,11,8,8,10,6,9,0,10,9,8,9,9,9,8,9,8,9,6,8,8,8,8,9,7,9,10,8,9,8,9,8,8,8,9,9,11,6,9,11,),
    (9,11,9,8,11,9,11,10,8,11,10,9,9,9,8,10,11,10,10,10,9,10,11,9,11,8,8,10,10,9,12,10,8,11,10,11,9,11,10,9,11,11,11,7,11,7,11,11,9,11,9,11,11,11,11,10,12,8,9,11,7,9,0,11,9,9,9,9,9,8,9,9,9,6,9,9,8,8,9,7,9,10,8,9,8,9,8,8,8,9,9,12,7,9,12,),
    (12,12,11,11,12,11,12,11,11,12,10,11,10,12,12,10,12,12,11,11,11,10,12,10,11,12,11,10,10,12,13,10,12,12,10,12,11,12,10,12,12,12,12,12,12,12,12,12,12,12,10,12,12,12,12,12,13,12,12,12,10,10,0,11,11,12,11,12,11,11,11,12,12,11,12,12,12,12,11,11,12,10,12,12,12,12,12,12,12,12,12,13,10,10,13,),
    (15,16,14,14,15,14,16,15,14,16,12,14,10,15,15,15,15,15,15,14,14,14,16,14,16,15,14,12,10,15,16,15,15,16,14,16,14,16,14,15,16,16,16,15,16,15,16,16,15,16,13,16,16,16,16,15,16,15,15,15,13,10,0,16,14,15,14,15,14,14,14,15,15,14,15,15,15,15,14,14,15,13,15,15,15,15,15,15,15,15,15,16,13,9,16,),
    (17,11,16,16,17,16,14,16,16,15,14,16,14,17,17,15,17,17,16,14,16,15,16,15,15,17,16,14,14,17,16,14,17,16,15,16,16,17,14,17,17,17,16,17,16,17,13,16,17,15,15,17,14,14,14,17,14,17,17,13,15,14,0,14,16,17,16,17,16,16,16,17,17,16,17,17,17,17,16,16,17,15,17,17,17,17,17,17,17,17,17,17,15,14,13,),
    (14,16,13,13,15,13,16,15,12,16,13,13,12,13,12,15,15,15,15,14,14,14,16,14,16,12,12,13,13,14,16,15,12,16,14,16,13,16,14,12,16,16,16,12,16,12,16,16,14,16,13,16,16,16,16,15,16,13,14,15,12,13,0,16,13,14,13,13,13,13,13,14,14,11,14,14,12,12,13,11,13,13,12,13,12,13,12,12,12,13,14,16,12,12,16,),
    (12,13,12,10,12,12,13,13,9,13,13,10,11,11,10,13,12,12,11,13,12,13,13,13,13,12,12,13,13,11,13,13,10,12,13,12,12,13,13,11,13,13,12,9,12,9,12,12,11,12,12,13,12,12,12,11,13,10,12,12,10,12,0,13,12,12,12,12,12,12,12,12,12,9,12,12,12,12,12,11,12,13,10,13,12,13,12,12,12,13,12,13,9,11,12,),
    (10,12,11,9,11,9,12,11,8,12,11,9,7,9,8,12,11,11,11,10,10,11,12,10,12,9,9,11,11,10,12,11,6,12,11,12,9,12,11,7,12,12,12,4,12,7,12,12,10,12,9,12,12,12,12,11,12,9,10,11,8,9,0,12,9,10,9,8,9,9,8,10,10,7,10,10,9,9,9,9,9,11,8,10,9,10,9,9,9,10,10,12,8,8,12,),
    (12,12,11,11,12,11,12,12,11,12,12,11,10,12,12,12,12,12,11,12,11,12,12,12,12,12,11,12,12,12,12,12,12,11,12,11,11,12,12,12,12,12,11,12,11,12,11,11,12,11,11,12,11,11,11,12,12,12,12,11,10,11,0,12,11,12,11,12,11,11,11,12,12,11,12,12,12,12,11,11,12,12,12,12,12,12,12,12,12,12,12,12,10,10,11,),
    (13,13,12,12,13,12,13,12,12,13,12,12,9,13,13,13,13,13,12,11,12,12,13,11,13,13,12,12,12,13,13,12,13,13,12,13,12,13,12,13,13,13,13,13,13,13,13,13,13,13,11,13,13,13,13,13,13,13,13,12,11,10,0,13,12,13,12,13,12,12,12,13,13,12,13,13,13,13,12,12,13,12,13,13,13,13,13,13,13,13,13,13,11,9,13,),
    (13,15,12,12,14,12,15,14,11,15,12,12,12,12,11,14,14,14,14,13,13,13,15,13,15,11,11,12,12,13,15,14,11,15,13,15,12,15,13,12,15,15,15,10,15,10,15,15,13,15,12,15,15,15,15,14,15,12,13,14,11,12,0,15,12,13,12,12,12,12,12,13,13,10,13,13,11,11,12,10,12,12,11,12,11,12,11,11,11,12,13,15,11,12,15,),
    (12,14,11,11,14,11,14,12,11,14,10,12,9,12,9,12,14,13,13,13,12,11,14,12,13,11,11,10,10,12,15,12,9,14,11,14,11,13,11,9,13,13,14,8,14,9,14,14,11,14,10,13,14,14,14,13,15,11,12,14,10,10,0,12,10,11,10,10,10,10,10,11,12,9,11,11,9,9,10,8,10,10,9,10,9,10,9,9,9,10,12,15,10,9,15,),
    (10,12,11,9,11,10,12,11,8,12,11,9,10,10,9,12,11,11,11,11,10,11,12,11,12,10,10,11,11,10,12,11,9,12,11,12,10,12,11,10,12,12,12,8,12,8,12,12,10,12,10,12,12,12,12,11,12,9,10,11,8,10,0,12,10,10,10,10,10,10,10,10,10,7,10,10,10,10,10,9,10,11,9,11,10,11,10,10,10,11,10,12,8,10,12,),
    (11,13,11,10,12,10,13,12,9,13,11,10,8,10,9,12,12,12,12,11,11,11,13,11,13,9,9,11,11,11,13,12,7,13,11,13,10,13,11,8,13,13,13,6,13,7,13,13,11,13,9,13,13,13,13,12,13,10,11,12,9,9,0,13,9,11,9,9,9,10,9,11,11,8,11,11,9,9,9,9,9,11,8,10,9,10,9,9,9,10,11,13,9,8,13,),
    (14,16,14,13,16,13,16,15,13,16,14,14,12,14,12,15,16,15,15,15,14,14,16,14,16,13,13,14,14,14,17,15,12,16,14,16,13,16,14,12,16,16,16,11,16,11,16,16,14,16,13,16,16,16,16,15,17,13,14,16,12,13,0,16,13,14,13,13,13,13,13,14,14,11,14,14,13,13,13,12,13,14,12,14,13,14,13,13,13,14,14,17,12,12,17,),
    (13,14,12,12,13,12,14,13,12,14,10,12,9,13,13,13,13,13,13,12,12,12,14,12,14,13,12,10,9,13,14,13,13,14,12,14,12,14,12,13,14,14,14,13,14,13,14,14,13,14,11,14,14,14,14,13,14,13,13,13,11,9,0,14,12,13,12,13,12,12,12,13,13,12,13,13,13,13,12,12,13,11,13,13,13,13,13,13,13,13,13,14,11,9,14,),
    (12,14,12,11,13,12,14,13,10,14,13,11,12,12,11,13,13,13,13,12,12,13,14,12,13,11,11,13,13,12,14,13,11,14,13,14,12,13,13,12,13,13,14,11,14,11,14,14,11,14,12,13,14,14,14,13,14,11,11,13,9,12,0,13,12,11,12,12,12,11,12,11,12,10,11,11,11,11,12,10,12,13,11,12,11,12,11,11,11,12,12,14,9,12,14,),
    (14,12,13,11,12,14,12,15,11,12,15,12,9,12,12,15,14,11,11,15,10,15,14,15,14,14,14,15,15,10,14,15,11,12,15,13,14,14,15,12,14,14,12,8,13,10,13,13,12,12,14,14,13,12,12,11,12,11,14,13,12,14,0,12,14,14,14,13,14,14,13,14,14,11,14,14,14,14,14,13,14,15,12,15,14,15,14,14,14,15,14,15,11,13,12,),
    (3,5,3,3,4,3,5,4,4,7,4,4,3,4,2,4,4,4,4,3,3,4,5,3,4,3,3,4,4,3,5,4,3,5,4,5,3,4,4,3,4,4,5,2,5,2,5,5,2,5,3,4,5,5,5,4,5,3,3,7,3,3,0,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,4,3,3,3,3,3,2,3,3,3,7,3,3,6,),
    (6,3,5,5,6,5,3,5,5,4,4,5,5,6,6,5,6,6,5,5,5,5,5,5,4,6,5,5,5,6,5,5,6,5,5,5,5,6,5,6,6,6,5,6,5,6,3,5,6,4,5,6,3,3,3,6,3,6,6,2,4,5,0,3,5,6,5,6,5,5,5,6,6,5,6,6,6,6,5,5,6,5,6,6,6,6,6,6,6,6,6,6,4,5,3,),
    (5,7,5,5,6,5,7,6,4,7,6,4,5,5,4,6,6,6,6,5,5,6,7,5,6,5,4,6,6,5,7,6,5,7,6,7,5,6,6,5,6,6,7,4,7,4,7,7,4,7,5,6,7,7,7,6,7,5,5,7,4,5,0,6,5,5,5,5,5,4,5,5,5,4,5,5,5,5,5,4,5,6,5,5,5,5,5,4,5,5,5,7,4,5,7,),
    (4,0,6,2,3,6,3,6,3,5,5,3,5,3,4,6,5,1,2,6,4,6,4,6,5,5,5,6,5,2,4,6,4,4,6,4,6,5,6,5,5,5,4,0,4,2,4,4,3,3,6,5,4,3,3,1,2,4,5,3,3,6,0,4,6,5,6,6,6,4,6,5,5,2,5,5,5,5,6,4,6,5,3,5,5,6,5,4,5,5,5,6,3,5,2,),
    (11,11,6,5,8,6,14,11,11,12,8,14,11,14,10,7,12,7,8,7,8,8,9,8,9,13,13,9,10,9,9,6,0,4,7,4,6,3,6,0,6,5,4,1,0,1,4,5,5,4,2,2,5,4,0,3,3,2,10,11,10,11,16,14,8,4,8,7,8,5,16,7,11,9,7,11,3,7,4,6,8,8,8,10,7,6,6,10,16,9,10,16,10,8,13,),
    (1,2,2,0,1,0,2,2,0,3,0,0,0,0,0,3,1,1,0,0,1,2,2,1,3,0,0,1,0,0,2,2,0,0,2,0,0,3,2,0,3,3,0,0,0,0,0,0,1,0,0,3,0,0,0,0,2,0,1,1,0,0,0,2,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,2,0,1,0,0,0,0,0,0,1,3,0,0,1,),
    (9,3,8,8,9,8,6,8,8,4,6,8,6,9,9,7,9,9,8,6,8,7,8,7,7,9,8,6,6,9,8,6,9,8,7,8,8,9,6,9,9,9,8,9,8,9,5,8,9,7,7,9,6,6,6,9,6,9,9,5,7,6,0,6,8,9,8,9,8,8,8,9,9,8,9,9,9,9,8,8,9,7,9,9,9,9,9,9,9,9,9,9,7,6,5,),
    (12,7,11,9,10,12,10,13,9,8,13,10,7,10,10,13,12,7,7,13,7,13,12,13,12,12,12,13,13,7,12,13,9,10,13,11,12,12,13,10,12,12,10,5,11,8,11,11,10,10,12,12,11,10,9,7,9,9,12,11,10,12,0,10,12,12,12,11,12,12,11,12,12,9,12,12,12,12,12,11,12,13,10,13,12,13,12,12,12,13,12,13,9,11,9,),
    (9,3,8,8,9,8,6,8,8,4,7,8,6,9,9,7,9,9,8,7,8,7,8,7,7,9,8,7,7,9,8,7,9,8,7,8,8,9,7,9,9,9,8,9,8,9,5,8,9,7,7,9,6,6,6,9,6,9,9,5,7,7,0,6,8,9,8,9,8,8,8,9,9,8,9,9,9,9,8,8,9,7,9,9,9,9,9,9,9,9,9,9,7,6,5,),
    (10,8,9,9,10,9,8,9,9,8,7,9,6,10,10,8,10,10,9,6,9,8,9,8,8,10,9,7,7,10,9,7,10,9,8,9,9,10,7,10,10,10,9,10,9,10,8,9,10,8,8,10,8,8,8,10,8,10,10,7,8,6,0,7,9,10,9,10,9,9,9,10,10,9,10,10,10,10,9,9,10,8,10,10,10,10,10,10,10,10,10,10,8,6,8,),
    (9,3,8,8,9,8,6,8,8,4,6,8,7,9,9,7,9,9,8,7,8,7,8,7,7,9,8,7,7,9,8,7,9,8,7,8,8,9,7,9,9,9,8,9,8,9,5,8,9,7,7,9,6,6,6,9,6,9,9,5,7,7,0,6,8,9,8,9,8,8,8,9,9,8,9,9,9,9,8,8,9,7,9,9,9,9,9,9,9,9,9,9,7,7,5,),
    (11,6,10,8,9,11,9,12,8,7,12,9,6,9,9,12,11,6,6,12,6,12,11,12,11,11,11,12,12,6,11,12,8,9,12,10,11,11,12,9,11,11,9,6,10,7,10,10,9,9,11,11,10,9,8,6,8,8,11,10,9,11,0,9,11,11,11,10,11,11,10,11,11,8,11,11,11,11,11,10,11,12,9,12,11,12,11,11,11,12,11,12,8,10,8,),
    (9,3,8,8,9,8,6,8,8,4,7,8,7,9,9,7,9,9,8,7,8,7,8,7,7,9,8,7,7,9,8,7,9,8,7,8,8,9,7,9,9,9,8,9,8,9,5,8,9,7,7,9,6,6,6,9,6,9,9,5,7,7,3,6,8,9,8,9,8,8,8,9,9,8,9,9,9,9,8,8,9,7,9,9,9,9,9,9,9,9,9,9,7,7,5,),
    (10,5,9,9,10,9,7,9,9,5,7,9,7,10,10,8,10,10,9,7,9,8,9,8,8,10,9,7,7,10,9,7,10,9,8,9,9,10,7,10,10,10,9,10,9,10,6,9,10,8,8,10,7,7,7,10,7,10,10,6,8,7,0,7,9,10,9,10,9,9,9,10,10,9,10,10,10,10,9,9,10,8,10,10,10,10,10,10,10,10,10,10,8,7,6,),
    (6,5,5,5,6,5,5,5,5,5,3,5,3,6,6,5,6,6,5,3,5,4,5,4,5,6,5,3,3,6,5,4,6,5,4,5,5,6,4,6,6,6,5,6,5,6,5,5,6,5,4,6,5,5,5,6,5,6,6,4,4,3,0,5,5,6,5,6,5,5,5,6,6,5,6,6,6,6,5,5,6,4,6,6,6,6,6,6,6,6,6,6,4,3,5,),
    (8,8,7,7,8,7,8,7,7,8,6,7,6,8,8,8,8,8,7,6,7,7,8,6,8,8,7,6,6,8,8,7,8,8,7,8,7,8,7,8,8,8,8,8,8,8,8,8,8,8,6,8,8,8,8,8,8,8,8,7,6,6,0,8,7,8,7,8,7,7,7,8,8,7,8,8,8,8,7,7,8,7,8,8,8,8,8,8,8,8,8,8,6,6,8,),
    (10,5,9,9,10,9,7,9,9,5,7,9,7,10,10,8,10,10,9,7,9,8,9,8,8,10,9,7,7,10,9,7,10,9,8,9,9,10,7,10,10,10,9,10,9,10,6,9,10,8,8,10,7,7,7,10,7,10,10,6,8,7,0,7,9,10,9,10,9,9,9,10,10,9,10,10,10,10,9,9,10,8,10,10,10,10,10,10,10,10,10,10,8,7,6,),
    (6,5,5,5,6,5,5,5,5,5,4,5,3,6,6,4,6,6,5,3,5,4,5,4,4,6,5,4,4,6,5,4,6,5,4,5,5,6,4,6,6,6,5,6,5,6,5,5,6,5,4,6,5,5,5,6,5,6,6,4,4,3,0,4,5,6,5,6,5,5,5,6,6,5,6,6,6,6,5,5,6,4,6,6,6,6,6,6,6,6,6,6,4,3,5,),
    (14,8,13,13,14,13,11,13,13,9,10,13,10,14,14,12,14,14,13,10,13,12,13,12,12,14,13,10,10,14,13,11,14,13,12,13,13,14,11,14,14,14,13,14,13,14,10,13,14,12,12,14,11,11,11,14,11,14,14,10,12,10,0,11,13,14,13,14,13,13,13,14,14,13,14,14,14,14,13,13,14,12,14,14,14,14,14,14,14,14,14,14,12,10,10,),
    (10,4,9,9,10,9,7,9,9,5,7,9,7,10,10,8,10,10,9,7,9,8,9,8,8,10,9,7,7,10,9,7,10,9,8,9,9,10,7,10,10,10,9,10,9,10,6,9,10,8,8,10,7,7,7,10,7,10,10,6,8,7,0,7,9,10,9,10,9,9,9,10,10,9,10,10,10,10,9,9,10,8,10,10,10,10,10,10,10,10,10,10,8,7,6,),
    (12,7,11,9,10,12,10,13,9,8,13,10,7,10,10,13,12,7,7,13,7,13,12,13,12,12,12,13,13,7,12,13,9,10,13,11,12,12,13,10,12,12,10,6,11,8,11,11,10,10,12,12,11,10,9,7,9,9,12,11,10,12,0,10,12,12,12,11,12,12,11,12,12,9,12,12,12,12,12,11,12,13,10,13,12,13,12,12,12,13,12,13,9,11,9,),
    (11,5,10,10,11,10,8,10,10,6,8,10,9,11,11,9,11,11,10,9,10,9,10,9,9,11,10,9,9,11,10,9,11,10,9,10,10,11,9,11,11,11,10,11,10,11,7,10,11,9,9,11,8,8,8,11,8,11,11,7,9,9,0,8,10,11,10,11,10,10,10,11,11,10,11,11,11,11,10,10,11,9,11,11,11,11,11,11,11,11,11,11,9,9,7,),
    (9,3,8,8,9,8,6,8,8,4,6,8,6,9,9,7,9,9,8,6,8,7,8,7,7,9,8,6,6,9,8,6,9,8,7,8,8,9,6,9,9,9,8,9,8,9,5,8,9,7,7,9,6,6,6,9,6,9,9,5,7,6,0,6,8,9,8,9,8,8,8,9,9,8,9,9,9,9,8,8,9,7,9,9,9,9,9,9,9,9,9,9,7,6,5,),
    (9,3,8,8,9,8,6,8,8,4,5,8,5,9,9,7,9,9,8,5,8,7,8,7,7,9,8,5,5,9,8,6,9,8,7,8,8,9,6,9,9,9,8,9,8,9,5,8,9,7,7,9,6,6,6,9,6,9,9,5,7,5,0,6,8,9,8,9,8,8,8,9,9,8,9,9,9,9,8,8,9,7,9,9,9,9,9,9,9,9,9,9,7,5,5,),
    (9,3,8,8,9,8,6,8,8,5,5,8,6,9,9,7,9,9,8,6,8,7,8,7,7,9,8,6,6,9,8,6,9,8,7,8,8,9,6,9,9,9,8,9,8,9,5,8,9,7,7,9,6,6,6,9,6,9,9,5,7,6,0,6,8,9,8,9,8,8,8,9,9,8,9,9,9,9,8,8,9,7,9,9,9,9,9,9,9,9,9,9,7,6,5,),
    (7,4,6,6,7,6,4,6,6,4,5,6,3,7,7,5,7,7,6,5,6,5,6,5,5,7,6,5,5,7,6,5,7,6,5,6,6,7,5,7,7,7,6,7,6,7,3,6,7,5,5,7,4,4,4,7,4,7,7,3,5,4,0,4,6,7,6,7,6,6,6,7,7,6,7,7,7,7,6,6,7,5,7,7,7,7,7,7,7,7,7,7,5,3,3,),
    (10,4,9,9,10,9,7,9,9,5,7,9,7,10,10,8,10,10,9,7,9,8,9,8,8,10,9,7,7,10,9,7,10,9,8,9,9,10,7,10,10,10,9,10,9,10,6,9,10,8,8,10,7,7,7,10,7,10,10,6,8,7,0,7,9,10,9,10,9,9,9,10,10,9,10,10,10,10,9,9,10,8,10,10,10,10,10,10,10,10,10,10,8,7,6,),
    (10,5,9,7,8,10,8,11,7,6,11,8,5,8,8,11,10,5,5,11,5,11,10,11,10,10,10,11,11,5,10,11,7,8,11,9,10,10,11,8,10,10,8,3,9,6,9,9,8,8,10,10,9,8,7,5,7,7,10,9,8,10,0,8,10,10,10,9,10,10,9,10,10,7,10,10,10,10,10,9,10,11,8,11,10,11,10,10,10,11,10,11,7,9,7,),
    (11,5,11,10,10,11,8,11,9,6,11,9,11,11,10,11,10,10,11,11,11,11,10,11,10,10,10,11,11,10,10,11,10,9,11,9,11,10,11,11,10,10,9,10,9,10,9,9,10,8,11,10,9,8,8,11,7,10,10,9,8,11,0,8,11,10,11,11,11,10,11,10,10,9,10,10,10,10,11,9,11,11,10,11,10,11,10,10,10,11,10,11,8,11,7,),
    (7,1,6,6,7,6,4,7,6,2,7,6,5,7,7,7,7,7,6,7,6,7,6,7,6,7,6,7,7,7,6,7,7,6,7,6,6,7,7,7,7,7,6,7,6,7,5,6,7,5,6,7,5,4,4,7,4,7,7,5,5,6,0,4,6,7,6,7,6,6,6,7,7,6,7,7,7,7,6,6,7,7,7,7,7,7,7,7,7,7,7,7,5,5,3,),
    (10,4,9,9,10,9,7,9,9,5,7,9,7,10,10,8,10,10,9,7,9,8,9,8,8,10,9,7,7,10,9,7,10,9,8,9,9,10,7,10,10,10,9,10,9,10,6,9,10,8,8,10,7,7,7,10,7,10,10,6,8,7,3,7,9,10,9,10,9,9,9,10,10,9,10,10,10,10,9,9,10,8,10,10,10,10,10,10,10,10,10,10,8,7,6,),
    (8,2,7,7,8,7,5,7,7,3,6,7,4,8,8,6,8,8,7,6,7,6,7,6,6,8,7,6,6,8,7,6,8,7,6,7,7,8,6,8,8,8,7,8,7,8,4,7,8,6,6,8,5,5,5,8,5,8,8,4,6,5,0,5,7,8,7,8,7,7,7,8,8,7,8,8,8,8,7,7,8,6,8,8,8,8,8,8,8,8,8,8,6,4,4,),
    (3,5,3,2,4,3,5,3,4,7,3,4,3,4,2,4,4,4,4,3,3,3,5,3,4,3,3,3,3,3,5,3,2,5,3,5,3,4,3,3,4,4,5,2,5,2,5,5,2,5,3,4,5,5,5,4,5,3,3,7,3,3,0,4,3,2,3,3,3,3,3,2,3,3,2,2,2,2,3,2,3,3,2,3,2,3,2,2,2,3,3,7,3,3,6,),
    (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,),
    (5,7,5,5,6,5,7,6,4,7,6,4,5,5,4,6,6,6,6,6,5,6,7,6,6,5,5,6,6,5,7,6,5,7,6,7,5,6,6,5,6,6,7,4,7,4,7,7,4,7,5,6,7,7,7,6,7,5,5,7,3,5,0,6,5,5,5,5,5,5,5,5,5,3,5,5,5,5,5,4,5,6,5,6,5,6,5,5,5,6,5,7,3,5,7,),
    (8,3,8,6,6,8,6,9,5,4,9,6,7,7,6,9,8,5,7,9,7,9,8,9,8,8,8,9,9,5,8,9,6,6,9,7,8,8,9,7,8,8,6,1,7,4,7,7,6,6,8,8,7,6,5,7,5,6,8,7,6,8,0,6,8,8,8,8,8,8,8,8,8,5,8,8,8,8,8,7,8,9,6,9,8,9,8,8,8,9,8,9,5,7,5,),
    (2,4,1,1,3,1,4,2,0,4,0,1,0,1,0,2,3,3,3,2,2,1,4,2,3,0,0,0,0,2,4,2,0,4,1,4,1,3,1,0,3,3,4,0,4,0,4,4,1,4,0,3,4,4,4,3,4,1,1,3,0,0,0,3,0,1,0,0,0,0,0,1,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,0,0,4,),
)

# End of font

