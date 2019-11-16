weight = int(input('Enter your weight: '))

moonweight = weight*165/1000

print('Your weight in the moon will be ' + str(moonweight) + ' kg')

print('Your weight after 15 years in the moon will be ' + str(moonweight+15) + ' kg')

print('Your weight if you will return to Earth will be ' + str(int((moonweight+15)*1000/165)) + ' kg')