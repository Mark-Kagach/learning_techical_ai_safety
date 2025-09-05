export const validateQuery = (input: unknown): string => {
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

export const validateEnvironmentVariables = (): void => {
    const required = ["OPENAI_API_KEY", "SUPABASE_URL", "SUPABASE_ANON_KEY"];
    const missing = required.filter((key) => !process.env[key]);

    if (missing.length > 0) {
        throw new Error(
            `Missing required environment variables: ${missing.join(", ")}`
        );
    }
};
