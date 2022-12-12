incoming_signals = []


def find_start_of_packet_marker(signal, distinct_chars):
    incoming_signals.append(signal)
    if len(set(incoming_signals[-distinct_chars:])) == distinct_chars:
        return len(incoming_signals)
    return 0


def process_datastream_line(line, distinct_chars):
    for single_char in list(line.rstrip()):
        response = find_start_of_packet_marker(single_char, distinct_chars)
        if response:
            return response


with open("resources/datastream.txt", "r") as f:
    print(process_datastream_line(f.readline(), 4))
    f.seek(0)
    incoming_signals = []
    print(process_datastream_line(f.readline(), 14))
