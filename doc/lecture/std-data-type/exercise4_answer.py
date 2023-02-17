import random
import struct

def main(seed=42, length=10):

    random.seed(seed)

    sensor1 = [ random.gauss(mu=0, sigma=1) for _ in range(length)]
    sensor2 = [ random.gauss(mu=0, sigma=1) for _ in range(length)]
    sensor3 = [ random.gauss(mu=0, sigma=1) for _ in range(length)]
    alert   = [ random.randint(0,1)         for _ in range(length)]


    for i in range(length):
        print(sensor1[i], sensor2[i], sensor3[i], alert[i])
        data = struct.pack('<f', sensor1[i])\
                + struct.pack('<f', sensor2[i])\
                + struct.pack('<f', sensor3[i])\
                + struct.pack('<h', alert  [i])
        # print(len(data))

if __name__ == "__main__":
    main()