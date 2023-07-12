import time
import socket

def send_event(destination_address, destination_port, event):
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send the event to the destination
    sock.sendto(event.encode(), (destination_address, destination_port))

    # Close the socket
    sock.close()

def check_jitter(expected_interval, destination_address, destination_port):
    previous_time = time.time()

    while True:
        # Perform your event or task here
        event = "Your event data here"
        send_event(destination_address, destination_port, event)

        current_time = time.time()

        actual_interval = current_time - previous_time
        jitter = abs(actual_interval - expected_interval)

        print("Expected Interval: {:.6f} s".format(expected_interval))
        print("Actual Interval:   {:.6f} s".format(actual_interval))

        print("Jitter:            {:.6f} s\n".format(jitter))


        previous_time = current_time

        # Wait for some time before the next event
        time.sleep(expected_interval)

# Specify the expected interval between events in seconds
expected_interval = 1.0

# Specify the destination address and port
destination_address = '203.99.40.1'  # Example IP address
destination_port = 443  # Example port number

# Call the function to check jitter
check_jitter(expected_interval, destination_address, destination_port)
