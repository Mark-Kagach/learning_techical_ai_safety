import { spawn } from "child_process";
import { createInterface } from "readline";

async function testMCPServer() {
    console.log("🧪 Testing MCP Server Integration...");
    console.log("===================================");

    // Start the MCP server as a child process
    const serverProcess = spawn("npm", ["start"], {
        cwd: process.cwd(),
        stdio: ["pipe", "pipe", "pipe"],
    });

    // Create readline interface for sending/receiving messages
    const rl = createInterface({
        input: serverProcess.stdout,
        output: process.stdout,
        terminal: false,
    });

    // Test queries to try
    const testQueries = [
        "What makes a successful startup?",
        "How should founders think about product development?",
        "What is Paul Graham's advice on fundraising?",
    ];

    console.log("📡 Server started, testing queries...\n");

    // Function to send MCP request
    function sendMCPRequest(query: string) {
        const request = {
            jsonrpc: "2.0",
            id: Date.now(),
            method: "tools/call",
            params: {
                name: "search_paragraphs",
                arguments: {
                    query: query,
                },
            },
        };

        console.log(`🔍 Searching: "${query}"`);
        console.log(`📤 Sending: ${JSON.stringify(request)}`);

        serverProcess.stdin.write(JSON.stringify(request) + "\n");
    }

    // Listen for responses
    let responseCount = 0;
    rl.on("line", (line) => {
        try {
            const response = JSON.parse(line);
            console.log(`📥 Response ${++responseCount}:`, response);

            if (response.result && response.result.content) {
                console.log("✅ Got results from Paul Graham essays!");
                console.log("─".repeat(50));
            }
        } catch (e) {
            console.log("📄 Server output:", line);
        }
    });

    // Send test queries with delays
    for (let i = 0; i < testQueries.length; i++) {
        setTimeout(() => {
            sendMCPRequest(testQueries[i]);
        }, i * 3000); // 3 second delays
    }

    // Clean up after 15 seconds
    setTimeout(() => {
        console.log("\n🏁 Test completed. Stopping server...");
        serverProcess.kill();
        process.exit(0);
    }, 15000);

    // Handle errors
    serverProcess.on("error", (error) => {
        console.error("❌ Server error:", error);
    });

    serverProcess.stderr.on("data", (data) => {
        console.log("🔧 Server stderr:", data.toString());
    });
}

testMCPServer().catch(console.error);
