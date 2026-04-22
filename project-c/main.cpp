// main.cpp
#include <iostream>
#include <string>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    int server_fd, client_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);

    // Create socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);

    // Attach socket to port
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;   // Listen on all interfaces
    address.sin_port = htons(8080);

    // Bind socket
    bind(server_fd, (struct sockaddr *)&address, sizeof(address));

    // Listen for connections
    listen(server_fd, 3);

    std::cout << "C++ Web Server started on port 8080..." << std::endl;

    while (true) {
        client_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen);

        std::string html =
            "<html>"
            "<head><title>C++ Docker App</title></head>"
            "<body style='font-family:Arial;text-align:center;margin-top:50px;'>"
            "<h1>Hello from C++ Docker Container 🚀</h1>"
            "<p>Web server is running successfully.</p>"
            "</body></html>";

        std::string response =
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Content-Length: " + std::to_string(html.size()) + "\r\n"
            "\r\n" + html;

        send(client_socket, response.c_str(), response.size(), 0);
        close(client_socket);
    }

    close(server_fd);
    return 0;
}
