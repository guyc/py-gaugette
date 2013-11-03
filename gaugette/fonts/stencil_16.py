# coding=utf-8
# Module stencil_16
# generated from Stencil 11.25pt

name        = "Stencil 16"
start_char  = '!'
end_char    = chr(127)
char_height = 16
space_width = 8
gap_width   = 2

bitmaps = (
    # @0 '!' (3 pixels wide)
    0x00, #    
    0x00, #    
    0x00, #    
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0x40, #  O 
    0x40, #  O 
    0x40, #  O 
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0x00, #    
    0x00, #    
    0x00, #    

    # @16 '"' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0xF8, # OOOOO
    0xD0, # OO O 
    0xD0, # OO O 
    0x90, # O  O 
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      

    # @32 '#' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x1B, 0x00, #    OO OO 
    0x12, 0x00, #    O  O  
    0x7B, 0x80, #  OOOO OOO
    0x32, 0x00, #   OO  O  
    0x36, 0x00, #   OO OO  
    0x24, 0x00, #   O  O   
    0x24, 0x00, #   O  O   
    0xF7, 0x00, # OOOO OOO 
    0x6C, 0x00, #  OO OO   
    0x4C, 0x00, #  O  OO   
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @64 '$' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x10, #    O   
    0x3C, #   OOOO 
    0xD6, # OO O OO
    0xD6, # OO O OO
    0xF6, # OOOO OO
    0xFC, # OOOOOO 
    0x7E, #  OOOOOO
    0x1E, #    OOOO
    0xD6, # OO O OO
    0xD6, # OO O OO
    0x7C, #  OOOOO 
    0x10, #    O   
    0x00, #        
    0x00, #        

    # @80 '%' (11 pixels wide)
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x71, 0x00, #  OOO   O   
    0xD9, 0x00, # OO OO  O   
    0xDA, 0x00, # OO OO O    
    0xDA, 0x00, # OO OO O    
    0x74, 0x00, #  OOO O     
    0x04, 0x00, #      O     
    0x0B, 0xC0, #     O OOOO 
    0x0E, 0x60, #     OOO  OO
    0x16, 0x60, #    O OO  OO
    0x12, 0x40, #    O  O  O 
    0x00, 0x00, #            
    0x00, 0x00, #            
    0x00, 0x00, #            

    # @112 '&' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x0D, 0x00, #     OO O  
    0x1D, 0x00, #    OOO O  
    0x1D, 0x00, #    OOO O  
    0x1D, 0x00, #    OOO O  
    0x0E, 0xC0, #     OOO OO
    0x6F, 0x40, #  OO OOOO O
    0xE7, 0x80, # OOO  OOOO 
    0xF7, 0x80, # OOOO OOOO 
    0xF3, 0x80, # OOOO  OOO 
    0x7F, 0xC0, #  OOOOOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @144 ''' (2 pixels wide)
    0x00, #   
    0x00, #   
    0x00, #   
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0x80, # O 
    0x00, #   
    0x00, #   
    0x00, #   
    0x00, #   
    0x00, #   
    0x00, #   
    0x00, #   
    0x00, #   
    0x00, #   

    # @160 '(' (4 pixels wide)
    0x00, #     
    0x00, #     
    0x00, #     
    0x10, #    O
    0x30, #   OO
    0x60, #  OO 
    0x60, #  OO 
    0xE0, # OOO 
    0xE0, # OOO 
    0xE0, # OOO 
    0xE0, # OOO 
    0x60, #  OO 
    0x60, #  OO 
    0x30, #   OO
    0x10, #    O
    0x00, #     

    # @176 ')' (4 pixels wide)
    0x00, #     
    0x00, #     
    0x00, #     
    0x80, # O   
    0xC0, # OO  
    0x60, #  OO 
    0x60, #  OO 
    0x70, #  OOO
    0x70, #  OOO
    0x70, #  OOO
    0x70, #  OOO
    0x60, #  OO 
    0x60, #  OO 
    0xC0, # OO  
    0x80, # O   
    0x00, #     

    # @192 '*' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0x60, #  OO  
    0xE8, # OOO O
    0xD8, # OO OO
    0x70, #  OOO 
    0xD8, # OO OO
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      
    0x00, #      

    # @208 '+' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x30, #   OO   
    0x30, #   OO   
    0x30, #   OO   
    0xFE, # OOOOOOO
    0xFE, # OOOOOOO
    0x30, #   OO   
    0x30, #   OO   
    0x30, #   OO   
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @224 ',' (3 pixels wide)
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
    0xE0, # OOO
    0xE0, # OOO
    0x20, #   O
    0xC0, # OO 
    0x00, #    

    # @240 '-' (4 pixels wide)
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0xF0, # OOOO
    0xF0, # OOOO
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     
    0x00, #     

    # @256 '.' (3 pixels wide)
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
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0x00, #    
    0x00, #    
    0x00, #    

    # @272 '/' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x0C, #     OO
    0x0C, #     OO
    0x18, #    OO 
    0x18, #    OO 
    0x18, #    OO 
    0x30, #   OO  
    0x30, #   OO  
    0x20, #   O   
    0x60, #  OO   
    0x60, #  OO   
    0x40, #  O    
    0xC0, # OO    
    0x00, #       

    # @288 '0' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x34, #   OO O  
    0x66, #  OO  OO 
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0x67, #  OO  OOO
    0x66, #  OO  OO 
    0x34, #   OO O  
    0x00, #         
    0x00, #         
    0x00, #         

    # @304 '1' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0xF0, # OOOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0xF8, # OOOOO
    0x00, #      
    0x00, #      
    0x00, #      

    # @320 '2' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x6C, #  OO OO  
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0x06, #      OO 
    0x0C, #     OO  
    0x30, #   OO    
    0x39, #   OOO  O
    0x7F, #  OOOOOOO
    0x4E, #  O  OOO 
    0x00, #         
    0x00, #         
    0x00, #         

    # @336 '3' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x2E, #   O OOO 
    0x67, #  OO  OOO
    0x67, #  OO  OOO
    0x67, #  OO  OOO
    0x06, #      OO 
    0x0E, #     OOO 
    0x07, #      OOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0x6E, #  OO OOO 
    0x00, #         
    0x00, #         
    0x00, #         

    # @352 '4' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x06, #      OO 
    0x0E, #     OOO 
    0x0E, #     OOO 
    0x2E, #   O OOO 
    0x2E, #   O OOO 
    0x4E, #  O  OOO 
    0x8E, # O   OOO 
    0xEF, # OOO OOOO
    0x0E, #     OOO 
    0x1F, #    OOOOO
    0x00, #         
    0x00, #         
    0x00, #         

    # @368 '5' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x44, #  O   O 
    0x7C, #  OOOOO 
    0xF8, # OOOOO  
    0x40, #  O     
    0x7C, #  OOOOO 
    0x4E, #  O  OOO
    0x0E, #     OOO
    0xEE, # OOO OOO
    0xEE, # OOO OOO
    0x7C, #  OOOOO 
    0x00, #        
    0x00, #        
    0x00, #        

    # @384 '6' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x2C, #   O OO 
    0x66, #  OO  OO
    0xEE, # OOO OOO
    0xEE, # OOO OOO
    0xFC, # OOOOOO 
    0xEE, # OOO OOO
    0xEE, # OOO OOO
    0xEE, # OOO OOO
    0x6E, #  OO OOO
    0x2C, #   O OO 
    0x00, #        
    0x00, #        
    0x00, #        

    # @400 '7' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0xBA, # O OOO O
    0xFE, # OOOOOOO
    0x9C, # O  OOO 
    0x08, #     O  
    0x08, #     O  
    0x18, #    OO  
    0x38, #   OOO  
    0x38, #   OOO  
    0x38, #   OOO  
    0x38, #   OOO  
    0x00, #        
    0x00, #        
    0x00, #        

    # @416 '8' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x6C, #  OO OO 
    0xEE, # OOO OOO
    0xEE, # OOO OOO
    0xEE, # OOO OOO
    0x6C, #  OO OO 
    0x6C, #  OO OO 
    0xEE, # OOO OOO
    0xEE, # OOO OOO
    0xEE, # OOO OOO
    0x6C, #  OO OO 
    0x00, #        
    0x00, #        
    0x00, #        

    # @432 '9' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x3C, #   OOOO  
    0x66, #  OO  OO 
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0x77, #  OOO OOO
    0x07, #      OOO
    0x77, #  OOO OOO
    0x76, #  OOO OO 
    0x3C, #   OOOO  
    0x00, #         
    0x00, #         
    0x00, #         

    # @448 ':' (3 pixels wide)
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
    0xE0, # OOO
    0xE0, # OOO
    0xE0, # OOO
    0x00, #    
    0x00, #    
    0x00, #    

    # @464 ';' (3 pixels wide)
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
    0xE0, # OOO
    0xE0, # OOO
    0x20, #   O
    0xC0, # OO 
    0x00, #    

    # @480 '<' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x04, #      O
    0x0C, #     OO
    0x18, #    OO 
    0x60, #  OO   
    0xE0, # OOO   
    0x78, #  OOOO 
    0x3C, #   OOOO
    0x0C, #     OO
    0x04, #      O
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @496 '=' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0xFE, # OOOOOOO
    0xFE, # OOOOOOO
    0xFE, # OOOOOOO
    0xFE, # OOOOOOO
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        
    0x00, #        

    # @512 '>' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0x80, # O     
    0x80, # O     
    0xE0, # OOO   
    0xF0, # OOOO  
    0x3C, #   OOOO
    0x1C, #    OOO
    0x30, #   OO  
    0x40, #  O    
    0x80, # O     
    0x00, #       
    0x00, #       
    0x00, #       
    0x00, #       

    # @528 '?' (7 pixels wide)
    0x00, #        
    0x00, #        
    0x00, #        
    0x6C, #  OO OO 
    0xE6, # OOO  OO
    0xE6, # OOO  OO
    0x0E, #     OOO
    0x3C, #   OOOO 
    0x38, #   OOO  
    0x20, #   O    
    0x70, #  OOO   
    0x70, #  OOO   
    0x70, #  OOO   
    0x00, #        
    0x00, #        
    0x00, #        

    # @544 '@' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x1F, 0x00, #    OOOOO  
    0x21, 0x80, #   O    OO 
    0x43, 0xC0, #  O    OOOO
    0x8F, 0x40, # O   OOOO O
    0x8A, 0x40, # O   O O  O
    0x9E, 0x40, # O  OOOO  O
    0x9E, 0x80, # O  OOOO O 
    0x5F, 0x00, #  O OOOOO  
    0x60, 0x00, #  OO       
    0x1F, 0x80, #    OOOOOO 
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @576 'A' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x1E, 0x00, #    OOOO  
    0x0E, 0x00, #     OOO  
    0x2E, 0x00, #   O OOO  
    0x2E, 0x00, #   O OOO  
    0x2E, 0x00, #   O OOO  
    0x2F, 0x00, #   O OOOO 
    0x27, 0x00, #   O  OOO 
    0x5F, 0x00, #  O OOOOO 
    0x47, 0x00, #  O   OOO 
    0xE7, 0x80, # OOO  OOOO
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @608 'B' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xF3, 0x00, # OOOO  OO  
    0x71, 0x80, #  OOO   OO 
    0x71, 0x80, #  OOO   OO 
    0x71, 0x80, #  OOO   OO 
    0x73, 0x00, #  OOO  OO  
    0x77, 0x80, #  OOO OOOO 
    0x71, 0xC0, #  OOO   OOO
    0x71, 0xC0, #  OOO   OOO
    0x71, 0xC0, #  OOO   OOO
    0xF3, 0x80, # OOOO  OOO 
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @640 'C' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x1F, #    OOOOO
    0x63, #  OO   OO
    0x61, #  OO    O
    0xE1, # OOO    O
    0xE0, # OOO     
    0xE0, # OOO     
    0xE0, # OOO     
    0xE1, # OOO    O
    0x61, #  OO    O
    0x3E, #   OOOOO 
    0x00, #         
    0x00, #         
    0x00, #         

    # @656 'D' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xF6, 0x00, # OOOO OO  
    0x73, 0x00, #  OOO  OO 
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x00, #  OOO  OO 
    0xF6, 0x00, # OOOO OO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @688 'E' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0xF7, # OOOO OOO
    0x73, #  OOO  OO
    0x71, #  OOO   O
    0x72, #  OOO  O 
    0x76, #  OOO OO 
    0x76, #  OOO OO 
    0x72, #  OOO  O 
    0x71, #  OOO   O
    0x71, #  OOO   O
    0xF7, # OOOO OOO
    0x00, #         
    0x00, #         
    0x00, #         

    # @704 'F' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0xF7, # OOOO OOO
    0x73, #  OOO  OO
    0x71, #  OOO   O
    0x72, #  OOO  O 
    0x76, #  OOO OO 
    0x76, #  OOO OO 
    0x72, #  OOO  O 
    0x70, #  OOO    
    0x70, #  OOO    
    0xF8, # OOOOO   
    0x00, #         
    0x00, #         
    0x00, #         

    # @720 'G' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x35, #   OO O O
    0x63, #  OO   OO
    0xE1, # OOO    O
    0xE1, # OOO    O
    0xE0, # OOO     
    0xEF, # OOO OOOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0x67, #  OO  OOO
    0x3E, #   OOOOO 
    0x00, #         
    0x00, #         
    0x00, #         

    # @736 'H' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xFF, 0xC0, # OOOOOOOOOO
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x7F, 0x80, #  OOOOOOOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0xFF, 0xC0, # OOOOOOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @768 'I' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0xF8, # OOOOO
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0xF8, # OOOOO
    0x00, #      
    0x00, #      
    0x00, #      

    # @784 'J' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x1F, #    OOOOO
    0x0E, #     OOO 
    0x0E, #     OOO 
    0x0E, #     OOO 
    0x0E, #     OOO 
    0x0E, #     OOO 
    0x6E, #  OO OOO 
    0xFE, # OOOOOOO 
    0xEE, # OOO OOO 
    0x6C, #  OO OO  
    0x00, #         
    0x00, #         
    0x00, #         

    # @800 'K' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xFB, 0x80, # OOOOO OOO 
    0x73, 0x00, #  OOO  OO  
    0x72, 0x00, #  OOO  O   
    0x76, 0x00, #  OOO OO   
    0x7E, 0x00, #  OOOOOO   
    0x7F, 0x00, #  OOOOOOO  
    0x7F, 0x00, #  OOOOOOO  
    0x77, 0x80, #  OOO OOOO 
    0x77, 0x80, #  OOO OOOO 
    0xFF, 0xC0, # OOOOOOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @832 'L' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0xF8, # OOOOO   
    0x70, #  OOO    
    0x70, #  OOO    
    0x70, #  OOO    
    0x70, #  OOO    
    0x70, #  OOO    
    0x70, #  OOO    
    0x71, #  OOO   O
    0x71, #  OOO   O
    0xF7, # OOOO OOO
    0x00, #         
    0x00, #         
    0x00, #         

    # @848 'M' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xF3, 0xC0, # OOOO  OOOO
    0x73, 0x80, #  OOO  OOO 
    0x7B, 0x80, #  OOOO OOO 
    0x3B, 0x80, #   OOO OOO 
    0xBF, 0x80, # O OOOOOOO 
    0x7F, 0x80, #  OOOOOOOO 
    0x5B, 0x80, #  O OO OOO 
    0x5B, 0x80, #  O OO OOO 
    0x5B, 0x80, #  O OO OOO 
    0xF7, 0xC0, # OOOO OOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @880 'N' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xF3, 0x80, # OOOO  OOO
    0x79, 0x00, #  OOOO  O 
    0x3D, 0x00, #   OOOO O 
    0xBD, 0x00, # O OOOO O 
    0x5F, 0x00, #  O OOOOO 
    0x5F, 0x00, #  O OOOOO 
    0x4F, 0x00, #  O  OOOO 
    0x47, 0x00, #  O   OOO 
    0x47, 0x00, #  O   OOO 
    0xE3, 0x00, # OOO   OO 
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @912 'O' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x36, 0x00, #   OO OO  
    0x63, 0x00, #  OO   OO 
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0x63, 0x00, #  OO   OO 
    0x36, 0x00, #   OO OO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @944 'P' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xF7, 0x00, # OOOO OOO 
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x00, #  OOO  OO 
    0x74, 0x00, #  OOO O   
    0x70, 0x00, #  OOO     
    0x70, 0x00, #  OOO     
    0xF8, 0x00, # OOOOO    
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @976 'Q' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x3E, 0x00, #   OOOOO  
    0x63, 0x00, #  OO   OO 
    0x63, 0x80, #  OO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0x63, 0x80, #  OO   OOO
    0x6F, 0x00, #  OO OOOO 
    0x3F, 0x80, #   OOOOOOO
    0x01, 0x80, #        OO
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1008 'R' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xF7, 0x00, # OOOO OOO  
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x00, #  OOO  OO  
    0x77, 0x00, #  OOO OOO  
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0xC0, #  OOO  OOOO
    0xFB, 0x80, # OOOOO OOO 
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1040 'S' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x6A, #  OO O O 
    0xE6, # OOO  OO 
    0xE2, # OOO   O 
    0xFA, # OOOOO O 
    0xFE, # OOOOOOO 
    0x7F, #  OOOOOOO
    0x9F, # O  OOOOO
    0x87, # O    OOO
    0xC6, # OO   OO 
    0xAC, # O O OO  
    0x00, #         
    0x00, #         
    0x00, #         

    # @1056 'T' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xDD, 0x80, # OO OOO OO
    0x9C, 0x80, # O  OOO  O
    0x9C, 0x80, # O  OOO  O
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x3E, 0x00, #   OOOOO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1088 'U' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xF9, 0xC0, # OOOOO  OOO
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x3B, 0x00, #   OOO OO  
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1120 'V' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xFB, 0x80, # OOOOO OOO
    0x71, 0x00, #  OOO   O 
    0x72, 0x00, #  OOO  O  
    0x7A, 0x00, #  OOOO O  
    0x3A, 0x00, #   OOO O  
    0x3A, 0x00, #   OOO O  
    0x3C, 0x00, #   OOOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1152 'W' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFB, 0x70, # OOOOO OO OOO
    0x73, 0x20, #  OOO  OO  O 
    0x73, 0xA0, #  OOO  OOO O 
    0x7B, 0xC0, #  OOOO OOOO  
    0x3B, 0xC0, #   OOO OOOO  
    0x3B, 0xC0, #   OOO OOOO  
    0x3F, 0xC0, #   OOOOOOOO  
    0x19, 0x80, #    OO  OO   
    0x19, 0x80, #    OO  OO   
    0x19, 0x80, #    OO  OO   
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1184 'X' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xFB, 0x80, # OOOOO OOO
    0x79, 0x00, #  OOOO  O 
    0x7E, 0x00, #  OOOOOO  
    0x3C, 0x00, #   OOOO   
    0x1C, 0x00, #    OOO   
    0x1E, 0x00, #    OOOO  
    0x0E, 0x00, #     OOO  
    0x2F, 0x00, #   O OOOO 
    0x47, 0x00, #  O   OOO 
    0xEF, 0x80, # OOO OOOOO
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1216 'Y' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xFB, 0x80, # OOOOO OOO
    0x71, 0x00, #  OOO   O 
    0x7A, 0x00, #  OOOO O  
    0x3A, 0x00, #   OOO O  
    0x3A, 0x00, #   OOO O  
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x3E, 0x00, #   OOOOO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1248 'Z' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x7F, #  OOOOOOO
    0x6F, #  OO OOOO
    0x5E, #  O OOOO 
    0x1E, #    OOOO 
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x78, #  OOOO   
    0x79, #  OOOO  O
    0xF1, # OOOO   O
    0xF7, # OOOO OOO
    0x00, #         
    0x00, #         
    0x00, #         

    # @1264 '[' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0xF8, # OOOOO
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
    0xF8, # OOOOO
    0x00, #      

    # @1280 '\' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x00, #       
    0xC0, # OO    
    0xC0, # OO    
    0x60, #  OO   
    0x60, #  OO   
    0x60, #  OO   
    0x30, #   OO  
    0x30, #   OO  
    0x10, #    O  
    0x18, #    OO 
    0x18, #    OO 
    0x08, #     O 
    0x0C, #     OO
    0x00, #       

    # @1296 ']' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0xF8, # OOOOO
    0x38, #   OOO
    0x38, #   OOO
    0x38, #   OOO
    0x38, #   OOO
    0x38, #   OOO
    0x38, #   OOO
    0x38, #   OOO
    0x38, #   OOO
    0x38, #   OOO
    0x38, #   OOO
    0xF8, # OOOOO
    0x00, #      

    # @1312 '^' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x10, #    O    
    0x18, #    OO   
    0x18, #    OO   
    0x3C, #   OOOO  
    0x2E, #   O OOO 
    0x46, #  O   OO 
    0x87, # O    OOO
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         
    0x00, #         

    # @1328 '_' (7 pixels wide)
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
    0xFE, # OOOOOOO

    # @1344 '`' (4 pixels wide)
    0xE0, # OOO 
    0x30, #   OO
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

    # @1360 'a' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x1E, 0x00, #    OOOO  
    0x0E, 0x00, #     OOO  
    0x2E, 0x00, #   O OOO  
    0x2E, 0x00, #   O OOO  
    0x2E, 0x00, #   O OOO  
    0x2F, 0x00, #   O OOOO 
    0x27, 0x00, #   O  OOO 
    0x5F, 0x00, #  O OOOOO 
    0x47, 0x00, #  O   OOO 
    0xE7, 0x80, # OOO  OOOO
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1392 'b' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xF3, 0x00, # OOOO  OO  
    0x71, 0x80, #  OOO   OO 
    0x71, 0x80, #  OOO   OO 
    0x71, 0x80, #  OOO   OO 
    0x73, 0x00, #  OOO  OO  
    0x77, 0x80, #  OOO OOOO 
    0x71, 0xC0, #  OOO   OOO
    0x71, 0xC0, #  OOO   OOO
    0x71, 0xC0, #  OOO   OOO
    0xF3, 0x80, # OOOO  OOO 
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1424 'c' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x1F, #    OOOOO
    0x63, #  OO   OO
    0x61, #  OO    O
    0xE1, # OOO    O
    0xE0, # OOO     
    0xE0, # OOO     
    0xE0, # OOO     
    0xE1, # OOO    O
    0x61, #  OO    O
    0x3E, #   OOOOO 
    0x00, #         
    0x00, #         
    0x00, #         

    # @1440 'd' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xF6, 0x00, # OOOO OO  
    0x73, 0x00, #  OOO  OO 
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x00, #  OOO  OO 
    0xF6, 0x00, # OOOO OO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1472 'e' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0xF7, # OOOO OOO
    0x73, #  OOO  OO
    0x71, #  OOO   O
    0x72, #  OOO  O 
    0x76, #  OOO OO 
    0x76, #  OOO OO 
    0x72, #  OOO  O 
    0x71, #  OOO   O
    0x71, #  OOO   O
    0xF7, # OOOO OOO
    0x00, #         
    0x00, #         
    0x00, #         

    # @1488 'f' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0xF7, # OOOO OOO
    0x73, #  OOO  OO
    0x71, #  OOO   O
    0x72, #  OOO  O 
    0x76, #  OOO OO 
    0x76, #  OOO OO 
    0x72, #  OOO  O 
    0x70, #  OOO    
    0x70, #  OOO    
    0xF8, # OOOOO   
    0x00, #         
    0x00, #         
    0x00, #         

    # @1504 'g' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x35, #   OO O O
    0x63, #  OO   OO
    0xE1, # OOO    O
    0xE1, # OOO    O
    0xE0, # OOO     
    0xEF, # OOO OOOO
    0xE7, # OOO  OOO
    0xE7, # OOO  OOO
    0x67, #  OO  OOO
    0x3E, #   OOOOO 
    0x00, #         
    0x00, #         
    0x00, #         

    # @1520 'h' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xFF, 0xC0, # OOOOOOOOOO
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x7F, 0x80, #  OOOOOOOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0xFF, 0xC0, # OOOOOOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1552 'i' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0xF8, # OOOOO
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0x70, #  OOO 
    0xF8, # OOOOO
    0x00, #      
    0x00, #      
    0x00, #      

    # @1568 'j' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x1F, #    OOOOO
    0x0E, #     OOO 
    0x0E, #     OOO 
    0x0E, #     OOO 
    0x0E, #     OOO 
    0x0E, #     OOO 
    0x6E, #  OO OOO 
    0xFE, # OOOOOOO 
    0xEE, # OOO OOO 
    0x6C, #  OO OO  
    0x00, #         
    0x00, #         
    0x00, #         

    # @1584 'k' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xFB, 0x80, # OOOOO OOO 
    0x73, 0x00, #  OOO  OO  
    0x72, 0x00, #  OOO  O   
    0x76, 0x00, #  OOO OO   
    0x7E, 0x00, #  OOOOOO   
    0x7F, 0x00, #  OOOOOOO  
    0x7F, 0x00, #  OOOOOOO  
    0x77, 0x80, #  OOO OOOO 
    0x77, 0x80, #  OOO OOOO 
    0xFF, 0xC0, # OOOOOOOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1616 'l' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0xF8, # OOOOO   
    0x70, #  OOO    
    0x70, #  OOO    
    0x70, #  OOO    
    0x70, #  OOO    
    0x70, #  OOO    
    0x70, #  OOO    
    0x71, #  OOO   O
    0x71, #  OOO   O
    0xF7, # OOOO OOO
    0x00, #         
    0x00, #         
    0x00, #         

    # @1632 'm' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xF3, 0xC0, # OOOO  OOOO
    0x73, 0x80, #  OOO  OOO 
    0x7B, 0x80, #  OOOO OOO 
    0x3B, 0x80, #   OOO OOO 
    0xBF, 0x80, # O OOOOOOO 
    0x7F, 0x80, #  OOOOOOOO 
    0x5B, 0x80, #  O OO OOO 
    0x5B, 0x80, #  O OO OOO 
    0x5B, 0x80, #  O OO OOO 
    0xF7, 0xC0, # OOOO OOOOO
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1664 'n' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xF3, 0x80, # OOOO  OOO
    0x79, 0x00, #  OOOO  O 
    0x3D, 0x00, #   OOOO O 
    0xBD, 0x00, # O OOOO O 
    0x5F, 0x00, #  O OOOOO 
    0x5F, 0x00, #  O OOOOO 
    0x4F, 0x00, #  O  OOOO 
    0x47, 0x00, #  O   OOO 
    0x47, 0x00, #  O   OOO 
    0xE3, 0x00, # OOO   OO 
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1696 'o' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x36, 0x00, #   OO OO  
    0x63, 0x00, #  OO   OO 
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0x63, 0x00, #  OO   OO 
    0x36, 0x00, #   OO OO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1728 'p' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xF7, 0x00, # OOOO OOO 
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x80, #  OOO  OOO
    0x73, 0x00, #  OOO  OO 
    0x74, 0x00, #  OOO O   
    0x70, 0x00, #  OOO     
    0x70, 0x00, #  OOO     
    0xF8, 0x00, # OOOOO    
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1760 'q' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x3E, 0x00, #   OOOOO  
    0x63, 0x00, #  OO   OO 
    0x63, 0x80, #  OO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0xE3, 0x80, # OOO   OOO
    0x63, 0x80, #  OO   OOO
    0x6F, 0x00, #  OO OOOO 
    0x3F, 0x80, #   OOOOOOO
    0x01, 0x80, #        OO
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1792 'r' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xF7, 0x00, # OOOO OOO  
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x00, #  OOO  OO  
    0x77, 0x00, #  OOO OOO  
    0x73, 0x80, #  OOO  OOO 
    0x73, 0x80, #  OOO  OOO 
    0x73, 0xC0, #  OOO  OOOO
    0xFB, 0x80, # OOOOO OOO 
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1824 's' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x6A, #  OO O O 
    0xE6, # OOO  OO 
    0xE2, # OOO   O 
    0xFA, # OOOOO O 
    0xFE, # OOOOOOO 
    0x7F, #  OOOOOOO
    0x9F, # O  OOOOO
    0x87, # O    OOO
    0xC6, # OO   OO 
    0xAC, # O O OO  
    0x00, #         
    0x00, #         
    0x00, #         

    # @1840 't' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xDD, 0x80, # OO OOO OO
    0x9C, 0x80, # O  OOO  O
    0x9C, 0x80, # O  OOO  O
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x3E, 0x00, #   OOOOO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1872 'u' (10 pixels wide)
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           
    0xF9, 0xC0, # OOOOO  OOO
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x70, 0x80, #  OOO    O 
    0x3B, 0x00, #   OOO OO  
    0x00, 0x00, #           
    0x00, 0x00, #           
    0x00, 0x00, #           

    # @1904 'v' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xFB, 0x80, # OOOOO OOO
    0x71, 0x00, #  OOO   O 
    0x72, 0x00, #  OOO  O  
    0x7A, 0x00, #  OOOO O  
    0x3A, 0x00, #   OOO O  
    0x3A, 0x00, #   OOO O  
    0x3C, 0x00, #   OOOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @1936 'w' (12 pixels wide)
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             
    0xFB, 0x70, # OOOOO OO OOO
    0x73, 0x20, #  OOO  OO  O 
    0x73, 0xA0, #  OOO  OOO O 
    0x7B, 0xC0, #  OOOO OOOO  
    0x3B, 0xC0, #   OOO OOOO  
    0x3B, 0xC0, #   OOO OOOO  
    0x3F, 0xC0, #   OOOOOOOO  
    0x19, 0x80, #    OO  OO   
    0x19, 0x80, #    OO  OO   
    0x19, 0x80, #    OO  OO   
    0x00, 0x00, #             
    0x00, 0x00, #             
    0x00, 0x00, #             

    # @1968 'x' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xFB, 0x80, # OOOOO OOO
    0x79, 0x00, #  OOOO  O 
    0x7E, 0x00, #  OOOOOO  
    0x3C, 0x00, #   OOOO   
    0x1C, 0x00, #    OOO   
    0x1E, 0x00, #    OOOO  
    0x0E, 0x00, #     OOO  
    0x2F, 0x00, #   O OOOO 
    0x47, 0x00, #  O   OOO 
    0xEF, 0x80, # OOO OOOOO
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @2000 'y' (9 pixels wide)
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          
    0xFB, 0x80, # OOOOO OOO
    0x71, 0x00, #  OOO   O 
    0x7A, 0x00, #  OOOO O  
    0x3A, 0x00, #   OOO O  
    0x3A, 0x00, #   OOO O  
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x1C, 0x00, #    OOO   
    0x3E, 0x00, #   OOOOO  
    0x00, 0x00, #          
    0x00, 0x00, #          
    0x00, 0x00, #          

    # @2032 'z' (8 pixels wide)
    0x00, #         
    0x00, #         
    0x00, #         
    0x7F, #  OOOOOOO
    0x6F, #  OO OOOO
    0x5E, #  O OOOO 
    0x1E, #    OOOO 
    0x3C, #   OOOO  
    0x3C, #   OOOO  
    0x78, #  OOOO   
    0x79, #  OOOO  O
    0xF1, # OOOO   O
    0xF7, # OOOO OOO
    0x00, #         
    0x00, #         
    0x00, #         

    # @2048 '{' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0x78, #  OOOO
    0x60, #  OO  
    0x60, #  OO  
    0x60, #  OO  
    0x60, #  OO  
    0x60, #  OO  
    0xC0, # OO   
    0x60, #  OO  
    0x60, #  OO  
    0x60, #  OO  
    0x60, #  OO  
    0x78, #  OOOO
    0x00, #      

    # @2064 '|' (2 pixels wide)
    0x00, #   
    0x00, #   
    0x00, #   
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO
    0xC0, # OO

    # @2080 '}' (5 pixels wide)
    0x00, #      
    0x00, #      
    0x00, #      
    0xF0, # OOOO 
    0x30, #   OO 
    0x30, #   OO 
    0x30, #   OO 
    0x30, #   OO 
    0x30, #   OO 
    0x18, #    OO
    0x30, #   OO 
    0x30, #   OO 
    0x30, #   OO 
    0x30, #   OO 
    0xF0, # OOOO 
    0x00, #      

    # @2096 '~' (6 pixels wide)
    0x00, #       
    0x00, #       
    0x64, #  OO  O
    0x98, # O  OO 
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

    # @2112 '°' (4 pixels wide)
    0x00, #     
    0x00, #     
    0x00, #     
    0x60, #  OO 
    0xF0, # OOOO
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
)

