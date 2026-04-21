import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class HelloWorld {
    public static void main(String[] args) throws Exception {

        HttpServer server =
            HttpServer.create(new InetSocketAddress("0.0.0.0", 8080), 0);

        server.createContext("/", new Handler());
        server.start();

        System.out.println("Server started on port 8080");
    }

    static class Handler implements HttpHandler {
        public void handle(HttpExchange exchange) {
            try {
                String response = "<h1>Hello from Java Docker Container 🚀</h1>";
                exchange.sendResponseHeaders(200, response.getBytes().length);
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
                os.close();
            } catch (Exception e) {}
        }
    }
}
