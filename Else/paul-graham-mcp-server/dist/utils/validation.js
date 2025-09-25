"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.validateEnvironmentVariables = exports.validateQuery = void 0;
const validateQuery = (input) => {
    if (typeof input !== "string") {
        throw new Error("Query must be a string");
    }
    if (!input || input.trim().length === 0) {
        throw new Error("Query cannot be empty");
    }
    if (input.length > 1000) {
        throw new Error("Query is too long (max 1000 characters)");
    }
    return input.trim();
};
exports.validateQuery = validateQuery;
const validateEnvironmentVariables = () => {
    const required = ["OPENAI_API_KEY", "SUPABASE_URL", "SUPABASE_ANON_KEY"];
    const missing = required.filter((key) => !process.env[key]);
    if (missing.length > 0) {
        throw new Error(`Missing required environment variables: ${missing.join(", ")}`);
    }
};
exports.validateEnvironmentVariables = validateEnvironmentVariables;
