
import time
import random

# Needed elements throughout the code
# Maximum send size.
max_send_size = 100
# Counts if sent frames are less than or equal to 100.
send_counter = 0
max_send_per_time = 4
bit_seq_number = 3
window_size = 4
# Holds all corrupted frames
corrupted_frames_total = []
# Holds corrupted frames in one try.
corrupted_frames = []
# Holds frames that the sender have sent.
sender_window = []
# Holds frames that the receiver have received.
receiver_window = []


# A function to send frame
def send_frame():
    global number_of_data
    number_of_data = int(input("How many frame do you want to send. Max is 4, enter 0 to exit and see the final result:"))

    if number_of_data <= max_send_per_time and number_of_data != 0:
        global send_counter
        send_counter += number_of_data
        # A for loop to get frames that the user wants to send
        for x in range(number_of_data):

            frame_to_send = input(f"Enter the {x+1}. frame that you want to send. You can't transmit more than "
                                  f"{number_of_data}: ")

            # Appends frame to be sent to sender_window and then generates a random number
            sender_window.append(frame_to_send)
            random_number = random.randint(0, 101)

            # If random number is less than or equal to 70
            if random_number <= 70:
                receiver_window.append(frame_to_send)

                # if number of frames has been sent greater than 100, it deletes last updated elements of sender window,
                # alerts the user with print statement and deletes the last update from send counter
                if send_counter > max_send_size:
                    del sender_window[-number_of_data:]

                    print(f"The maximum frame size to be sent has been exceeded. You can send "
                          f"{max_send_size - send_counter} more frame")

                    send_counter -= number_of_data

            else:
                # If the frame is corrupted, appends that frame to corrupted_frames_total. This one stores all
                # corrupted frames because we will use it to display the final result
                corrupted_frames_total.append(frame_to_send)

                # If the frame is corrupted in last try, appends that frame to corrupted_frame list. Then we are going
                # to clear this list window display because it will show us which one is corrupted in every try.
                corrupted_frames.append(frame_to_send)

                # Sets the send_counter to -1 if the frame is corrupted.
                send_counter -= 1

        print("sending...")
        time.sleep(1)
    elif number_of_data > max_send_per_time:
        print("\nYou wanted to enter more than 4. Try again.\n")
    elif number_of_data == 0:
        print("Sender exited.")


# Prints 'receiving...' and sleeps 1 second if number_of_data is less than 4 and not equal to 0.
def receive_frame():
    if number_of_data <= max_send_per_time and number_of_data != 0:
        print("receiving...")
        time.sleep(1)


# This function displays sender_window, receiver_window and corrupted_frames lists
def window_display(sender_window, receiver_window, corrupted_frames):
    if number_of_data <= max_send_per_time and number_of_data != 0:
        # Sender Window
        print("\nSender Window:")
        print(sender_window)

        # Receiver Window Display
        receiver_window_display = []
        print("\nReceiver Window:")
        if len(receiver_window) <= window_size:
            receiver_window_display += receiver_window
            print(receiver_window_display)
        elif len(receiver_window) > window_size:
            receiver_window_display += receiver_window[-window_size:]
            print(receiver_window_display)

        # Corrupted Window Display
        print(f"\n{len(corrupted_frames)} frame corrupted: {corrupted_frames}\n")
        corrupted_frames.clear()

    elif number_of_data == 0:
        print("Final result:")
        print(f"Sender Window: {sender_window}")
        print(f"Receiver Window: {receiver_window}")
        print(f"Corrupted Frames: {corrupted_frames_total}")
        global send_counter
        send_counter = -1

# Combines send_frame(), receive_frame() and window_display() functions together in order to get the final program
while send_counter < 101 and send_counter != -1:
    send_frame()
    receive_frame()
    window_display(sender_window, receiver_window, corrupted_frames)
    # Calls window_display() function if send_counter not equal to -1.
    if send_counter != -1:
        print(f"The system will continue until you send 100 frames or enter 0. You sent {send_counter} frame.")

