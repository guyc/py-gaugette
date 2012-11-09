class Tahoma16:
    # 
    #  Font data for Tahoma 12pt
    # 

    # Font information for Tahoma 12pt
    start_char  = '!'
    end_char    = '~'
    char_height = 16
    space_width = 8      # pixels
    gap_width = 2
    
    # Character bitmaps for Tahoma 12pt
    bitmaps = (
        # @0 '!' (1 pixels wide)
        0x00, #  
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
        0x80, # O
        0x80, # O
        0x00, #  
        0x00, #  
        0x00, #  
    
        # @16 '"' (4 pixels wide)
        0x90, # O  O
        0x90, # O  O
        0x90, # O  O
        0x90, # O  O
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
        0x00, #     
        0x00, #     
    
        # @32 '#' (11 pixels wide)
        0x00, 0x00, #            
        0x08, 0x40, #     O    O 
        0x08, 0x40, #     O    O 
        0x10, 0x80, #    O    O  
        0x7F, 0xE0, #  OOOOOOOOOO
        0x10, 0x80, #    O    O  
        0x10, 0x80, #    O    O  
        0x21, 0x00, #   O    O   
        0x21, 0x00, #   O    O   
        0xFF, 0xC0, # OOOOOOOOOO 
        0x21, 0x00, #   O    O   
        0x42, 0x00, #  O    O    
        0x42, 0x00, #  O    O    
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x00, 0x00, #            
    
        # @64 '$' (7 pixels wide)
        0x00, #        
        0x10, #    O   
        0x10, #    O   
        0x7C, #  OOOOO 
        0x92, # O  O  O
        0x90, # O  O   
        0x90, # O  O   
        0x70, #  OOO   
        0x1C, #    OOO 
        0x12, #    O  O
        0x12, #    O  O
        0x92, # O  O  O
        0x7C, #  OOOOO 
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
    
        # @80 '%' (14 pixels wide)
        0x00, 0x00, #               
        0x78, 0x20, #  OOOO     O   
        0x84, 0x40, # O    O   O    
        0x84, 0x40, # O    O   O    
        0x84, 0x80, # O    O  O     
        0x85, 0x00, # O    O O      
        0x85, 0x78, # O    O O OOOO 
        0x7A, 0x84, #  OOOO O O    O
        0x02, 0x84, #       O O    O
        0x04, 0x84, #      O  O    O
        0x08, 0x84, #     O   O    O
        0x08, 0x84, #     O   O    O
        0x10, 0x78, #    O     OOOO 
        0x00, 0x00, #               
        0x00, 0x00, #               
        0x00, 0x00, #               
    
        # @112 '&' (10 pixels wide)
        0x00, 0x00, #           
        0x3C, 0x00, #   OOOO    
        0x42, 0x00, #  O    O   
        0x42, 0x00, #  O    O   
        0x42, 0x00, #  O    O   
        0x24, 0x00, #   O  O    
        0x38, 0x80, #   OOO   O 
        0x48, 0x80, #  O  O   O 
        0x84, 0x80, # O    O  O 
        0x83, 0x00, # O     OO  
        0x81, 0x00, # O      O  
        0x42, 0x80, #  O    O O 
        0x3C, 0x40, #   OOOO   O
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
    
        # @144 ''' (1 pixels wide)
        0x80, # O
        0x80, # O
        0x80, # O
        0x80, # O
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
        0x00, #  
        0x00, #  
    
        # @160 '(' (4 pixels wide)
        0x10, #    O
        0x20, #   O 
        0x40, #  O  
        0x40, #  O  
        0x80, # O   
        0x80, # O   
        0x80, # O   
        0x80, # O   
        0x80, # O   
        0x80, # O   
        0x80, # O   
        0x80, # O   
        0x40, #  O  
        0x40, #  O  
        0x20, #   O 
        0x10, #    O
    
        # @176 ')' (4 pixels wide)
        0x80, # O   
        0x40, #  O  
        0x20, #   O 
        0x20, #   O 
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x20, #   O 
        0x20, #   O 
        0x40, #  O  
        0x80, # O   
    
        # @192 '*' (7 pixels wide)
        0x10, #    O   
        0x92, # O  O  O
        0x54, #  O O O 
        0x38, #   OOO  
        0x54, #  O O O 
        0x92, # O  O  O
        0x10, #    O   
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @208 '+' (9 pixels wide)
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0xFF, 0x80, # OOOOOOOOO
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
    
        # @240 ',' (2 pixels wide)
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
        0x40, #  O
        0x40, #  O
        0x40, #  O
        0x80, # O 
        0x80, # O 
    
        # @256 '-' (5 pixels wide)
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
        0xF8, # OOOOO
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
    
        # @272 '.' (1 pixels wide)
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
        0x80, # O
        0x80, # O
        0x00, #  
        0x00, #  
        0x00, #  
    
        # @288 '/' (6 pixels wide)
        0x04, #      O
        0x04, #      O
        0x08, #     O 
        0x08, #     O 
        0x08, #     O 
        0x10, #    O  
        0x10, #    O  
        0x10, #    O  
        0x20, #   O   
        0x20, #   O   
        0x20, #   O   
        0x40, #  O    
        0x40, #  O    
        0x40, #  O    
        0x80, # O     
        0x80, # O     
    
        # @304 '0' (8 pixels wide)
        0x00, #         
        0x3C, #   OOOO  
        0x42, #  O    O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x42, #  O    O 
        0x3C, #   OOOO  
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @320 '1' (5 pixels wide)
        0x00, #      
        0x20, #   O  
        0x20, #   O  
        0xE0, # OOO  
        0x20, #   O  
        0x20, #   O  
        0x20, #   O  
        0x20, #   O  
        0x20, #   O  
        0x20, #   O  
        0x20, #   O  
        0x20, #   O  
        0xF8, # OOOOO
        0x00, #      
        0x00, #      
        0x00, #      
    
        # @336 '2' (7 pixels wide)
        0x00, #        
        0x78, #  OOOO  
        0x84, # O    O 
        0x02, #       O
        0x02, #       O
        0x02, #       O
        0x04, #      O 
        0x08, #     O  
        0x10, #    O   
        0x20, #   O    
        0x40, #  O     
        0x80, # O      
        0xFE, # OOOOOOO
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @352 '3' (7 pixels wide)
        0x00, #        
        0x78, #  OOOO  
        0x84, # O    O 
        0x02, #       O
        0x02, #       O
        0x04, #      O 
        0x38, #   OOO  
        0x04, #      O 
        0x02, #       O
        0x02, #       O
        0x02, #       O
        0x84, # O    O 
        0x78, #  OOOO  
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @368 '4' (8 pixels wide)
        0x00, #         
        0x02, #       O 
        0x06, #      OO 
        0x0A, #     O O 
        0x12, #    O  O 
        0x22, #   O   O 
        0x42, #  O    O 
        0x82, # O     O 
        0xFF, # OOOOOOOO
        0x02, #       O 
        0x02, #       O 
        0x02, #       O 
        0x02, #       O 
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @384 '5' (7 pixels wide)
        0x00, #        
        0xFE, # OOOOOOO
        0x80, # O      
        0x80, # O      
        0x80, # O      
        0xF8, # OOOOO  
        0x04, #      O 
        0x02, #       O
        0x02, #       O
        0x02, #       O
        0x02, #       O
        0x84, # O    O 
        0x78, #  OOOO  
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @400 '6' (8 pixels wide)
        0x00, #         
        0x1E, #    OOOO 
        0x20, #   O     
        0x40, #  O      
        0x80, # O       
        0xBC, # O OOOO  
        0xC2, # OO    O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x42, #  O    O 
        0x3C, #   OOOO  
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @416 '7' (7 pixels wide)
        0x00, #        
        0xFE, # OOOOOOO
        0x02, #       O
        0x04, #      O 
        0x04, #      O 
        0x08, #     O  
        0x08, #     O  
        0x10, #    O   
        0x10, #    O   
        0x20, #   O    
        0x20, #   O    
        0x40, #  O     
        0x40, #  O     
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @432 '8' (8 pixels wide)
        0x00, #         
        0x3C, #   OOOO  
        0x42, #  O    O 
        0x81, # O      O
        0x81, # O      O
        0x42, #  O    O 
        0x3C, #   OOOO  
        0x42, #  O    O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x42, #  O    O 
        0x3C, #   OOOO  
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @448 '9' (8 pixels wide)
        0x00, #         
        0x3C, #   OOOO  
        0x42, #  O    O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x43, #  O    OO
        0x3D, #   OOOO O
        0x01, #        O
        0x02, #       O 
        0x04, #      O  
        0x78, #  OOOO   
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @464 ':' (1 pixels wide)
        0x00, #  
        0x00, #  
        0x00, #  
        0x00, #  
        0x80, # O
        0x80, # O
        0x00, #  
        0x00, #  
        0x00, #  
        0x00, #  
        0x00, #  
        0x80, # O
        0x80, # O
        0x00, #  
        0x00, #  
        0x00, #  
    
        # @480 ';' (2 pixels wide)
        0x00, #   
        0x00, #   
        0x00, #   
        0x00, #   
        0x40, #  O
        0x40, #  O
        0x00, #   
        0x00, #   
        0x00, #   
        0x00, #   
        0x00, #   
        0x40, #  O
        0x40, #  O
        0x40, #  O
        0x80, # O 
        0x80, # O 
    
        # @496 '<' (8 pixels wide)
        0x00, #         
        0x00, #         
        0x00, #         
        0x01, #        O
        0x06, #      OO 
        0x18, #    OO   
        0x60, #  OO     
        0x80, # O       
        0x60, #  OO     
        0x18, #    OO   
        0x06, #      OO 
        0x01, #        O
        0x00, #         
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @512 '=' (9 pixels wide)
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
        0xFF, 0x80, # OOOOOOOOO
        0x00, 0x00, #          
        0x00, 0x00, #          
        0xFF, 0x80, # OOOOOOOOO
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
    
        # @544 '>' (8 pixels wide)
        0x00, #         
        0x00, #         
        0x00, #         
        0x80, # O       
        0x60, #  OO     
        0x18, #    OO   
        0x06, #      OO 
        0x01, #        O
        0x06, #      OO 
        0x18, #    OO   
        0x60, #  OO     
        0x80, # O       
        0x00, #         
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @560 '?' (6 pixels wide)
        0x00, #       
        0x70, #  OOO  
        0x88, # O   O 
        0x04, #      O
        0x04, #      O
        0x04, #      O
        0x08, #     O 
        0x10, #    O  
        0x20, #   O   
        0x20, #   O   
        0x00, #       
        0x20, #   O   
        0x20, #   O   
        0x00, #       
        0x00, #       
        0x00, #       
    
        # @576 '@' (13 pixels wide)
        0x00, 0x00, #              
        0x0F, 0x80, #     OOOOO    
        0x30, 0x60, #   OO     OO  
        0x40, 0x10, #  O         O 
        0x47, 0xD0, #  O   OOOOO O 
        0x88, 0x48, # O   O    O  O
        0x90, 0x48, # O  O     O  O
        0x90, 0x48, # O  O     O  O
        0x90, 0x48, # O  O     O  O
        0x90, 0x48, # O  O     O  O
        0x88, 0xC8, # O   O   OO  O
        0x47, 0x70, #  O   OOO OOO 
        0x40, 0x00, #  O           
        0x30, 0x00, #   OO         
        0x0F, 0x80, #     OOOOO    
        0x00, 0x00, #              
    
        # @608 'A' (10 pixels wide)
        0x00, 0x00, #           
        0x0C, 0x00, #     OO    
        0x12, 0x00, #    O  O   
        0x12, 0x00, #    O  O   
        0x12, 0x00, #    O  O   
        0x21, 0x00, #   O    O  
        0x21, 0x00, #   O    O  
        0x21, 0x00, #   O    O  
        0x7F, 0x80, #  OOOOOOOO 
        0x40, 0x80, #  O      O 
        0x40, 0x80, #  O      O 
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
    
        # @640 'B' (8 pixels wide)
        0x00, #         
        0xFC, # OOOOOO  
        0x82, # O     O 
        0x82, # O     O 
        0x82, # O     O 
        0x84, # O    O  
        0xFC, # OOOOOO  
        0x82, # O     O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x82, # O     O 
        0xFC, # OOOOOO  
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @656 'C' (9 pixels wide)
        0x00, 0x00, #          
        0x1F, 0x00, #    OOOOO 
        0x60, 0x80, #  OO     O
        0x40, 0x00, #  O       
        0x80, 0x00, # O        
        0x80, 0x00, # O        
        0x80, 0x00, # O        
        0x80, 0x00, # O        
        0x80, 0x00, # O        
        0x80, 0x00, # O        
        0x40, 0x00, #  O       
        0x60, 0x80, #  OO     O
        0x1F, 0x00, #    OOOOO 
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
    
        # @688 'D' (10 pixels wide)
        0x00, 0x00, #           
        0xFC, 0x00, # OOOOOO    
        0x83, 0x00, # O     OO  
        0x80, 0x80, # O       O 
        0x80, 0x80, # O       O 
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x80, # O       O 
        0x80, 0x80, # O       O 
        0x83, 0x00, # O     OO  
        0xFC, 0x00, # OOOOOO    
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
    
        # @720 'E' (8 pixels wide)
        0x00, #         
        0xFF, # OOOOOOOO
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0xFF, # OOOOOOOO
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0xFF, # OOOOOOOO
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @736 'F' (7 pixels wide)
        0x00, #        
        0xFE, # OOOOOOO
        0x80, # O      
        0x80, # O      
        0x80, # O      
        0x80, # O      
        0xFE, # OOOOOOO
        0x80, # O      
        0x80, # O      
        0x80, # O      
        0x80, # O      
        0x80, # O      
        0x80, # O      
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @752 'G' (10 pixels wide)
        0x00, 0x00, #           
        0x1F, 0x80, #    OOOOOO 
        0x60, 0x40, #  OO      O
        0x40, 0x00, #  O        
        0x80, 0x00, # O         
        0x80, 0x00, # O         
        0x80, 0x00, # O         
        0x87, 0xC0, # O    OOOOO
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x40, 0x40, #  O       O
        0x60, 0x40, #  OO      O
        0x1F, 0x80, #    OOOOOO 
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
    
        # @784 'H' (10 pixels wide)
        0x00, 0x00, #           
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0xFF, 0xC0, # OOOOOOOOOO
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
    
        # @816 'I' (3 pixels wide)
        0x00, #    
        0xE0, # OOO
        0x40, #  O 
        0x40, #  O 
        0x40, #  O 
        0x40, #  O 
        0x40, #  O 
        0x40, #  O 
        0x40, #  O 
        0x40, #  O 
        0x40, #  O 
        0x40, #  O 
        0xE0, # OOO
        0x00, #    
        0x00, #    
        0x00, #    
    
        # @832 'J' (6 pixels wide)
        0x00, #       
        0x3C, #   OOOO
        0x04, #      O
        0x04, #      O
        0x04, #      O
        0x04, #      O
        0x04, #      O
        0x04, #      O
        0x04, #      O
        0x04, #      O
        0x04, #      O
        0x04, #      O
        0xF8, # OOOOO 
        0x00, #       
        0x00, #       
        0x00, #       
    
        # @848 'K' (8 pixels wide)
        0x00, #         
        0x81, # O      O
        0x82, # O     O 
        0x84, # O    O  
        0x88, # O   O   
        0x90, # O  O    
        0xA0, # O O     
        0xE0, # OOO     
        0x90, # O  O    
        0x88, # O   O   
        0x84, # O    O  
        0x82, # O     O 
        0x81, # O      O
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @864 'L' (7 pixels wide)
        0x00, #        
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
        0xFE, # OOOOOOO
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @880 'M' (11 pixels wide)
        0x00, 0x00, #            
        0xC0, 0x60, # OO       OO
        0xC0, 0x60, # OO       OO
        0xA0, 0xA0, # O O     O O
        0xA0, 0xA0, # O O     O O
        0x91, 0x20, # O  O   O  O
        0x91, 0x20, # O  O   O  O
        0x8A, 0x20, # O   O O   O
        0x8A, 0x20, # O   O O   O
        0x84, 0x20, # O    O    O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x00, 0x00, #            
    
        # @912 'N' (10 pixels wide)
        0x00, 0x00, #           
        0x80, 0x40, # O        O
        0xC0, 0x40, # OO       O
        0xA0, 0x40, # O O      O
        0x90, 0x40, # O  O     O
        0x90, 0x40, # O  O     O
        0x88, 0x40, # O   O    O
        0x84, 0x40, # O    O   O
        0x82, 0x40, # O     O  O
        0x82, 0x40, # O     O  O
        0x81, 0x40, # O      O O
        0x80, 0xC0, # O       OO
        0x80, 0x40, # O        O
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
    
        # @944 'O' (11 pixels wide)
        0x00, 0x00, #            
        0x1F, 0x00, #    OOOOO   
        0x60, 0xC0, #  OO     OO 
        0x40, 0x40, #  O       O 
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x40, 0x40, #  O       O 
        0x60, 0xC0, #  OO     OO 
        0x1F, 0x00, #    OOOOO   
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x00, 0x00, #            
    
        # @976 'P' (8 pixels wide)
        0x00, #         
        0xFC, # OOOOOO  
        0x82, # O     O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x82, # O     O 
        0xFC, # OOOOOO  
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @992 'Q' (11 pixels wide)
        0x00, 0x00, #            
        0x1F, 0x00, #    OOOOO   
        0x60, 0xC0, #  OO     OO 
        0x40, 0x40, #  O       O 
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x80, 0x20, # O         O
        0x40, 0x40, #  O       O 
        0x60, 0xC0, #  OO     OO 
        0x1F, 0x00, #    OOOOO   
        0x02, 0x00, #       O    
        0x02, 0x00, #       O    
        0x01, 0xE0, #        OOOO
    
        # @1024 'R' (9 pixels wide)
        0x00, 0x00, #          
        0xFC, 0x00, # OOOOOO   
        0x82, 0x00, # O     O  
        0x82, 0x00, # O     O  
        0x82, 0x00, # O     O  
        0x82, 0x00, # O     O  
        0x84, 0x00, # O    O   
        0xF8, 0x00, # OOOOO    
        0x88, 0x00, # O   O    
        0x84, 0x00, # O    O   
        0x82, 0x00, # O     O  
        0x81, 0x00, # O      O 
        0x80, 0x80, # O       O
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
    
        # @1056 'S' (8 pixels wide)
        0x00, #         
        0x3E, #   OOOOO 
        0x41, #  O     O
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0x70, #  OOO    
        0x0E, #     OOO 
        0x01, #        O
        0x01, #        O
        0x01, #        O
        0x82, # O     O 
        0x7C, #  OOOOO  
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @1072 'T' (9 pixels wide)
        0x00, 0x00, #          
        0xFF, 0x80, # OOOOOOOOO
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
    
        # @1104 'U' (10 pixels wide)
        0x00, 0x00, #           
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x80, 0x40, # O        O
        0x40, 0x80, #  O      O 
        0x3F, 0x00, #   OOOOOO  
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
    
        # @1136 'V' (9 pixels wide)
        0x00, 0x00, #          
        0x80, 0x80, # O       O
        0x80, 0x80, # O       O
        0x41, 0x00, #  O     O 
        0x41, 0x00, #  O     O 
        0x41, 0x00, #  O     O 
        0x22, 0x00, #   O   O  
        0x22, 0x00, #   O   O  
        0x22, 0x00, #   O   O  
        0x14, 0x00, #    O O   
        0x14, 0x00, #    O O   
        0x14, 0x00, #    O O   
        0x08, 0x00, #     O    
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
    
        # @1168 'W' (13 pixels wide)
        0x00, 0x00, #              
        0x82, 0x08, # O     O     O
        0x85, 0x08, # O    O O    O
        0x45, 0x10, #  O   O O   O 
        0x45, 0x10, #  O   O O   O 
        0x45, 0x10, #  O   O O   O 
        0x45, 0x10, #  O   O O   O 
        0x48, 0x90, #  O  O   O  O 
        0x28, 0xA0, #   O O   O O  
        0x28, 0xA0, #   O O   O O  
        0x28, 0xA0, #   O O   O O  
        0x30, 0x60, #   OO     OO  
        0x10, 0x40, #    O     O   
        0x00, 0x00, #              
        0x00, 0x00, #              
        0x00, 0x00, #              
    
        # @1200 'X' (8 pixels wide)
        0x00, #         
        0x81, # O      O
        0x42, #  O    O 
        0x42, #  O    O 
        0x24, #   O  O  
        0x18, #    OO   
        0x18, #    OO   
        0x18, #    OO   
        0x18, #    OO   
        0x24, #   O  O  
        0x42, #  O    O 
        0x42, #  O    O 
        0x81, # O      O
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @1216 'Y' (9 pixels wide)
        0x00, 0x00, #          
        0x80, 0x80, # O       O
        0x41, 0x00, #  O     O 
        0x41, 0x00, #  O     O 
        0x22, 0x00, #   O   O  
        0x14, 0x00, #    O O   
        0x14, 0x00, #    O O   
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x08, 0x00, #     O    
        0x00, 0x00, #          
        0x00, 0x00, #          
        0x00, 0x00, #          
    
        # @1248 'Z' (8 pixels wide)
        0x00, #         
        0xFF, # OOOOOOOO
        0x01, #        O
        0x02, #       O 
        0x04, #      O  
        0x04, #      O  
        0x08, #     O   
        0x10, #    O    
        0x20, #   O     
        0x20, #   O     
        0x40, #  O      
        0x80, # O       
        0xFF, # OOOOOOOO
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @1264 '[' (4 pixels wide)
        0xF0, # OOOO
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
        0x80, # O   
        0x80, # O   
        0xF0, # OOOO
    
        # @1280 '\' (6 pixels wide)
        0x80, # O     
        0x80, # O     
        0x40, #  O    
        0x40, #  O    
        0x40, #  O    
        0x20, #   O   
        0x20, #   O   
        0x20, #   O   
        0x10, #    O  
        0x10, #    O  
        0x10, #    O  
        0x08, #     O 
        0x08, #     O 
        0x08, #     O 
        0x04, #      O
        0x04, #      O
    
        # @1296 ']' (4 pixels wide)
        0xF0, # OOOO
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0xF0, # OOOO
    
        # @1312 '^' (10 pixels wide)
        0x00, 0x00, #           
        0x0C, 0x00, #     OO    
        0x12, 0x00, #    O  O   
        0x12, 0x00, #    O  O   
        0x21, 0x00, #   O    O  
        0x40, 0x80, #  O      O 
        0x80, 0x40, # O        O
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
    
        # @1344 '_' (9 pixels wide)
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
        0xFF, 0x80, # OOOOOOOOO
        0x00, 0x00, #          
    
        # @1376 '`' (2 pixels wide)
        0x80, # O 
        0x80, # O 
        0x40, #  O
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
    
        # @1392 'a' (7 pixels wide)
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x3C, #   OOOO 
        0x42, #  O    O
        0x02, #       O
        0x3E, #   OOOOO
        0x42, #  O    O
        0x82, # O     O
        0x82, # O     O
        0x86, # O    OO
        0x7A, #  OOOO O
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @1408 'b' (8 pixels wide)
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0xBC, # O OOOO  
        0xC2, # OO    O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x82, # O     O 
        0xFC, # OOOOOO  
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @1424 'c' (6 pixels wide)
        0x00, #       
        0x00, #       
        0x00, #       
        0x00, #       
        0x38, #   OOO 
        0x44, #  O   O
        0x80, # O     
        0x80, # O     
        0x80, # O     
        0x80, # O     
        0x80, # O     
        0x44, #  O   O
        0x38, #   OOO 
        0x00, #       
        0x00, #       
        0x00, #       
    
        # @1440 'd' (8 pixels wide)
        0x01, #        O
        0x01, #        O
        0x01, #        O
        0x01, #        O
        0x3F, #   OOOOOO
        0x41, #  O     O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x43, #  O    OO
        0x3D, #   OOOO O
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @1456 'e' (7 pixels wide)
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x38, #   OOO  
        0x44, #  O   O 
        0x82, # O     O
        0x82, # O     O
        0xFE, # OOOOOOO
        0x80, # O      
        0x80, # O      
        0x42, #  O    O
        0x3C, #   OOOO 
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @1472 'f' (5 pixels wide)
        0x38, #   OOO
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0xF0, # OOOO 
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x00, #      
        0x00, #      
        0x00, #      
    
        # @1488 'g' (8 pixels wide)
        0x00, #         
        0x00, #         
        0x00, #         
        0x00, #         
        0x3F, #   OOOOOO
        0x41, #  O     O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x43, #  O    OO
        0x3D, #   OOOO O
        0x01, #        O
        0x42, #  O    O 
        0x3C, #   OOOO  
    
        # @1504 'h' (8 pixels wide)
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0x80, # O       
        0xBC, # O OOOO  
        0xC2, # OO    O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @1520 'i' (1 pixels wide)
        0x00, #  
        0x80, # O
        0x80, # O
        0x00, #  
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
    
        # @1536 'j' (4 pixels wide)
        0x00, #     
        0x10, #    O
        0x10, #    O
        0x00, #     
        0x70, #  OOO
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0x10, #    O
        0xE0, # OOO 
    
        # @1552 'k' (7 pixels wide)
        0x80, # O      
        0x80, # O      
        0x80, # O      
        0x80, # O      
        0x84, # O    O 
        0x88, # O   O  
        0x90, # O  O   
        0xA0, # O O    
        0xE0, # OOO    
        0x90, # O  O   
        0x88, # O   O  
        0x84, # O    O 
        0x82, # O     O
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @1568 'l' (1 pixels wide)
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
        0x80, # O
        0x00, #  
        0x00, #  
        0x00, #  
    
        # @1584 'm' (11 pixels wide)
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x00, 0x00, #            
        0xB9, 0xC0, # O OOO  OOO 
        0xC6, 0x20, # OO   OO   O
        0x84, 0x20, # O    O    O
        0x84, 0x20, # O    O    O
        0x84, 0x20, # O    O    O
        0x84, 0x20, # O    O    O
        0x84, 0x20, # O    O    O
        0x84, 0x20, # O    O    O
        0x84, 0x20, # O    O    O
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x00, 0x00, #            
    
        # @1616 'n' (8 pixels wide)
        0x00, #         
        0x00, #         
        0x00, #         
        0x00, #         
        0xBC, # O OOOO  
        0xC2, # OO    O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @1632 'o' (8 pixels wide)
        0x00, #         
        0x00, #         
        0x00, #         
        0x00, #         
        0x3C, #   OOOO  
        0x42, #  O    O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x42, #  O    O 
        0x3C, #   OOOO  
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @1648 'p' (8 pixels wide)
        0x00, #         
        0x00, #         
        0x00, #         
        0x00, #         
        0xBC, # O OOOO  
        0xC2, # OO    O 
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x82, # O     O 
        0xFC, # OOOOOO  
        0x80, # O       
        0x80, # O       
        0x80, # O       
    
        # @1664 'q' (8 pixels wide)
        0x00, #         
        0x00, #         
        0x00, #         
        0x00, #         
        0x3F, #   OOOOOO
        0x41, #  O     O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x43, #  O    OO
        0x3D, #   OOOO O
        0x01, #        O
        0x01, #        O
        0x01, #        O
    
        # @1680 'r' (5 pixels wide)
        0x00, #      
        0x00, #      
        0x00, #      
        0x00, #      
        0xB8, # O OOO
        0xC0, # OO   
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
    
        # @1696 's' (6 pixels wide)
        0x00, #       
        0x00, #       
        0x00, #       
        0x00, #       
        0x78, #  OOOO 
        0x84, # O    O
        0x80, # O     
        0x80, # O     
        0x78, #  OOOO 
        0x04, #      O
        0x04, #      O
        0x84, # O    O
        0x78, #  OOOO 
        0x00, #       
        0x00, #       
        0x00, #       
    
        # @1712 't' (5 pixels wide)
        0x00, #      
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0xF8, # OOOOO
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x40, #  O   
        0x38, #   OOO
        0x00, #      
        0x00, #      
        0x00, #      
    
        # @1728 'u' (8 pixels wide)
        0x00, #         
        0x00, #         
        0x00, #         
        0x00, #         
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x81, # O      O
        0x43, #  O    OO
        0x3D, #   OOOO O
        0x00, #         
        0x00, #         
        0x00, #         
    
        # @1744 'v' (7 pixels wide)
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x82, # O     O
        0x82, # O     O
        0x44, #  O   O 
        0x44, #  O   O 
        0x44, #  O   O 
        0x28, #   O O  
        0x28, #   O O  
        0x10, #    O   
        0x10, #    O   
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @1760 'w' (11 pixels wide)
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x84, 0x20, # O    O    O
        0x84, 0x20, # O    O    O
        0x4A, 0x40, #  O  O O  O 
        0x4A, 0x40, #  O  O O  O 
        0x4A, 0x40, #  O  O O  O 
        0x51, 0x40, #  O O   O O 
        0x31, 0x80, #   OO   OO  
        0x20, 0x80, #   O     O  
        0x20, 0x80, #   O     O  
        0x00, 0x00, #            
        0x00, 0x00, #            
        0x00, 0x00, #            
    
        # @1792 'x' (7 pixels wide)
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x82, # O     O
        0x44, #  O   O 
        0x28, #   O O  
        0x28, #   O O  
        0x10, #    O   
        0x28, #   O O  
        0x28, #   O O  
        0x44, #  O   O 
        0x82, # O     O
        0x00, #        
        0x00, #        
        0x00, #        
    
        # @1808 'y' (7 pixels wide)
        0x00, #        
        0x00, #        
        0x00, #        
        0x00, #        
        0x82, # O     O
        0x82, # O     O
        0x44, #  O   O 
        0x44, #  O   O 
        0x44, #  O   O 
        0x28, #   O O  
        0x28, #   O O  
        0x10, #    O   
        0x10, #    O   
        0x20, #   O    
        0x20, #   O    
        0x20, #   O    
    
        # @1824 'z' (6 pixels wide)
        0x00, #       
        0x00, #       
        0x00, #       
        0x00, #       
        0xFC, # OOOOOO
        0x04, #      O
        0x08, #     O 
        0x10, #    O  
        0x20, #   O   
        0x20, #   O   
        0x40, #  O    
        0x80, # O     
        0xFC, # OOOOOO
        0x00, #       
        0x00, #       
        0x00, #       
    
        # @1840 '(' (7 pixels wide)
        0x0E, #     OOO
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x20, #   O    
        0xC0, # OO     
        0x20, #   O    
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x0E, #     OOO
    
        # @1856 '|' (1 pixels wide)
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
        0x80, # O
        0x80, # O
        0x80, # O
        0x80, # O
    
        # @1872 ')' (7 pixels wide)
        0xE0, # OOO    
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x08, #     O  
        0x06, #      OO
        0x08, #     O  
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0x10, #    O   
        0xE0, # OOO    
    
        # @1888 '~' (10 pixels wide)
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x30, 0x40, #   OO     O
        0x48, 0x40, #  O  O    O
        0x84, 0x80, # O    O  O 
        0x83, 0x00, # O     OO  
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
        0x00, 0x00, #           
    )
    
    # Character descriptors for Tahoma 12pt
    # ( [Char width in bits], [Offset into bitmaps in bytes] )
    descriptors = (
        (1, 0),         # ! 
        (4, 16),        # " 
        (11, 32),       # # 
        (7, 64),        # $ 
        (14, 80),       # % 
        (10, 112),      # & 
        (1, 144),       # ' 
        (4, 160),       # ( 
        (4, 176),       # ) 
        (7, 192),       # * 
        (9, 208),       # + 
        (2, 240),       # , 
        (5, 256),       # - 
        (1, 272),       # . 
        (6, 288),       # / 
        (8, 304),       # 0 
        (5, 320),       # 1 
        (7, 336),       # 2 
        (7, 352),       # 3 
        (8, 368),       # 4 
        (7, 384),       # 5 
        (8, 400),       # 6 
        (7, 416),       # 7 
        (8, 432),       # 8 
        (8, 448),       # 9 
        (1, 464),       # : 
        (2, 480),       # ; 
        (8, 496),       # < 
        (9, 512),       # = 
        (8, 544),       # > 
        (6, 560),       # ? 
        (13, 576),      # @ 
        (10, 608),      # A 
        (8, 640),       # B 
        (9, 656),       # C 
        (10, 688),      # D 
        (8, 720),       # E 
        (7, 736),       # F 
        (10, 752),      # G 
        (10, 784),      # H 
        (3, 816),       # I 
        (6, 832),       # J 
        (8, 848),       # K 
        (7, 864),       # L 
        (11, 880),      # M 
        (10, 912),      # N 
        (11, 944),      # O 
        (8, 976),       # P 
        (11, 992),      # Q 
        (9, 1024),      # R 
        (8, 1056),      # S 
        (9, 1072),      # T 
        (10, 1104),     # U 
        (9, 1136),      # V 
        (13, 1168),     # W 
        (8, 1200),      # X 
        (9, 1216),      # Y 
        (8, 1248),      # Z 
        (4, 1264),      # [ 
        (6, 1280),      # \ 
        (4, 1296),      # ] 
        (10, 1312),     # ^ 
        (9, 1344),      # _ 
        (2, 1376),      # ` 
        (7, 1392),      # a 
        (8, 1408),      # b 
        (6, 1424),      # c 
        (8, 1440),      # d 
        (7, 1456),      # e 
        (5, 1472),      # f 
        (8, 1488),      # g 
        (8, 1504),      # h 
        (1, 1520),      # i 
        (4, 1536),      # j 
        (7, 1552),      # k 
        (1, 1568),      # l 
        (11, 1584),     # m 
        (8, 1616),      # n 
        (8, 1632),      # o 
        (8, 1648),      # p 
        (8, 1664),      # q 
        (5, 1680),      # r 
        (6, 1696),      # s 
        (5, 1712),      # t 
        (8, 1728),      # u 
        (7, 1744),      # v 
        (11, 1760),     # w 
        (7, 1792),      # x 
        (7, 1808),      # y 
        (6, 1824),      # z 
        (7, 1840),      # ( 
        (1, 1856),      # | 
        (7, 1872),      # ) 
        (10, 1888),     # ~ 
    )
    
