# Use java base image
FROM eclipse-temurin:21-jdk
# Set working directory inside container
WORKDIR /app
# Copy project file from host to image
COPY . .
# Compile Java program during build
RUN javac HelloWorld.java
# Document application port
EXPOSE 8080
#Default command when container starts
CMD ["java", "HelloWorld"]
