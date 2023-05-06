def filter_province(p):
    if p == "Bangkok":
        num_p = 1
    elif p == "Samut Prakan":
        num_p = 2
    elif p == "Nonthaburi":
        num_p = 3
    elif p == "Ayutthaya":
        num_p = 4
    elif p == "Ratchaburi":
        num_p = 5
    elif p == "Nakhon Nayok":
        num_p = 6
    elif p == "Nakhon Ratchasima":
        num_p = 7
    elif p == "Suphan Buri":
        num_p = 8
    elif p == "Kanchanaburi":
        num_p = 9
    elif p == "Chai Nat":
        num_p = 10
    elif p == "Samut Songkhram":
        num_p = 11
    elif p == "Chon Buri":
        num_p = 12
    elif p == "Nakhon Pathom":
        num_p = 13
    elif p == "Saraburi":
        num_p = 14
    elif p == "Khon Kaen":
        num_p = 15
    elif p == "Chiang Mai":
        num_p = 16
    elif p == "Lampang":
        num_p = 17
    elif p == "Phuket":
        num_p = 18
    elif p == "Prachuap Khiri Khan":
        num_p = 19
    elif p == "Saraburi":
        num_p = 20
    elif p == "Phetchaburi":
        num_p = 21
    elif p == "Prachinburi":
        num_p = 22
    elif p == "Phitsanulok":
        num_p = 24
    elif p == "Uttaradit":
        num_p = 25
    elif p == "Loey":
        num_p = 26
    else:
        num_p = 27

    return num_p

def filter_feature(f):
    if f == "Have different biking lane":
        num_f = 1
    elif f == "Have kids zone":
        num_f = 2
    elif f == "Have different facilities":
        num_f = 3
    elif f == "Have bicycle rental service":
        num_f = 4
    elif f == "Have a lot of trees":
        num_f = 5
    elif f == "Have a lake within or near a river":
        num_f = 6
    elif f == "Have a lot food":
        num_f = 7
    elif f == "Close on the weekend":
        num_f = 8
    elif f == "Open only on the weekend":
        num_f = 9
    elif f == "Close on holiday":
        num_f = 10
    elif f == "Have a short distance track":
        num_f = 11
    elif f == "Have a long distance track":
        num_f = 12
    elif f == "Located near the sea":
        num_f = 13
    elif f == "Is within a hotel area":
        num_f = 14
    elif f == "A biking route between provinces":
        num_f = 15
    elif f == "Have a track in a stadium":
        num_f = 16
    elif f == "Have a racing track":
        num_f = 17
    else:
        num_f = 18
    
    return num_f

def filter_activity(a):
    if a == "Both":
        num_a = 1
    elif a == "Casual Ride":
        num_a = 2
    else:
        num_a = 3
    
    return num_a