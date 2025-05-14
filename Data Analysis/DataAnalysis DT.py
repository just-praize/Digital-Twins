import random
import time


class DataAnalyticsEngine:
    def __init__(self):
        self.data_queue = []

    def receive_data(self, data):
        print(f"Received data is {data}")
        self.data_queue.append(data)

    def process_data(self):
        if self.data_queue:
            processed_data = [x * 2 for x in self.data_queue]
            print(f"Processed data is {processed_data}")
            self.data_queue.clear()
        else:
            print("No data to process")


class DataANalyticsDigitalTwin:
    def __init__(self, analytics_engine):
        self.analytics_engine = analytics_engine

    def simulate_data_processing(self, no_of_iterations):
        for i in range(no_of_iterations):
            random_data = [random.randint(1, 5) for j in range(random.randint(1, 5))]
            self.analytics_engine.receive_data(random_data)

            self.analytics_engine.process_data()

            time.sleep(1)


DAE = DataAnalyticsEngine()

DADT = DataANalyticsDigitalTwin(DAE)

DADT.simulate_data_processing(5)
