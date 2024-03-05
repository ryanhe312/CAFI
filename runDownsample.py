# parse xml file

import xml.etree.ElementTree as ET
import argparse

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    tracks = root.findall('particle')
    for track in tracks:
        for d in track.findall('detection'):
            t_frame = d.get('t')
            t_x = d.get('x')
            t_y = d.get('y')
            t_z = d.get('z')
            print(t_frame, t_x, t_y, t_z)

            # delete detection if t_frame is odd
            if int(t_frame) % 2 != 0:
                track.remove(d)

            # change t_frame to t_frame/2
            else:
                d.set('t', str(int(t_frame)//2))
        
        # delete track if no detection left
        if len(track.findall('detection')) == 0:
            root.remove(track)

    # write to new xml file
    tree.write(xml_file[:-4] + "_downsampled.xml", xml_declaration=True, encoding='utf-8')

# argparse
parser = argparse.ArgumentParser(description='parse xml file')
parser.add_argument('xml_file', type=str, help='xml file to parse')
args = parser.parse_args()

# parse xml file
parse_xml(args.xml_file)