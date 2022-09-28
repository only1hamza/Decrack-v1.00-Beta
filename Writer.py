def Writer()
    f= open("2022A03.P","w+")
    f.write("
    [MESURE]\n
    200=2022A03\n
    201=VF218\n
    202=15648\n
    203=5123\n
    [CRC]\n
    200=2004\n
    201=584\n
    202=2296\n
    203=236\n
    ")
    f.close()
    print("done")