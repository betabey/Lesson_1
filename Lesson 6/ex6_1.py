from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i < 3:
            print(f'TrafficLight turned on {TrafficLight.__color[i]} ')
            if i == 0:
                print('Wait 7 sec')
                sleep(7)

            elif i == 1:
                print('Wait 2 sec')
                sleep(2)

            elif i == 2:
                print('Wait 7 sec')
                sleep(7)

            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
