import time, random, string, sys, getopt
import multiprocessing as mp

def getOpts():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'c:a:b:n:m:', [])
        return opts
    except getopt.GetoptError as err:
        print('Error: ' + str(err))
        exit()


def attentionActivity(slot, id, d_time):
    (d_min, d_max) = d_time
    attention_time = random.randint(d_min, d_max)
    print("\n---> Patient:", id, "arrives at the hospital.", slot.get_value(), "available slots.")
    slot.acquire()
    print("\n *** Patient", id, "is entering doctor's consulting room.", slot.get_value(), "available slots.")
    time.sleep(attention_time)
    slot.release()
    print("\n<---Patient", id, "is leaving the hospital.", slot.get_value(), "available slots.")


def randomPeople(rooms, pt, dt):
    while True:
        arrival_time = random.randint(pt[0], pt[1])
        time.sleep(arrival_time)
        patient_id = random.choice(string.ascii_uppercase)
        patient_arriving = mp.Process(target=attentionActivity, args=(rooms, patient_id, dt))
        patient_arriving.start()

def main():
    if len(sys.argv[1:]) > 1:
        opts = getOpts()
        for (opt, arg) in opts:
            if opt == "-c":
                hospital_rooms = int(arg)
            if opt == "-a":
                min_people = int(arg)
            if opt == "-b":
                max_people = int(arg)
            if opt == "-n":
                min_attention = int(arg)
            if opt == "-m":
                max_attention = int(arg)

        p_time = [min_people, max_people]
        d_time = [min_attention, max_attention]

    else:
        print("Try again...")

    consulting_rooms = mp.Semaphore(5)
    hospital = mp.Process(target=randomPeople, args=(consulting_rooms, p_time, d_time))
    hospital.start()


if __name__ == '__main__':
    main()