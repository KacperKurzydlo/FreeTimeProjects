import numpy as np
import matplotlib.pyplot as plt


class Life:
    def __init__(self, col, row, num_ones):
        self.planes = np.zeros([col, row], dtype=int)

        total_positions = col * row
        random_indices = np.random.choice(total_positions, size=num_ones, replace=False)

        self.planes.flat[random_indices] = 1
        self.add_life_when = []
        self.destroy_life_when = []

    def get_state_of_life(self):
        return self.planes

    def check_neighbours(self, type):
        if type == 4:
            neighbours = (
                    np.roll(self.planes, 1, axis=1) +  # left
                    np.roll(self.planes, -1, axis=1) +  # right
                    np.roll(self.planes, 1, axis=0) +  # top
                    np.roll(self.planes, -1, axis=0)  # bottom
            )
        if type == 8:
            neighbours = (
                    np.roll(np.roll(self.planes, 1, axis=0), 1, axis=1) +  # top-left
                    np.roll(np.roll(self.planes, 1, axis=0), 0, axis=1) +  # top
                    np.roll(np.roll(self.planes, 1, axis=0), -1, axis=1) +  # top-right
                    np.roll(np.roll(self.planes, 0, axis=0), -1, axis=1) +  # right
                    np.roll(np.roll(self.planes, -1, axis=0), -1, axis=1) +  # bottom-right
                    np.roll(np.roll(self.planes, -1, axis=0), 0, axis=1) +  # bottom
                    np.roll(np.roll(self.planes, -1, axis=0), 1, axis=1) +  # bottom-left
                    np.roll(np.roll(self.planes, 0, axis=0), 1, axis=1)  # left
            )
        return neighbours

    def add_condition_to_create_life(self, *num_neighbours):
        for i in num_neighbours:
            self.add_life_when.append(i)

    def add_condition_to_exterminate_life(self, *num_neighbours):
        for i in num_neighbours:
            self.destroy_life_when.append(i)

    def remove_condition_to_create_life(self, *num_neighbours):
        for i in num_neighbours:
            if i in self.add_life_when:
                self.add_life_when.remove(i)

    def remove_condition_to_exterminate_life(self, *num_neighbours):
        for i in num_neighbours:
            if i in self.destroy_life_when:
                self.destroy_life_when.remove(i)

    def check_rules(self):
        print(f"Add life when: {self.add_life_when} \n Destroy life when: {self.destroy_life_when}")

    def create_life(self, type_neighbours):
        neighbours = self.check_neighbours(type_neighbours)
        mask = np.where((self.planes == 0) & np.isin(neighbours, self.add_life_when), True, False)
        self.planes[mask] += 1

    def exterminate_life(self, type_neighbours):
        neighbours = self.check_neighbours(type_neighbours)
        mask = np.where((self.planes == 1) & np.isin(neighbours, self.destroy_life_when), True, False)
        self.planes[mask] -= 1

    def make_a_time_step(self, type_neighbours):
        self.create_life(type_neighbours)
        self.exterminate_life(type_neighbours)

    def plot_state(self, prt=False):
        plane_state = self.get_state_of_life()
        if prt:
            print(np.flipud(plane_state))

        plt.figure(figsize=(3, 3))
        plt.pcolormesh(plane_state, cmap='binary')
        plt.show()

