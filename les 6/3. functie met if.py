def lang_genoeg():
    print('hoe lang ben je ')
    lengte = input()
    if int(lengte) > 120:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Sorry, je bent te klein!')


lang_genoeg()
