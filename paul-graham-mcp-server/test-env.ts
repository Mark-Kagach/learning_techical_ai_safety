import * as dotenv from "dotenv";
import { validateEnvironmentVariables } from "./src/utils/validation";

// Load environment variables
dotenv.config();

console.log("Testing Environment Variables...");
console.log("================================");

// Check if .env file exists and variables are loaded
console.log("OPENAI_API_KEY:", process.env.OPENAI_API_KEY ? "SET" : "NOT SET");
console.log("SUPABASE_URL:", process.env.SUPABASE_URL ? "SET" : "NOT SET");
console.log(
    "SUPABASE_ANON_KEY:",
    process.env.SUPABASE_ANON_KEY ? "SET" : "NOT SET"
);

try {
    validateEnvironmentVariables();
    console.log("✅ Environment validation passed!");
} catch (error) {
    console.log(
        "❌ Environment validation failed:",
        error instanceof Error ? error.message : "Unknown error"
    );
    console.log("\nPlease:");
    console.log("1. Copy .env.example to .env");
    console.log("2. Fill in your actual API keys");
}
