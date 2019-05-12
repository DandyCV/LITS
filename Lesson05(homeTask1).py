def star_string(ss):
    ss = ss.strip()
    ss = ' '.join(ss.split())
    ss = ss.replace(' ', '*')
    print(ss)


star_string('  s f    gd  ')