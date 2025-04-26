from dnslib import DNSRecord, RR, QTYPE, A
from socketserver import UDPServer, BaseRequestHandler

BLOCKED_DOMAINS = set()

with open("blocklist.txt", "r") as f:
    for line in f:
        if line.strip() and not line.startswith("#"):
            BLOCKED_DOMAINS.add(line.strip().lower())

class DNSHandler(BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        request = DNSRecord.parse(data)
        qname = str(request.q.qname)[:-1].lower()

        reply = request.reply()
        if qname in BLOCKED_DOMAINS:
            print(f"Blocked: {qname}")
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("0.0.0.0"), ttl=60))
        else:
            # Forward to real DNS (e.g. 8.8.8.8) -- for now, just block known ads
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("8.8.8.8"), ttl=60))

        socket.sendto(reply.pack(), self.client_address)

if __name__ == "__main__":
    print("AdBlock DNS Service Running on 127.0.0.1:53094")
    UDPServer(("127.0.0.1", 53094), DNSHandler).serve_forever()
