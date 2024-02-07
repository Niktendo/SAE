def alle_rts_sind_zombies():
    tage = 0
    rts = 116033
    rts_start = rts
    inzidenz = 1.5
    zombies = 1
    i = 0
    
    while zombies < rts_start:
        print("Zombies:", zombies, "Reutlinger:", rts)
        rts = rts - zombies * 1.5
        zombies = zombies + zombies * 1.5
        i = i + 1
        
        
alle_rts_sind_zombies()