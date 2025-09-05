import { spawn } from "child_process";
import * as path from "path";

async function testMCPProtocol() {
    console.log("Testing MCP protocol...");

    // Path to the built server
    const serverPath = path.join(__dirname, "dist", "server.js");

    // Spawn the MCP server
    const server = spawn("node", [serverPath], {
        stdio: ["pipe", "pipe", "pipe"],
        cwd: __dirname,
    });

    let responseData = "";

    // Set up data handlers
    server.stdout.on("data", (data) => {
        responseData += data.toString();
        console.log("Server response:", data.toString());
    });

    server.stderr.on("data", (data) => {
        console.log("Server stderr:", data.toString());
    });

    // Send initialize request
    const initializeRequest = {
        jsonrpc: "2.0",
        id: 1,
        method: "initialize",
        params: {
            protocolVersion: "2024-11-05",
            capabilities: {},
            clientInfo: {
                name: "test-client",
                version: "1.0.0",
            },
        },
    };

    console.log("Sending initialize request...");
    server.stdin.write(JSON.stringify(initializeRequest) + "\n");

    // Wait for response
    await new Promise((resolve) => setTimeout(resolve, 2000));

    // Send list tools request
    const listToolsRequest = {
        jsonrpc: "2.0",
        id: 2,
        method: "tools/list",
        params: {},
    };

    console.log("Sending list tools request...");
    server.stdin.write(JSON.stringify(listToolsRequest) + "\n");

    // Wait for response
    await new Promise((resolve) => setTimeout(resolve, 2000));

    // Clean up
    server.kill();
    console.log("Test completed.");
}

testMCPProtocol().catch(console.error);
