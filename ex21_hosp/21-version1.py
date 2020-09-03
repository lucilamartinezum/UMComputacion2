import time, random, string
import multiprocessing as mp


def attentionActivity(slot, id):
    attention_time = random.randint(5, 7)
    print("\n---> Patient:", id, "arrives at the hospital.", slot.get_value(), "available slots.")
    slot.acquire()
    print("\n *** Patient", id, "is entering doctor's consulting room.", slot.get_value(), "available slots.")
    time.sleep(attention_time)
    slot.release()
    print("\n<---Patient", id, "is leaving the hospital.", slot.get_value(), "available slots.")


def randomPeople(rooms):
    while True:
        arrival_time = random.randint(1, 3)
        time.sleep(arrival_time)
        patient_id = random.choice(string.ascii_uppercase)
        patient_arriving = mp.Process(target=attentionActivity, args=(rooms, patient_id))
        patient_arriving.start()


if __name__ == '__main__':
    consulting_rooms = mp.Semaphore(5)
    hospital = mp.Process(target=randomPeople, args=(consulting_rooms,))
    hospital.start()