descriptors = (
    (3,0),# !
    (5,16),# "
    (9,32),# #
    (7,64),# $
    (11,80),# %
    (10,112),# &
    (2,144),# '
    (4,160),# (
    (4,176),# )
    (5,192),# *
    (7,208),# +
    (3,224),# ,
    (4,240),# -
    (3,256),# .
    (6,272),# /
    (8,288),# 0
    (5,304),# 1
    (8,320),# 2
    (8,336),# 3
    (8,352),# 4
    (7,368),# 5
    (7,384),# 6
    (7,400),# 7
    (7,416),# 8
    (8,432),# 9
    (3,448),# :
    (3,464),# ;
    (6,480),# <
    (7,496),# =
    (6,512),# >
    (7,528),# ?
    (10,544),# @
    (9,576),# A
    (10,608),# B
    (8,640),# C
    (9,656),# D
    (8,688),# E
    (8,704),# F
    (8,720),# G
    (10,736),# H
    (5,768),# I
    (8,784),# J
    (10,800),# K
    (8,832),# L
    (10,848),# M
    (9,880),# N
    (9,912),# O
    (9,944),# P
    (9,976),# Q
    (10,1008),# R
    (8,1040),# S
    (9,1056),# T
    (10,1088),# U
    (9,1120),# V
    (12,1152),# W
    (9,1184),# X
    (9,1216),# Y
    (8,1248),# Z
    (5,1264),# [
    (6,1280),# \
    (5,1296),# ]
    (8,1312),# ^
    (7,1328),# _
    (4,1344),# `
    (9,1360),# a
    (10,1392),# b
    (8,1424),# c
    (9,1440),# d
    (8,1472),# e
    (8,1488),# f
    (8,1504),# g
    (10,1520),# h
    (5,1552),# i
    (8,1568),# j
    (10,1584),# k
    (8,1616),# l
    (10,1632),# m
    (9,1664),# n
    (9,1696),# o
    (9,1728),# p
    (9,1760),# q
    (10,1792),# r
    (8,1824),# s
    (9,1840),# t
    (10,1872),# u
    (9,1904),# v
    (12,1936),# w
    (9,1968),# x
    (9,2000),# y
    (8,2032),# z
    (5,2048),# {
    (2,2064),# |
    (5,2080),# }
    (6,2096),# ~
    (4,2112),# °
)

