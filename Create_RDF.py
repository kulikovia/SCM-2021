import xml.etree.ElementTree as xml
import random
from random import randrange
from datetime import datetime
from datetime import timedelta
import csv

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('2/1/20 00:00:00', '%m/%d/%y %H:%M:%S')
d2 = datetime.strptime('2/3/20 23:59:59', '%m/%d/%y %H:%M:%S')

Max_Devices = 9
Max_Users = 9

class tune:

    def start(self, event_timestamp, device_id, channel_id, state_id):
        self.event_timestamp = event_timestamp
        self.device_id = device_id
        self.channel_id = channel_id
        self.state_id = state_id





def createXML():
    """
    Создаем XML файл.
    """


#Open SPARQL file
    f = open("States.nq", "wt")

# Add header
    header = str("<?xml version='1.0' encoding='UTF-8'?>\n<rdf:RDF\nxmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'\nxmlns:vCard='http://www.w3.org/2001/vcard-rdf/3.0#'\nxmlns:my='http://127.0.0.1/bg/ont/test1#'\n>")
    f.write(header)

# Add State nodes
    i = 0
    tunes = []
    with open('output.csv') as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        for line in reader:
            tunes.append(tune())
            tunes[i].event_timestamp = line["TIMESTAMP"]
            tunes[i].device_id = line["DEVICE_ID"]
            tunes[i].channel_id = line["CHANNEL_ID"]
            tunes[i].state_id = line["DEVICE_STATE"]
            body = str("\n<rdf:Description rdf:about = 'http://127.0.0.1/Event_") + str(i) + "/'>\n<my:request_timestamp rdf:datatype = 'http://www.w3.org/2001/XMLSchema#datetime'>" + str(tunes[i].event_timestamp) + "</my:request_timestamp>\n<my:has_req_type>STATE_CHANGE</my:has_req_type>\n<my:has_state>" + str(tunes[i].state_id) + "</my:has_state>\n<my:request_detailes>\n<rdf:Description>\n<rdf:type>:statement</rdf:type>\n<rdf:predicat>:new_state</rdf:predicat>\n<rdf:subject>Watch_TV</rdf:subject>\n<rdf:object><rdf:Description rdf:about = 'http://127.0.0.1/" + str(tunes[i].channel_id)+ "/'>\n</rdf:Description>\n</rdf:object>\n</rdf:Description>\n</my:request_detailes>\n<my:uses_dev>\n<rdf:Description rdf:about = 'http://127.0.0.1/Device_" + str(tunes[i].device_id) + "/'>\n</rdf:Description>\n</my:uses_dev>\n</rdf:Description>\n"
            f.write(body)
            i = i + 1


    f.write("\n</rdf:RDF>\n")

    f.close()

if __name__ == "__main__":
    createXML()
