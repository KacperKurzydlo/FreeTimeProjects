import matplotlib.pyplot as plt
import matplotlib.animation as animation
from GameLife import Life


Earth = Life(col=25, row=25, num_ones=200)
Earth.add_condition_to_create_life(2, 3)
Earth.add_condition_to_exterminate_life(0, 1, 4, 5, 6, 7, 8)


def time_of_earth():

    fig, ax = plt.subplots()

    plot = ax.imshow(Earth.get_state_of_life(), cmap="binary")

    def animate(i):
        plot.set_data(Earth.get_state_of_life())
        Earth.make_a_time_step(8)
        return plot,

    ani = animation.FuncAnimation(fig, animate, cache_frame_data=False, interval=100, blit=True)

    plt.show()


time_of_earth()
