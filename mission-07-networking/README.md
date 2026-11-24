# Mission 7 — How computers communicate

## 1. Mission title
Mission 7 — How computers communicate

## 2. Task / objective
Explain common network concepts, test a public example domain, perform a DNS lookup and describe how a browser opens a website.

## 3. Work completed
I checked reachability with `ping` and looked up the A records for `example.com` with `dig`. Two ping replies arrived with no packet loss. The DNS lookup returned two public addresses at the time checked. I recorded only the example domain's public results and left out local IP and Wi-Fi information.

| Concept | Explanation | Example |
|---|---|---|
| LAN | A Local Area Network connects devices in a limited place. | Devices connected to a home router. |
| MAN | A Metropolitan Area Network links locations across a city or large campus. | A city-wide education network. |
| WAN | A Wide Area Network connects networks across large distances. | The Internet. |
| DNS | The Domain Name System finds an IP address associated with a domain name. | Looking up `example.com` before connecting. |
| Router | A router forwards traffic between networks. | A home router passing traffic between a LAN and the Internet. |
| Protocol | A protocol is an agreed set of communication rules. | HTTPS uses HTTP over an encrypted connection. |
| Packet switching | Data is split into packets that can travel through a network and be reassembled. | A web page response sent as many packets. |
| Client-server | A client requests a service; a server responds. | A browser asks a web server for a page. |

### Connectivity and DNS observations

`ping -c 2 example.com` received 2 replies from the public example domain address, with 0% packet loss and about 20 ms average round-trip time in this check. `dig example.com A +short` returned `104.20.23.154` and `172.66.147.243`. These addresses belong to the example domain response and can change; they are not the computer's local address. A connectivity test checks whether a host responds over the network. A DNS lookup asks the naming system for records, such as the IP addresses associated with a domain. DNS lets people use names that are easier to remember than numeric network addresses.

### What happens when I open a website

1. I enter a web address in the browser; the browser separates the host name from the requested path.
2. The browser checks whether it already has a usable address or cached response.
3. If needed, DNS resolves the host name to one or more IP addresses.
4. The client establishes a connection to a server, using network protocols such as TCP with TLS or QUIC.
5. The browser sends an HTTP request through the network; routers forward packets toward the server.
6. The server processes the request and returns an HTTP response, which travels back as packets.
7. The browser interprets the response and displays the page, often requesting additional images, styles or scripts.

## 4. Commands / tools used
- `ping -c 2 example.com` — sent two connectivity-check packets; both received replies.
- `dig example.com A +short` — requested IPv4 A records for the public example domain.

## 5. My understanding
A network gives devices a way to exchange data using shared rules. DNS turns a human-readable name into network addresses, and a router moves packets between networks. When a browser opens a page, it acts as a client: it finds the server, sends a request using protocols, and presents the server's response. Packet switching allows a larger message to travel in smaller pieces.

## 6. Difficulties faced
No major difficulties. Network answers can vary because DNS and routing depend on time and location.

## 7. How I resolved them
I recorded the domain and the results returned during this check, and noted that they may change. I did not save local network information.

## 8. Evidence / files
- `network-observations.md` — privacy-safe connectivity and DNS results.
- This README — network concepts and the website request sequence.

## 9. Commit details
Commit message: `Explain networking concepts and website communication`. Mission 6's Pull Request #1 remains open and unmerged for instructor review.
