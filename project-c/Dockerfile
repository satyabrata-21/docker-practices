# Use GCC base image for C++
FROM gcc:14

# Set working directory inside container
WORKDIR /app

# Copy source code from host to image
COPY . .

# Compile C++ program during vuild
RUN g++ -o hello main.cpp

# Document applicaion port
EXPOSE 8080

# Default command when container starts
CMD ["./hello"]
