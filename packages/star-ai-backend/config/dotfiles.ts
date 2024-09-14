import { config } from "dotenv";
config();

const PORT = process.env.PORT || 5123;
const HOST = process.env.HOST || "localhost";

const HTTPSERVER = {
    port: PORT,
    host: HOST,
};

const Server = {
    httpServer: HTTPSERVER,
};

export default Server;