kerning = (
    (3,3,3,3,3,3,3,3,3,3,2,3,2,3,2,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,),
    (5,5,3,4,4,1,5,3,5,4,2,2,1,2,1,4,5,4,3,2,4,4,5,4,4,4,4,3,4,5,4,4,2,5,4,5,5,5,4,5,5,2,5,5,5,5,4,5,4,5,4,5,5,5,5,5,5,4,5,5,5,2,0,1,2,5,4,5,5,5,4,5,5,2,5,5,5,5,4,5,4,5,4,5,5,5,5,5,5,4,4,5,5,5,4,),
    (9,9,8,9,9,8,9,8,8,9,7,6,7,8,6,9,8,9,8,8,9,9,9,9,9,8,7,7,7,9,9,8,7,8,8,8,8,8,9,8,8,8,8,8,8,8,9,8,8,8,9,9,8,8,8,8,8,8,9,8,8,7,2,5,7,8,8,8,8,8,9,8,8,8,8,8,8,8,9,8,8,8,9,9,8,8,8,8,8,8,8,9,8,8,9,),
    (7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,7,7,7,6,6,7,6,6,6,7,6,6,7,6,6,6,7,7,6,7,6,7,7,6,6,6,6,6,7,7,7,6,7,0,3,6,6,7,6,6,6,7,6,6,7,6,6,6,7,7,6,7,6,7,7,6,6,6,6,6,7,7,7,6,6,7,),
    (11,8,11,11,8,11,9,11,10,8,9,11,7,11,10,10,10,10,11,11,11,11,9,11,10,11,11,8,10,11,10,10,10,10,11,10,10,10,11,10,10,11,10,10,10,10,11,10,10,10,11,8,10,8,8,10,8,11,11,8,9,6,4,7,10,10,11,10,10,10,11,10,10,11,10,10,10,10,11,10,10,10,11,8,10,8,8,10,8,11,10,11,9,8,8,),
    (10,8,9,10,9,9,8,10,9,10,10,10,10,10,9,10,10,9,9,9,9,10,8,9,10,10,10,10,10,9,9,10,10,10,10,10,10,10,10,10,10,9,10,10,10,10,10,10,10,10,10,8,9,8,8,10,8,10,10,9,8,10,3,6,10,10,10,10,10,10,10,10,10,9,10,10,10,10,10,10,10,10,10,8,9,8,8,10,8,10,9,10,8,8,9,),
    (2,2,1,2,2,0,2,1,2,2,0,0,0,0,0,2,2,2,1,0,2,2,2,2,2,1,1,0,1,2,2,1,0,2,1,2,2,2,2,2,2,0,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1,2,2,2,0,0,0,0,2,1,2,2,2,2,2,2,0,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1,1,2,2,2,2,),
    (4,4,3,4,4,3,4,3,4,4,3,4,3,3,4,3,4,4,3,3,3,3,4,4,3,3,4,3,3,4,4,3,3,4,3,4,4,4,3,4,4,3,4,4,4,4,3,4,3,4,4,4,4,4,4,4,4,3,4,4,4,3,0,0,3,4,3,4,4,4,3,4,4,3,4,4,4,4,3,4,3,4,4,4,4,4,4,4,4,3,3,4,4,4,4,),
    (4,3,4,4,3,4,3,4,3,4,4,3,4,4,2,4,3,3,4,4,4,4,3,4,4,4,4,4,4,3,3,4,3,3,4,3,3,3,4,3,3,4,3,3,4,3,4,3,4,3,4,3,3,2,2,3,2,3,4,3,2,4,0,0,3,3,4,3,3,3,4,3,3,4,3,3,4,3,4,3,4,3,4,3,3,2,2,3,2,3,4,4,2,1,3,),
    (5,5,4,5,5,2,5,5,5,5,5,2,5,2,2,5,4,5,4,3,5,5,5,5,5,5,5,5,5,5,5,5,3,4,5,4,4,4,5,4,4,1,4,4,5,4,5,4,5,4,5,5,4,4,4,4,4,4,5,5,3,4,0,1,3,4,5,4,4,4,5,4,4,1,4,4,5,4,5,4,5,4,5,5,4,4,4,4,4,4,4,5,3,3,5,),
    (6,4,5,7,6,6,5,7,6,7,7,4,7,4,5,7,6,4,4,6,6,7,4,6,7,7,7,7,7,5,5,7,5,6,7,6,6,6,7,6,6,4,6,6,7,6,7,6,7,6,7,4,6,5,5,4,5,5,7,6,5,7,0,3,5,6,7,6,6,6,7,6,6,4,6,6,7,6,7,6,7,6,7,4,6,5,5,4,5,5,6,7,5,1,6,),
    (3,0,2,3,0,3,1,2,3,0,1,3,0,3,2,2,3,2,3,0,3,2,1,3,2,3,3,0,0,3,2,2,3,3,2,3,3,3,2,3,3,3,3,3,3,3,2,3,2,3,3,1,2,0,0,3,1,3,3,0,2,0,0,0,3,3,2,3,3,3,2,3,3,3,3,3,3,3,2,3,2,3,3,1,2,0,0,3,1,3,2,3,2,0,0,),
    (3,0,2,4,3,3,2,4,3,4,4,1,4,1,2,4,3,0,0,3,3,4,1,3,4,4,4,4,4,2,2,4,2,3,4,3,3,3,4,3,3,0,3,3,4,3,4,3,4,3,4,1,3,2,2,1,2,2,4,3,2,4,0,0,2,3,4,3,3,3,4,3,3,0,3,3,4,3,4,3,4,3,4,1,3,2,2,1,2,2,3,4,2,0,3,),
    (3,0,3,3,0,3,1,3,2,0,1,3,0,3,2,2,3,2,3,3,3,3,1,3,2,3,3,0,0,3,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,1,2,0,0,3,1,3,3,0,1,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,1,2,0,0,3,1,3,2,3,1,0,0,),
    (6,6,4,6,6,4,6,5,6,6,5,3,5,3,2,5,6,6,5,4,5,5,6,6,5,5,5,5,5,6,6,5,3,6,5,6,6,6,5,6,6,3,6,6,6,6,5,6,5,6,6,6,6,6,6,6,6,5,6,6,6,4,0,2,3,6,5,6,6,6,5,6,6,3,6,6,6,6,5,6,5,6,6,6,6,6,6,6,6,5,5,6,6,6,6,),
    (8,8,8,8,8,8,8,8,7,8,8,7,8,8,6,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,8,7,7,7,8,7,7,8,7,7,8,8,8,7,8,7,8,8,7,7,7,7,7,7,8,7,6,8,1,4,7,7,8,7,7,7,8,7,7,8,7,7,8,8,8,7,8,7,8,8,7,7,7,7,7,7,8,8,6,6,8,),
    (5,4,4,4,4,4,4,4,4,4,4,5,4,5,4,4,5,4,4,4,4,4,4,4,4,5,5,4,4,4,4,4,5,5,4,5,5,5,4,5,5,4,5,5,5,5,4,5,4,5,5,4,4,4,4,5,4,5,5,4,4,4,0,1,5,5,4,5,5,5,4,5,5,4,5,5,5,5,4,5,4,5,5,4,4,4,4,5,4,5,4,5,4,4,4,),
    (8,8,8,8,8,8,8,8,8,8,7,8,7,8,7,8,7,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,7,7,8,7,7,7,8,7,7,8,7,7,7,8,8,7,8,7,8,8,7,7,7,7,7,8,8,8,6,6,1,4,7,7,8,7,7,7,8,7,7,8,7,7,7,8,8,7,8,7,8,8,7,7,7,7,7,8,7,8,6,6,8,),
    (8,8,8,8,8,8,8,8,8,8,7,8,7,8,7,8,7,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,7,7,8,7,7,7,8,7,7,8,7,7,7,8,8,7,8,7,8,8,7,7,7,7,7,8,8,8,7,7,1,4,7,7,8,7,7,7,8,7,7,8,7,7,7,8,8,7,8,7,8,8,7,7,7,7,7,8,8,8,7,7,8,),
    (8,7,8,8,7,8,7,8,7,7,7,8,7,8,7,7,8,7,8,8,8,8,7,8,7,8,8,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,7,7,7,7,8,7,8,8,7,7,7,1,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,7,7,7,7,8,7,8,7,8,7,7,7,),
    (7,6,7,7,6,7,6,7,6,6,7,7,7,7,6,7,6,6,7,7,7,7,6,7,6,7,7,6,7,7,6,7,6,6,7,6,6,6,7,6,6,7,6,6,6,6,7,6,7,6,7,6,6,6,6,6,6,7,7,6,6,7,0,3,6,6,7,6,6,6,7,6,6,7,6,6,6,6,7,6,7,6,7,6,6,6,6,6,6,7,7,7,6,6,6,),
    (7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,7,7,7,6,6,7,6,6,6,7,6,6,7,6,6,6,7,7,6,7,6,7,7,6,6,6,6,6,7,7,7,6,7,0,3,6,6,7,6,6,6,7,6,6,7,6,6,6,7,7,6,7,6,7,7,6,6,6,6,6,7,7,7,6,6,7,),
    (7,7,5,7,7,5,7,5,7,7,5,5,5,5,4,6,7,7,6,5,6,6,7,7,6,5,5,5,5,7,7,5,5,7,6,7,7,7,6,7,7,5,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,6,7,7,7,5,0,3,5,7,6,7,7,7,6,7,7,5,7,7,7,7,6,7,6,7,7,7,7,7,7,7,7,6,6,7,7,7,7,),
    (7,7,7,7,7,7,7,7,7,7,6,7,6,7,6,7,6,7,7,7,7,7,7,7,7,7,7,6,7,7,7,7,6,6,7,6,6,6,7,6,6,7,6,6,6,7,7,6,7,6,7,7,6,6,6,6,6,7,7,7,6,6,0,3,6,6,7,6,6,6,7,6,6,7,6,6,6,7,7,6,7,6,7,7,6,6,6,6,6,7,7,7,6,6,7,),
    (8,8,8,8,8,8,8,8,7,8,8,7,8,8,6,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,8,7,7,7,8,7,7,8,7,7,8,8,8,7,8,7,8,8,7,7,7,7,7,7,8,7,6,8,1,4,7,7,8,7,7,7,8,7,7,8,7,7,8,8,8,7,8,7,8,8,7,7,7,7,7,7,8,8,6,6,8,),
    (3,3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,2,3,1,3,3,2,1,3,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,2,3,1,3,2,3,1,0,3,),
    (3,3,2,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,2,3,3,1,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,2,3,1,3,3,2,2,3,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,2,2,3,1,3,2,3,2,0,3,),
    (6,6,6,6,6,6,6,6,6,6,5,6,5,6,5,6,6,6,6,6,6,6,6,6,5,6,6,4,6,6,6,6,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,0,2,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,),
    (7,7,5,7,7,7,7,7,6,7,7,4,7,4,5,7,6,7,6,7,6,7,5,7,7,7,7,7,7,7,5,7,5,6,7,6,6,6,7,6,6,6,6,6,7,7,7,6,7,6,7,4,6,6,6,5,5,6,7,6,5,7,0,3,5,6,7,6,6,6,7,6,6,6,6,6,7,7,7,6,7,6,7,4,6,6,6,5,5,6,7,7,5,1,7,),
    (5,4,4,6,5,5,4,6,5,6,6,3,6,3,4,6,5,4,3,5,5,6,3,5,6,6,6,6,6,4,4,6,4,5,6,5,5,5,6,5,5,3,5,5,6,5,6,5,6,5,6,3,5,4,4,3,4,4,6,5,4,6,0,2,4,5,6,5,5,5,6,5,5,3,5,5,6,5,6,5,6,5,6,3,5,4,4,3,4,4,5,6,4,1,5,),
    (7,7,6,7,7,4,7,6,7,7,6,4,6,4,4,7,6,7,6,5,7,7,7,7,7,7,7,6,7,7,7,7,5,6,7,6,6,6,7,6,6,4,6,6,6,7,7,6,7,6,7,7,6,6,6,6,6,6,7,7,6,5,0,3,5,6,7,6,6,6,7,6,6,4,6,6,6,7,7,6,7,6,7,7,6,6,6,6,6,6,6,7,6,6,7,),
    (10,10,9,10,10,9,10,10,9,10,10,9,10,9,8,10,9,10,9,9,10,10,10,10,10,10,10,10,10,10,10,10,9,9,10,9,9,9,10,9,9,8,9,9,10,10,10,9,10,9,10,10,9,9,9,9,9,9,10,9,8,10,3,6,9,9,10,9,9,9,10,9,9,8,9,9,10,10,10,9,10,9,10,10,9,9,9,9,9,9,9,10,8,8,10,),
    (9,7,8,8,7,8,7,8,8,7,8,9,8,9,8,8,9,8,8,8,8,8,7,8,7,9,9,7,8,8,8,8,9,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,8,9,9,7,7,7,7,9,7,9,9,7,7,8,2,5,9,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,8,9,9,7,7,7,7,9,7,9,8,9,7,7,7,),
    (10,9,10,10,9,10,9,10,9,9,9,10,9,10,9,10,9,9,10,10,10,10,9,10,9,10,10,8,10,10,9,10,9,9,10,9,9,9,10,9,9,10,9,9,9,9,10,9,10,9,10,9,9,8,8,9,8,10,10,9,8,9,3,6,9,9,10,9,9,9,10,9,9,10,9,9,9,9,10,9,10,9,10,9,9,8,8,9,8,10,10,10,8,8,9,),
    (8,8,8,8,8,8,8,8,8,8,6,8,4,8,7,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,6,1,4,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,),
    (9,9,9,9,9,9,9,9,8,9,9,8,9,9,7,9,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,9,8,8,8,9,8,8,9,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,8,7,9,2,5,8,8,9,8,8,8,9,8,8,9,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,9,7,7,9,),
    (8,8,8,8,8,8,8,8,8,8,7,8,7,8,7,8,8,8,8,8,8,8,8,8,8,8,8,7,7,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,7,1,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,7,8,8,8,8,),
    (8,8,7,8,8,7,8,7,8,8,7,5,7,5,5,8,8,8,7,7,8,8,8,8,8,7,7,7,7,8,8,7,6,8,7,8,8,8,8,8,8,6,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,7,8,8,8,7,1,4,6,8,7,8,8,8,8,8,8,6,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,7,7,8,8,8,8,),
    (8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,1,4,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,),
    (10,10,9,9,9,9,10,9,10,9,9,10,9,10,9,9,10,9,9,9,9,9,10,9,9,10,10,9,9,10,9,9,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,10,10,10,10,10,10,10,10,10,10,10,9,3,6,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,10,10,10,10,10,10,10,10,9,10,10,10,9,),
    (5,5,4,4,4,4,5,4,5,4,4,5,4,5,4,4,5,4,4,4,4,4,5,4,4,5,5,4,4,5,4,4,5,5,4,5,5,5,4,5,5,4,5,5,5,5,4,5,4,5,5,5,5,5,5,5,5,5,5,5,5,4,0,1,5,5,4,5,5,5,4,5,5,4,5,5,5,5,4,5,4,5,5,5,5,5,5,5,5,5,4,5,5,5,4,),
    (8,8,7,7,7,7,8,7,8,7,7,7,7,7,6,7,8,7,7,7,7,7,8,7,7,7,7,7,7,8,7,7,6,8,7,8,8,8,7,8,8,7,8,8,8,8,7,8,7,8,7,8,8,8,8,8,8,7,8,8,8,7,1,4,6,8,7,8,8,8,7,8,8,7,8,8,8,8,7,8,7,8,7,8,8,8,8,8,8,7,7,8,8,8,7,),
    (10,9,9,9,8,9,9,9,9,8,8,10,8,10,9,8,10,9,9,9,9,9,9,9,8,10,10,7,8,9,9,8,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,8,10,10,9,9,9,9,10,9,10,10,9,9,8,3,6,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,8,10,10,9,9,9,9,10,9,10,9,10,9,9,8,),
    (8,5,8,8,5,8,6,8,7,4,6,8,4,8,7,7,8,7,8,8,8,8,6,8,7,8,8,4,4,8,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,6,7,5,5,8,6,8,8,5,6,4,1,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,6,7,5,5,8,6,8,7,8,6,5,4,),
    (10,10,9,9,9,9,10,9,10,9,9,10,9,10,9,9,10,9,9,9,9,9,10,9,9,10,10,9,9,10,9,9,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,10,10,10,10,10,10,10,10,10,10,10,9,3,6,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,10,10,10,10,10,10,10,10,9,10,10,10,9,),
    (9,9,8,8,8,8,9,8,9,8,8,8,8,8,7,8,9,8,8,8,8,8,9,8,8,8,8,8,8,9,8,8,8,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,8,9,8,9,9,9,9,9,9,8,9,9,9,8,2,5,8,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,8,9,8,9,9,9,9,9,9,8,8,9,9,9,8,),
    (9,9,9,9,9,9,9,9,8,9,9,8,9,9,7,9,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,9,8,8,8,9,8,8,9,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,8,7,9,2,5,8,8,9,8,8,8,9,8,8,9,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,9,7,7,9,),
    (9,9,8,9,9,7,9,9,9,9,9,6,9,6,6,9,8,9,8,7,9,9,9,9,9,9,9,9,9,9,9,9,7,8,9,8,8,8,9,8,8,5,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,9,8,8,2,5,7,8,9,8,8,8,9,8,8,5,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,8,9,8,8,9,),
    (9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,9,8,9,9,8,7,9,2,5,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,9,8,9,9,9,7,7,9,),
    (10,9,9,10,9,10,9,9,9,9,8,10,8,10,9,9,9,9,10,9,10,9,9,10,9,10,10,8,9,10,9,9,9,9,9,9,9,9,9,9,9,10,9,9,9,9,9,9,9,9,10,9,9,8,8,9,8,10,10,9,8,8,3,6,9,9,9,9,9,9,9,9,9,10,9,9,9,9,9,9,9,9,10,9,9,8,8,9,8,10,9,10,8,8,9,),
    (8,7,8,8,7,8,7,8,7,7,8,7,8,8,6,8,7,7,8,8,8,8,7,8,7,8,8,7,8,7,7,8,7,7,8,7,7,7,8,7,7,8,7,7,7,7,8,7,8,7,8,7,7,7,7,7,7,7,8,7,7,8,1,4,7,7,8,7,7,7,8,7,7,8,7,7,7,7,8,7,8,7,8,7,7,7,7,7,7,7,8,8,7,7,7,),
    (9,9,8,9,9,6,9,8,9,9,7,7,6,7,6,9,9,9,8,6,9,9,9,9,9,7,7,6,6,9,9,8,7,9,8,9,9,9,9,9,9,6,9,9,9,9,9,9,8,9,9,9,9,9,9,9,9,8,9,9,9,7,2,5,7,9,8,9,9,9,9,9,9,6,9,9,9,9,9,9,8,9,9,9,9,9,9,9,9,8,8,9,9,9,9,),
    (10,10,9,9,9,9,10,9,10,9,9,9,9,9,8,9,10,9,9,9,9,9,10,9,9,9,9,9,9,10,9,9,8,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,9,10,10,10,10,10,10,9,10,10,10,9,3,6,8,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,9,10,10,10,10,10,10,9,9,10,10,10,9,),
    (9,9,6,8,8,6,9,7,9,8,7,6,7,6,5,7,9,8,7,6,8,7,9,8,7,7,7,7,7,9,8,7,6,9,7,9,9,9,7,9,9,6,9,9,9,9,7,9,7,9,8,9,9,9,9,9,9,8,9,9,9,7,2,5,6,9,7,9,9,9,7,9,9,6,9,9,9,9,7,9,7,9,8,9,9,9,9,9,9,8,8,9,9,9,8,),
    (12,12,10,11,11,10,12,10,12,11,10,9,10,9,8,11,12,11,10,10,11,11,12,11,11,10,10,10,10,12,11,10,9,12,10,12,12,12,11,12,12,9,12,12,12,12,11,12,10,12,11,12,12,12,12,12,12,11,12,12,12,10,5,8,9,12,10,12,12,12,11,12,12,9,12,12,12,12,11,12,10,12,11,12,12,12,12,12,12,11,11,12,12,12,11,),
    (9,9,8,8,8,8,9,8,9,8,7,9,7,9,8,7,9,8,8,8,8,8,9,8,7,9,9,6,7,9,8,7,9,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,7,9,9,9,9,9,9,9,9,9,9,9,9,7,2,5,9,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,7,9,9,9,9,9,9,9,9,9,8,9,9,9,8,),
    (9,9,6,8,8,6,9,7,9,8,7,7,7,7,6,7,9,8,7,6,8,7,9,8,7,7,7,7,7,9,8,7,7,9,7,9,9,9,7,9,9,6,9,9,9,9,7,9,7,9,8,9,9,9,9,9,9,8,9,9,9,6,2,5,7,9,7,9,9,9,7,9,9,6,9,9,9,9,7,9,7,9,8,9,9,9,9,9,9,8,8,9,9,9,8,),
    (8,8,8,8,8,8,8,8,8,8,6,8,6,8,7,7,8,8,8,8,8,8,8,8,7,8,8,6,7,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,6,1,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,7,8,8,8,8,),
    (5,5,3,3,4,3,5,3,5,4,3,5,3,3,5,3,5,4,3,3,4,3,5,4,3,3,5,3,3,5,4,3,3,5,3,5,5,5,3,5,5,3,5,5,5,5,3,5,3,5,4,5,5,5,5,5,5,4,5,5,5,3,0,1,3,5,3,5,5,5,3,5,5,3,5,5,5,5,3,5,3,5,4,5,5,5,5,5,5,4,4,5,5,5,4,),
    (5,3,4,5,3,5,4,4,6,3,4,6,4,5,6,4,5,4,5,4,5,4,3,5,4,5,6,3,4,5,4,4,5,5,4,5,5,5,4,5,5,5,5,5,5,5,4,5,4,5,5,3,4,2,2,5,3,5,6,2,6,4,0,2,5,5,4,5,5,5,4,5,5,5,5,5,5,5,4,5,4,5,5,3,4,2,2,5,3,5,5,6,6,2,3,),
    (5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,0,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,),
    (7,7,6,7,7,7,7,8,7,7,8,5,8,5,6,8,7,7,6,7,7,8,6,7,7,8,8,7,8,7,6,8,6,7,8,7,7,7,8,7,7,4,7,7,7,7,8,7,8,7,7,6,7,6,6,5,5,6,8,6,6,8,1,4,6,7,8,7,7,7,8,7,7,4,7,7,7,7,8,7,8,7,7,6,7,6,6,5,5,6,7,8,6,5,7,),
    (4,2,0,0,0,0,5,3,3,2,0,4,3,4,1,0,2,0,0,0,0,0,0,0,0,4,4,1,0,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,7,3,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,7,2,1,3,),
    (1,0,0,0,0,0,2,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,),
    (9,7,8,8,7,8,7,8,8,7,8,9,8,9,8,8,9,8,8,8,8,8,7,8,7,9,9,7,8,8,8,8,9,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,8,9,9,7,7,7,7,9,7,9,9,7,7,8,2,5,9,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,8,9,9,7,7,7,7,9,7,9,8,9,7,7,7,),
    (10,9,10,10,9,10,9,10,9,9,9,10,9,10,9,10,9,9,10,10,10,10,9,10,9,10,10,8,10,10,9,10,9,9,10,9,9,9,10,9,9,10,9,9,9,9,10,9,10,9,10,9,9,8,8,9,8,10,10,9,8,9,3,6,9,9,10,9,9,9,10,9,9,10,9,9,9,9,10,9,10,9,10,9,9,8,8,9,8,10,10,10,8,8,9,),
    (8,8,8,8,8,8,8,8,8,8,6,8,4,8,7,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,6,1,4,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,),
    (9,9,9,9,9,9,9,9,8,9,9,8,9,9,7,9,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,9,8,8,8,9,8,8,9,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,8,7,9,2,5,8,8,9,8,8,8,9,8,8,9,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,9,7,7,9,),
    (8,8,8,8,8,8,8,8,8,8,7,8,7,8,7,8,8,8,8,8,8,8,8,8,8,8,8,7,7,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,7,1,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,7,8,8,8,8,),
    (8,8,7,8,8,7,8,7,8,8,7,5,7,5,5,8,8,8,7,7,8,8,8,8,8,7,7,7,7,8,8,7,6,8,7,8,8,8,8,8,8,6,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,7,8,8,8,7,1,4,6,8,7,8,8,8,8,8,8,6,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,7,7,8,8,8,8,),
    (8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,1,4,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,),
    (10,10,9,9,9,9,10,9,10,9,9,10,9,10,9,9,10,9,9,9,9,9,10,9,9,10,10,9,9,10,9,9,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,10,10,10,10,10,10,10,10,10,10,10,9,3,6,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,10,10,10,10,10,10,10,10,9,10,10,10,9,),
    (5,5,4,4,4,4,5,4,5,4,4,5,4,5,4,4,5,4,4,4,4,4,5,4,4,5,5,4,4,5,4,4,5,5,4,5,5,5,4,5,5,4,5,5,5,5,4,5,4,5,5,5,5,5,5,5,5,5,5,5,5,4,0,1,5,5,4,5,5,5,4,5,5,4,5,5,5,5,4,5,4,5,5,5,5,5,5,5,5,5,4,5,5,5,4,),
    (8,8,7,7,7,7,8,7,8,7,7,7,7,7,6,7,8,7,7,7,7,7,8,7,7,7,7,7,7,8,7,7,6,8,7,8,8,8,7,8,8,7,8,8,8,8,7,8,7,8,7,8,8,8,8,8,8,7,8,8,8,7,1,4,6,8,7,8,8,8,7,8,8,7,8,8,8,8,7,8,7,8,7,8,8,8,8,8,8,7,7,8,8,8,7,),
    (10,9,9,9,8,9,9,9,9,8,8,10,8,10,9,8,10,9,9,9,9,9,9,9,8,10,10,7,8,9,9,8,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,8,10,10,9,9,9,9,10,9,10,10,9,9,8,3,6,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,8,10,10,9,9,9,9,10,9,10,9,10,9,9,8,),
    (8,5,8,8,5,8,6,8,7,4,6,8,4,8,7,7,8,7,8,8,8,8,6,8,7,8,8,4,4,8,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,6,7,5,5,8,6,8,8,5,6,4,1,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,6,7,5,5,8,6,8,7,8,6,5,4,),
    (10,10,9,9,9,9,10,9,10,9,9,10,9,10,9,9,10,9,9,9,9,9,10,9,9,10,10,9,9,10,9,9,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,10,10,10,10,10,10,10,10,10,10,10,9,3,6,10,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,10,10,10,10,10,10,10,10,9,10,10,10,9,),
    (9,9,8,8,8,8,9,8,9,8,8,8,8,8,7,8,9,8,8,8,8,8,9,8,8,8,8,8,8,9,8,8,8,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,8,9,8,9,9,9,9,9,9,8,9,9,9,8,2,5,8,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,8,9,8,9,9,9,9,9,9,8,8,9,9,9,8,),
    (9,9,9,9,9,9,9,9,8,9,9,8,9,9,7,9,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,9,8,8,8,9,8,8,9,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,8,7,9,2,5,8,8,9,8,8,8,9,8,8,9,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,9,7,7,9,),
    (9,9,8,9,9,7,9,9,9,9,9,6,9,6,6,9,8,9,8,7,9,9,9,9,9,9,9,9,9,9,9,9,7,8,9,8,8,8,9,8,8,5,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,9,9,8,8,2,5,7,8,9,8,8,8,9,8,8,5,8,8,9,9,9,8,9,8,9,9,8,8,8,8,8,8,8,9,8,8,9,),
    (9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,9,8,9,9,8,7,9,2,5,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,9,8,9,9,9,7,7,9,),
    (10,9,9,10,9,10,9,9,9,9,8,10,8,10,9,9,9,9,10,9,10,9,9,10,9,10,10,8,9,10,9,9,9,9,9,9,9,9,9,9,9,10,9,9,9,9,9,9,9,9,10,9,9,8,8,9,8,10,10,9,8,8,3,6,9,9,9,9,9,9,9,9,9,10,9,9,9,9,9,9,9,9,10,9,9,8,8,9,8,10,9,10,8,8,9,),
    (8,7,8,8,7,8,7,8,7,7,8,7,8,8,6,8,7,7,8,8,8,8,7,8,7,8,8,7,8,7,7,8,7,7,8,7,7,7,8,7,7,8,7,7,7,7,8,7,8,7,8,7,7,7,7,7,7,7,8,7,7,8,1,4,7,7,8,7,7,7,8,7,7,8,7,7,7,7,8,7,8,7,8,7,7,7,7,7,7,7,8,8,7,7,7,),
    (9,9,8,9,9,6,9,8,9,9,7,7,6,7,6,9,9,9,8,6,9,9,9,9,9,7,7,6,6,9,9,8,7,9,8,9,9,9,9,9,9,6,9,9,9,9,9,9,8,9,9,9,9,9,9,9,9,8,9,9,9,7,2,5,7,9,8,9,9,9,9,9,9,6,9,9,9,9,9,9,8,9,9,9,9,9,9,9,9,8,8,9,9,9,9,),
    (10,10,9,9,9,9,10,9,10,9,9,9,9,9,8,9,10,9,9,9,9,9,10,9,9,9,9,9,9,10,9,9,8,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,9,10,10,10,10,10,10,9,10,10,10,9,3,6,8,10,9,10,10,10,9,10,10,9,10,10,10,10,9,10,9,10,9,10,10,10,10,10,10,9,9,10,10,10,9,),
    (9,9,6,8,8,6,9,7,9,8,7,6,7,6,5,7,9,8,7,6,8,7,9,8,7,7,7,7,7,9,8,7,6,9,7,9,9,9,7,9,9,6,9,9,9,9,7,9,7,9,8,9,9,9,9,9,9,8,9,9,9,7,2,5,6,9,7,9,9,9,7,9,9,6,9,9,9,9,7,9,7,9,8,9,9,9,9,9,9,8,8,9,9,9,8,),
    (12,12,10,11,11,10,12,10,12,11,10,9,10,9,8,11,12,11,10,10,11,11,12,11,11,10,10,10,10,12,11,10,9,12,10,12,12,12,11,12,12,9,12,12,12,12,11,12,10,12,11,12,12,12,12,12,12,11,12,12,12,10,5,8,9,12,10,12,12,12,11,12,12,9,12,12,12,12,11,12,10,12,11,12,12,12,12,12,12,11,11,12,12,12,11,),
    (9,9,8,8,8,8,9,8,9,8,7,9,7,9,8,7,9,8,8,8,8,8,9,8,7,9,9,6,7,9,8,7,9,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,7,9,9,9,9,9,9,9,9,9,9,9,9,7,2,5,9,9,8,9,9,9,8,9,9,8,9,9,9,9,8,9,7,9,9,9,9,9,9,9,9,9,8,9,9,9,8,),
    (9,9,6,8,8,6,9,7,9,8,7,7,7,7,6,7,9,8,7,6,8,7,9,8,7,7,7,7,7,9,8,7,7,9,7,9,9,9,7,9,9,6,9,9,9,9,7,9,7,9,8,9,9,9,9,9,9,8,9,9,9,6,2,5,7,9,7,9,9,9,7,9,9,6,9,9,9,9,7,9,7,9,8,9,9,9,9,9,9,8,8,9,9,9,8,),
    (8,8,8,8,8,8,8,8,8,8,6,8,6,8,7,7,8,8,8,8,8,8,8,8,7,8,8,6,7,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,8,8,8,6,1,4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,7,8,8,8,8,8,8,8,8,8,7,8,8,8,8,),
    (5,5,3,3,4,3,5,3,5,4,3,5,3,3,5,3,5,4,3,3,4,3,5,4,3,3,5,3,3,5,4,3,3,5,3,5,5,5,3,5,5,3,5,5,5,5,3,5,3,5,4,5,5,5,5,5,5,4,5,5,5,3,0,1,3,5,3,5,5,5,3,5,5,3,5,5,5,5,3,5,3,5,4,5,5,5,5,5,5,4,4,5,5,5,4,),
    (2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,),
    (4,4,4,4,4,5,4,5,4,4,4,4,4,4,4,5,4,4,4,5,4,5,4,5,4,4,4,4,5,4,4,5,4,4,5,4,4,4,5,4,4,4,4,4,4,4,5,4,5,4,5,4,4,4,4,4,4,4,5,4,4,4,0,1,4,4,5,4,4,4,5,4,4,4,4,4,4,4,5,4,5,4,5,4,4,4,4,4,4,4,5,5,4,4,4,),
    (5,5,2,3,4,1,5,2,5,4,0,3,2,3,1,3,5,4,3,0,4,3,5,4,3,3,3,0,0,5,4,2,2,5,2,5,5,5,3,5,5,2,5,5,5,5,3,5,3,5,4,5,5,5,5,5,5,4,5,5,5,3,0,2,2,5,2,5,5,5,3,5,5,2,5,5,5,5,3,5,3,5,4,5,5,5,5,5,5,4,4,5,5,5,4,),
    (4,4,3,4,4,1,4,3,4,4,3,1,3,1,1,4,3,4,3,2,4,4,4,4,4,4,4,3,4,4,4,4,2,3,4,3,3,3,4,3,3,0,3,3,3,4,4,3,4,3,4,4,3,3,3,3,3,3,4,4,3,2,0,0,2,3,4,3,3,3,4,3,3,0,3,3,3,4,4,3,4,3,4,4,3,3,3,3,3,3,3,4,3,3,4,),
)

# End of font

