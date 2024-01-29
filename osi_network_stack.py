class PhysicalLayer:
    def __init__(self):
        pass

    def send(self, data):
        print("Physical Layer: Sending data as electrical signals")
        return data

    def receive(self, signals):
        print("Physical Layer: Receiving signals and converting to data")
        return signals


class DataLinkLayer:
    def __init__(self, physical_layer):
        self.physical_layer = physical_layer

    def send(self, data):
        print("Data Link Layer: Framing data")
        framed_data = "<" + data + ">"
        return self.physical_layer.send(framed_data)

    def receive(self, signals):
        print("Data Link Layer: De-framing data")
        deframed_data = signals[1:-1]
        return self.physical_layer.receive(deframed_data)


class NetworkLayer:
    def __init__(self, data_link_layer):
        self.data_link_layer = data_link_layer

    def send(self, data):
        print("Network Layer: Adding network header")
        data_with_header = "[N]" + data
        return self.data_link_layer.send(data_with_header)

    def receive(self, signals):
        print("Network Layer: Removing network header")
        data_without_header = signals[3:]
        return self.data_link_layer.receive(data_without_header)


class TransportLayer:
    def __init__(self, network_layer):
        self.network_layer = network_layer

    def send(self, data):
        print("Transport Layer: Adding transport header")
        data_with_header = "[T]" + data
        return self.network_layer.send(data_with_header)

    def receive(self, signals):
        print("Transport Layer: Removing transport header")
        data_without_header = signals[3:]
        return self.network_layer.receive(data_without_header)


class ApplicationLayer:
    def __init__(self, transport_layer):
        self.transport_layer = transport_layer

    def send(self, data):
        print("Application Layer: Sending data")
        return self.transport_layer.send(data)

    def receive(self, signals):
        print("Application Layer: Receiving data")
        return self.transport_layer.receive(signals)


def main():
    physical_layer = PhysicalLayer()
    data_link_layer = DataLinkLayer(physical_layer)
    network_layer = NetworkLayer(data_link_layer)
    transport_layer = TransportLayer(network_layer)
    application_layer = ApplicationLayer(transport_layer)

    message = "Applied computer networking"
    print("Original message:", message)
    print()

    received_signals = application_layer.send(message)
    print()
    received_data = application_layer.receive(received_signals)
    print("Received message:", received_data)


if __name__ == "__main__":
    main()
