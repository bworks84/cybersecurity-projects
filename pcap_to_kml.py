import pyshark
import simplekml

def extract_coordinates(packet):
    try:
        src_lat, src_lon = packet.ip.src.split('.')
        dst_lat, dst_lon = packet.ip.dst.split('.')
        return f"{src_lon},{src_lat},0", f"{dst_lon},{dst_lat},0"
    except AttributeError:
        return None, None

def pcap_to_kml(pcap_file, output_file):
    kml = simplekml.Kml()

    cap = pyshark.FileCapture(pcap_file, display_filter="ip")

    for packet in cap:
        src_coordinates, dst_coordinates = extract_coordinates(packet)
        if src_coordinates and dst_coordinates:
            kml.newpoint(name=f"Source: {packet.ip.src} -> Destination: {packet.ip.dst}",
                         coords=[src_coordinates, dst_coordinates])

    kml.save(output_file)
    print(f"KML file '{output_file}' created successfully!")

if __name__ == "__main__":
    input_pcap_file = "wire.pcap"
    output_kml_file = "output.kml"

    pcap_to_kml(input_pcap_file, output_kml_file)
